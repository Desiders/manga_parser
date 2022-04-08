from typing import Callable, Optional, Union

from manga_parser.client.base import Response
from manga_parser.requests.requests import Requests
from manga_parser.schemas.readmanga import Manga
from manga_parser.typehints.readmanga import MangaOrUrlType, MangaShortUrlType
from manga_parser.urls.readmanga import ReadmangaUrls
from manga_parser.urls.urls import get_short_url, is_url, urls_concat


def unpacking_manga_to_id(
    fn: Callable[
        ["ReadmangaRequests",
         MangaShortUrlType],
        Response,
    ],
):
    def wrap(
        *args,
        manga_or_url: MangaOrUrlType,
        **kwargs,
    ):
        if isinstance(manga_or_url, Manga):
            short_url = manga_or_url.short_url
        else:
            if is_url(manga_or_url):
                short_url = get_short_url(manga_or_url)
            else:
                short_url = manga_or_url

        return fn(
            *args,
            **kwargs,
            short_url=short_url,
        )
    return wrap


class ReadmangaRequests(Requests):
    urls = ReadmangaUrls

    def handle_exceptions(self, status_code: int) -> None:
        super().handle_exceptions(status_code)

    def request(
        self,
        url: str,
        method: Optional[str] = "GET",
        **kwargs,
    ) -> Response:
        response = super().request(url=url, method=method, **kwargs)

        self.handle_exceptions(response.status_code)

        return response

    def manga_search(
        self,
        name: str,
        offset: Union[int, str] = 0,
    ) -> Response:
        """
        Search the manga by name

        Returns a maximum of 50 results.
        Site and this library doesn't responsibility to return
        the transmitted amount of manga, because together with manga they
        return books and manga from other sites (librebook and mintmanga).

        :name:
        :offset:
        """
        return self.request(
            url=urls_concat(
                self.urls.SITE.value,
                self.urls.SEARCH.value,
                sep="/",
            ),
            method="POST",
            params={"q": name, "offset": offset},
        )

    @unpacking_manga_to_id
    def manga_info(self, short_url: MangaShortUrlType) -> Response:
        """
        Return the manga's information

        :short_url:
        """
        return self.request(
            url=urls_concat(
                self.urls.SITE.value,
                short_url,
                sep="/",
            ),
            method="GET",
        )
