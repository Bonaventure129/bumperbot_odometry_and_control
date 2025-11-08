#!/usr/bin/env python3
"""
A simple ROS 2 service client in Python (rclpy)
This client sends two integers to the 'add_two_ints' service and prints the result.
"""

import sys
import rclpy
from rclpy.node import Node

# Import the custom service type
from bumperbot_msgs.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')

        # Create a client for the 'add_two_ints' service
        self.client = self.create_client(AddTwoInts, 'add_two_ints')

        # Wait until the service becomes available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service "add_two_ints" to be available...')

        self.request = AddTwoInts.Request()

    def send_request(self, a, b):
        """Fill the request and send it asynchronously."""
        self.request.a = a
        self.request.b = b
        self.get_logger().info(f"Sending request: a={a}, b={b}")

        # Call the service asynchronously
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)

        # Return the response once the service call is complete
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    # Create client node instance
    node = AddTwoIntsClient()

    # Parse command-line arguments for input numbers
    if len(sys.argv) != 3:
        node.get_logger().info("Usage: ros2 run add_two_ints_srv add_two_ints_client <a> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Send the request and receive response
    response = node.send_request(a, b)
    node.get_logger().info(f"Result of {a} + {b} = {response.sum}")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
