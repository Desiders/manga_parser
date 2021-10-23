import typing

from .. import parsers, requests
from ..schemas import remanga
from ..utils import get_short_url, urls_concat


class ReManga(parsers.ReMangaParser, requests.Requests):
    """
    The client for working with the site https://remanga.org
    """

    __slots__ = ()

    def manga_search(
        self,
        name: str,
        count: int = 1,
    ) -> typing.List[remanga.MangaBriefly]:
        """
        Search for a similar manga by name.

        * :name: The name to search for similar.
        * :count: The number of manga to get.
        * :return: The objects representing manga.
        """
        return self.parse_manga_search(
            manga_json=self.json(
                url=self.URL_SEARCH,
                params={"query": name, "count": count},
            ),
        )

    def manga_info(
        self,
        url: str,
    ) -> remanga.Manga:
        """
        Returns the manga's information.

        * :url: Short url or full url.
         You can get the short url from the object representing manga
         or just open any manga on the site
         and send what comes after the last slash. For example
         from "https://remanga.org/manga/the_beginning_after_the_end"
         need to pull out "the_beginning_after_the_end".
         Full url it's "https://remanga.org/manga/the_beginning_after_the_end".
        * :return: The object representing manga.
        """
        short_url = get_short_url(url)
        url = urls_concat([self.URL_MANGA_API, short_url], "/")

        return self.parse_manga_info(
            manga_json=self.json(
                url=url,
            ),
            short_url=short_url,
        )

    def manga_chapters(
        self,
        branch_id: typing.Union[int, str],
        offset: int = 0,
        count: typing.Optional[int] = None,
        primarily_new: bool = True,
    ) -> typing.List[remanga.Chapter]:
        """
        Returns the chapters' information.

        * :branch_id:
         You can get the branch id from the object representing manga
         or just open to the branch any manga on the site
         and send what comes after "branch=". For example from
         "https://remanga.org/manga/tomb-raider?subpath=content&branch=3786"
         need to pull out "3786".
        * :offset: The number of the manga chapter to start with.
        * :count: The number of the manga chapters to get.
        * :primarily_new: First of chapters is new.
        * :return: The objects representing manga.
        """
        return self.parse_manga_chapters(
            chapters_json=self.json(
                url=self.URL_CHAPTERS,
                params={"branch_id": branch_id},
            ),
            offset=offset,
            count=count,
            primarily_new=primarily_new,
        )

    def chapter_pages(
        self,
        chapter_id: typing.Union[int, str],
        offset: int = 0,
        count: typing.Optional[int] = None,
        primarily_first: bool = True,
    ):
        """
        Returns the chapter's pages.

        * :chapter_id:
         You can get the chapter id from the object representing chapter
         or just open to the chapter any manga on the site
         and send what comes after the last slash and "ch". For example
         from "https://remanga.org/manga/blade_of_demon_destruction/ch542404"
         need to pull out "542404" or "ch542404".
        * :offset: The number of the chapter pages to start with.
        * :count: The number of the chapter pages to get.
        * :primarily_first: First page is first.
        * :return: The objects representing page of the chapter.
        """
        if isinstance(chapter_id, str) and chapter_id.startswith("ch"):
            _, chapter_id = chapter_id.split("ch")

        url = urls_concat([self.URL_CHAPTERS, chapter_id], "/")

        return self.parse_chapter_pages(
            pages_json=self.json(
                url=url,
            ),
            offset=offset,
            count=count,
            primarily_first=primarily_first,
        )

    def translator_info(
        self,
        url: str,
    ) -> remanga.Translator:
        """
        Returns the translator's information.

        * :url: Short url or full url.
         You can get the short url from the object representing translator
         or just open to the page any translator on the site
         and send what comes after the last slash. For example
         from "https://remanga.org/team/vesperum"
         need to pull out "vesperum".
         Full url it's "https://remanga.org/team/vesperum".
        * :return: The object representing translator.
        """
        short_url = get_short_url(url)
        url = urls_concat([self.URL_TEAM_API, short_url], "/")

        return self.parse_translator_info(
            translator_json=self.json(
                url=url,
            ),
            short_url=short_url,
        )

    def manga_by_url(
        self,
        url: str,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[remanga.MangaAverage]:
        """
        Returns information about the manga by url.
        "manga_recommendations", "manga_views"
        "manga_votes" and "manga_new"
        are wrappers for this function.

        Returns a maximum of 20 results

        * :url: The url for returns the manga.
        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        page = offset // 20

        return self.parse_manga_by_url(
            manga_json=self.json(
                url=url,
                params={"page": page + 1},
            ),
            offset=offset,
            count=count,
        )

    def manga_recommendations(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[remanga.MangaAverage]:
        """
        Returns information about a popular manga.

        Returns a maximum of 20 results

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.manga_by_url(
            url=self.URL_RECOMMENDATIONS,
            offset=offset,
            count=count,
        )

    def manga_views(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[remanga.MangaAverage]:
        """
        Returns information about the most viewed manga.

        Returns a maximum of 20 results

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.manga_by_url(
            url=self.URL_VIEWS,
            offset=offset,
            count=count,
        )

    def manga_liked(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[remanga.MangaAverage]:
        """
        Returns information about the most liked manga.

        Returns a maximum of 20 results

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.manga_by_url(
            url=self.URL_LIKED,
            offset=offset,
            count=count,
        )

    def manga_new(
        self,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[remanga.MangaAverage]:
        """
        Returns information about a new manga.

        Returns a maximum of 20 results

        * :offset: The manga number to start with.
        * :count: The number of manga to get. None is everything.
        * :return: The objects representing manga.
        """
        return self.manga_by_url(
            url=self.URL_NEW,
            offset=offset,
            count=count,
        )
