# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: battle.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62\x61ttle.proto\x12\x06\x62\x61ttle\x1a\x1bgoogle/protobuf/empty.proto\"\x15\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\"7\n\x0fIncomingMissile\x12\n\n\x02pX\x18\x01 \x01(\x05\x12\n\n\x02pY\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\x05\"\x1d\n\x0bStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\"!\n\rPositionReply\x12\x10\n\x08position\x18\x01 \x01(\x05\x32\xe4\x02\n\x07Soldier\x12=\n\x12SetBattleFieldSize\x12\x0f.battle.Request\x1a\x16.google.protobuf.Empty\x12\x38\n\rSetSoldierNum\x12\x0f.battle.Request\x1a\x16.google.protobuf.Empty\x12\x36\n\x0cGetPositionX\x12\x0f.battle.Request\x1a\x15.battle.PositionReply\x12\x36\n\x0cGetPositionY\x12\x0f.battle.Request\x1a\x15.battle.PositionReply\x12?\n\x0ctake_shelter\x12\x17.battle.IncomingMissile\x1a\x16.google.protobuf.Empty\x12/\n\x07was_hit\x12\x0f.battle.Request\x1a\x13.battle.StatusReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'battle_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=53
  _globals['_REQUEST']._serialized_end=74
  _globals['_INCOMINGMISSILE']._serialized_start=76
  _globals['_INCOMINGMISSILE']._serialized_end=131
  _globals['_STATUSREPLY']._serialized_start=133
  _globals['_STATUSREPLY']._serialized_end=162
  _globals['_POSITIONREPLY']._serialized_start=164
  _globals['_POSITIONREPLY']._serialized_end=197
  _globals['_SOLDIER']._serialized_start=200
  _globals['_SOLDIER']._serialized_end=556
# @@protoc_insertion_point(module_scope)
