import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vishal/ros2_ws/src/my_robot_controller/install/my_robot_controller'
