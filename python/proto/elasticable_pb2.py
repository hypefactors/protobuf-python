# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/elasticable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/elasticable.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17proto/elasticable.proto\"J\n\x0b\x45lasticable\x12\x0e\n\x06_index\x18\x01 \x01(\t\x12\r\n\x05_type\x18\x02 \x01(\t\x12\x0b\n\x03_id\x18\x03 \x01(\t\x12\x0f\n\x07_source\x18\x04 \x01(\tb\x06proto3')
)




_ELASTICABLE = _descriptor.Descriptor(
  name='Elasticable',
  full_name='Elasticable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_index', full_name='Elasticable._index', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_type', full_name='Elasticable._type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_id', full_name='Elasticable._id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_source', full_name='Elasticable._source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['Elasticable'] = _ELASTICABLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Elasticable = _reflection.GeneratedProtocolMessageType('Elasticable', (_message.Message,), dict(
  DESCRIPTOR = _ELASTICABLE,
  __module__ = 'proto.elasticable_pb2'
  # @@protoc_insertion_point(class_scope:Elasticable)
  ))
_sym_db.RegisterMessage(Elasticable)


# @@protoc_insertion_point(module_scope)
