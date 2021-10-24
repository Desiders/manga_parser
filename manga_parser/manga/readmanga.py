import typing

from .. import parsers, requests
from ..schemas import readmanga
from ..utils import get_short_url, urls_concat


class ReadManga(parsers.ReadMangaParser, requests.Requests):
    """
    The client for working with the site https://readmanga.io
    """

    __slots__ = ()

    def manga_search(
        self,
        name: str,
        offset: typing.Union[int, str] = 0,
        count: typing.Optional[int] = 1,
    ) -> typing.List[readmanga.MangaBriefly]:
        """
        Search for a similar manga by name.

        Returns a maximum of 50 results.

        * :name: The name to search for similar.
        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.parse_manga_search(
            soup=self.body(
                url=self.URL_SEARCH,
                method="POST",
                params={"q": name, "offset": offset},
            ),
            count=count,
        )

    def manga_info(
        self,
        url: str,
        chapters_offset: int = 0,
        chapters_count: typing.Optional[int] = None,
        chapters_primarily_new: bool = True,
    ) -> readmanga.Manga:
        """
        Returns the manga's information.

        * :url: Short url or full url.
         You can get short url from the object representing manga
         or just open any manga on the site
         and send what comes after the last slash. For example
         from "https://readmanga.live/dvorianstvo__A201945"
         need to pull out "dvorianstvo__A201945".
         Full url it's "https://readmanga.live/dvorianstvo__A201945".
        * :chapters_offset: The number of the manga chapter to start with.
        * :chapters_count: The number of the manga chapters to get.
        * :chapters_primarily_new: First of chapters is new.
        * :return: The object representing manga.
        """
        short_url = get_short_url(url)
        url = urls_concat([self.URL_SITE, short_url], "/")

        return self.parse_manga_info(
            soup=self.body(
                url=url,
            ),
            short_url=short_url,
            chapters_offset=chapters_offset,
            chapters_count=chapters_count,
            chapters_primarily_new=chapters_primarily_new,
        )

    def chapter_pages(
        self,
        url: str,
        offset: int = 0,
        count: typing.Optional[int] = None,
        primarily_first: bool = True,
    ) -> typing.List[readmanga.Page]:
        """
        Returns the chapter's pages.

        Links to photos expire after a time.

        * :url:
         You can get the url from the object representing chapter
         or just open to the chapter any manga on the site
         and send full url. For example
         "https://readmanga.io/bashnia_boga__A339d2/vol1/0"
        * :offset: The number of the chapter pages to start with.
        * :count: The number of the chapter pages to get.
        * :primarily_first: First page is first.
        * :return: The objects representing page of the chapter.
        """
        return self.parse_chapter_pages(
            soup=self.body(
                url=url,
            ),
            offset=offset,
            count=count,
            primarily_first=primarily_first,
        )

    def translator_info(
        self,
        url: str,
    ) -> readmanga.Translator:
        """
        Returns the translator's information.

        * :url: Short url or full url.
         You can get short url from the object representing translator
         or just open to the page any translator on the site
         and send what comes after the last slash. For example
         from "https://readmanga.live/list/person/rikudou_sennin_clan"
         need to pull out "rikudou_sennin_clan". Full url it's
         "https://readmanga.live/list/person/rikudou_sennin_clan".
        * :return: The object representing translator
        """
        short_url = get_short_url(url)
        url = urls_concat([self.URL_TRANSLATOR, short_url], "/")

        return self.parse_translator_info(
            soup=self.body(
                url=url,
            ),
            short_url=short_url,
            url=url,
        )

    def manga_popular(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[readmanga.MangaBriefly]:
        """
        Returns information about a popular manga.

        Returns a maximum of 30 results
        (not by one request, but in general).

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.parse_manga_popular(
            soup=self.body(
                url=self.URL_POPULAR,
            ),
            offset=offset,
            count=count,
        )

    def manga_by_url(
        self,
        url: str,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[readmanga.MangaBriefly]:
        """
        Returns information about the manga by url.
        "manga_best" and "manga_new"
        are wrappers for this function.

        Returns a maximum of 70 results

        * :url: The url for returns the manga.
        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.parse_manga_by_url(
            soup=self.body(
                url=url,
                params={"offset": offset},
            ),
            count=count,
        )

    def manga_best(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[readmanga.MangaBriefly]:
        """
        Returns information about the best manga.

        Returns a maximum of 70 results

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.manga_by_url(
            url=self.URL_BEST,
            offset=offset,
            count=count,
        )

    def manga_new(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[readmanga.MangaBriefly]:
        """
        Returns information about a new manga.

        Returns a maximum of 70 results

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.manga_by_url(
            url=self.URL_NEW,
            offset=offset,
            count=count,
        )
