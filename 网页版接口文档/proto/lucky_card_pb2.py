# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lucky_card.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import base_pb2 as base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lucky_card.proto',
  package='Proto',
  syntax='proto3',
  serialized_pb=b'\n\x10lucky_card.proto\x12\x05Proto\x1a\x0cheader.proto\x1a\nbase.proto\";\n\x0c\x46\x65tchCardReq\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03uin\x18\x01 \x01(\r\"\x96\x01\n\x0c\x46\x65tchCardRsp\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t\x12\x16\n\x0enum_cards_left\x18\x03 \x01(\r\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12#\n\tcard_list\x18\x05 \x03(\x0b\x32\x10.Proto.LuckyCard\")\n\tLuckyCard\x12\x0b\n\x03hit\x18\x01 \x01(\r\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\t\"K\n\x0bOpenCardReq\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03uin\x18\x01 \x01(\r\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\t\"\x88\x01\n\x0bOpenCardRsp\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x12\n\nthumbImage\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\"T\n\x0cH5GetCardReq\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x11\n\tgiver_uin\x18\x01 \x01(\r\x12\x11\n\tsignature\x18\x02 \x01(\t\"V\n\x0cH5GetCardRsp\x12\x1e\n\x06header\x18\xf4\x03 \x01(\x0b\x32\r.Proto.Header\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03\x65rr\x18\x02 \x01(\t\x12\x0c\n\x04luck\x18\x03 \x01(\x05\x32\xe0\x01\n\x0cRpcLuckyCard\x12(\n\x04\x45\x63ho\x12\x0e.Proto.EchoReq\x1a\x0e.Proto.EchoRsp\"\x00\x12\x37\n\tFetchCard\x12\x13.Proto.FetchCardReq\x1a\x13.Proto.FetchCardRsp\"\x00\x12\x34\n\x08OpenCard\x12\x12.Proto.OpenCardReq\x1a\x12.Proto.OpenCardRsp\"\x00\x12\x37\n\tH5GetCard\x12\x13.Proto.H5GetCardReq\x1a\x13.Proto.H5GetCardRsp\"\x00\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,base__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FETCHCARDREQ = _descriptor.Descriptor(
  name='FetchCardReq',
  full_name='Proto.FetchCardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.FetchCardReq.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uin', full_name='Proto.FetchCardReq.uin', index=1,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=53,
  serialized_end=112,
)


_FETCHCARDRSP = _descriptor.Descriptor(
  name='FetchCardRsp',
  full_name='Proto.FetchCardRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.FetchCardRsp.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='Proto.FetchCardRsp.ret', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Proto.FetchCardRsp.err', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cards_left', full_name='Proto.FetchCardRsp.num_cards_left', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='Proto.FetchCardRsp.content', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card_list', full_name='Proto.FetchCardRsp.card_list', index=5,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=115,
  serialized_end=265,
)


_LUCKYCARD = _descriptor.Descriptor(
  name='LuckyCard',
  full_name='Proto.LuckyCard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hit', full_name='Proto.LuckyCard.hit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='Proto.LuckyCard.card_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=267,
  serialized_end=308,
)


_OPENCARDREQ = _descriptor.Descriptor(
  name='OpenCardReq',
  full_name='Proto.OpenCardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.OpenCardReq.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uin', full_name='Proto.OpenCardReq.uin', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='Proto.OpenCardReq.card_id', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=310,
  serialized_end=385,
)


_OPENCARDRSP = _descriptor.Descriptor(
  name='OpenCardRsp',
  full_name='Proto.OpenCardRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.OpenCardRsp.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='Proto.OpenCardRsp.ret', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Proto.OpenCardRsp.err', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Proto.OpenCardRsp.title', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='Proto.OpenCardRsp.content', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbImage', full_name='Proto.OpenCardRsp.thumbImage', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='Proto.OpenCardRsp.url', index=6,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=388,
  serialized_end=524,
)


_H5GETCARDREQ = _descriptor.Descriptor(
  name='H5GetCardReq',
  full_name='Proto.H5GetCardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.H5GetCardReq.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='giver_uin', full_name='Proto.H5GetCardReq.giver_uin', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Proto.H5GetCardReq.signature', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=526,
  serialized_end=610,
)


_H5GETCARDRSP = _descriptor.Descriptor(
  name='H5GetCardRsp',
  full_name='Proto.H5GetCardRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Proto.H5GetCardRsp.header', index=0,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='Proto.H5GetCardRsp.ret', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Proto.H5GetCardRsp.err', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='luck', full_name='Proto.H5GetCardRsp.luck', index=3,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=612,
  serialized_end=698,
)

_FETCHCARDREQ.fields_by_name['header'].message_type = header__pb2._HEADER
_FETCHCARDRSP.fields_by_name['header'].message_type = header__pb2._HEADER
_FETCHCARDRSP.fields_by_name['card_list'].message_type = _LUCKYCARD
_OPENCARDREQ.fields_by_name['header'].message_type = header__pb2._HEADER
_OPENCARDRSP.fields_by_name['header'].message_type = header__pb2._HEADER
_H5GETCARDREQ.fields_by_name['header'].message_type = header__pb2._HEADER
_H5GETCARDRSP.fields_by_name['header'].message_type = header__pb2._HEADER
DESCRIPTOR.message_types_by_name['FetchCardReq'] = _FETCHCARDREQ
DESCRIPTOR.message_types_by_name['FetchCardRsp'] = _FETCHCARDRSP
DESCRIPTOR.message_types_by_name['LuckyCard'] = _LUCKYCARD
DESCRIPTOR.message_types_by_name['OpenCardReq'] = _OPENCARDREQ
DESCRIPTOR.message_types_by_name['OpenCardRsp'] = _OPENCARDRSP
DESCRIPTOR.message_types_by_name['H5GetCardReq'] = _H5GETCARDREQ
DESCRIPTOR.message_types_by_name['H5GetCardRsp'] = _H5GETCARDRSP

FetchCardReq = _reflection.GeneratedProtocolMessageType('FetchCardReq', (_message.Message,), dict(
  DESCRIPTOR = _FETCHCARDREQ,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.FetchCardReq)
  ))
_sym_db.RegisterMessage(FetchCardReq)

FetchCardRsp = _reflection.GeneratedProtocolMessageType('FetchCardRsp', (_message.Message,), dict(
  DESCRIPTOR = _FETCHCARDRSP,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.FetchCardRsp)
  ))
_sym_db.RegisterMessage(FetchCardRsp)

LuckyCard = _reflection.GeneratedProtocolMessageType('LuckyCard', (_message.Message,), dict(
  DESCRIPTOR = _LUCKYCARD,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.LuckyCard)
  ))
_sym_db.RegisterMessage(LuckyCard)

OpenCardReq = _reflection.GeneratedProtocolMessageType('OpenCardReq', (_message.Message,), dict(
  DESCRIPTOR = _OPENCARDREQ,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.OpenCardReq)
  ))
_sym_db.RegisterMessage(OpenCardReq)

OpenCardRsp = _reflection.GeneratedProtocolMessageType('OpenCardRsp', (_message.Message,), dict(
  DESCRIPTOR = _OPENCARDRSP,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.OpenCardRsp)
  ))
_sym_db.RegisterMessage(OpenCardRsp)

H5GetCardReq = _reflection.GeneratedProtocolMessageType('H5GetCardReq', (_message.Message,), dict(
  DESCRIPTOR = _H5GETCARDREQ,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.H5GetCardReq)
  ))
_sym_db.RegisterMessage(H5GetCardReq)

H5GetCardRsp = _reflection.GeneratedProtocolMessageType('H5GetCardRsp', (_message.Message,), dict(
  DESCRIPTOR = _H5GETCARDRSP,
  __module__ = 'lucky_card_pb2'
  # @@protoc_insertion_point(class_scope:Proto.H5GetCardRsp)
  ))
_sym_db.RegisterMessage(H5GetCardRsp)


import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterRpcLuckyCardServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Echo(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def FetchCard(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OpenCard(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def H5GetCard(self, request, context):
    raise NotImplementedError()
class EarlyAdopterRpcLuckyCardServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterRpcLuckyCardStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Echo(self, request):
    raise NotImplementedError()
  Echo.async = None
  @abc.abstractmethod
  def FetchCard(self, request):
    raise NotImplementedError()
  FetchCard.async = None
  @abc.abstractmethod
  def OpenCard(self, request):
    raise NotImplementedError()
  OpenCard.async = None
  @abc.abstractmethod
  def H5GetCard(self, request):
    raise NotImplementedError()
  H5GetCard.async = None
def early_adopter_create_RpcLuckyCard_server(servicer, port, private_key=None, certificate_chain=None):
  import base_pb2
  import base_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  method_service_descriptions = {
    "Echo": alpha_utilities.unary_unary_service_description(
      servicer.Echo,
      base_pb2.EchoReq.FromString,
      base_pb2.EchoRsp.SerializeToString,
    ),
    "FetchCard": alpha_utilities.unary_unary_service_description(
      servicer.FetchCard,
      lucky_card_pb2.FetchCardReq.FromString,
      lucky_card_pb2.FetchCardRsp.SerializeToString,
    ),
    "H5GetCard": alpha_utilities.unary_unary_service_description(
      servicer.H5GetCard,
      lucky_card_pb2.H5GetCardReq.FromString,
      lucky_card_pb2.H5GetCardRsp.SerializeToString,
    ),
    "OpenCard": alpha_utilities.unary_unary_service_description(
      servicer.OpenCard,
      lucky_card_pb2.OpenCardReq.FromString,
      lucky_card_pb2.OpenCardRsp.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("Proto.RpcLuckyCard", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_RpcLuckyCard_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import base_pb2
  import base_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  method_invocation_descriptions = {
    "Echo": alpha_utilities.unary_unary_invocation_description(
      base_pb2.EchoReq.SerializeToString,
      base_pb2.EchoRsp.FromString,
    ),
    "FetchCard": alpha_utilities.unary_unary_invocation_description(
      lucky_card_pb2.FetchCardReq.SerializeToString,
      lucky_card_pb2.FetchCardRsp.FromString,
    ),
    "H5GetCard": alpha_utilities.unary_unary_invocation_description(
      lucky_card_pb2.H5GetCardReq.SerializeToString,
      lucky_card_pb2.H5GetCardRsp.FromString,
    ),
    "OpenCard": alpha_utilities.unary_unary_invocation_description(
      lucky_card_pb2.OpenCardReq.SerializeToString,
      lucky_card_pb2.OpenCardRsp.FromString,
    ),
  }
  return early_adopter_implementations.stub("Proto.RpcLuckyCard", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaRpcLuckyCardServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Echo(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def FetchCard(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OpenCard(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def H5GetCard(self, request, context):
    raise NotImplementedError()

class BetaRpcLuckyCardStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Echo(self, request, timeout):
    raise NotImplementedError()
  Echo.future = None
  @abc.abstractmethod
  def FetchCard(self, request, timeout):
    raise NotImplementedError()
  FetchCard.future = None
  @abc.abstractmethod
  def OpenCard(self, request, timeout):
    raise NotImplementedError()
  OpenCard.future = None
  @abc.abstractmethod
  def H5GetCard(self, request, timeout):
    raise NotImplementedError()
  H5GetCard.future = None

def beta_create_RpcLuckyCard_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import base_pb2
  import base_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  request_deserializers = {
    ('Proto.RpcLuckyCard', 'Echo'): base_pb2.EchoReq.FromString,
    ('Proto.RpcLuckyCard', 'FetchCard'): lucky_card_pb2.FetchCardReq.FromString,
    ('Proto.RpcLuckyCard', 'H5GetCard'): lucky_card_pb2.H5GetCardReq.FromString,
    ('Proto.RpcLuckyCard', 'OpenCard'): lucky_card_pb2.OpenCardReq.FromString,
  }
  response_serializers = {
    ('Proto.RpcLuckyCard', 'Echo'): base_pb2.EchoRsp.SerializeToString,
    ('Proto.RpcLuckyCard', 'FetchCard'): lucky_card_pb2.FetchCardRsp.SerializeToString,
    ('Proto.RpcLuckyCard', 'H5GetCard'): lucky_card_pb2.H5GetCardRsp.SerializeToString,
    ('Proto.RpcLuckyCard', 'OpenCard'): lucky_card_pb2.OpenCardRsp.SerializeToString,
  }
  method_implementations = {
    ('Proto.RpcLuckyCard', 'Echo'): face_utilities.unary_unary_inline(servicer.Echo),
    ('Proto.RpcLuckyCard', 'FetchCard'): face_utilities.unary_unary_inline(servicer.FetchCard),
    ('Proto.RpcLuckyCard', 'H5GetCard'): face_utilities.unary_unary_inline(servicer.H5GetCard),
    ('Proto.RpcLuckyCard', 'OpenCard'): face_utilities.unary_unary_inline(servicer.OpenCard),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_RpcLuckyCard_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import base_pb2
  import base_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  import lucky_card_pb2
  request_serializers = {
    ('Proto.RpcLuckyCard', 'Echo'): base_pb2.EchoReq.SerializeToString,
    ('Proto.RpcLuckyCard', 'FetchCard'): lucky_card_pb2.FetchCardReq.SerializeToString,
    ('Proto.RpcLuckyCard', 'H5GetCard'): lucky_card_pb2.H5GetCardReq.SerializeToString,
    ('Proto.RpcLuckyCard', 'OpenCard'): lucky_card_pb2.OpenCardReq.SerializeToString,
  }
  response_deserializers = {
    ('Proto.RpcLuckyCard', 'Echo'): base_pb2.EchoRsp.FromString,
    ('Proto.RpcLuckyCard', 'FetchCard'): lucky_card_pb2.FetchCardRsp.FromString,
    ('Proto.RpcLuckyCard', 'H5GetCard'): lucky_card_pb2.H5GetCardRsp.FromString,
    ('Proto.RpcLuckyCard', 'OpenCard'): lucky_card_pb2.OpenCardRsp.FromString,
  }
  cardinalities = {
    'Echo': cardinality.Cardinality.UNARY_UNARY,
    'FetchCard': cardinality.Cardinality.UNARY_UNARY,
    'H5GetCard': cardinality.Cardinality.UNARY_UNARY,
    'OpenCard': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'Proto.RpcLuckyCard', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
