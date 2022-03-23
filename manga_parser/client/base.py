from typing import Any, Protocol


class Response(Protocol):
    status_code: int
    content: bytes

    def json(self, **kwargs) -> Any:
        ...


class Client(Protocol):
    def get(self, **kwargs) -> Response:
        ...

    def post(self, **kwargs) -> Response:
        ...
