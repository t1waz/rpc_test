from django.conf import settings

from utils.models import (
    GetDataRequest,
    GetDataResponse,
)
from utils.rpc import RpcCommandClient


class ScrapRpcClient(RpcCommandClient):
    QUEUE_NAME = settings.SCRAP_RPC_QUEUE

    def process_scrap(self) -> GetDataResponse:
        return GetDataResponse(**self.call(msg=GetDataRequest()))
