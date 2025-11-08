#!/usr/bin/env python3
"""
A simple ROS 2 service server in Python (rclpy)
This server adds two integers sent in a service request and returns the sum.
"""

import rclpy
from rclpy.node import Node

# Import the custom service interface
from bumperbot_msgs.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')

        # Create a service named 'add_two_ints'
        # It uses our custom service type AddTwoInts
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info("Service Server 'add_two_ints' is ready to receive requests.")

    def add_two_ints_callback(self, request, response):
        """
        This callback is automatically triggered when a client calls the service.
        It receives the request (with a and b), computes the sum, and returns it.
        """
        response.sum = request.a + request.b
        self.get_logger().info(f"Received request: a={request.a}, b={request.b}")
        self.get_logger().info(f"Returning response: sum={response.sum}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Service Server stopped manually.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
