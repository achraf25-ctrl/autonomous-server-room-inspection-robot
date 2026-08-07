#!/usr/bin/env python3
"""
Nœud ROS2 de la couche Vision :
  - S'abonne à /camera/image_raw (image de la caméra du TurtleBot3)
  - Fait tourner detect_anomalies() (YOLOv8 si dispo, sinon fallback OpenCV)
  - Si une anomalie est détectée :
      * sauvegarde une photo (pour le rapport PDF)
      * publie un message AnomalyEvent sur /anomaly_event (pour inspection_commander)
      * publie une alerte JSON sur MQTT topic "inspection/alerts" (pour le dashboard)

Usage :
    ros2 run inspection_bot_vision anomaly_detector
"""

import json
import os
import time
from datetime import datetime, timezone

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import paho.mqtt.client as mqtt

try:
    from inspection_bot_msgs.msg import AnomalyEvent
    HAVE_ANOMALY_MSG = True
except ImportError:
    HAVE_ANOMALY_MSG = False

from inspection_bot_vision.detectors import detect_anomalies


MQTT_BROKER_HOST = os.environ.get("MQTT_BROKER_HOST", "localhost")
MQTT_BROKER_PORT = int(os.environ.get("MQTT_BROKER_PORT", "1883"))
MQTT_ALERT_TOPIC = "inspection/alerts"

SNAPSHOT_DIR = os.environ.get(
    "INSPECTION_SNAPSHOT_DIR",
    os.path.expanduser("~/inspection_bot_snapshots"),
)

# Anti-spam : ne pas republier la même anomalie sur le même rack en boucle
RE_ALERT_COOLDOWN_SEC = 15.0


class AnomalyDetectorNode(Node):

    def __init__(self):
        super().__init__("anomaly_detector")

        self.bridge = CvBridge()
        self.current_rack_id = "unknown"   # mis à jour via un topic /current_inspection_target si dispo
        self._last_alert_time = {}

        os.makedirs(SNAPSHOT_DIR, exist_ok=True)

        self.declare_parameter("yolo_weights_path", "")
        self.yolo_weights_path = self.get_parameter("yolo_weights_path").value or None

        self.create_subscription(Image, "/camera/image_raw", self.on_image, 5)

        # Optionnel : si inspection_commander publie le rack courant sur
        # /current_inspection_target (std_msgs/String), décommente ces deux
        # lignes pour que les alertes soient étiquetées avec le bon rack_id
        # au lieu de "unknown".
        # from std_msgs.msg import String
        # self.create_subscription(String, "/current_inspection_target", self.on_current_target, 5)

        if HAVE_ANOMALY_MSG:
            self.anomaly_pub = self.create_publisher(AnomalyEvent, "/anomaly_event", 10)
        else:
            self.anomaly_pub = None
            self.get_logger().warn(
                "inspection_bot_msgs indisponible -> publication ROS2 désactivée, "
                "seule l'alerte MQTT sera envoyée."
            )

        self.mqtt_client = mqtt.Client()
        try:
            self.mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, keepalive=30)
            self.mqtt_client.loop_start()
            self.get_logger().info(f"Connecté au broker MQTT {MQTT_BROKER_HOST}:{MQTT_BROKER_PORT}")
        except Exception as e:
            self.get_logger().error(f"Connexion MQTT impossible : {e}")

        self.get_logger().info("Nœud anomaly_detector prêt.")

    def on_current_target(self, msg):
        self.current_rack_id = msg.data

    def on_image(self, msg: Image):
        frame_bgr = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        detections = detect_anomalies(frame_bgr, yolo_weights_path=self.yolo_weights_path)

        for det in detections:
            key = (self.current_rack_id, det.anomaly_type)
            now = time.time()
            if now - self._last_alert_time.get(key, 0) < RE_ALERT_COOLDOWN_SEC:
                continue
            self._last_alert_time[key] = now

            image_path = self._save_snapshot(frame_bgr, det)
            self._publish_ros_event(det, image_path)
            self._publish_mqtt_alert(det, image_path)

    def _save_snapshot(self, frame_bgr, det) -> str:
        import cv2
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
        filename = f"{self.current_rack_id}_{det.anomaly_type}_{timestamp}.jpg"
        path = os.path.join(SNAPSHOT_DIR, filename)
        cv2.imwrite(path, frame_bgr)
        return path

    def _publish_ros_event(self, det, image_path):
        if self.anomaly_pub is None:
            return
        msg = AnomalyEvent()
        msg.anomaly_type = det.anomaly_type
        msg.rack_id = self.current_rack_id
        msg.confidence = float(det.confidence)
        msg.critical = bool(det.critical)
        msg.image_path = image_path
        msg.stamp = self.get_clock().now().to_msg()
        self.anomaly_pub.publish(msg)

    def _publish_mqtt_alert(self, det, image_path):
        payload = {
            "rack_id": self.current_rack_id,
            "anomaly_type": det.anomaly_type,
            "confidence": det.confidence,
            "critical": det.critical,
            "image_path": image_path,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        try:
            self.mqtt_client.publish(MQTT_ALERT_TOPIC, json.dumps(payload), qos=1)
            self.get_logger().info(f"Alerte MQTT envoyée : {payload}")
        except Exception as e:
            self.get_logger().error(f"Échec publication MQTT : {e}")


def main():
    rclpy.init()
    node = AnomalyDetectorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
