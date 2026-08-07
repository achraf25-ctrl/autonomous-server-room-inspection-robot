// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#ifndef INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__BUILDER_HPP_
#define INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__BUILDER_HPP_

#include "inspection_bot_msgs/msg/detail/anomaly_event__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace inspection_bot_msgs
{

namespace msg
{

namespace builder
{

class Init_AnomalyEvent_stamp
{
public:
  explicit Init_AnomalyEvent_stamp(::inspection_bot_msgs::msg::AnomalyEvent & msg)
  : msg_(msg)
  {}
  ::inspection_bot_msgs::msg::AnomalyEvent stamp(::inspection_bot_msgs::msg::AnomalyEvent::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

class Init_AnomalyEvent_image_path
{
public:
  explicit Init_AnomalyEvent_image_path(::inspection_bot_msgs::msg::AnomalyEvent & msg)
  : msg_(msg)
  {}
  Init_AnomalyEvent_stamp image_path(::inspection_bot_msgs::msg::AnomalyEvent::_image_path_type arg)
  {
    msg_.image_path = std::move(arg);
    return Init_AnomalyEvent_stamp(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

class Init_AnomalyEvent_robot_pose
{
public:
  explicit Init_AnomalyEvent_robot_pose(::inspection_bot_msgs::msg::AnomalyEvent & msg)
  : msg_(msg)
  {}
  Init_AnomalyEvent_image_path robot_pose(::inspection_bot_msgs::msg::AnomalyEvent::_robot_pose_type arg)
  {
    msg_.robot_pose = std::move(arg);
    return Init_AnomalyEvent_image_path(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

class Init_AnomalyEvent_critical
{
public:
  explicit Init_AnomalyEvent_critical(::inspection_bot_msgs::msg::AnomalyEvent & msg)
  : msg_(msg)
  {}
  Init_AnomalyEvent_robot_pose critical(::inspection_bot_msgs::msg::AnomalyEvent::_critical_type arg)
  {
    msg_.critical = std::move(arg);
    return Init_AnomalyEvent_robot_pose(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

class Init_AnomalyEvent_confidence
{
public:
  explicit Init_AnomalyEvent_confidence(::inspection_bot_msgs::msg::AnomalyEvent & msg)
  : msg_(msg)
  {}
  Init_AnomalyEvent_critical confidence(::inspection_bot_msgs::msg::AnomalyEvent::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_AnomalyEvent_critical(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

class Init_AnomalyEvent_rack_id
{
public:
  explicit Init_AnomalyEvent_rack_id(::inspection_bot_msgs::msg::AnomalyEvent & msg)
  : msg_(msg)
  {}
  Init_AnomalyEvent_confidence rack_id(::inspection_bot_msgs::msg::AnomalyEvent::_rack_id_type arg)
  {
    msg_.rack_id = std::move(arg);
    return Init_AnomalyEvent_confidence(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

class Init_AnomalyEvent_anomaly_type
{
public:
  Init_AnomalyEvent_anomaly_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnomalyEvent_rack_id anomaly_type(::inspection_bot_msgs::msg::AnomalyEvent::_anomaly_type_type arg)
  {
    msg_.anomaly_type = std::move(arg);
    return Init_AnomalyEvent_rack_id(msg_);
  }

private:
  ::inspection_bot_msgs::msg::AnomalyEvent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::inspection_bot_msgs::msg::AnomalyEvent>()
{
  return inspection_bot_msgs::msg::builder::Init_AnomalyEvent_anomaly_type();
}

}  // namespace inspection_bot_msgs

#endif  // INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__BUILDER_HPP_
