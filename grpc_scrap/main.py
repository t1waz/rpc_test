from concurrent import futures

import grpc

from utils.grpc import services_pb2
from utils.grpc import services_pb2_grpc


class ScrapServiceServicer(services_pb2_grpc.ScrapServiceServicer):
    def AuthLaunchUrl(self, request, context):
        return services_pb2.AuthResponse(msg='hello')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_ScrapServiceServicer_to_server(ScrapServiceServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print('started')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
