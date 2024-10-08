#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    pkg_yolov8_ros2_gazebo = get_package_share_directory('yolov8_ros2_gazebo')
    pkg_yolov8_ros2_description = get_package_share_directory('yolov8_ros2_description')
    pkg_yolov8_ros2_control = get_package_share_directory('yolov8_ros2_control')
    pkg_yolov8_ros2_recognition = get_package_share_directory('yolov8_ros2_recognition')

    joy_node = Node(
        package = "joy",
        executable = "joy_node"
    )

    start_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolov8_ros2_gazebo, 'launch', 'start_world_launch.py'),
        )
    )

    spawn_robot_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolov8_ros2_description, 'launch', 'spawn_yolov8_ros2_launch.launch.py'),
        )
    )     

    spawn_robot_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolov8_ros2_control, 'launch', 'yolov8_ros2_control.launch.py'),
        )
    )  

    spawn_yolo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_yolov8_ros2_recognition, 'launch', 'launch_yolov8.launch.py'),
        )
    )  

    return LaunchDescription([
        joy_node,
        start_world,
        spawn_robot_world,
        spawn_robot_control,
        spawn_yolo,
    ])