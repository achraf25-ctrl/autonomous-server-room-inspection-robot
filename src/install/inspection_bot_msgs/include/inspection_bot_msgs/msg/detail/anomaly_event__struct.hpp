// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#ifndef INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__STRUCT_HPP_
#define INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'robot_pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__inspection_bot_msgs__msg__AnomalyEvent __attribute__((deprecated))
#else
# define DEPRECATED__inspection_bot_msgs__msg__AnomalyEvent __declspec(deprecated)
#endif

namespace inspection_bot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AnomalyEvent_
{
  using Type = AnomalyEvent_<ContainerAllocator>;

  explicit AnomalyEvent_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_pose(_init),
    stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anomaly_type = "";
      this->rack_id = "";
      this->confidence = 0.0f;
      this->critical = false;
      this->image_path = "";
    }
  }

  explicit AnomalyEvent_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : anomaly_type(_alloc),
    rack_id(_alloc),
    robot_pose(_alloc, _init),
    image_path(_alloc),
    stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->anomaly_type = "";
      this->rack_id = "";
      this->confidence = 0.0f;
      this->critical = false;
      this->image_path = "";
    }
  }

  // field types and members
  using _anomaly_type_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _anomaly_type_type anomaly_type;
  using _rack_id_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _rack_id_type rack_id;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _critical_type =
    bool;
  _critical_type critical;
  using _robot_pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _robot_pose_type robot_pose;
  using _image_path_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _image_path_type image_path;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__anomaly_type(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->anomaly_type = _arg;
    return *this;
  }
  Type & set__rack_id(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->rack_id = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__critical(
    const bool & _arg)
  {
    this->critical = _arg;
    return *this;
  }
  Type & set__robot_pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->robot_pose = _arg;
    return *this;
  }
  Type & set__image_path(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->image_path = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator> *;
  using ConstRawPtr =
    const inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__inspection_bot_msgs__msg__AnomalyEvent
    std::shared_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__inspection_bot_msgs__msg__AnomalyEvent
    std::shared_ptr<inspection_bot_msgs::msg::AnomalyEvent_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnomalyEvent_ & other) const
  {
    if (this->anomaly_type != other.anomaly_type) {
      return false;
    }
    if (this->rack_id != other.rack_id) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->critical != other.critical) {
      return false;
    }
    if (this->robot_pose != other.robot_pose) {
      return false;
    }
    if (this->image_path != other.image_path) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnomalyEvent_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnomalyEvent_

// alias to use template instance with default allocator
using AnomalyEvent =
  inspection_bot_msgs::msg::AnomalyEvent_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace inspection_bot_msgs

#endif  // INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__STRUCT_HPP_
