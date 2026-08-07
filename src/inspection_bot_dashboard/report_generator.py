#!/usr/bin/env python3
"""
Génère le rapport PDF de fin d'inspection :
  - Carte schématique de la salle avec les racks colorés par statut
  - Score de santé global
  - Liste des anomalies détectées (avec photo si le fichier existe)
  - Recommandations générées automatiquement selon les types d'anomalies

Utilisable en standalone pour tester :
    python3 report_generator.py
"""

import os
from datetime import datetime, timezone

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

STATUS_COLORS = {
    "ok": HexColor("#2ecc71"),
    "warning": HexColor("#f39c12"),
    "critical": HexColor("#e74c3c"),
}

RECOMMENDATIONS_BY_TYPE = {
    "red_led": "Vérifier l'état du serveur concerné (voyant d'alerte allumé) "
               "et consulter les journaux système du rack.",
    "open_rack_door": "Refermer et verrouiller la baie ouverte — risque de "
                       "sécurité et de refroidissement anormal.",
    "disconnected_cable": "Reconnecter le câble détecté débranché et vérifier "
                           "l'intégrité de la liaison réseau/alimentation.",
    "smoke": "URGENT : évacuer la zone et déclencher la procédure incendie, "
             "puis faire intervenir un technicien immédiatement.",
}

# Disposition de la salle : 3 rangées x 4 racks (voir server_room.world)
ROOM_LAYOUT = [
    [f"rack_1_{c}" for c in (1, 2, 3, 4)],
    [f"rack_2_{c}" for c in (1, 2, 3, 4)],
    [f"rack_3_{c}" for c in (1, 2, 3, 4)],
]


def _draw_room_map(c: canvas.Canvas, x0: float, y0: float, racks_state: dict):
    """Dessine une petite carte de la salle : une grille de racks colorés."""
    cell_w, cell_h = 2.2 * cm, 1.6 * cm
    gap = 0.4 * cm

    c.setFont("Helvetica-Bold", 11)
    c.drawString(x0, y0 + 3 * (cell_h + gap) + 0.3 * cm, "Plan de la salle serveur")

    for row_idx, row in enumerate(ROOM_LAYOUT):
        for col_idx, rack_id in enumerate(row):
            status = racks_state.get(rack_id, {}).get("status", "ok")
            color = STATUS_COLORS.get(status, STATUS_COLORS["ok"])

            rx = x0 + col_idx * (cell_w + gap)
            ry = y0 + (len(ROOM_LAYOUT) - 1 - row_idx) * (cell_h + gap)

            c.setFillColor(color)
            c.rect(rx, ry, cell_w, cell_h, fill=1, stroke=1)
            c.setFillColor(black)
            c.setFont("Helvetica", 7)
            c.drawCentredString(rx + cell_w / 2, ry + cell_h / 2 - 3, rack_id)

    # légende
    legend_y = y0 - 0.9 * cm
    legend_x = x0
    for label, status in (("OK", "ok"), ("Avertissement", "warning"), ("Critique", "critical")):
        c.setFillColor(STATUS_COLORS[status])
        c.rect(legend_x, legend_y, 0.4 * cm, 0.4 * cm, fill=1, stroke=1)
        c.setFillColor(black)
        c.setFont("Helvetica", 8)
        c.drawString(legend_x + 0.55 * cm, legend_y + 0.05 * cm, label)
        legend_x += 3.2 * cm


def _build_recommendations(alerts: list) -> list:
    seen_types = []
    for alert in alerts:
        t = alert.get("anomaly_type")
        if t and t not in seen_types:
            seen_types.append(t)

    if not seen_types:
        return ["Aucune anomalie détectée — aucune action requise."]

    return [RECOMMENDATIONS_BY_TYPE.get(t, f"Vérifier l'anomalie de type '{t}'.")
            for t in seen_types]


def generate_report(output_path: str, racks_state: dict, alerts: list, health_score: int):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # --- En-tête -------------------------------------------------------
    c.setFillColor(HexColor("#1b2733"))
    c.rect(0, height - 2.5 * cm, width, 2.5 * cm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(1.5 * cm, height - 1.5 * cm, "Rapport d'inspection — Salle serveur")
    c.setFont("Helvetica", 10)
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    c.drawString(1.5 * cm, height - 2.1 * cm, f"Généré le {now_str}")

    c.setFillColor(black)

    # --- Score de santé --------------------------------------------------
    score_color = (
        STATUS_COLORS["ok"] if health_score >= 85 else
        STATUS_COLORS["warning"] if health_score >= 60 else
        STATUS_COLORS["critical"]
    )
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1.5 * cm, height - 3.5 * cm, "Score de santé global de la salle :")
    c.setFillColor(score_color)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(9.5 * cm, height - 3.6 * cm, f"{health_score}%")
    c.setFillColor(black)

    # --- Carte de la salle -----------------------------------------------
    _draw_room_map(c, x0=1.5 * cm, y0=height - 9.5 * cm, racks_state=racks_state)

    # --- Liste des anomalies détectées ------------------------------------
    y = height - 12.5 * cm
    c.setFont("Helvetica-Bold", 13)
    c.drawString(1.5 * cm, y, f"Anomalies détectées ({len(alerts)})")
    y -= 0.7 * cm

    c.setFont("Helvetica", 9)
    if not alerts:
        c.drawString(1.5 * cm, y, "Aucune anomalie détectée pendant cette tournée.")
        y -= 0.5 * cm
    else:
        for alert in alerts[:12]:   # limite raisonnable pour tenir sur quelques pages
            if y < 3 * cm:
                c.showPage()
                y = height - 2 * cm
                c.setFont("Helvetica", 9)

            severity = "CRITIQUE" if alert.get("critical") else "avertissement"
            line = (f"• {alert.get('rack_id', '?')} — {alert.get('anomaly_type', '?')} "
                    f"({severity}, confiance {alert.get('confidence', 0):.2f}) "
                    f"— {alert.get('timestamp', '')}")
            c.drawString(1.5 * cm, y, line)
            y -= 0.45 * cm

            image_path = alert.get("image_path")
            if image_path and os.path.exists(image_path):
                try:
                    img = ImageReader(image_path)
                    img_h = 2.2 * cm
                    img_w = 2.2 * cm
                    c.drawImage(img, 2.0 * cm, y - img_h, width=img_w, height=img_h,
                                preserveAspectRatio=True, mask='auto')
                    y -= img_h + 0.3 * cm
                except Exception:
                    pass

    # --- Recommandations ---------------------------------------------------
    if y < 4 * cm:
        c.showPage()
        y = height - 2 * cm

    y -= 0.5 * cm
    c.setFont("Helvetica-Bold", 13)
    c.drawString(1.5 * cm, y, "Recommandations automatiques")
    y -= 0.7 * cm

    c.setFont("Helvetica", 9)
    for rec in _build_recommendations(alerts):
        c.drawString(1.5 * cm, y, f"- {rec}")
        y -= 0.5 * cm

    c.save()
    return output_path


if __name__ == "__main__":
    # Démo standalone : génère un rapport avec des données factices
    demo_racks = {
        "rack_1_1": {"status": "ok"},
        "rack_1_2": {"status": "warning"},
        "rack_2_3": {"status": "critical"},
        "rack_3_4": {"status": "ok"},
    }
    demo_alerts = [
        {"rack_id": "rack_1_2", "anomaly_type": "red_led", "confidence": 0.82,
         "critical": False, "timestamp": datetime.now(timezone.utc).isoformat(), "image_path": ""},
        {"rack_id": "rack_2_3", "anomaly_type": "open_rack_door", "confidence": 0.91,
         "critical": True, "timestamp": datetime.now(timezone.utc).isoformat(), "image_path": ""},
    ]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports", "demo_report.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    generate_report(out, demo_racks, demo_alerts, health_score=72)
    print(f"Rapport de démo généré : {out}")
