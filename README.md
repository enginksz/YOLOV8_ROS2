# YOLOV8_ROS2

This repository contains the implementation of **YOLOv8** integrated with **ROS 2 (Robot Operating System 2)** for real-time object detection. YOLOv8 is the version of the "You Only Look Once" (YOLO) family of models, designed for efficient and accurate object detection.

## Features

- **YOLOv8 integration**: Utilize the latest advancements in object detection using the YOLOv8 architecture.
- **ROS 2 support**: Communicate and control through ROS 2, making it easier to use in robotics applications.
- **Real-time detection**: Optimized for real-time object detection on robotic platforms.
- **Extensible design**: Easily customizable for different detection tasks and sensors.

## Requirements

To run this project, you need to have the following installed:

- Python 3.8+
- ROS 2 (Foxy, Galactic, or later)
- PyTorch
- OpenCV
- TensorRT (optional for GPU acceleration)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/enginksz/YOLOV8_ROS2.git
    cd YOLOV8_ROS2
    ```

2. Install dependencies:

    ```bash
    pip install ultralytics
    sudo apt install gazebo
    sudo apt install python3-colcon-common-extensions
    sudo apt install ros-foxy-gazebo-ros
    ```

3. Ensure that ROS 2 is properly installed and sourced on your machine.

## Running YOLOv8 with ROS 2

1. Colcon build:

    ```bash
    cd yolov8_ros2
    colcon build
    source yolov8_ros2/install/setup.bash
    ```

2. Launch ROS 2 nodes:

    ```bash
    ros2 launch yolov8_gazebo yolov8_ros2_launch.py
    ```

    Open a second terminal for recognition:

    ```bash
    ros2 launch yolov8_ros2_recognition launch_yolov8.launch.py
    ```

3. Start detection by publishing images to the corresponding ROS 2 topic.

## Usage

### ROS 2 Topics

- `/image_raw`: Input image topic for object detection.
- `/yolov8/detections`: Output topic with detected objects.

## Contributing

Feel free to submit issues, create pull requests, or fork this repository to improve and extend the project.
