from dependency_injector import (
    providers,
    containers,
)
from django.conf import settings

from backend.rpc import ScrapRpcClient
from utils.rpc import create_pika_connection


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    pika_conn = providers.Singleton(
        create_pika_connection,
        rabbit_mq_host=settings.RABBITMQ_HOST,
        rabbit_mq_port=settings.RABBITMQ_PORT,
    )

    scrap_rpc_client = providers.Factory(
        ScrapRpcClient,
        conn=pika_conn,
    )
