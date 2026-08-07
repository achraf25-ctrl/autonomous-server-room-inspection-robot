🤖 Server Room Inspector Robot — Autonomous Virtual TechnicianSimulated mobile robot (TurtleBot3 + Gazebo) that navigates autonomously through a server room, plans its inspection route by solving a Travelling Salesperson Problem (TSP), detects visual anomalies (red indicator lights, unplugged cables, open rack doors, smoke), sends real-time alerts via MQTT to a web dashboard, and generates an automatic room health PDF report at the end of each inspection run.ArchitectureGazebo (3D server room + TurtleBot3)
        │  /scan (LiDAR)   /camera/image_raw (RGB)
        ▼
ROS 2 : SLAM Toolbox + Nav2  ──────────────►  inspection_bot_nav
        │                                        │  (TSP + commander)
        ▼                                        ▼
inspection_bot_vision (YOLOv8 / OpenCV detector) → /anomaly_event
        │
        ▼  MQTT (topic inspection/alerts)
inspection_bot_dashboard (Flask + Socket.IO)
        │
        ▼
Automated PDF Report (report_generator.py)
Repository Structure (ROS 2 Packages + Web App)inspection_bot_ws/
├── src/
│   ├── inspection_bot_bringup/     # Launches Gazebo + SLAM + Nav2 + nodes
│   ├── inspection_bot_description/ # Gazebo world (server room) + camera URDF
│   ├── inspection_bot_msgs/        # Custom ROS 2 message AnomalyEvent.msg
│   ├── inspection_bot_nav/         # TSP planner + inspection commander
│   ├── inspection_bot_vision/      # Anomaly detection (YOLOv8 + OpenCV fallback)
│   └── inspection_bot_dashboard/   # Flask dashboard + PDF generation
├── requirements.txt
├── docker-compose.yml              # MQTT Broker (Mosquitto) + dashboard, to test
│                                   # the web interface WITHOUT having ROS 2/Gazebo installed
└── README.md
Ready-to-Run Components vs. ROS 2 Environment RequirementsComponentStatusTSP planner (tsp_planner.py)✅ Pure Python code, instantly testable without ROS 2Flask dashboard + PDF generation✅ Instantly testable using python3 app.pyOpenCV anomaly detector (red lights)✅ Testable on any image/webcamYOLOv8 detector (ultralytics)⚠️ Code provided, but requires pip install ultralytics + trained weights — automatically falls back to the OpenCV detector if the model is not foundGazebo world, Nav2/SLAM launch, ROS 2 nodes⚠️ Requires a ROS 2 installation (Humble/Iron recommended) + Gazebo + turtlebot3, nav2_bringup, and slam_toolbox packagesThis environment cannot run Gazebo/ROS 2 (no display, no ROS 2 packages installed), so these files are written to be correct and ready to use on your Ubuntu machine with ROS 2, but could not be executed here. Everything written in pure Python (TSP, dashboard, OpenCV detector, PDF generation) has been tested and works.Installation (On Your Machine with ROS 2 Installed)Bash# 1. ROS 2 system dependencies (Humble recommended)
sudo apt install ros-humble-turtlebot3* ros-humble-nav2-bringup ros-humble-slam-toolbox ros-humble-nav2-simple-commander

# 2. Python dependencies
cd inspection_bot_ws
pip install -r requirements.txt --break-system-packages

# 3. Build ROS 2 workspace
export TURTLEBOT3_MODEL=waffle_pi
colcon build --symlink-install
source install/setup.bash
Running the Project, Phase by PhasePhase 1 — Navigation (Gazebo + SLAM + Nav2)Bashros2 launch inspection_bot_bringup bringup.launch.py
Open RViz, run teleop or send a waypoint to verify that the robot maps and navigates through the server room correctly.Phase 2 — Inspection Planning (TSP)Bashpython3 src/inspection_bot_nav/inspection_bot_nav/tsp_planner.py
Then, once Nav2 is running:Bashros2 run inspection_bot_nav inspection_commander
Phase 3 — Vision (Anomaly Detection)Bashros2 run inspection_bot_vision anomaly_detector
Phase 4 — Dashboard + MQTT AlertsBashdocker compose up -d mosquitto   # local MQTT broker
cd src/inspection_bot_dashboard
python3 app.py
Open http://localhost:5000Phase 5 — PDF ReportThe dashboard features a "Generate Report" button that calls report_generator.py and generates a PDF inside inspection_bot_dashboard/reports/.Testing the Web Component Without ROS 2 (Quick Demo)A demo script demo_simulate_inspection.py (located in inspection_bot_dashboard/) simulates a full inspection run (rack positions + random anomalies) and feeds data to the dashboard, allowing you to showcase the dashboard UI and PDF report without needing Gazebo during a presentation.
