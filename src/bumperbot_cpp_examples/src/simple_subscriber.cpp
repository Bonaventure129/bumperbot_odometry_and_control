#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

using std::placeholders::_1;
using namespace rclcpp;         // Removes 'rclcpp::'
using namespace std_msgs::msg;  // Removes 'std_msgs::msg::'

class SimpleSubscriber : public Node
{
public:
  SimpleSubscriber() : Node("simple_subscriber1")
  {
    // Simpler types in the template: <String> instead of <std_msgs::msg::String>
    sub_ = create_subscription<String>(
        "chatter", 10, std::bind(&SimpleSubscriber::msgCallback, this, _1));
  }

private:
  // Much shorter declaration
  Subscription<String>::SharedPtr sub_;

  void msgCallback(const String &msg) const
  {
    // 'this->' is technically optional in C++ member functions, so we can remove it too
    RCLCPP_INFO_STREAM(get_logger(), "I heard: " << msg.data.c_str());
  }
};

int main(int argc, char * argv[])
{
  init(argc, argv); // Removes rclcpp::
  spin(std::make_shared<SimpleSubscriber>());
  shutdown();
  return 0;
}