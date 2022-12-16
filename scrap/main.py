from typing import Optional

import requests

import settings
from utils.models import (
    RpcCommand,
    RpcResponse,
    GetDataRequest,
    GetDataResponse,
)
from utils.rpc import RpcCommandServer


class ScrapRpcCommandServer(RpcCommandServer):
    QUEUE_NAME = settings.SCRAP_RPC_QUEUE

    def handle_get_data(self, request: GetDataRequest) -> GetDataResponse:
        response = requests.get('https://google.com')

        return GetDataResponse(is_valid=True, content=response.content)

    def _dispatch_command(self, command: RpcCommand, **data) -> Optional[dict]:
        if command == RpcCommand.GET_DATA:
            response = self.handle_get_data(GetDataRequest(**data))
        else:
            response = RpcResponse(is_valid=False)

        return response.dict()


if __name__ == '__main__':
    ScrapRpcCommandServer.run(
        rabbit_mq_host=settings.RABBITMQ_HOST, rabbit_mq_port=settings.RABBITMQ_PORT
    )
