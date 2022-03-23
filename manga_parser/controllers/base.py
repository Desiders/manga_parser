from typing import Protocol

from manga_parser.parsers.base import Parser
from manga_parser.requests.base import Requests


class Controller(Protocol):
    def __init__(
        self,
        requests: Requests,
        parser: Parser,
    ):
        ...
