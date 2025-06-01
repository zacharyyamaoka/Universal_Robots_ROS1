from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

# ros2 launch ur_ros1_description display.launch.py 
def generate_launch_description():
    ld = LaunchDescription()

    description_package = FindPackageShare('ur_ros1_description')
    default_model_path = PathJoinSubstitution(['urdf', 'ur3.xacro'])
    default_rviz_config_path = PathJoinSubstitution([description_package, 'cfg', 'urdf.rviz'])

    # These parameters are maintained for backwards compatibility
    gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    ld.add_action(gui_arg)
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                     description='Absolute path to rviz config file')
    ld.add_action(rviz_arg)

    # This parameter has changed its meaning slightly from previous versions

    model_arg = DeclareLaunchArgument(name='model', default_value=default_model_path,
                                        description='Path to robot urdf file relative to urdf_tutorial package')
    ld.add_action(model_arg)

    package_arg = DeclareLaunchArgument(name='package', default_value='ur_ros1_description',
                                        description='Path to package with urdf_file')
    ld.add_action(package_arg)

    
    # add a nestested launch file from urdf_launch package
    # this launch files requires that you define certain launch arguments!

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': LaunchConfiguration('package') , #name of package where urdf model is in
            'urdf_package_path': LaunchConfiguration('model'), #path to urdf file in the package
            'rviz_config': LaunchConfiguration('rvizconfig'),
            # 'jsp_gui': LaunchConfiguration('gui')
            }.items()
    ))

    return ld
