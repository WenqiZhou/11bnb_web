# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: count.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='count.proto',
  package='Proto',
  syntax='proto3',
  serialized_pb=b'\n\x0b\x63ount.proto\x12\x05Proto\x1a\x0cheader.proto\"r\n\tCountInfo\x12#\n\x07op_type\x18\x01 \x01(\x0e\x32\x12.Proto.OperateType\x12$\n\ncount_type\x18\x02 \x01(\x0e\x32\x10.Proto.CountType\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x0b\n\x03uin\x18\x04 \x01(\r\"\x9b\x01\n\x0bSetCountReq\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x13\n\x0boperate_uin\x18\x01 \x01(\r\x12\x0e\n\x06to_uin\x18\x02 \x01(\r\x12%\n\x0cto_user_type\x18\x03 \x01(\x0e\x32\x0f.Proto.UserType\x12 \n\x06\x63ounts\x18\x04 \x03(\x0b\x32\x10.Proto.CountInfo\"\x80\x01\n\x0bSetCountRsp\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t\x12\x11\n\tall_count\x18\x03 \x01(\r\x12$\n\nrsp_counts\x18\x04 \x03(\x0b\x32\x10.Proto.CountInfo\"x\n\x0bGetCountReq\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x10\n\x08user_uin\x18\x01 \x01(\r\x12\"\n\tuser_type\x18\x02 \x01(\x0e\x32\x0f.Proto.UserType\x12\x13\n\x0b\x63ount_types\x18\x03 \x01(\x04\"\xb6\x01\n\x0bGetCountRsp\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t\x12\x10\n\x08user_uin\x18\x03 \x01(\r\x12\"\n\tuser_type\x18\x04 \x01(\x0e\x32\x0f.Proto.UserType\x12$\n\nrsp_counts\x18\x05 \x03(\x0b\x32\x10.Proto.CountInfo\x12\x11\n\tall_count\x18\x06 \x01(\r*\xa8\x01\n\tCountType\x12\x11\n\rNoneCountType\x10\x00\x12\x11\n\rNeedToConfirm\x10\x01\x12\r\n\tNeedToPay\x10\x02\x12\x19\n\x15NeedLandlordToComment\x10\x04\x12\x17\n\x13NeedTenantToComment\x10\x08\x12\x19\n\x15LandlordUnReadMessage\x10\x10\x12\x17\n\x13TenantUnReadMessage\x10 *9\n\x08UserType\x12\x13\n\x0f\x44\x65\x66\x61ultUserType\x10\x00\x12\x0c\n\x08Landlord\x10\x01\x12\n\n\x06Tenant\x10\x02*?\n\x0bOperateType\x12\x13\n\x0fNoneOperateType\x10\x00\x12\x07\n\x03\x41\x64\x64\x10\x01\x12\x07\n\x03\x44\x65l\x10\x02\x12\t\n\x05\x43lear\x10\x03\x32v\n\x08RpcCount\x12\x34\n\x08SetCount\x12\x12.Proto.SetCountReq\x1a\x12.Proto.SetCountRsp\"\x00\x12\x34\n\x08GetCount\x12\x12.Proto.GetCountReq\x1a\x12.Proto.GetCountRsp\"\x00\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_COUNTTYPE = _descriptor.EnumDescriptor(
  name='CountType',
  full_name='Proto.CountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneCountType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NeedToConfirm', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NeedToPay', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NeedLandlordToComment', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NeedTenantToComment', index=4, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LandlordUnReadMessage', index=5, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TenantUnReadMessage', index=6, number=32,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=749,
  serialized_end=917,
)
_sym_db.RegisterEnumDescriptor(_COUNTTYPE)

CountType = enum_type_wrapper.EnumTypeWrapper(_COUNTTYPE)
_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='Proto.UserType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DefaultUserType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Landlord', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Tenant', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=919,
  serialized_end=976,
)
_sym_db.RegisterEnumDescriptor(_USERTYPE)

UserType = enum_type_wrapper.EnumTypeWrapper(_USERTYPE)
_OPERATETYPE = _descriptor.EnumDescriptor(
  name='OperateType',
  full_name='Proto.OperateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneOperateType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Add', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Del', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Clear', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=978,
  serialized_end=1041,
)
_sym_db.RegisterEnumDescriptor(_OPERATETYPE)

OperateType = enum_type_wrapper.EnumTypeWrapper(_OPERATETYPE)
NoneCountType = 0
NeedToConfirm = 1
NeedToPay = 2
NeedLandlordToComment = 4
NeedTenantToComment = 8
LandlordUnReadMessage = 16
TenantUnReadMessage = 32
DefaultUserType = 0
Landlord = 1
Tenant = 2
NoneOperateType = 0
Add = 1
Del = 2
Clear = 3



_COUNTINFO = _descriptor.Descriptor(
  name='CountInfo',
  full_name='Proto.CountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op_type', full_name='Proto.CountInfo.op_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count_type', full_name='Proto.CountInfo.count_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='Proto.CountInfo.count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uin', full_name='Proto.CountInfo.uin', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=36,
  serialized_end=150,
)


_SETCOUNTREQ = _descriptor.Descriptor(
  name='SetCountReq',
  full_name='Proto.SetCountReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.SetCountReq.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operate_uin', full_name='Proto.SetCountReq.operate_uin', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_uin', full_name='Proto.SetCountReq.to_uin', index=2,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_user_type', full_name='Proto.SetCountReq.to_user_type', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counts', full_name='Proto.SetCountReq.counts', index=4,
      number=4, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=308,
)


_SETCOUNTRSP = _descriptor.Descriptor(
  name='SetCountRsp',
  full_name='Proto.SetCountRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.SetCountRsp.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='Proto.SetCountRsp.ret', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Proto.SetCountRsp.err', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all_count', full_name='Proto.SetCountRsp.all_count', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rsp_counts', full_name='Proto.SetCountRsp.rsp_counts', index=4,
      number=4, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=439,
)


_GETCOUNTREQ = _descriptor.Descriptor(
  name='GetCountReq',
  full_name='Proto.GetCountReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.GetCountReq.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_uin', full_name='Proto.GetCountReq.user_uin', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='Proto.GetCountReq.user_type', index=2,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count_types', full_name='Proto.GetCountReq.count_types', index=3,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=441,
  serialized_end=561,
)


_GETCOUNTRSP = _descriptor.Descriptor(
  name='GetCountRsp',
  full_name='Proto.GetCountRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.GetCountRsp.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='Proto.GetCountRsp.ret', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Proto.GetCountRsp.err', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_uin', full_name='Proto.GetCountRsp.user_uin', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='Proto.GetCountRsp.user_type', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rsp_counts', full_name='Proto.GetCountRsp.rsp_counts', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all_count', full_name='Proto.GetCountRsp.all_count', index=6,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=564,
  serialized_end=746,
)

_COUNTINFO.fields_by_name['op_type'].enum_type = _OPERATETYPE
_COUNTINFO.fields_by_name['count_type'].enum_type = _COUNTTYPE
_SETCOUNTREQ.fields_by_name['header'].message_type = header__pb2._HEADER
_SETCOUNTREQ.fields_by_name['to_user_type'].enum_type = _USERTYPE
_SETCOUNTREQ.fields_by_name['counts'].message_type = _COUNTINFO
_SETCOUNTRSP.fields_by_name['header'].message_type = header__pb2._HEADER
_SETCOUNTRSP.fields_by_name['rsp_counts'].message_type = _COUNTINFO
_GETCOUNTREQ.fields_by_name['header'].message_type = header__pb2._HEADER
_GETCOUNTREQ.fields_by_name['user_type'].enum_type = _USERTYPE
_GETCOUNTRSP.fields_by_name['header'].message_type = header__pb2._HEADER
_GETCOUNTRSP.fields_by_name['user_type'].enum_type = _USERTYPE
_GETCOUNTRSP.fields_by_name['rsp_counts'].message_type = _COUNTINFO
DESCRIPTOR.message_types_by_name['CountInfo'] = _COUNTINFO
DESCRIPTOR.message_types_by_name['SetCountReq'] = _SETCOUNTREQ
DESCRIPTOR.message_types_by_name['SetCountRsp'] = _SETCOUNTRSP
DESCRIPTOR.message_types_by_name['GetCountReq'] = _GETCOUNTREQ
DESCRIPTOR.message_types_by_name['GetCountRsp'] = _GETCOUNTRSP
DESCRIPTOR.enum_types_by_name['CountType'] = _COUNTTYPE
DESCRIPTOR.enum_types_by_name['UserType'] = _USERTYPE
DESCRIPTOR.enum_types_by_name['OperateType'] = _OPERATETYPE

CountInfo = _reflection.GeneratedProtocolMessageType('CountInfo', (_message.Message,), dict(
  DESCRIPTOR = _COUNTINFO,
  __module__ = 'count_pb2'
  # @@protoc_insertion_point(class_scope:Proto.CountInfo)
  ))
_sym_db.RegisterMessage(CountInfo)

SetCountReq = _reflection.GeneratedProtocolMessageType('SetCountReq', (_message.Message,), dict(
  DESCRIPTOR = _SETCOUNTREQ,
  __module__ = 'count_pb2'
  # @@protoc_insertion_point(class_scope:Proto.SetCountReq)
  ))
_sym_db.RegisterMessage(SetCountReq)

SetCountRsp = _reflection.GeneratedProtocolMessageType('SetCountRsp', (_message.Message,), dict(
  DESCRIPTOR = _SETCOUNTRSP,
  __module__ = 'count_pb2'
  # @@protoc_insertion_point(class_scope:Proto.SetCountRsp)
  ))
_sym_db.RegisterMessage(SetCountRsp)

GetCountReq = _reflection.GeneratedProtocolMessageType('GetCountReq', (_message.Message,), dict(
  DESCRIPTOR = _GETCOUNTREQ,
  __module__ = 'count_pb2'
  # @@protoc_insertion_point(class_scope:Proto.GetCountReq)
  ))
_sym_db.RegisterMessage(GetCountReq)

GetCountRsp = _reflection.GeneratedProtocolMessageType('GetCountRsp', (_message.Message,), dict(
  DESCRIPTOR = _GETCOUNTRSP,
  __module__ = 'count_pb2'
  # @@protoc_insertion_point(class_scope:Proto.GetCountRsp)
  ))
_sym_db.RegisterMessage(GetCountRsp)


import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterRpcCountServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SetCount(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetCount(self, request, context):
    raise NotImplementedError()
class EarlyAdopterRpcCountServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterRpcCountStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SetCount(self, request):
    raise NotImplementedError()
  SetCount.async = None
  @abc.abstractmethod
  def GetCount(self, request):
    raise NotImplementedError()
  GetCount.async = None
def early_adopter_create_RpcCount_server(servicer, port, private_key=None, certificate_chain=None):
  import count_pb2
  import count_pb2
  import count_pb2
  import count_pb2
  method_service_descriptions = {
    "GetCount": alpha_utilities.unary_unary_service_description(
      servicer.GetCount,
      count_pb2.GetCountReq.FromString,
      count_pb2.GetCountRsp.SerializeToString,
    ),
    "SetCount": alpha_utilities.unary_unary_service_description(
      servicer.SetCount,
      count_pb2.SetCountReq.FromString,
      count_pb2.SetCountRsp.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("Proto.RpcCount", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_RpcCount_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import count_pb2
  import count_pb2
  import count_pb2
  import count_pb2
  method_invocation_descriptions = {
    "GetCount": alpha_utilities.unary_unary_invocation_description(
      count_pb2.GetCountReq.SerializeToString,
      count_pb2.GetCountRsp.FromString,
    ),
    "SetCount": alpha_utilities.unary_unary_invocation_description(
      count_pb2.SetCountReq.SerializeToString,
      count_pb2.SetCountRsp.FromString,
    ),
  }
  return early_adopter_implementations.stub("Proto.RpcCount", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaRpcCountServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SetCount(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetCount(self, request, context):
    raise NotImplementedError()

class BetaRpcCountStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SetCount(self, request, timeout):
    raise NotImplementedError()
  SetCount.future = None
  @abc.abstractmethod
  def GetCount(self, request, timeout):
    raise NotImplementedError()
  GetCount.future = None

def beta_create_RpcCount_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import count_pb2
  import count_pb2
  import count_pb2
  import count_pb2
  request_deserializers = {
    ('Proto.RpcCount', 'GetCount'): count_pb2.GetCountReq.FromString,
    ('Proto.RpcCount', 'SetCount'): count_pb2.SetCountReq.FromString,
  }
  response_serializers = {
    ('Proto.RpcCount', 'GetCount'): count_pb2.GetCountRsp.SerializeToString,
    ('Proto.RpcCount', 'SetCount'): count_pb2.SetCountRsp.SerializeToString,
  }
  method_implementations = {
    ('Proto.RpcCount', 'GetCount'): face_utilities.unary_unary_inline(servicer.GetCount),
    ('Proto.RpcCount', 'SetCount'): face_utilities.unary_unary_inline(servicer.SetCount),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_RpcCount_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import count_pb2
  import count_pb2
  import count_pb2
  import count_pb2
  request_serializers = {
    ('Proto.RpcCount', 'GetCount'): count_pb2.GetCountReq.SerializeToString,
    ('Proto.RpcCount', 'SetCount'): count_pb2.SetCountReq.SerializeToString,
  }
  response_deserializers = {
    ('Proto.RpcCount', 'GetCount'): count_pb2.GetCountRsp.FromString,
    ('Proto.RpcCount', 'SetCount'): count_pb2.SetCountRsp.FromString,
  }
  cardinalities = {
    'GetCount': cardinality.Cardinality.UNARY_UNARY,
    'SetCount': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'Proto.RpcCount', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
