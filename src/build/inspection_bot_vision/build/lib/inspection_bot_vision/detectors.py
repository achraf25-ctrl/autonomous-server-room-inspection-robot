#!/usr/bin/env python3
"""
Détection d'anomalies visuelles — logique pure (aucune dépendance ROS2),
pour pouvoir être testée sur n'importe quelle image ou flux webcam.

Deux modes :
  - YOLOv8 (via `ultralytics`) si le package est installé ET qu'un modèle
    entraîné est fourni dans inspection_bot_vision/models/. C'est la voie
    "production" décrite dans le projet (dataset MVTec AD + images
    synthétiques de racks/câbles/portes).
  - Détecteur de secours 100% OpenCV (aucune dépendance lourde), qui
    détecte au minimum les "voyants rouges allumés" par seuillage HSV,
    et une heuristique simple de "porte de rack ouverte" par détection de
    grand rectangle sombre (silhouette d'ouverture) — suffisant pour faire
    une démo fonctionnelle sans avoir à entraîner un modèle au préalable.

Retourne une liste de dicts : {type, confidence, bbox, critical}
"""

from dataclasses import dataclass, field
from typing import List, Tuple
import os

import cv2
import numpy as np


@dataclass
class Detection:
    anomaly_type: str          # "red_led", "open_rack_door", "disconnected_cable", "smoke"
    confidence: float
    bbox: Tuple[int, int, int, int]   # x, y, w, h
    critical: bool = False


# ---------------------------------------------------------------------------
# Détecteur de secours : OpenCV pur
# ---------------------------------------------------------------------------

def detect_red_leds(frame_bgr: np.ndarray, min_area: int = 15) -> List[Detection]:
    """Détecte les points rouges vifs (voyants d'alerte allumés sur les racks)."""
    hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)

    # Le rouge est à cheval sur 0° et 180° en teinte HSV -> deux masques
    lower_red_1 = np.array([0, 120, 120])
    upper_red_1 = np.array([8, 255, 255])
    lower_red_2 = np.array([172, 120, 120])
    upper_red_2 = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_red_1, upper_red_1) | cv2.inRange(hsv, lower_red_2, upper_red_2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for c in contours:
        area = cv2.contourArea(c)
        if area < min_area:
            continue
        x, y, w, h = cv2.boundingRect(c)
        # Un voyant est petit et à peu près carré/rond ; un gros aplat rouge
        # est plus probablement un objet rouge quelconque -> confiance plus basse
        aspect = w / max(h, 1)
        roundness_ok = 0.4 < aspect < 2.5
        confidence = min(0.95, 0.5 + area / 500.0) if roundness_ok else 0.35
        detections.append(Detection(
            anomaly_type="red_led",
            confidence=round(confidence, 2),
            bbox=(x, y, w, h),
            critical=confidence > 0.7,
        ))
    return detections


def detect_open_rack_door(frame_bgr: np.ndarray, min_area_ratio: float = 0.05) -> List[Detection]:
    """
    Heuristique simplifiée : une porte de rack ouverte laisse voir l'intérieur
    sombre du rack -> on cherche de grandes zones très sombres et rectangulaires
    au milieu de l'image. C'est volontairement simple (pas un vrai modèle
    entraîné) pour donner une démo fonctionnelle sans dataset annoté au départ.
    """
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    _, dark_mask = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(dark_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    h_img, w_img = gray.shape
    frame_area = h_img * w_img

    detections = []
    for c in contours:
        area = cv2.contourArea(c)
        if area / frame_area < min_area_ratio:
            continue
        x, y, w, h = cv2.boundingRect(c)
        rectangularity = area / (w * h + 1e-6)
        if rectangularity < 0.6:
            continue
        confidence = round(min(0.9, 0.4 + rectangularity * 0.5), 2)
        detections.append(Detection(
            anomaly_type="open_rack_door",
            confidence=confidence,
            bbox=(x, y, w, h),
            critical=True,   # une baie ouverte est toujours traitée comme prioritaire
        ))
    return detections


def detect_with_opencv_fallback(frame_bgr: np.ndarray) -> List[Detection]:
    return detect_red_leds(frame_bgr) + detect_open_rack_door(frame_bgr)


# ---------------------------------------------------------------------------
# Détecteur "production" : YOLOv8 (optionnel, chargé paresseusement)
# ---------------------------------------------------------------------------

_YOLO_MODEL = None
_YOLO_CLASS_MAP = {
    0: "red_led",
    1: "open_rack_door",
    2: "disconnected_cable",
    3: "smoke",
}
_CRITICAL_CLASSES = {"open_rack_door", "smoke"}


def _try_load_yolo(weights_path: str):
    global _YOLO_MODEL
    if _YOLO_MODEL is not None:
        return _YOLO_MODEL
    try:
        from ultralytics import YOLO
    except ImportError:
        return None
    if not os.path.exists(weights_path):
        return None
    _YOLO_MODEL = YOLO(weights_path)
    return _YOLO_MODEL


def detect_with_yolo(frame_bgr: np.ndarray, weights_path: str, conf_threshold: float = 0.5):
    model = _try_load_yolo(weights_path)
    if model is None:
        return None  # pas dispo -> l'appelant doit basculer sur le fallback

    results = model.predict(frame_bgr, conf=conf_threshold, verbose=False)
    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            anomaly_type = _YOLO_CLASS_MAP.get(cls_id, f"class_{cls_id}")
            detections.append(Detection(
                anomaly_type=anomaly_type,
                confidence=round(conf, 2),
                bbox=(int(x1), int(y1), int(x2 - x1), int(y2 - y1)),
                critical=anomaly_type in _CRITICAL_CLASSES,
            ))
    return detections


def detect_anomalies(frame_bgr: np.ndarray, yolo_weights_path: str = None) -> List[Detection]:
    """Point d'entrée unique : essaie YOLOv8, retombe sur OpenCV si indisponible."""
    if yolo_weights_path:
        yolo_result = detect_with_yolo(frame_bgr, yolo_weights_path)
        if yolo_result is not None:
            return yolo_result
    return detect_with_opencv_fallback(frame_bgr)
