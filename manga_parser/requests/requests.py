from abc import ABC
from typing import Optional

from manga_parser.client.base import Client, Response
from manga_parser.exceptions.client import (DefaultClientNotInstalled,
                                            NeedPaymentForUsingSite)
from manga_parser.exceptions.site import ManyRequests, SiteInternalServerError


class Requests(ABC):
    def __init__(self, client: Optional[Client] = None):
        """
        Class for sending requests to sites

        :client:
         - default:
          httpx.Client
        :examples:
         Requests(),
         Requests(httpx.Client()),
         Requests(requests.Session()),
         class ClientWrap:
             def get(self, **kwargs):
                 return requests.get(**kwargs)
             ...

         Requests(ClientWrap()).
        """
        if client is None:
            try:
                import httpx
            except ImportError:
                raise DefaultClientNotInstalled(
                    DefaultClientNotInstalled.__doc__.format(
                        default_client="httpx",
                        default_client_version="0.21.3",
                    ),
                )
            self._client = httpx.Client(
                timeout=30.0,
            )
        else:
            self._client = client

    @property
    def client(self) -> Client:
        return self._client

    def close(self) -> None:
        self._client.close()

    def handle_exceptions(self, status_code: int) -> None:
        if status_code < 400:
            return None
        if 400 <= status_code < 500:
            if status_code == 402:
                raise NeedPaymentForUsingSite(NeedPaymentForUsingSite.__doc__)
            if status_code == 429:
                raise ManyRequests(ManyRequests.__doc__)
        if status_code >= 500:
            raise SiteInternalServerError(SiteInternalServerError.__doc__)

    def request(
        self,
        url: str,
        method: Optional[str] = "GET",
        **kwargs,
    ) -> Response:
        if method == "GET":
            response = self.client.get(url=url, **kwargs)
        elif method == "POST":
            response = self.client.post(url=url, **kwargs)

        self.handle_exceptions(response.status_code)

        return response
