#!/usr/bin/env python3
"""
Dashboard web du robot inspecteur.

  - Reçoit les alertes d'anomalie via MQTT (topic "inspection/alerts",
    publiées par inspection_bot_vision/anomaly_detector.py)
  - Maintient un état en mémoire : statut de chaque rack (ok / warning /
    critical), historique des alertes, score de santé global
  - Pousse les mises à jour en temps réel aux clients connectés via
    Socket.IO
  - Expose /api/generate_report pour déclencher la génération du PDF
    (appelé automatiquement par inspection_commander.py en fin de tournée,
    ou manuellement via le bouton du dashboard)

Lancer :
    python3 app.py
Puis ouvrir http://localhost:5000
"""

import json
import os
import threading
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_socketio import SocketIO

import paho.mqtt.client as mqtt

from report_generator import generate_report

MQTT_BROKER_HOST = os.environ.get("MQTT_BROKER_HOST", "localhost")
MQTT_BROKER_PORT = int(os.environ.get("MQTT_BROKER_PORT", "1883"))
MQTT_ALERT_TOPIC = "inspection/alerts"

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# 12 racks, 3 rangées de 4 — correspond à server_room.world / inspection_points.yaml
RACK_IDS = [f"rack_{row}_{col}" for row in (1, 2, 3) for col in (1, 2, 3, 4)]

app = Flask(__name__)
app.config["SECRET_KEY"] = "inspection-bot-dashboard"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

# ---------------------------------------------------------------------------
# État en mémoire (partagé entre le thread MQTT et les requêtes Flask)
# ---------------------------------------------------------------------------
state_lock = threading.Lock()
racks_state = {rack_id: {"status": "ok", "last_anomaly": None} for rack_id in RACK_IDS}
alerts_history = []   # liste de dicts, la plus récente en tête


def _severity_rank(status: str) -> int:
    return {"ok": 0, "warning": 1, "critical": 2}.get(status, 0)


def _apply_alert(alert: dict):
    rack_id = alert.get("rack_id", "unknown")
    new_status = "critical" if alert.get("critical") else "warning"

    with state_lock:
        alerts_history.insert(0, alert)
        del alerts_history[200:]   # garde un historique borné

        current = racks_state.setdefault(rack_id, {"status": "ok", "last_anomaly": None})
        if _severity_rank(new_status) >= _severity_rank(current["status"]):
            current["status"] = new_status
        current["last_anomaly"] = alert

    socketio.emit("new_alert", alert)
    socketio.emit("racks_update", get_racks_snapshot())


def get_racks_snapshot():
    with state_lock:
        return {rid: dict(info) for rid, info in racks_state.items()}


def compute_health_score() -> int:
    with state_lock:
        statuses = [info["status"] for info in racks_state.values()]
    if not statuses:
        return 100
    penalty = sum({"ok": 0, "warning": 5, "critical": 15}[s] for s in statuses)
    return max(0, 100 - penalty)


# ---------------------------------------------------------------------------
# MQTT : thread d'écoute des alertes envoyées par la couche vision
# ---------------------------------------------------------------------------

def on_mqtt_message(client, userdata, msg):
    try:
        alert = json.loads(msg.payload.decode("utf-8"))
    except Exception:
        return
    _apply_alert(alert)


def start_mqtt_listener():
    client = mqtt.Client()
    client.on_message = on_mqtt_message

    def _connect_loop():
        while True:
            try:
                client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, keepalive=30)
                client.subscribe(MQTT_ALERT_TOPIC, qos=1)
                client.loop_forever()
            except Exception as e:
                print(f"[mqtt] connexion échouée ({e}), nouvelle tentative dans 5s...")
                import time
                time.sleep(5)

    t = threading.Thread(target=_connect_loop, daemon=True)
    t.start()


# ---------------------------------------------------------------------------
# Routes HTTP
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/racks")
def api_racks():
    return jsonify(get_racks_snapshot())


@app.route("/api/alerts")
def api_alerts():
    with state_lock:
        return jsonify(alerts_history[:50])


@app.route("/api/health_score")
def api_health_score():
    return jsonify({"health_score": compute_health_score()})


@app.route("/api/simulate_alert", methods=["POST"])
def api_simulate_alert():
    """Endpoint de secours utilisé par demo_simulate_inspection.py quand aucun
    broker MQTT n'est disponible (démo rapide sans Docker/Mosquitto)."""
    alert = request.get_json(force=True)
    _apply_alert(alert)
    return jsonify({"ok": True})


@app.route("/api/generate_report", methods=["POST"])
def api_generate_report():
    with state_lock:
        racks_snapshot = {rid: dict(info) for rid, info in racks_state.items()}
        alerts_snapshot = list(alerts_history)

    health_score = compute_health_score()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"inspection_report_{timestamp}.pdf"
    output_path = os.path.join(REPORTS_DIR, filename)

    generate_report(
        output_path=output_path,
        racks_state=racks_snapshot,
        alerts=alerts_snapshot,
        health_score=health_score,
    )

    socketio.emit("report_ready", {"filename": filename})
    return jsonify({"ok": True, "filename": filename, "health_score": health_score})


@app.route("/reports/<path:filename>")
def download_report(filename):
    return send_from_directory(REPORTS_DIR, filename, as_attachment=True)


@app.route("/api/reset_demo", methods=["POST"])
def api_reset_demo():
    """Remet tous les racks à 'ok' et vide l'historique — pratique entre deux démos."""
    with state_lock:
        for info in racks_state.values():
            info["status"] = "ok"
            info["last_anomaly"] = None
        alerts_history.clear()
    socketio.emit("racks_update", get_racks_snapshot())
    return jsonify({"ok": True})


if __name__ == "__main__":
    start_mqtt_listener()
    socketio.run(app, host="0.0.0.0", port=5000, debug=False, allow_unsafe_werkzeug=True)
