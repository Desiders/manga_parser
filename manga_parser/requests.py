import typing

import bs4

from . import client


class Requests(client.Client):
    """
    The parent class for requests to various sites
    """

    __slots__ = ()

    def body(
        self,
        url: str,
        method: typing.Optional[str] = "GET",
        **kwargs,
    ) -> bs4.BeautifulSoup:
        page = self.request(url, method=method, **kwargs)

        return bs4.BeautifulSoup(page.content, "lxml")

    def json(
        self,
        url: str,
        method: typing.Optional[str] = "GET",
        **kwargs,
    ) -> typing.Dict[str, typing.Any]:
        page = self.request(url, method=method, **kwargs)

        return page.json()
