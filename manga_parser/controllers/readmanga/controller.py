from typing import Optional, Union

from manga_parser.controllers.base import Controller
from manga_parser.parsers.readmanga import ReadmangaParser
from manga_parser.requests.readmanga import ReadmangaRequests
from manga_parser.schemas.readmanga import MangaBriefly
from manga_parser.typehints.readmanga import MangaOrUrlType


class ReadmangaController(Controller):
    def __init__(self, requests: ReadmangaRequests, parser: ReadmangaParser):
        self._requests = requests
        self._parser = parser

    @property
    def requests(self):
        return self._requests

    @property
    def parser(self):
        return self._parser

    def manga_search(
        self,
        name: str,
        offset: Union[int, str] = 0,
        limit: Optional[int] = None,
    ) -> list[MangaBriefly]:
        """
        Search the manga by name

        Returns a maximum of 50 results.
        Site and this library doesn't responsibility to return
        the transmitted amount of manga, because together with manga they
        return books and manga from other sites (librebook and mintmanga).

        :name:
         The name by which the manga will be searched.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        """
        return self.parser.manga_search(
            response=self.requests.manga_search(
                name=name,
                offset=offset,
            ),
            limit=limit,
        )

    def manga_info(
        self,
        manga_or_url: MangaOrUrlType,
        parse_chapters: bool = False,
        chapters_offset: int = 0,
        chapters_limit: Optional[int] = None,
        primarily_new_chapters: bool = True,
    ):
        """
        Return the manga's information

        :manga_or_url:
         The manga required to return the information.
         You can transmit url and short url, for example:
          `https://readmanga.io/klinok__rassekaiuchii_demonov__A5327`,
          `klinok__rassekaiuchii_demonov__A5327`.
         (Manga | Manga.url | Manga.short_url)
        :parse_chapters:
         The site returns chapters together with the manga for avoid
         new request. It may parse chapters immediately.
        :chapters_offset:
         The index of the chapter to start with.
        :chapters_limit:
         The amount of the chapters required to return.
        :primarily_new_chapters:
         The first of the chapters is new.
        """
        return self.parser.manga_info(
            response=self.requests.manga_info(
                manga_or_url=manga_or_url,
            ),
            parse_chapters=parse_chapters,
            chapters_offset=chapters_offset,
            chapters_limit=chapters_limit,
            primarily_new_chapters=primarily_new_chapters,
        )
