# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from .services_pb2 import *


class ScrapServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuthLaunchUrl = channel.unary_unary(
                '/ScrapService/AuthLaunchUrl',
                request_serializer=LaunchUrlData.SerializeToString,
                response_deserializer=AuthResponse.FromString,
                )


class ScrapServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AuthLaunchUrl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScrapServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuthLaunchUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthLaunchUrl,
                    request_deserializer=LaunchUrlData.FromString,
                    response_serializer=AuthResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ScrapService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScrapService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AuthLaunchUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ScrapService/AuthLaunchUrl',
            LaunchUrlData.SerializeToString,
            AuthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)