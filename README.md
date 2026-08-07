# 🤖 Robot Inspecteur de Salle Serveur — Technicien Virtuel Autonome

Robot mobile simulé (TurtleBot3 + Gazebo) qui navigue de manière autonome dans une
salle serveur, planifie sa tournée d'inspection en résolvant un problème de type
TSP, détecte des anomalies visuelles (voyants rouges, câbles débranchés, portes de
rack ouvertes, fumée), remonte des alertes en temps réel via MQTT vers un dashboard
web, et génère un rapport PDF automatique de santé de la salle à la fin de chaque
tournée.

## Architecture

```
Gazebo (salle serveur 3D + TurtleBot3)
        │  /scan (LiDAR)   /camera/image_raw (RGB)
        ▼
ROS 2 : SLAM Toolbox + Nav2  ──────────────►  inspection_bot_nav
        │                                        │  (TSP + commander)
        ▼                                        ▼
inspection_bot_vision (YOLOv8 / détecteur OpenCV) → /anomaly_event
        │
        ▼  MQTT (topic inspection/alerts)
inspection_bot_dashboard (Flask + Socket.IO)
        │
        ▼
Rapport PDF automatique (report_generator.py)
```

## Structure du repo (packages ROS 2 + app web)

```
inspection_bot_ws/
├── src/
│   ├── inspection_bot_bringup/     # Lance Gazebo + SLAM + Nav2 + les nœuds
│   ├── inspection_bot_description/ # Monde Gazebo (salle serveur) + URDF caméra
│   ├── inspection_bot_msgs/        # Message ROS2 custom AnomalyEvent.msg
│   ├── inspection_bot_nav/         # TSP planner + commander d'inspection
│   ├── inspection_bot_vision/      # Détection d'anomalies (YOLOv8 + fallback OpenCV)
│   └── inspection_bot_dashboard/   # Dashboard Flask + génération PDF
├── requirements.txt
├── docker-compose.yml              # Broker MQTT (Mosquitto) + dashboard, pour tester
│                                    # la partie web SANS avoir ROS2/Gazebo installés
└── README.md
```

## Ce qui est fourni "prêt à tourner" vs. ce qui nécessite ton environnement ROS2

| Composant | État |
|---|---|
| TSP planner (`tsp_planner.py`) | ✅ Code pur Python, testable tout de suite, sans ROS2 |
| Dashboard Flask + génération PDF | ✅ Testable tout de suite avec `python3 app.py` |
| Détecteur d'anomalies OpenCV (voyants rouges) | ✅ Testable sur n'importe quelle image/webcam |
| Détecteur YOLOv8 (`ultralytics`) | ⚠️ Code fourni, mais nécessite `pip install ultralytics` + poids entraînés — bascule automatique sur le détecteur OpenCV si le modèle n'est pas trouvé |
| Monde Gazebo, launch Nav2/SLAM, nœuds ROS2 | ⚠️ Nécessite une installation ROS 2 (Humble/Iron recommandé) + Gazebo + les packages `turtlebot3`, `nav2_bringup`, `slam_toolbox` |

Ce sandbox ne peut pas exécuter Gazebo/ROS2 (pas de display, pas de packages ROS2
installés), donc ces fichiers sont écrits pour être corrects et prêts à l'emploi
**sur ta machine Ubuntu avec ROS2**, mais n'ont pas pu être testés ici. Tout ce qui
est en Python pur (TSP, dashboard, détecteur OpenCV, génération PDF) A été testé
dans ce sandbox et fonctionne.

## Installation (sur ta machine, avec ROS2 déjà installé)

```bash
# 1. Dépendances système ROS2 (Humble recommandé)
sudo apt install ros-humble-turtlebot3* ros-humble-nav2-bringup ros-humble-slam-toolbox ros-humble-nav2-simple-commander

# 2. Dépendances Python
cd inspection_bot_ws
pip install -r requirements.txt --break-system-packages

# 3. Build du workspace ROS2
export TURTLEBOT3_MODEL=waffle_pi
colcon build --symlink-install
source install/setup.bash
```

## Lancer le projet, phase par phase

### Phase 1 — Navigation (Gazebo + SLAM + Nav2)
```bash
ros2 launch inspection_bot_bringup bringup.launch.py
```
Ouvre RViz, lance la téléop ou un waypoint pour vérifier que le robot cartographie
et navigue correctement dans la salle serveur.

### Phase 2 — Planification d'inspection (TSP)
```bash
python3 src/inspection_bot_nav/inspection_bot_nav/tsp_planner.py
```
Puis, une fois Nav2 lancé :
```bash
ros2 run inspection_bot_nav inspection_commander
```

### Phase 3 — Vision (détection d'anomalies)
```bash
ros2 run inspection_bot_vision anomaly_detector
```

### Phase 4 — Dashboard + alertes MQTT
```bash
docker compose up -d mosquitto   # broker MQTT local
cd src/inspection_bot_dashboard
python3 app.py
```
Ouvre http://localhost:5000

### Phase 5 — Rapport PDF
Le dashboard expose un bouton "Générer le rapport" qui appelle
`report_generator.py` et produit un PDF dans `inspection_bot_dashboard/reports/`.

## Tester la partie web sans ROS2 (démo rapide)

Un script `demo_simulate_inspection.py` (voir `inspection_bot_dashboard/`) simule
une tournée complète (positions de racks + anomalies aléatoires) et alimente le
dashboard, pour que tu puisses démontrer le rendu du dashboard et du rapport PDF
sans avoir besoin de Gazebo pendant une soutenance.
