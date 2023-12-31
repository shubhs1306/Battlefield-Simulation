# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import battle_pb2 as battle__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class SoldierStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetBattleFieldSize = channel.unary_unary(
                '/battle.Soldier/SetBattleFieldSize',
                request_serializer=battle__pb2.Request.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetSoldierNum = channel.unary_unary(
                '/battle.Soldier/SetSoldierNum',
                request_serializer=battle__pb2.Request.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetPositionX = channel.unary_unary(
                '/battle.Soldier/GetPositionX',
                request_serializer=battle__pb2.Request.SerializeToString,
                response_deserializer=battle__pb2.PositionReply.FromString,
                )
        self.GetPositionY = channel.unary_unary(
                '/battle.Soldier/GetPositionY',
                request_serializer=battle__pb2.Request.SerializeToString,
                response_deserializer=battle__pb2.PositionReply.FromString,
                )
        self.take_shelter = channel.unary_unary(
                '/battle.Soldier/take_shelter',
                request_serializer=battle__pb2.IncomingMissile.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.was_hit = channel.unary_unary(
                '/battle.Soldier/was_hit',
                request_serializer=battle__pb2.Request.SerializeToString,
                response_deserializer=battle__pb2.StatusReply.FromString,
                )


class SoldierServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetBattleFieldSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSoldierNum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPositionX(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPositionY(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def take_shelter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def was_hit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SoldierServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetBattleFieldSize': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBattleFieldSize,
                    request_deserializer=battle__pb2.Request.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetSoldierNum': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSoldierNum,
                    request_deserializer=battle__pb2.Request.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetPositionX': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPositionX,
                    request_deserializer=battle__pb2.Request.FromString,
                    response_serializer=battle__pb2.PositionReply.SerializeToString,
            ),
            'GetPositionY': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPositionY,
                    request_deserializer=battle__pb2.Request.FromString,
                    response_serializer=battle__pb2.PositionReply.SerializeToString,
            ),
            'take_shelter': grpc.unary_unary_rpc_method_handler(
                    servicer.take_shelter,
                    request_deserializer=battle__pb2.IncomingMissile.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'was_hit': grpc.unary_unary_rpc_method_handler(
                    servicer.was_hit,
                    request_deserializer=battle__pb2.Request.FromString,
                    response_serializer=battle__pb2.StatusReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'battle.Soldier', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Soldier(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetBattleFieldSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/battle.Soldier/SetBattleFieldSize',
            battle__pb2.Request.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSoldierNum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/battle.Soldier/SetSoldierNum',
            battle__pb2.Request.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPositionX(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/battle.Soldier/GetPositionX',
            battle__pb2.Request.SerializeToString,
            battle__pb2.PositionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPositionY(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/battle.Soldier/GetPositionY',
            battle__pb2.Request.SerializeToString,
            battle__pb2.PositionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def take_shelter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/battle.Soldier/take_shelter',
            battle__pb2.IncomingMissile.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def was_hit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/battle.Soldier/was_hit',
            battle__pb2.Request.SerializeToString,
            battle__pb2.StatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
