#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <chrono>

using namespace std::chrono_literals;
using namespace rclcpp;         // Allows using Node, Publisher, etc. directly
using namespace std_msgs::msg;  // Allows using String directly

class SimplePublisher : public Node
{
public:
  SimplePublisher() : Node("simple_publisher1"), counter_(0)
  {
    // No need for rclcpp:: or std_msgs::msg:: prefixes here
    pub_ = create_publisher<String>("chatter", 10);
    timer_ = create_wall_timer(1s, std::bind(&SimplePublisher::timerCallback, this));
    
    // RCLCPP_INFO is a macro, so it stays the same, but uses get_logger() directly
    RCLCPP_INFO(get_logger(), "Publishing at 1 Hz");
  }

  void timerCallback()
  {
    auto message = String();
    message.data = "Hello ROS 2 - counter:" + std::to_string(counter_++);
    pub_->publish(message);
  }

private:
  // Clean types without long prefixes
  Publisher<String>::SharedPtr pub_;
  TimerBase::SharedPtr timer_;
  unsigned int counter_;
};

int main(int argc, char* argv[])
{
  init(argc, argv); // 'rclcpp::' is removed here too
  auto node = std::make_shared<SimplePublisher>();
  spin(node);
  shutdown();
  return 0;
}