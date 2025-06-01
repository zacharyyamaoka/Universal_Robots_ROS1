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

1. Edit until it is able to build in ROS2, see the various changes that were made. ✅
- packages have changed
- the way you make plugins change
- generate_parameter_library: https://github.com/PickNikRobotics/generate_parameter_library

2. Verify its building and displaying correctly: ✅

    ros2 launch ur_ros1_description display.launch.py 
    ros2 launch ur3_moveit2_config demo.launch.py 

4. Verify that it works for a new ur package?
    You may need to turn of the bam_eff SRDF
    /home/bam/public_ws/src/Universal_Robots_ROS2_Driver/ur_moveit_config/srdf/ur.srdf.xacro

    The ur_moveit_config is generic and is set to UR5e, so only fors for that!

    This doesn't launch the robot description, you need to do that seperately!
    The type is not really used at all! just to name the srdf...

    To test:
    ros2 launch ur_description view_ur.launch.py ur_type:=ur5e 

    To launch:
    ros2 launch ur_description view_ur_ns.launch.py ur_type:=ur5e launch_rviz:=false launch_pub_gui:=false  
    ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur5e launch_rviz:=true 

    Edit `kinematics.yaml` to be like this:
    
    ```
    manipulator:
        kinematics_solver: ur_kinematics/UR5eKinematicsPlugin
        kinematics_solver_search_resolution: 0.0050000000000000001
        kinematics_solver_timeout: 0.0050000000000000001
    ```

    I think I will need to add the correct frame for the IK!

    Yes this is a helpful debug message:

    ```
    [rviz2-3] [INFO] [1748807100.743650753] [bam_GPU.moveit_350047040.moveit.kinematics.ur_kinematics_plugin]: Initalizing IK
    [rviz2-3] [INFO] [1748807100.743705237] [bam_GPU.moveit_350047040.moveit.kinematics.ur_kinematics_plugin]: UR link [0]: base_link ✅
    [rviz2-3] [INFO] [1748807100.743711389] [bam_GPU.moveit_350047040.moveit.kinematics.ur_kinematics_plugin]: UR link [1]: wrist_3_link ✅
    [rviz2-3] [ERROR] [1748807100.743715877] [bam_GPU.moveit_350047040.moveit.kinematics.ur_kinematics_plugin]: UR link 'ee_link' not found in the robot model! Check your URDF.
    ```

    Ok I belive this is caused by not wrapping the angles:

    ```
    [move_group-2] [INFO] [1748807893.427285790] [bam_GPU.move_group]: Calling Planner 'Pilz Industrial Motion Planner'
    [move_group-2] [INFO] [1748807893.427292834] [bam_GPU.moveit.moveit.planners.pilz.trajectory_generator]: Generating PTP trajectory...
    [move_group-2] [ERROR] [1748807893.427318352] [bam_GPU.moveit.moveit.planners.pilz.trajectory_generator]: Joint "elbow_joint" violates joint limits in goal constraints
    [move_group-2] [ERROR] [1748807893.427352006] [bam_GPU.move_group]: Planner 'Pilz Industrial Motion Planner' failed with error code INVALID_GOAL_CONSTRAINTS
    [move_group-2] [INFO] [1748807893.427386833] [bam_GPU.moveit.moveit.ros.move_group.move_action]: INVALID_GOAL_CONSTRAINTS
    ```

3. Create Package with BAM dh params ✅

