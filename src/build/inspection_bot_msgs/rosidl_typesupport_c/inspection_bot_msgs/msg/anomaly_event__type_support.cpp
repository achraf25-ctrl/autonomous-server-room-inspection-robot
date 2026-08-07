// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "inspection_bot_msgs/msg/rosidl_typesupport_c__visibility_control.h"
#include "inspection_bot_msgs/msg/detail/anomaly_event__struct.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace inspection_bot_msgs
{

namespace msg
{

namespace rosidl_typesupport_c
{

typedef struct _AnomalyEvent_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AnomalyEvent_type_support_ids_t;

static const _AnomalyEvent_type_support_ids_t _AnomalyEvent_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _AnomalyEvent_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AnomalyEvent_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AnomalyEvent_type_support_symbol_names_t _AnomalyEvent_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, inspection_bot_msgs, msg, AnomalyEvent)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, inspection_bot_msgs, msg, AnomalyEvent)),
  }
};

typedef struct _AnomalyEvent_type_support_data_t
{
  void * data[2];
} _AnomalyEvent_type_support_data_t;

static _AnomalyEvent_type_support_data_t _AnomalyEvent_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AnomalyEvent_message_typesupport_map = {
  2,
  "inspection_bot_msgs",
  &_AnomalyEvent_message_typesupport_ids.typesupport_identifier[0],
  &_AnomalyEvent_message_typesupport_symbol_names.symbol_name[0],
  &_AnomalyEvent_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t AnomalyEvent_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AnomalyEvent_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace msg

}  // namespace inspection_bot_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_inspection_bot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, inspection_bot_msgs, msg, AnomalyEvent)() {
  return &::inspection_bot_msgs::msg::rosidl_typesupport_c::AnomalyEvent_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
