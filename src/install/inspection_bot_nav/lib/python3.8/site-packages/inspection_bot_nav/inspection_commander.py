#!/usr/bin/env python3
"""
Nœud ROS2 "chef d'orchestre" de l'inspection :

  1. Charge la liste des racks et calcule l'ordre optimal (TSP, tsp_planner.py)
  2. Envoie les waypoints un par un à Nav2 (nav2_simple_commander)
  3. À chaque rack, marque une pause de quelques secondes pour laisser le
     nœud de vision (anomaly_detector) analyser l'image caméra
  4. Écoute le topic /anomaly_event : si une anomalie CRITIQUE est
     remontée, elle est mise en tête de la file des racks restants
     (le robot y retourne en priorité dès qu'il a fini son point courant)
  5. À la fin de la tournée, déclenche la génération du rapport en
     appelant l'endpoint /api/generate_report du dashboard Flask

Usage :
    ros2 run inspection_bot_nav inspection_commander
"""

import math
import time
from collections import deque

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

try:
    from inspection_bot_msgs.msg import AnomalyEvent
    HAVE_ANOMALY_MSG = True
except ImportError:
    HAVE_ANOMALY_MSG = False

import os
from ament_index_python.packages import get_package_share_directory

from inspection_bot_nav.tsp_planner import load_inspection_points, solve_tsp


DWELL_TIME_PER_RACK_SEC = 4.0   # temps d'arrêt devant chaque rack pour l'inspection visuelle


def yaw_to_quaternion(yaw_deg: float):
    yaw = math.radians(yaw_deg)
    return (0.0, 0.0, math.sin(yaw / 2.0), math.cos(yaw / 2.0))


def make_pose(navigator: BasicNavigator, x: float, y: float, yaw_deg: float) -> PoseStamped:
    pose = PoseStamped()
    pose.header.frame_id = "map"
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    qz_qw = yaw_to_quaternion(yaw_deg)
    pose.pose.orientation.z = qz_qw[2]
    pose.pose.orientation.w = qz_qw[3]
    return pose


class InspectionCommander(Node):

    def __init__(self):
        super().__init__("inspection_commander")

        self.critical_queue = deque()   # racks critiques à revisiter en priorité
        self.visited = set()

        if HAVE_ANOMALY_MSG:
            self.create_subscription(
                AnomalyEvent, "/anomaly_event", self.on_anomaly_event, 10
            )
        else:
            self.get_logger().warn(
                "inspection_bot_msgs indisponible : la logique de retour "
                "prioritaire sur anomalie critique est désactivée."
            )

    def on_anomaly_event(self, msg):
        self.get_logger().info(
            f"Anomalie reçue : {msg.anomaly_type} sur {msg.rack_id} "
            f"(confiance={msg.confidence:.2f}, critique={msg.critical})"
        )
        if msg.critical and msg.rack_id not in self.visited:
            self.get_logger().warn(
                f"⚠️ Anomalie CRITIQUE sur {msg.rack_id} — ajoutée en priorité."
            )
            self.critical_queue.appendleft(msg.rack_id)


def run_inspection_tour():
    rclpy.init()
    node = InspectionCommander()
    navigator = BasicNavigator()

    nav_pkg = get_package_share_directory("inspection_bot_nav")
    points_yaml = os.path.join(nav_pkg, "config", "inspection_points.yaml")

    start_xy, points = load_inspection_points(points_yaml)
    ordered_points, total_distance = solve_tsp(start_xy, points)

    node.get_logger().info(
        f"Tournée planifiée : {len(ordered_points)} racks, "
        f"{total_distance:.1f} m au total."
    )

    navigator.waitUntilNav2Active()

    points_by_id = {p["id"]: p for p in points}
    remaining = deque(ordered_points)

    while remaining or node.critical_queue:
        # Priorité aux racks marqués critiques par la vision
        if node.critical_queue:
            rack_id = node.critical_queue.popleft()
            target = points_by_id[rack_id]
        else:
            target = remaining.popleft()

        goal_pose = make_pose(navigator, target["x"], target["y"], target["yaw_deg"])
        node.get_logger().info(f"→ Direction {target['id']} ({target['x']}, {target['y']})")
        navigator.goToPose(goal_pose)

        while not navigator.isTaskComplete():
            rclpy.spin_once(node, timeout_sec=0.1)

        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            node.get_logger().info(f"✅ Arrivé à {target['id']}, inspection visuelle...")
            node.visited.add(target["id"])
            # Laisse le temps au nœud de vision d'analyser la scène
            end_time = time.time() + DWELL_TIME_PER_RACK_SEC
            while time.time() < end_time:
                rclpy.spin_once(node, timeout_sec=0.1)
        else:
            node.get_logger().error(f"❌ Échec de navigation vers {target['id']} ({result})")

    node.get_logger().info("🏁 Tournée d'inspection terminée. Génération du rapport...")
    try:
        import requests
        requests.post("http://localhost:5000/api/generate_report", timeout=5)
    except Exception as e:
        node.get_logger().warn(f"Impossible d'appeler le dashboard pour le rapport : {e}")

    navigator.lifecycleShutdown()
    rclpy.shutdown()


def main():
    run_inspection_tour()


if __name__ == "__main__":
    main()
