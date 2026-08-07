# generated from rosidl_generator_py/resource/_idl.py.em
# with input from inspection_bot_msgs:msg/AnomalyEvent.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AnomalyEvent(type):
    """Metaclass of message 'AnomalyEvent'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('inspection_bot_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'inspection_bot_msgs.msg.AnomalyEvent')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__anomaly_event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__anomaly_event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__anomaly_event
            cls._TYPE_SUPPORT = module.type_support_msg__msg__anomaly_event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__anomaly_event

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AnomalyEvent(metaclass=Metaclass_AnomalyEvent):
    """Message class 'AnomalyEvent'."""

    __slots__ = [
        '_anomaly_type',
        '_rack_id',
        '_confidence',
        '_critical',
        '_robot_pose',
        '_image_path',
        '_stamp',
    ]

    _fields_and_field_types = {
        'anomaly_type': 'string',
        'rack_id': 'string',
        'confidence': 'float',
        'critical': 'boolean',
        'robot_pose': 'geometry_msgs/Pose',
        'image_path': 'string',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.anomaly_type = kwargs.get('anomaly_type', str())
        self.rack_id = kwargs.get('rack_id', str())
        self.confidence = kwargs.get('confidence', float())
        self.critical = kwargs.get('critical', bool())
        from geometry_msgs.msg import Pose
        self.robot_pose = kwargs.get('robot_pose', Pose())
        self.image_path = kwargs.get('image_path', str())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.anomaly_type != other.anomaly_type:
            return False
        if self.rack_id != other.rack_id:
            return False
        if self.confidence != other.confidence:
            return False
        if self.critical != other.critical:
            return False
        if self.robot_pose != other.robot_pose:
            return False
        if self.image_path != other.image_path:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def anomaly_type(self):
        """Message field 'anomaly_type'."""
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'anomaly_type' field must be of type 'str'"
        self._anomaly_type = value

    @property
    def rack_id(self):
        """Message field 'rack_id'."""
        return self._rack_id

    @rack_id.setter
    def rack_id(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'rack_id' field must be of type 'str'"
        self._rack_id = value

    @property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'confidence' field must be of type 'float'"
        self._confidence = value

    @property
    def critical(self):
        """Message field 'critical'."""
        return self._critical

    @critical.setter
    def critical(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'critical' field must be of type 'bool'"
        self._critical = value

    @property
    def robot_pose(self):
        """Message field 'robot_pose'."""
        return self._robot_pose

    @robot_pose.setter
    def robot_pose(self, value):
        if __debug__:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'robot_pose' field must be a sub message of type 'Pose'"
        self._robot_pose = value

    @property
    def image_path(self):
        """Message field 'image_path'."""
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'image_path' field must be of type 'str'"
        self._image_path = value

    @property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value
