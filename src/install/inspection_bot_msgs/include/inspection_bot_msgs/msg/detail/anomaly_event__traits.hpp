// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#ifndef INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__TRAITS_HPP_
#define INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__TRAITS_HPP_

#include "inspection_bot_msgs/msg/detail/anomaly_event__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'robot_pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<inspection_bot_msgs::msg::AnomalyEvent>()
{
  return "inspection_bot_msgs::msg::AnomalyEvent";
}

template<>
inline const char * name<inspection_bot_msgs::msg::AnomalyEvent>()
{
  return "inspection_bot_msgs/msg/AnomalyEvent";
}

template<>
struct has_fixed_size<inspection_bot_msgs::msg::AnomalyEvent>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<inspection_bot_msgs::msg::AnomalyEvent>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<inspection_bot_msgs::msg::AnomalyEvent>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__TRAITS_HPP_
