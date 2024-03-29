# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: id_alloc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='id_alloc.proto',
  package='Proto',
  syntax='proto3',
  serialized_pb=b'\n\x0eid_alloc.proto\x12\x05Proto\"\x18\n\x08GetIdReq\x12\x0c\n\x04name\x18\x01 \x01(\t\">\n\x08GetIdRsp\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x04\x32\x39\n\nRpcIdAlloc\x12+\n\x05GetId\x12\x0f.Proto.GetIdReq\x1a\x0f.Proto.GetIdRsp\"\x00\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETIDREQ = _descriptor.Descriptor(
  name='GetIdReq',
  full_name='Proto.GetIdReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Proto.GetIdReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=49,
)


_GETIDRSP = _descriptor.Descriptor(
  name='GetIdRsp',
  full_name='Proto.GetIdRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Proto.GetIdRsp.ret', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Proto.GetIdRsp.err', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Proto.GetIdRsp.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Proto.GetIdRsp.id', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['GetIdReq'] = _GETIDREQ
DESCRIPTOR.message_types_by_name['GetIdRsp'] = _GETIDRSP

GetIdReq = _reflection.GeneratedProtocolMessageType('GetIdReq', (_message.Message,), dict(
  DESCRIPTOR = _GETIDREQ,
  __module__ = 'id_alloc_pb2'
  # @@protoc_insertion_point(class_scope:Proto.GetIdReq)
  ))
_sym_db.RegisterMessage(GetIdReq)

GetIdRsp = _reflection.GeneratedProtocolMessageType('GetIdRsp', (_message.Message,), dict(
  DESCRIPTOR = _GETIDRSP,
  __module__ = 'id_alloc_pb2'
  # @@protoc_insertion_point(class_scope:Proto.GetIdRsp)
  ))
_sym_db.RegisterMessage(GetIdRsp)


import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterRpcIdAllocServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetId(self, request, context):
    raise NotImplementedError()
class EarlyAdopterRpcIdAllocServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterRpcIdAllocStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetId(self, request):
    raise NotImplementedError()
  GetId.async = None
def early_adopter_create_RpcIdAlloc_server(servicer, port, private_key=None, certificate_chain=None):
  import id_alloc_pb2
  import id_alloc_pb2
  method_service_descriptions = {
    "GetId": alpha_utilities.unary_unary_service_description(
      servicer.GetId,
      id_alloc_pb2.GetIdReq.FromString,
      id_alloc_pb2.GetIdRsp.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("Proto.RpcIdAlloc", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_RpcIdAlloc_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import id_alloc_pb2
  import id_alloc_pb2
  method_invocation_descriptions = {
    "GetId": alpha_utilities.unary_unary_invocation_description(
      id_alloc_pb2.GetIdReq.SerializeToString,
      id_alloc_pb2.GetIdRsp.FromString,
    ),
  }
  return early_adopter_implementations.stub("Proto.RpcIdAlloc", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaRpcIdAllocServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetId(self, request, context):
    raise NotImplementedError()

class BetaRpcIdAllocStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetId(self, request, timeout):
    raise NotImplementedError()
  GetId.future = None

def beta_create_RpcIdAlloc_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import id_alloc_pb2
  import id_alloc_pb2
  request_deserializers = {
    ('Proto.RpcIdAlloc', 'GetId'): id_alloc_pb2.GetIdReq.FromString,
  }
  response_serializers = {
    ('Proto.RpcIdAlloc', 'GetId'): id_alloc_pb2.GetIdRsp.SerializeToString,
  }
  method_implementations = {
    ('Proto.RpcIdAlloc', 'GetId'): face_utilities.unary_unary_inline(servicer.GetId),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_RpcIdAlloc_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import id_alloc_pb2
  import id_alloc_pb2
  request_serializers = {
    ('Proto.RpcIdAlloc', 'GetId'): id_alloc_pb2.GetIdReq.SerializeToString,
  }
  response_deserializers = {
    ('Proto.RpcIdAlloc', 'GetId'): id_alloc_pb2.GetIdRsp.FromString,
  }
  cardinalities = {
    'GetId': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'Proto.RpcIdAlloc', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
