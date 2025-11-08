#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParamNode(Node):
    def __init__(self):
        super().__init__('simple_param_node')

        # Declare parameters with default values
        self.declare_parameter('robot_name', 'BonaBot')
        self.declare_parameter('speed_limit', 1.0)
        self.declare_parameter('use_sensors', True)

        # Initialize local copies
        self.robot_name = self.get_parameter('robot_name').value
        self.speed_limit = self.get_parameter('speed_limit').value
        self.use_sensors = self.get_parameter('use_sensors').value

        # Log startup parameters
        self.get_logger().info('--- Node Started ---')
        self.log_parameters()

        # Add callback for parameter updates
        self.add_on_set_parameters_callback(self.param_callback)

    def param_callback(self, params):
        """Handle parameter updates instantly."""
        for param in params:
            if param.name == 'speed_limit' and param.type_ == param.Type.DOUBLE:
                self.speed_limit = param.value
                self.get_logger().info(f'⚡ Speed Limit changed instantly to: {self.speed_limit}')

            elif param.name == 'robot_name' and param.type_ == param.Type.STRING:
                self.robot_name = param.value
                self.get_logger().info(f'🤖 Robot Name updated to: {self.robot_name}')

            elif param.name == 'use_sensors' and param.type_ == param.Type.BOOL:
                self.use_sensors = param.value
                self.get_logger().info(f'📡 Sensor usage toggled to: {self.use_sensors}')

        return SetParametersResult(successful=True)

    def log_parameters(self):
        """Helper to print all parameter values."""
        self.get_logger().info(f'Robot Name: {self.robot_name}')
        self.get_logger().info(f'Speed Limit: {self.speed_limit}')
        self.get_logger().info(f'Use Sensors: {self.use_sensors}')


def main(args=None):
    rclpy.init(args=args)
    simple_parameter_node = SimpleParamNode()
    rclpy.spin(simple_parameter_node)
    simple_parameter_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
