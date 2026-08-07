"""
Lance la simulation complète Phase 1 :
  - Gazebo avec le monde server_room.world
  - Spawn du TurtleBot3 (waffle_pi recommandé : caméra RGB intégrée)
  - SLAM Toolbox (cartographie en ligne)
  - Nav2 bringup (navigation autonome)

Usage :
    export TURTLEBOT3_MODEL=waffle_pi
    ros2 launch inspection_bot_bringup bringup.launch.py
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    description_pkg = get_package_share_directory('inspection_bot_description')
    turtlebot3_gazebo_pkg = get_package_share_directory('turtlebot3_gazebo')
    slam_toolbox_pkg = get_package_share_directory('slam_toolbox')
    nav2_bringup_pkg = get_package_share_directory('nav2_bringup')
    nav_pkg = get_package_share_directory('inspection_bot_nav')

    world_file = os.path.join(description_pkg, 'worlds', 'server_room.world')
    nav2_params_file = os.path.join(nav_pkg, 'config', 'nav2_params.yaml')
    slam_params_file = os.path.join(nav_pkg, 'config', 'slam_toolbox_params.yaml')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # 1. Gazebo avec le monde de la salle serveur (utilise le launch fourni par
    #    turtlebot3_gazebo pour garder le spawn du robot cohérent avec le modèle
    #    choisi via la variable d'environnement TURTLEBOT3_MODEL).
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(turtlebot3_gazebo_pkg, 'launch', 'turtlebot3_world.launch.py')
        ),
        launch_arguments={'world': world_file}.items()
    )

    # 2. SLAM Toolbox — cartographie en ligne pendant la navigation
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(slam_toolbox_pkg, 'launch', 'online_async_launch.py')
        ),
        launch_arguments={
            'slam_params_file': slam_params_file,
            'use_sim_time': use_sim_time,
        }.items()
    )

    # 3. Nav2 — pile de navigation complète (planner, controller, behavior tree...)
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_pkg, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'params_file': nav2_params_file,
            'use_sim_time': use_sim_time,
        }.items()
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='true',
            description='Utiliser le temps simulé de Gazebo'),
        gazebo,
        slam,
        nav2,
    ])
