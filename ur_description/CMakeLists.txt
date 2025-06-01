cmake_minimum_required(VERSION 3.10)
project(ur_ros1_description)

# Find ament packages
find_package(ament_cmake REQUIRED)

# Install resources
install(DIRECTORY cfg config launch meshes urdf
  DESTINATION share/${PROJECT_NAME}
)

# Package
ament_package()