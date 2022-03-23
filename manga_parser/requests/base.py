from typing import Optional, Protocol

from manga_parser.client.base import Client, Response


class Requests(Protocol):
    def __init__(self, client: Optional[Client] = None):
        ...

    @property
    def client(self) -> Client:
        ...

    def close(self) -> None:
        ...

    def handle_exceptions(self, status_code: int) -> None:
        ...

    def request(
        self,
        url: str,
        method: Optional[str],
        **kwargs,
    ) -> Response:
        ...
