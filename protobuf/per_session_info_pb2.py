# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: per-session-info.proto

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
  name='per-session-info.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16per-session-info.proto\"#\n\x0ePerSessionInfo\x12\x11\n\trelay_url\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERSESSIONINFO = _descriptor.Descriptor(
  name='PerSessionInfo',
  full_name='PerSessionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relay_url', full_name='PerSessionInfo.relay_url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=26,
  serialized_end=61,
)

DESCRIPTOR.message_types_by_name['PerSessionInfo'] = _PERSESSIONINFO

PerSessionInfo = _reflection.GeneratedProtocolMessageType('PerSessionInfo', (_message.Message,), dict(
  DESCRIPTOR = _PERSESSIONINFO,
  __module__ = 'per_session_info_pb2'
  # @@protoc_insertion_point(class_scope:PerSessionInfo)
  ))
_sym_db.RegisterMessage(PerSessionInfo)


# @@protoc_insertion_point(module_scope)
