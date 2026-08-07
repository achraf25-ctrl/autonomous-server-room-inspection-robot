// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#ifndef INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__STRUCT_H_
#define INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'anomaly_type'
// Member 'rack_id'
// Member 'image_path'
#include "rosidl_runtime_c/string.h"
// Member 'robot_pose'
#include "geometry_msgs/msg/detail/pose__struct.h"
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in msg/AnomalyEvent in the package inspection_bot_msgs.
typedef struct inspection_bot_msgs__msg__AnomalyEvent
{
  rosidl_runtime_c__String anomaly_type;
  rosidl_runtime_c__String rack_id;
  float confidence;
  bool critical;
  geometry_msgs__msg__Pose robot_pose;
  rosidl_runtime_c__String image_path;
  builtin_interfaces__msg__Time stamp;
} inspection_bot_msgs__msg__AnomalyEvent;

// Struct for a sequence of inspection_bot_msgs__msg__AnomalyEvent.
typedef struct inspection_bot_msgs__msg__AnomalyEvent__Sequence
{
  inspection_bot_msgs__msg__AnomalyEvent * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} inspection_bot_msgs__msg__AnomalyEvent__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__STRUCT_H_
