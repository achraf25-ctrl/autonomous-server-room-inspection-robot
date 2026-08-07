cmake_minimum_required(VERSION 3.8)
project(inspection_bot_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY worlds urdf meshes
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
