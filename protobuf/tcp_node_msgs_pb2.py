# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tcp-node-msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tcp-node-msgs.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13tcp-node-msgs.proto\"A\n\rServerDetails\x12\n\n\x02\x66\x31\x18\x01 \x02(\x05\x12\n\n\x02\x66\x32\x18\x02 \x02(\x05\x12\n\n\x02ip\x18\x03 \x02(\t\x12\x0c\n\x04port\x18\x04 \x02(\x05\"S\n\x0cServersType1\x12\x1f\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x0e.ServerDetails\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\"Y\n\x1eServerConnectionDetailsWrapper\x12\n\n\x02\x66\x31\x18\x01 \x02(\x05\x12\n\n\x02\x66\x32\x18\x02 \x02(\x05\x12\x1f\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32\x0e.ServerDetails\"V\n\x0cServersType2\x12\x38\n\x0f\x64\x65tails_wrapper\x18\x01 \x03(\x0b\x32\x1f.ServerConnectionDetailsWrapper\x12\x0c\n\x04port\x18\x02 \x02(\x05\"\x80\x01\n\rTCPServerInfo\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\n\n\x02\x66\x33\x18\x03 \x02(\x05\x12\x1e\n\x07servers\x18\x18 \x03(\x0b\x32\r.ServersType1\x12$\n\rother_servers\x18\x19 \x03(\x0b\x32\r.ServersType2\"\x1d\n\x08TCPHello\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\"N\n\x14RecurringTCPResponse\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\x11\n\tplayer_id\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SERVERDETAILS = _descriptor.Descriptor(
  name='ServerDetails',
  full_name='ServerDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='ServerDetails.f1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f2', full_name='ServerDetails.f2', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='ServerDetails.ip', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='ServerDetails.port', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=88,
)


_SERVERSTYPE1 = _descriptor.Descriptor(
  name='ServersType1',
  full_name='ServersType1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='ServersType1.details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f2', full_name='ServersType1.f2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f3', full_name='ServersType1.f3', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f4', full_name='ServersType1.f4', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=173,
)


_SERVERCONNECTIONDETAILSWRAPPER = _descriptor.Descriptor(
  name='ServerConnectionDetailsWrapper',
  full_name='ServerConnectionDetailsWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='ServerConnectionDetailsWrapper.f1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f2', full_name='ServerConnectionDetailsWrapper.f2', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='details', full_name='ServerConnectionDetailsWrapper.details', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=264,
)


_SERVERSTYPE2 = _descriptor.Descriptor(
  name='ServersType2',
  full_name='ServersType2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details_wrapper', full_name='ServersType2.details_wrapper', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='ServersType2.port', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=352,
)


_TCPSERVERINFO = _descriptor.Descriptor(
  name='TCPServerInfo',
  full_name='TCPServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='TCPServerInfo.f1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='TCPServerInfo.player_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f3', full_name='TCPServerInfo.f3', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='servers', full_name='TCPServerInfo.servers', index=3,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_servers', full_name='TCPServerInfo.other_servers', index=4,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=483,
)


_TCPHELLO = _descriptor.Descriptor(
  name='TCPHello',
  full_name='TCPHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='TCPHello.player_id', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=514,
)


_RECURRINGTCPRESPONSE = _descriptor.Descriptor(
  name='RecurringTCPResponse',
  full_name='RecurringTCPResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='RecurringTCPResponse.f1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='RecurringTCPResponse.player_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f3', full_name='RecurringTCPResponse.f3', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f11', full_name='RecurringTCPResponse.f11', index=3,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=594,
)

_SERVERSTYPE1.fields_by_name['details'].message_type = _SERVERDETAILS
_SERVERCONNECTIONDETAILSWRAPPER.fields_by_name['details'].message_type = _SERVERDETAILS
_SERVERSTYPE2.fields_by_name['details_wrapper'].message_type = _SERVERCONNECTIONDETAILSWRAPPER
_TCPSERVERINFO.fields_by_name['servers'].message_type = _SERVERSTYPE1
_TCPSERVERINFO.fields_by_name['other_servers'].message_type = _SERVERSTYPE2
DESCRIPTOR.message_types_by_name['ServerDetails'] = _SERVERDETAILS
DESCRIPTOR.message_types_by_name['ServersType1'] = _SERVERSTYPE1
DESCRIPTOR.message_types_by_name['ServerConnectionDetailsWrapper'] = _SERVERCONNECTIONDETAILSWRAPPER
DESCRIPTOR.message_types_by_name['ServersType2'] = _SERVERSTYPE2
DESCRIPTOR.message_types_by_name['TCPServerInfo'] = _TCPSERVERINFO
DESCRIPTOR.message_types_by_name['TCPHello'] = _TCPHELLO
DESCRIPTOR.message_types_by_name['RecurringTCPResponse'] = _RECURRINGTCPRESPONSE

ServerDetails = _reflection.GeneratedProtocolMessageType('ServerDetails', (_message.Message,), dict(
  DESCRIPTOR = _SERVERDETAILS,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerDetails)
  ))
_sym_db.RegisterMessage(ServerDetails)

ServersType1 = _reflection.GeneratedProtocolMessageType('ServersType1', (_message.Message,), dict(
  DESCRIPTOR = _SERVERSTYPE1,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServersType1)
  ))
_sym_db.RegisterMessage(ServersType1)

ServerConnectionDetailsWrapper = _reflection.GeneratedProtocolMessageType('ServerConnectionDetailsWrapper', (_message.Message,), dict(
  DESCRIPTOR = _SERVERCONNECTIONDETAILSWRAPPER,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerConnectionDetailsWrapper)
  ))
_sym_db.RegisterMessage(ServerConnectionDetailsWrapper)

ServersType2 = _reflection.GeneratedProtocolMessageType('ServersType2', (_message.Message,), dict(
  DESCRIPTOR = _SERVERSTYPE2,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServersType2)
  ))
_sym_db.RegisterMessage(ServersType2)

TCPServerInfo = _reflection.GeneratedProtocolMessageType('TCPServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _TCPSERVERINFO,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:TCPServerInfo)
  ))
_sym_db.RegisterMessage(TCPServerInfo)

TCPHello = _reflection.GeneratedProtocolMessageType('TCPHello', (_message.Message,), dict(
  DESCRIPTOR = _TCPHELLO,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:TCPHello)
  ))
_sym_db.RegisterMessage(TCPHello)

RecurringTCPResponse = _reflection.GeneratedProtocolMessageType('RecurringTCPResponse', (_message.Message,), dict(
  DESCRIPTOR = _RECURRINGTCPRESPONSE,
  __module__ = 'tcp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:RecurringTCPResponse)
  ))
_sym_db.RegisterMessage(RecurringTCPResponse)


# @@protoc_insertion_point(module_scope)
