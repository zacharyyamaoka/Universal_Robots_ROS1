# Taken from
https://github.com/ros-industrial/universal_robot/tree/indigo-devel/ur_kinematics

I made various edits to port it to ROS2

See how to make plugins in ROS2
https://docs.ros.org/en/kilted/Tutorials/Beginner-Client-Libraries/Pluginlib.html

You can also reference the existing Moveit Kinematic Plugins:
https://github.com/moveit/moveit2/tree/main/moveit_kinematics

Plan on Action
1 - Verify that the kinematics work within the package
- If I remember there was some issues with the RVIZ marker skipping around...
- In order to do this build 
    - moveit package
    - ur_ros1_descriptions -> ur_ros1_descriptions
    - ur_kinematics

# edits where made so it can build with ROS2


# Steps for Porting

1. Edit until it is able to build in ROS2, see the various changes that were made.
- packages have changed
- the way you make plugins change

Verify its building and displaying correctly:

    ros2 launch ur_ros1_description display.launch.py 
    ros2 launch ur3_moveit2_config demo.launch.py 
