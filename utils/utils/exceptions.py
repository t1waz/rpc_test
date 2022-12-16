class RpcException(Exception):
    def __init__(self, msg):
        self._msg = msg

    @property
    def msg(self) -> str:
        return self._msg


class RpcCommandClientTimeout(RpcException):
    pass
