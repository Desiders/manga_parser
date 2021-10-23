import typing

import httpx

from . import exceptions


class BaseClient(object):
    """
    The parent class of parsers of clients
    for sending requests to sites
    """

    __hash__ = None
    __slots__ = (
        "client_kwargs",
        "request_kwargs",
        "_client",
    )

    def __init__(
        self,
        client_kwargs: typing.Dict[str, typing.Any] = {},
        request_kwargs: typing.Dict[str, typing.Any] = {},
    ):
        """
        You can pass various parameters for requests and the client,
        for example, headers or cookies.

        * :client_kwargs: Parameters for client.
        * :request_kwargs: Parameters for requests.
        """
        self.client_kwargs = client_kwargs
        self.request_kwargs = request_kwargs
        self._client: typing.Optional[httpx.Client] = None


class Client(BaseClient):
    """
    The client for sending requests to sites
    """

    def __enter__(self):
        return self

    def new_client(self) -> httpx.Client:
        return httpx.Client(**self.client_kwargs)

    @property
    def client(self) -> httpx.Client:
        if self._client is None or self._client.is_closed:
            self._client = self.new_client()
        return self._client

    def close(self):
        if self._client is not None:
            self._client.close()

    def __exit__(self, exc, val, trace):
        self.close()

    def request(
        self,
        url: str,
        method: typing.Optional[str] = "GET",
        **kwargs,
    ) -> httpx.Response:
        kwargs = dict(
            url=url,
            **self.request_kwargs,
            **kwargs,
        )
        try:
            if method == "GET":
                response = self.client.get(**kwargs)
            elif method == "POST":
                response = self.client.post(**kwargs)
            else:
                raise exceptions.MethodNotFound((
                    "There is support for only "
                    "GET and POST methods! "
                ))
        except httpx.UnsupportedProtocol:
            raise exceptions.IncorrectProtocol((
                "Missing either an \"http://\" or "
                "\"https://\" protocol! "
                "Make sure that the url is entered correctly. "
            ))
        if response.status_code >= 400:
            if response.status_code == 401:
                raise exceptions.MangaNeedAuthorization((
                    "Needs authorization to view this manga! "
                    "The manga unavailable for viewing by minors. "
                    "You can change the headers and set token. "
                ))
            elif response.status_code == 402:
                raise exceptions.PaymentRequired((
                    "The site returns a status_code about "
                    "the need for payment! "
                    "You can change the headers. "
                ))
            raise exceptions.BadStatusCode((
                "The source returned the error status_code! "
                "You may have passed some parameters incorrectly. "
                f"More: {response}. "
            ))
        return response
