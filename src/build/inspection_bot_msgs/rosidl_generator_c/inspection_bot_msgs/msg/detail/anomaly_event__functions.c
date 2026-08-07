// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice
#include "inspection_bot_msgs/msg/detail/anomaly_event__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `anomaly_type`
// Member `rack_id`
// Member `image_path`
#include "rosidl_runtime_c/string_functions.h"
// Member `robot_pose`
#include "geometry_msgs/msg/detail/pose__functions.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
inspection_bot_msgs__msg__AnomalyEvent__init(inspection_bot_msgs__msg__AnomalyEvent * msg)
{
  if (!msg) {
    return false;
  }
  // anomaly_type
  if (!rosidl_runtime_c__String__init(&msg->anomaly_type)) {
    inspection_bot_msgs__msg__AnomalyEvent__fini(msg);
    return false;
  }
  // rack_id
  if (!rosidl_runtime_c__String__init(&msg->rack_id)) {
    inspection_bot_msgs__msg__AnomalyEvent__fini(msg);
    return false;
  }
  // confidence
  // critical
  // robot_pose
  if (!geometry_msgs__msg__Pose__init(&msg->robot_pose)) {
    inspection_bot_msgs__msg__AnomalyEvent__fini(msg);
    return false;
  }
  // image_path
  if (!rosidl_runtime_c__String__init(&msg->image_path)) {
    inspection_bot_msgs__msg__AnomalyEvent__fini(msg);
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    inspection_bot_msgs__msg__AnomalyEvent__fini(msg);
    return false;
  }
  return true;
}

void
inspection_bot_msgs__msg__AnomalyEvent__fini(inspection_bot_msgs__msg__AnomalyEvent * msg)
{
  if (!msg) {
    return;
  }
  // anomaly_type
  rosidl_runtime_c__String__fini(&msg->anomaly_type);
  // rack_id
  rosidl_runtime_c__String__fini(&msg->rack_id);
  // confidence
  // critical
  // robot_pose
  geometry_msgs__msg__Pose__fini(&msg->robot_pose);
  // image_path
  rosidl_runtime_c__String__fini(&msg->image_path);
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
inspection_bot_msgs__msg__AnomalyEvent__are_equal(const inspection_bot_msgs__msg__AnomalyEvent * lhs, const inspection_bot_msgs__msg__AnomalyEvent * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // anomaly_type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->anomaly_type), &(rhs->anomaly_type)))
  {
    return false;
  }
  // rack_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->rack_id), &(rhs->rack_id)))
  {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // critical
  if (lhs->critical != rhs->critical) {
    return false;
  }
  // robot_pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->robot_pose), &(rhs->robot_pose)))
  {
    return false;
  }
  // image_path
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->image_path), &(rhs->image_path)))
  {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
inspection_bot_msgs__msg__AnomalyEvent__copy(
  const inspection_bot_msgs__msg__AnomalyEvent * input,
  inspection_bot_msgs__msg__AnomalyEvent * output)
{
  if (!input || !output) {
    return false;
  }
  // anomaly_type
  if (!rosidl_runtime_c__String__copy(
      &(input->anomaly_type), &(output->anomaly_type)))
  {
    return false;
  }
  // rack_id
  if (!rosidl_runtime_c__String__copy(
      &(input->rack_id), &(output->rack_id)))
  {
    return false;
  }
  // confidence
  output->confidence = input->confidence;
  // critical
  output->critical = input->critical;
  // robot_pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->robot_pose), &(output->robot_pose)))
  {
    return false;
  }
  // image_path
  if (!rosidl_runtime_c__String__copy(
      &(input->image_path), &(output->image_path)))
  {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

inspection_bot_msgs__msg__AnomalyEvent *
inspection_bot_msgs__msg__AnomalyEvent__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inspection_bot_msgs__msg__AnomalyEvent * msg = (inspection_bot_msgs__msg__AnomalyEvent *)allocator.allocate(sizeof(inspection_bot_msgs__msg__AnomalyEvent), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(inspection_bot_msgs__msg__AnomalyEvent));
  bool success = inspection_bot_msgs__msg__AnomalyEvent__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
inspection_bot_msgs__msg__AnomalyEvent__destroy(inspection_bot_msgs__msg__AnomalyEvent * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    inspection_bot_msgs__msg__AnomalyEvent__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
inspection_bot_msgs__msg__AnomalyEvent__Sequence__init(inspection_bot_msgs__msg__AnomalyEvent__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inspection_bot_msgs__msg__AnomalyEvent * data = NULL;

  if (size) {
    data = (inspection_bot_msgs__msg__AnomalyEvent *)allocator.zero_allocate(size, sizeof(inspection_bot_msgs__msg__AnomalyEvent), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = inspection_bot_msgs__msg__AnomalyEvent__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        inspection_bot_msgs__msg__AnomalyEvent__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
inspection_bot_msgs__msg__AnomalyEvent__Sequence__fini(inspection_bot_msgs__msg__AnomalyEvent__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      inspection_bot_msgs__msg__AnomalyEvent__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

inspection_bot_msgs__msg__AnomalyEvent__Sequence *
inspection_bot_msgs__msg__AnomalyEvent__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  inspection_bot_msgs__msg__AnomalyEvent__Sequence * array = (inspection_bot_msgs__msg__AnomalyEvent__Sequence *)allocator.allocate(sizeof(inspection_bot_msgs__msg__AnomalyEvent__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = inspection_bot_msgs__msg__AnomalyEvent__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
inspection_bot_msgs__msg__AnomalyEvent__Sequence__destroy(inspection_bot_msgs__msg__AnomalyEvent__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    inspection_bot_msgs__msg__AnomalyEvent__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
inspection_bot_msgs__msg__AnomalyEvent__Sequence__are_equal(const inspection_bot_msgs__msg__AnomalyEvent__Sequence * lhs, const inspection_bot_msgs__msg__AnomalyEvent__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!inspection_bot_msgs__msg__AnomalyEvent__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
inspection_bot_msgs__msg__AnomalyEvent__Sequence__copy(
  const inspection_bot_msgs__msg__AnomalyEvent__Sequence * input,
  inspection_bot_msgs__msg__AnomalyEvent__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(inspection_bot_msgs__msg__AnomalyEvent);
    inspection_bot_msgs__msg__AnomalyEvent * data =
      (inspection_bot_msgs__msg__AnomalyEvent *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!inspection_bot_msgs__msg__AnomalyEvent__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          inspection_bot_msgs__msg__AnomalyEvent__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!inspection_bot_msgs__msg__AnomalyEvent__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
