#!/usr/bin/env python3
"""
Simule une tournée d'inspection complète pour démontrer le dashboard et le
rapport PDF SANS avoir besoin de Gazebo/ROS2 — utile pour une démo rapide ou
une soutenance.

Envoie les alertes directement au dashboard Flask via /api/simulate_alert
(pas besoin d'un broker MQTT pour ce script de démo, même si le vrai
anomaly_detector.py utilise MQTT en conditions réelles).

Usage :
    # Terminal 1
    python3 app.py
    # Terminal 2
    python3 demo_simulate_inspection.py
"""

import random
import time
from datetime import datetime, timezone

import requests

DASHBOARD_URL = "http://localhost:5000"

RACK_IDS = [f"rack_{row}_{col}" for row in (1, 2, 3) for col in (1, 2, 3, 4)]

ANOMALY_TYPES = [
    ("red_led", False),
    ("red_led", True),
    ("open_rack_door", True),
    ("disconnected_cable", False),
    ("smoke", True),
]


def simulate_tour(n_anomalies: int = 4, delay_sec: float = 2.0):
    print(f"Simulation d'une tournée sur {len(RACK_IDS)} racks...")
    requests.post(f"{DASHBOARD_URL}/api/reset_demo")

    anomalous_racks = random.sample(RACK_IDS, k=min(n_anomalies, len(RACK_IDS)))

    for rack_id in RACK_IDS:
        print(f"  → Inspection de {rack_id}...")
        time.sleep(delay_sec)

        if rack_id in anomalous_racks:
            anomaly_type, critical = random.choice(ANOMALY_TYPES)
            alert = {
                "rack_id": rack_id,
                "anomaly_type": anomaly_type,
                "confidence": round(random.uniform(0.6, 0.97), 2),
                "critical": critical,
                "image_path": "",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            print(f"    ⚠️ Anomalie simulée : {anomaly_type} (critique={critical})")
            requests.post(f"{DASHBOARD_URL}/api/simulate_alert", json=alert)

    print("Tournée simulée terminée. Génération du rapport...")
    res = requests.post(f"{DASHBOARD_URL}/api/generate_report")
    print("Rapport :", res.json())


if __name__ == "__main__":
    simulate_tour()
