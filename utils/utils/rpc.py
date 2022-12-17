import json
import uuid
from typing import Optional

import pika

from .exceptions import RpcCommandClientTimeout
from .models import (
    RpcRequest,
    RpcCommand,
)


class RpcCommandClient:
    QUEUE_NAME = None

    def __init__(self, rabbit_mq_host, rabbit_mq_port):
        self._corr_id = None
        self._response = None
        self._conn = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host, port=rabbit_mq_port)
        )
        self._ch = self._conn.channel()

        self._ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

        self._callback_q = self._ch.queue_declare(queue='', exclusive=True).method.queue

        self._ch.basic_consume(
            queue=self._callback_q, on_message_callback=self._on_response, auto_ack=True
        )

    def _on_response(self, ch, method, props, body):  # noqa
        if self._corr_id == props.correlation_id:
            self._response = body

    def call(self, msg: RpcRequest, time_limit=None) -> Optional[dict]:
        self._response = None
        self._corr_id = str(uuid.uuid4())

        # self._ch.basic_publish(
        #     exchange='',
        #     body=msg.to_bytes(),
        #     routing_key=self.QUEUE_NAME,
        #     properties=pika.BasicProperties(
        #         reply_to=self._callback_q,
        #         correlation_id=self._corr_id,
        #     ),
        # )
        self._ch.basic_publish(
            exchange='topic_logs',
            body=msg.to_bytes(),
            routing_key=f'test.{str(uuid.uuid4())}',
            properties=pika.BasicProperties(
                reply_to=self._callback_q,
                correlation_id=self._corr_id,
            ),
        )

        self._conn.process_data_events(time_limit=time_limit)

        if not self._response:
            raise RpcCommandClientTimeout('timeout to get message')

        return json.loads(self._response)


class RpcCommandServer:
    QUEUE_NAME = None

    def _dispatch_command(self, command: RpcCommand, **data) -> dict:
        ...

    def on_request(self, ch, method, props, body: bytes) -> None:  # TODO - typing
        rpc_message = RpcRequest.from_bytes(body)

        response = self._dispatch_command(command=rpc_message.command, **rpc_message.payload)
        if response is None:
            return

        ch.basic_publish(
            exchange='',
            body=json.dumps(response),
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    @classmethod
    def run(cls, rabbit_mq_host, rabbit_mq_port) -> None:
        server = cls()

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_mq_host, port=rabbit_mq_port)
        )

        channel = connection.channel()

        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(
            exchange='topic_logs', queue=queue_name, routing_key='test.#')
        channel.basic_consume(
            queue=queue_name, on_message_callback=server.on_request, auto_ack=False)

        # channel.queue_declare(queue=cls.QUEUE_NAME)
        # channel.basic_qos(prefetch_count=100)
        # channel.basic_consume(queue=cls.QUEUE_NAME, on_message_callback=server.on_request)
        channel.start_consuming()
