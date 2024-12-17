from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    # Uruchomienie Gazebo Garden z określonym światem
    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', '-v', '4', '/home/c/Pulpit/gazebo-wolski-gawlowski/camera_sensor.sdf'],  # Podmień na swój plik świata
        output='screen'
    )

    # Node ROS-Gazebo Bridge dla kamery
    ros_gz_bridge_camera = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='camera_bridge',
        arguments=[
            '/camera/image@sensor_msgs/msg/Image@gz.msgs.Image',  # Obraz
            '/camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'  # Informacje o kamerze
        ],
        output='screen'
    )

    # Node RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', '/home/c/Pulpit/rviz_gazebo_config.rviz']  # Podaj ścieżkę do pliku konfiguracyjnego RViz
    )

    return LaunchDescription([
        gazebo,
        ros_gz_bridge_camera,
        rviz
    ])
