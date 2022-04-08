from typing import Optional

from bs4 import BeautifulSoup, ResultSet, Tag
from manga_parser.client.base import Response
from manga_parser.exceptions.readmanga.manga import MangaNotFound
from manga_parser.parsers.base import Parser
from manga_parser.pre_data_edit import limit_offset
from manga_parser.schemas.readmanga import (Genre, ImageLow, MangaBriefly,
                                            PublisherBriefly)
from manga_parser.urls.readmanga import ReadmangaUrls
from manga_parser.urls.urls import (get_en_genre_from_short_url,
                                    get_short_publisher_url_from_href,
                                    get_short_url_from_href, urls_concat)


class ReadmangaParser(Parser):
    urls = ReadmangaUrls

    def soup(self, response: Response) -> BeautifulSoup:
        result = BeautifulSoup(response.content, "lxml")

        return result

    @staticmethod
    def is_manga_in_search(class_: str) -> bool:
        return (
            class_.startswith("tile col-md-6")
        )

    @staticmethod
    def is_publisher_in_search(href: str) -> bool:
        return (
            href and
            href.startswith("/list/person/")
        )

    @staticmethod
    def is_genre_in_search(href: Optional[str]) -> bool:
        return (
            href and
            href.startswith("/list/genre/")
        )

    @staticmethod
    def is_holder_in_search(tag: Tag):
        return (
            tag.name == "div" and
            tag.has_attr("class") and
            "html-popover-holder" in tag["class"] and
            tag.parent.name == "noindex"
        )

    def parse_genres(self, genres: ResultSet[Tag]) -> list[Genre]:
        genres_returning = []
        for genre_data in genres:
            genre_short_url: str = genre_data["href"]
            ru_genre: str = genre_data.string

            en_genre = get_en_genre_from_short_url(genre_short_url)

            genres_returning.append(
                Genre(
                    en_value=en_genre,
                    ru_value=ru_genre,
                ),
            )
        return genres_returning

    def parse_publisher_briefly(self, publisher: Tag) -> PublisherBriefly:
        publisher_href: str = publisher["href"]
        publisher_short_url = get_short_publisher_url_from_href(publisher_href)
        publisher_name: str = publisher.string

        url = urls_concat(
            self.urls.SITE.value,
            self.urls.PUBLISHERS.value,
            publisher_short_url,
            sep="/",
        )

        return PublisherBriefly(
            name=publisher_name,
            short_url=publisher_short_url,
            url=url,
        )

    def parse_image_low(self, img: Tag) -> Optional[ImageLow]:
        image: Tag = img.a.find("img")

        if not image:
            return None

        image_url: str = image["data-original"] or image["src"]
        width: str = image["width"]
        height: str = image["height"]

        return ImageLow(
            url=image_url,
            width=width,
            height=height,
        )

    def parse_manga_briefly(self, manga: list[Tag]) -> list[MangaBriefly]:
        manga_returning = []
        for manga_data in manga:
            desc = manga_data.find(class_="desc", recursive=False)

            holder = desc.find(self.is_holder_in_search, recursive=True)

            if not holder:
                # isn't a manga type
                continue

            manga_description: str = holder.find(
                class_="manga-description", recursive=False,
            ).string.strip()
            img_data = manga_data.find(class_="img", recursive=False)
            desc_h3 = desc.find("h3", recursive=False)
            tile_info = desc.find(class_="tile-info", recursive=False)
            publisher_data = tile_info.find(
                href=self.is_publisher_in_search, recursive=False,
            )
            genres_data: ResultSet[Tag] = holder.find_all(
                href=self.is_genre_in_search, recursive=False,
            )

            desc_a: Tag = desc_h3.a
            manga_href: str = desc_a["href"]
            manga_ru_name: str = desc_a.string
            manga_short_url = get_short_url_from_href(manga_href)

            image = self.parse_image_low(img_data)
            genres = self.parse_genres(genres_data)

            if publisher_data:
                publisher = self.parse_publisher_briefly(publisher_data)
            else:
                publisher = None

            manga_url = urls_concat(
                self.urls.SITE.value,
                self.urls.MANGA.value,
                manga_short_url,
                sep="/",
            )

            manga_returning.append(
                MangaBriefly(
                    ru_name=manga_ru_name,
                    description=manga_description,
                    short_url=manga_short_url,
                    url=manga_url,
                    image=image,
                    publisher=publisher,
                    genres=genres,
                ),
            )
        return manga_returning

    def manga_search(
        self,
        response: Response,
        limit: Optional[int] = None,
    ) -> list[MangaBriefly]:
        soup = self.soup(response)

        content = (
            soup.find(class_="leftContent")
                .find(class_="tiles row")
        )

        if content is None:
            raise MangaNotFound(MangaNotFound.__doc__)

        manga_data = content.find_all(
            class_=self.is_manga_in_search,
            recursive=False,
        )
        manga_data = limit_offset(manga_data, 0, limit)

        manga = self.parse_manga_briefly(manga_data)

        return manga

    def manga_info(
        self,
        response: Response,
        parse_chapters: bool = False,
        chapters_offset: int = 0,
        chapters_limit: Optional[int] = None,
        primarily_new_chapters: bool = True,
    ):
        pass
