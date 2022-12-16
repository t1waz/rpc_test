from __future__ import annotations

import enum
import json

from pydantic import (
    Extra,
    Field,
    BaseModel,
)


class RpcCommand(str, enum.Enum):
    GET_DATA = 'get_data'


class RpcMessage(BaseModel):
    @classmethod
    def from_bytes(cls, msg_bytes: bytes) -> RpcMessage:
        return cls(**json.loads(msg_bytes))

    def to_bytes(self) -> bytes:
        return json.dumps(self.dict()).encode()


class RpcRequest(RpcMessage, extra=Extra.allow):
    command: RpcCommand

    @property
    def payload(self) -> dict:
        return {k: v for k, v in self.dict().items() if k not in ('command',)}


class RpcResponse(RpcMessage):
    is_valid: bool


class GetDataRequest(RpcRequest):
    command: RpcCommand = Field(RpcCommand.GET_DATA, const=True)


class GetDataResponse(RpcResponse):
    content: str
