from dependency_injector import (
    providers,
    containers,
)
from django.conf import settings

from backend.rpc import ScrapRpcClient


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    scrap_rpc_client = providers.Factory(
        ScrapRpcClient,
        rabbit_mq_host=settings.RABBITMQ_HOST,
        rabbit_mq_port=settings.RABBITMQ_PORT,
    )
