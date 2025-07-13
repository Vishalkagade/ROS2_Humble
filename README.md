# My Robot Controller

A ROS2 package containing various turtle controller nodes for the turtlesim simulator.

## Description

This package provides several ROS2 nodes for controlling and monitoring a turtle in the turtlesim simulator:

- **turtle_controller**: A reactive controller that moves the turtle forward based on pose feedback
- **draw_circle**: Makes the turtle draw a circle by publishing continuous velocity commands
- **pose_subscriber**: Subscribes to turtle pose data and logs it to the console
- **test_node**: A simple test node that prints "Hello" messages periodically

## Dependencies

- ROS2 (tested with ROS2 Humble/Foxy)
- Python 3.6+
- rclpy
- geometry_msgs
- turtlesim

## Installation

1. Clone this package into your ROS2 workspace:

```bash
cd ~/ros2_ws/src
git clone <repository_url> my_robot_controller
```

2. Install dependencies:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

3. Build the package:

```bash
colcon build --packages-select my_robot_controller
```

4. Source the workspace:

```bash
source install/setup.bash
```

## Usage

### Prerequisites

First, start the turtlesim simulator:

```bash
ros2 run turtlesim turtlesim_node
```

### Available Nodes

#### 1. Turtle Controller

A reactive controller that moves the turtle forward when it receives pose updates:

```bash
ros2 run my_robot_controller turtle_controller
```

#### 2. Draw Circle

Makes the turtle draw a circle continuously:

```bash
ros2 run my_robot_controller draw_circle
```

#### 3. Pose Subscriber

Subscribes to turtle pose and displays it in the terminal:

```bash
ros2 run my_robot_controller pose_subscriber
```

#### 4. Test Node

A simple test node that prints periodic messages:

```bash
ros2 run my_robot_controller test_node
```

### Running Multiple Nodes

You can run multiple nodes simultaneously. For example, to visualize the turtle's pose while controlling it:

Terminal 1:

```bash
ros2 run turtlesim turtlesim_node
```

Terminal 2:

```bash
ros2 run my_robot_controller turtle_controller
```

Terminal 3:

```bash
ros2 run my_robot_controller pose_subscriber
```

## Node Details

### TurtleControllerNode

- **Publishes to**: `/turtle1/cmd_vel` (geometry_msgs/Twist)
- **Subscribes to**: `/turtle1/pose` (turtlesim/Pose)
- **Behavior**: Moves the turtle forward at 5.0 m/s when pose updates are received

### DrawCircleNode

- **Publishes to**: `/turtle1/cmd_vel` (geometry_msgs/Twist)
- **Behavior**: Continuously publishes velocity commands to make the turtle draw a circle
- **Parameters**: Linear velocity: 2.0 m/s, Angular velocity: 1.0 rad/s

### PoseSubscriberNode

- **Subscribes to**: `/turtle1/pose` (turtlesim/Pose)
- **Behavior**: Logs received pose information to the console

### TestNode

- **Behavior**: Prints "Hello" message every second

## File Structure

```text
my_robot_controller/
├── my_robot_controller/
│   ├── __init__.py
│   ├── turtle_controller.py    # Main turtle controller
│   ├── draw_circle.py          # Circle drawing node
│   ├── pose_subscriber.py      # Pose monitoring node
│   └── my_first_node.py        # Test node
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

## Development

### Adding New Nodes

1. Create a new Python file in the `my_robot_controller/` directory
2. Implement your node class inheriting from `rclpy.node.Node`
3. Add the entry point in `setup.py`:

```python
entry_points={
    'console_scripts': [
        "your_node_name = my_robot_controller.your_file:main"
    ],
},
```

### Testing

Run the test suite:

```bash
colcon test --packages-select my_robot_controller
```

## Troubleshooting

- **Node not found**: Make sure you've sourced your workspace (`source install/setup.bash`)
- **Turtlesim not responding**: Ensure the turtlesim node is running before starting the controller nodes
- **Permission denied**: Make sure Python files have execute permissions (`chmod +x *.py`)
