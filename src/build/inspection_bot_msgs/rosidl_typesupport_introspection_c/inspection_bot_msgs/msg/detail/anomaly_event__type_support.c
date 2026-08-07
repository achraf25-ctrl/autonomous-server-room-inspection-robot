// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "inspection_bot_msgs/msg/detail/anomaly_event__rosidl_typesupport_introspection_c.h"
#include "inspection_bot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "inspection_bot_msgs/msg/detail/anomaly_event__functions.h"
#include "inspection_bot_msgs/msg/detail/anomaly_event__struct.h"


// Include directives for member types
// Member `anomaly_type`
// Member `rack_id`
// Member `image_path`
#include "rosidl_runtime_c/string_functions.h"
// Member `robot_pose`
#include "geometry_msgs/msg/pose.h"
// Member `robot_pose`
#include "geometry_msgs/msg/detail/pose__rosidl_typesupport_introspection_c.h"
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  inspection_bot_msgs__msg__AnomalyEvent__init(message_memory);
}

void AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_fini_function(void * message_memory)
{
  inspection_bot_msgs__msg__AnomalyEvent__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_member_array[7] = {
  {
    "anomaly_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, anomaly_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rack_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, rack_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "confidence",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, confidence),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "critical",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, critical),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "robot_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, robot_pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "image_path",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, image_path),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(inspection_bot_msgs__msg__AnomalyEvent, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_members = {
  "inspection_bot_msgs__msg",  // message namespace
  "AnomalyEvent",  // message name
  7,  // number of fields
  sizeof(inspection_bot_msgs__msg__AnomalyEvent),
  AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_member_array,  // message members
  AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_init_function,  // function to initialize message memory (memory has to be allocated)
  AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_type_support_handle = {
  0,
  &AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_inspection_bot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, inspection_bot_msgs, msg, AnomalyEvent)() {
  AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_member_array[6].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_type_support_handle.typesupport_identifier) {
    AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &AnomalyEvent__rosidl_typesupport_introspection_c__AnomalyEvent_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
