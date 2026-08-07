// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from inspection_bot_msgs:msg/AnomalyEvent.idl
// generated code does not contain a copyright notice

#ifndef INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__FUNCTIONS_H_
#define INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "inspection_bot_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "inspection_bot_msgs/msg/detail/anomaly_event__struct.h"

/// Initialize msg/AnomalyEvent message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * inspection_bot_msgs__msg__AnomalyEvent
 * )) before or use
 * inspection_bot_msgs__msg__AnomalyEvent__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
bool
inspection_bot_msgs__msg__AnomalyEvent__init(inspection_bot_msgs__msg__AnomalyEvent * msg);

/// Finalize msg/AnomalyEvent message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
void
inspection_bot_msgs__msg__AnomalyEvent__fini(inspection_bot_msgs__msg__AnomalyEvent * msg);

/// Create msg/AnomalyEvent message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * inspection_bot_msgs__msg__AnomalyEvent__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
inspection_bot_msgs__msg__AnomalyEvent *
inspection_bot_msgs__msg__AnomalyEvent__create();

/// Destroy msg/AnomalyEvent message.
/**
 * It calls
 * inspection_bot_msgs__msg__AnomalyEvent__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
void
inspection_bot_msgs__msg__AnomalyEvent__destroy(inspection_bot_msgs__msg__AnomalyEvent * msg);

/// Check for msg/AnomalyEvent message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
bool
inspection_bot_msgs__msg__AnomalyEvent__are_equal(const inspection_bot_msgs__msg__AnomalyEvent * lhs, const inspection_bot_msgs__msg__AnomalyEvent * rhs);

/// Copy a msg/AnomalyEvent message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
bool
inspection_bot_msgs__msg__AnomalyEvent__copy(
  const inspection_bot_msgs__msg__AnomalyEvent * input,
  inspection_bot_msgs__msg__AnomalyEvent * output);

/// Initialize array of msg/AnomalyEvent messages.
/**
 * It allocates the memory for the number of elements and calls
 * inspection_bot_msgs__msg__AnomalyEvent__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
bool
inspection_bot_msgs__msg__AnomalyEvent__Sequence__init(inspection_bot_msgs__msg__AnomalyEvent__Sequence * array, size_t size);

/// Finalize array of msg/AnomalyEvent messages.
/**
 * It calls
 * inspection_bot_msgs__msg__AnomalyEvent__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
void
inspection_bot_msgs__msg__AnomalyEvent__Sequence__fini(inspection_bot_msgs__msg__AnomalyEvent__Sequence * array);

/// Create array of msg/AnomalyEvent messages.
/**
 * It allocates the memory for the array and calls
 * inspection_bot_msgs__msg__AnomalyEvent__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
inspection_bot_msgs__msg__AnomalyEvent__Sequence *
inspection_bot_msgs__msg__AnomalyEvent__Sequence__create(size_t size);

/// Destroy array of msg/AnomalyEvent messages.
/**
 * It calls
 * inspection_bot_msgs__msg__AnomalyEvent__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
void
inspection_bot_msgs__msg__AnomalyEvent__Sequence__destroy(inspection_bot_msgs__msg__AnomalyEvent__Sequence * array);

/// Check for msg/AnomalyEvent message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
bool
inspection_bot_msgs__msg__AnomalyEvent__Sequence__are_equal(const inspection_bot_msgs__msg__AnomalyEvent__Sequence * lhs, const inspection_bot_msgs__msg__AnomalyEvent__Sequence * rhs);

/// Copy an array of msg/AnomalyEvent messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_inspection_bot_msgs
bool
inspection_bot_msgs__msg__AnomalyEvent__Sequence__copy(
  const inspection_bot_msgs__msg__AnomalyEvent__Sequence * input,
  inspection_bot_msgs__msg__AnomalyEvent__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // INSPECTION_BOT_MSGS__MSG__DETAIL__ANOMALY_EVENT__FUNCTIONS_H_
