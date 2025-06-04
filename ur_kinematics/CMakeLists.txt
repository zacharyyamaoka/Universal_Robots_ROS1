cmake_minimum_required(VERSION 3.8)
project(ur_kinematics)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(pluginlib REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(moveit_core REQUIRED)
find_package(moveit_kinematics REQUIRED)
find_package(moveit_ros_planning REQUIRED)
find_package(moveit_msgs REQUIRED)
find_package(Boost REQUIRED COMPONENTS system)
find_package(tf2_kdl REQUIRED)
find_package(generate_parameter_library REQUIRED)

include_directories(include ${Boost_INCLUDE_DIRS})


###########
## Build ##
###########

generate_parameter_library(
  ur_kinematics_parameters
  src/ur_kinematics_parameters.yaml
)


add_library(dummy_dh_kin src/ur_kin.cpp)
set_target_properties(dummy_dh_kin PROPERTIES COMPILE_DEFINITIONS "DUMMY_DH_PARAMS")

add_library(bam_arm_kin src/ur_kin.cpp)
set_target_properties(bam_arm_kin PROPERTIES COMPILE_DEFINITIONS "BAM_ARM_PARAMS")

add_library(ur3_kin src/ur_kin.cpp)
set_target_properties(ur3_kin PROPERTIES COMPILE_DEFINITIONS "UR3_PARAMS")

add_library(ur3e_kin src/ur_kin.cpp)
set_target_properties(ur3e_kin PROPERTIES COMPILE_DEFINITIONS "UR3e_PARAMS")

add_library(ur5_kin src/ur_kin.cpp)
set_target_properties(ur5_kin PROPERTIES COMPILE_DEFINITIONS "UR5_PARAMS")

add_library(ur5e_kin src/ur_kin.cpp)
set_target_properties(ur5e_kin PROPERTIES COMPILE_DEFINITIONS "UR5e_PARAMS")

add_library(ur10_kin src/ur_kin.cpp)
set_target_properties(ur10_kin PROPERTIES COMPILE_DEFINITIONS "UR10_PARAMS")

add_library(ur10e_kin src/ur_kin.cpp)
set_target_properties(ur10e_kin PROPERTIES COMPILE_DEFINITIONS "UR10e_PARAMS")

add_library(ur16e_kin src/ur_kin.cpp)
set_target_properties(ur16e_kin PROPERTIES COMPILE_DEFINITIONS "UR16e_PARAMS")

add_library(ur20_kin src/ur_kin.cpp)
set_target_properties(ur20_kin PROPERTIES COMPILE_DEFINITIONS "UR20_PARAMS")

add_library(ur30_kin src/ur_kin.cpp)
set_target_properties(ur30_kin PROPERTIES COMPILE_DEFINITIONS "UR30_PARAMS")

add_library(dummy_dh_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(dummy_dh_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "DUMMY_DH_PARAMS;DUMMY_ROBOT")
target_link_libraries(dummy_dh_moveit_plugin dummy_dh_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(dummy_dh_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(bam_arm_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(bam_arm_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "BAM_ARM_PARAMS;BAM_ROBOT")
target_link_libraries(bam_arm_moveit_plugin bam_arm_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(bam_arm_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur3_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur3_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR3_PARAMS;UR_ROBOT")
target_link_libraries(ur3_moveit_plugin ur3_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur3_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur3e_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur3e_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR3e_PARAMS;UR_ROBOT")
target_link_libraries(ur3e_moveit_plugin ur3e_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur3e_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur5_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur5_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR5_PARAMS;UR_ROBOT")
target_link_libraries(ur5_moveit_plugin ur5_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur5_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur5e_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur5e_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR5e_PARAMS;UR_ROBOT")
target_link_libraries(ur5e_moveit_plugin ur5e_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur5e_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur10_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur10_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR10_PARAMS;UR_ROBOT")
target_link_libraries(ur10_moveit_plugin ur10_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur10_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur10e_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur10e_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR10e_PARAMS;UR_ROBOT")
target_link_libraries(ur10e_moveit_plugin ur10e_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur10e_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur16e_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur16e_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR16e_PARAMS;UR_ROBOT")
target_link_libraries(ur16e_moveit_plugin ur16e_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur16e_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur20_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur20_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR20_PARAMS;UR_ROBOT")
target_link_libraries(ur20_moveit_plugin ur20_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur20_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )

add_library(ur30_moveit_plugin SHARED src/ur_moveit_plugin.cpp)
set_target_properties(ur30_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR30_PARAMS;UR_ROBOT")
target_link_libraries(ur30_moveit_plugin ur30_kin ${Boost_LIBRARIES} ur_kinematics_parameters)
ament_target_dependencies(ur30_moveit_plugin
  rclcpp tf2_kdl moveit_msgs geometry_msgs pluginlib tf2_geometry_msgs moveit_core moveit_kinematics moveit_ros_planning Boost )



#############
## Install ##
#############

install(TARGETS
  dummy_dh_kin dummy_dh_moveit_plugin
  bam_arm_kin bam_arm_moveit_plugin
  ur3_kin ur3e_kin ur5_kin ur5e_kin ur10_kin ur10e_kin ur16e_kin ur20_kin ur30_kin
  ur3_moveit_plugin ur3e_moveit_plugin ur5_moveit_plugin ur5e_moveit_plugin
  ur10_moveit_plugin ur10e_moveit_plugin ur16e_moveit_plugin ur20_moveit_plugin ur30_moveit_plugin
  ur_kinematics_parameters
  EXPORT ${PROJECT_NAME}Targets
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

install(DIRECTORY include/
  DESTINATION include
)

# install(FILES ur_moveit_plugins.xml
#   DESTINATION share/${PROJECT_NAME}
# )

pluginlib_export_plugin_description_file(
  moveit_core ur_moveit_plugins.xml)

ament_export_targets(${PROJECT_NAME}Targets HAS_LIBRARY_TARGET)

ament_package()