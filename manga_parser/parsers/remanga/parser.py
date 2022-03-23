from typing import Optional, Type

from manga_parser.client.base import Response
from manga_parser.exceptions.remanga.client import \
    NeedAuthorizhationForViewManga
from manga_parser.exceptions.remanga.manga import (ChapterNotFound,
                                                   ChaptersNotFound,
                                                   MangaNotFound)
from manga_parser.exceptions.remanga.publisher import PublisherNotFound
from manga_parser.parsers.base import Parser
from manga_parser.parsers.remanga.helper import (age_limit_by_id,
                                                 category_by_id,
                                                 escape_html_tags, genre_by_id,
                                                 publisher_type_by_id,
                                                 publisher_type_by_raw,
                                                 rank_by_id, status_by_id,
                                                 title_type_by_id,
                                                 title_type_by_raw)
from manga_parser.pre_data_edit import limit_offset, reverse
from manga_parser.schemas.remanga import (Branch, Category, Chapter, Contacts,
                                          Genre, ImageHigh, ImageLow,
                                          ImageMiddle, MangaBriefly, MangaHigh,
                                          MangaMedium, Page, Publisher,
                                          PublisherHigh, PublisherMedium,
                                          Subscription)
from manga_parser.urls.remanga import RemangaApiUrls, RemangaUrls
from manga_parser.urls.urls import urls_concat


class RemangaParser(Parser):
    urls = RemangaUrls
    urls_api = RemangaApiUrls

    def payload(self, response: Response) -> dict:
        result = response.json()

        return result

    def parse_genres(self, genres: list[dict]) -> list[Genre]:
        return [
            genre_by_id(genre["id"])
            for genre in genres
        ]

    def parse_categories(self, categories: list[dict]) -> list[Category]:
        return [
            category_by_id(category["id"])
            for category in categories
        ]

    def parse_manga_briefly(self, manga: list[dict]) -> list[MangaBriefly]:
        _site = self.urls.SITE.value
        _manga = self.urls.MANGA.value

        manga_returning = []
        for manga_data in manga:
            manga_id = manga_data["id"]
            en_name = manga_data["en_name"]
            ru_name = manga_data["rus_name"]
            short_url = manga_data["dir"]
            issue_year = manga_data["issue_year"]
            rating = manga_data["avg_rating"]
            count_chapters = manga_data["count_chapters"]

            title_type = title_type_by_id(manga_data["type"])
            images = self.parse_images(manga_data["img"])

            url = urls_concat(
                _site, _manga, short_url,
                sep="/",
            )

            manga_returning.append(
                MangaBriefly(
                    id=manga_id,
                    en_name=en_name,
                    ru_name=ru_name,
                    short_url=short_url,
                    url=url,
                    title_type=title_type,
                    images=images,
                    issue_year=issue_year,
                    rating=rating,
                    count_chapters=count_chapters,
                ),
            )
        return manga_returning

    def parse_manga_medium(self, manga: list[dict]) -> list[MangaMedium]:
        _site = self.urls.SITE.value
        _manga = self.urls.MANGA.value

        manga_returning = []
        for manga_data in manga:
            manga_id = manga_data["id"]
            en_name = manga_data["en_name"]
            ru_name = manga_data["rus_name"]
            short_url = manga_data["dir"]
            issue_year = manga_data["issue_year"]
            rating = manga_data["avg_rating"]
            liked = manga_data["total_votes"]
            views = manga_data["total_views"]

            title_type = title_type_by_raw(manga_data["type"])
            images = self.parse_images(manga_data["img"])

            genres_data = manga_data["genres"]
            if genres_data:
                genres = self.parse_genres(manga_data["genres"])
            else:
                genres = []

            categories_data = manga_data["categories"]
            if categories_data:
                categories = self.parse_categories(manga_data["categories"])
            else:
                categories = []

            url = urls_concat(
                _site, _manga, short_url,
                sep="/",
            )

            manga_returning.append(
                MangaMedium(
                    id=manga_id,
                    en_name=en_name,
                    ru_name=ru_name,
                    short_url=short_url,
                    url=url,
                    title_type=title_type,
                    images=images,
                    issue_year=issue_year,
                    rating=rating,
                    liked=liked,
                    views=views,
                    genres=genres,
                    categories=categories,
                ),
            )
        return manga_returning

    def parse_manga_high(self, manga_data: dict) -> MangaHigh:
        manga_id = manga_data["id"]
        en_name = manga_data["en_name"]
        ru_name = manga_data["rus_name"]
        short_url = manga_data["dir"]
        issue_year = manga_data["issue_year"]
        rating = manga_data["avg_rating"]
        count_chapters = manga_data["count_chapters"]
        liked = manga_data["total_votes"]
        views = manga_data["total_views"]
        another_name = manga_data["another_name"]
        count_chapters = manga_data["count_chapters"]
        votes = manga_data["count_rating"]
        bookmarks = manga_data["count_bookmarks"]

        title_type = title_type_by_id(manga_data["type"]["id"])
        images = self.parse_images(manga_data["img"])
        description = escape_html_tags(manga_data["description"])
        status = status_by_id(manga_data["type"]["id"])
        age_limit = age_limit_by_id(manga_data["age_limit"])
        publishers = self.parse_publishers_medium(manga_data["publishers"])
        branches = self.parse_branches(manga_data["branches"], publishers)

        genres_data = manga_data["genres"]
        if genres_data:
            genres = self.parse_genres(manga_data["genres"])
        else:
            genres = []

        categories_data = manga_data["categories"]
        if categories_data:
            categories = self.parse_categories(manga_data["categories"])
        else:
            categories = []

        url = urls_concat(
            self.urls.SITE.value, self.urls.MANGA.value,
            short_url, sep="/",
        )

        return MangaHigh(
            id=manga_id,
            en_name=en_name,
            ru_name=ru_name,
            short_url=short_url,
            url=url,
            title_type=title_type,
            images=images,
            issue_year=issue_year,
            rating=rating,
            liked=liked,
            views=views,
            genres=genres,
            categories=categories,
            another_name=another_name,
            count_chapters=count_chapters,
            votes=votes,
            bookmarks=bookmarks,
            description=description,
            status=status,
            age_limit=age_limit,
            publishers=publishers,
            branches=branches,
        )

    def parse_publishers_medium(
        self,
        publishers: list[dict],
    ) -> list[PublisherMedium]:
        _site = self.urls.SITE.value
        _publishers = self.urls.PUBLISHERS.value

        publishers_returning = []
        for publisher_data in publishers:
            publisher_id = publisher_data["id"]
            name = publisher_data["name"]
            short_url = publisher_data["dir"]

            short_description = escape_html_tags(publisher_data["tagline"])
            publisher_type = publisher_type_by_raw(publisher_data["type"])
            image = self.parse_image_low(publisher_data["img"])

            url = urls_concat(
                _site, _publishers, short_url,
                sep="/",
            )

            publishers_returning.append(
                PublisherMedium(
                    id=publisher_id,
                    name=name,
                    short_description=short_description,
                    publisher_type=publisher_type,
                    short_url=short_url,
                    url=url,
                    image=image,
                ),
            )
        return publishers_returning

    def parse_publisher_high(self, publisher: dict) -> PublisherHigh:
        _site = self.urls.SITE.value
        _publishers = self.urls.PUBLISHERS.value

        publisher_id = publisher["id"]
        name = publisher["name"]
        short_url = publisher["dir"]
        liked = publisher["count_votes"]
        count_titles = publisher["count_titles"]
        chapters_per_month = publisher["count_period_chapters"]
        subscription_data = publisher["paid_subscription"]

        short_description = escape_html_tags(publisher["tagline"])
        description = escape_html_tags(publisher["description"])
        publisher_type = publisher_type_by_id(publisher["type"]["id"])
        image = self.parse_image_low(publisher["img"]["low"])
        images = self.parse_images(publisher["img"])
        rank = rank_by_id(publisher["rank"]["id"])
        contacts = self.parse_contacts(publisher["links"])

        if subscription_data is not None:
            subscription = self.parse_subscription(subscription_data)
        else:
            subscription = None

        url = urls_concat(
            _site, _publishers, short_url,
            sep="/",
        )

        return PublisherHigh(
            id=publisher_id,
            name=name,
            short_description=short_description,
            description=description,
            publisher_type=publisher_type,
            short_url=short_url,
            url=url,
            image=image,
            images=images,
            rank=rank,
            liked=liked,
            count_titles=count_titles,
            chapters_per_month=chapters_per_month,
            contacts=contacts,
            subscription=subscription,
        )

    def cache_publishers_by_id(
        self,
        publishers: list[Type[Publisher]],
        publishers_raw: list[dict],
    ) -> list[Type[Publisher]]:
        publishers_ids: list[int] = [
            publisher_raw["id"]
            for publisher_raw in publishers_raw
        ]

        publishers = []
        for publisher_data in publishers:
            publisher_id = publisher_data.id
            if publisher_id in publishers_ids:
                publishers.append(publisher_data)

        return publishers

    def parse_branches(
        self,
        branches: list[dict],
        publishers: list[Type[Publisher]],
    ) -> list[Branch]:
        branches_returning = []
        for branch_data in branches:
            branch_id = branch_data["id"]
            liked = branch_data["total_votes"]
            count_chapters = branch_data["count_chapters"]

            image = self.parse_image_low(branch_data["img"])

            publishers = self.cache_publishers_by_id(
                publishers=publishers,
                publishers_raw=branch_data["publishers"],
            )
            # publishers = self.parse_publishers(branch_data["publishers"])
            # we have already parsed publishers and get their
            # from the saved data

            branches_returning.append(
                Branch(
                    id=branch_id,
                    image=image,
                    liked=liked,
                    count_chapters=count_chapters,
                    publishers=publishers,
                ),
            )
        return branches_returning

    def parse_chapters(self, chapters: list[dict]) -> list[Chapter]:
        chapters_returning = []
        for chapter_data in chapters:
            chapter_id = chapter_data["id"]
            tome = chapter_data["tome"]
            chapter_number = chapter_data["chapter"]
            chapter_index = chapter_data["index"]
            name = chapter_data["name"]
            liked = chapter_data["score"]
            is_paid = chapter_data["is_paid"]
            price = chapter_data["price"]
            upload_date = chapter_data["upload_date"]
            free_date = chapter_data["pub_date"]

            chapters_returning.append(
                Chapter(
                    id=chapter_id,
                    tome=tome,
                    chapter_number=chapter_number,
                    chapter_index=chapter_index,
                    name=name,
                    liked=liked,
                    is_paid=is_paid,
                    price=price,
                    upload_date=upload_date,
                    free_date=free_date,
                ),
            )
        return chapters_returning

    def parse_pages(self, pages: list[dict]) -> list[Page]:
        pages_returning = []
        for page_data in pages:
            page_id = page_data["id"]
            url = page_data["link"]
            height = page_data["height"]
            width = page_data["width"]
            count_comments = page_data["count_comments"]

            pages_returning.append(
                Page(
                    id=page_id,
                    url=url,
                    height=height,
                    width=width,
                    count_comments=count_comments,
                ),
            )
        return pages_returning

    def parse_contacts(self, contacts: dict) -> Contacts:
        vk = contacts["vk"] or None
        facebook = contacts["fb"] or None
        youtube = contacts["youtube"] or None
        twitter = contacts["twitter"] or None
        instagram = contacts["insta"] or None
        discord = contacts["discord"] or None

        return Contacts(
            vk=vk,
            facebook=facebook,
            youtube=youtube,
            twitter=twitter,
            instagram=instagram,
            discord=discord,
        )

    def parse_subscription(self, subscription: dict) -> Subscription:
        subscription_id = subscription["id"]
        name = subscription["name"]
        description = subscription["description"]
        price = subscription["price"]
        period = subscription["period"]

        return Subscription(
            id=subscription_id,
            name=name,
            description=description,
            price=price,
            period=period,
        )

    def parse_image_low(self, image: str) -> ImageLow:
        return ImageLow(url=urls_concat(self.urls.SITE.value, image))

    def parse_image_middle(self, image: str) -> ImageMiddle:
        return ImageMiddle(url=urls_concat(self.urls.SITE.value, image))

    def parse_image_high(self, image: str) -> ImageHigh:
        return ImageHigh(url=urls_concat(self.urls.SITE.value, image))

    def parse_images(
        self,
        images: dict,
    ) -> tuple[ImageLow, ImageMiddle, ImageHigh]:
        return (
            self.parse_image_low(images["low"]),
            self.parse_image_middle(images["mid"]),
            self.parse_image_high(images["high"]),
        )

    def manga_search(self, response: Response) -> list[MangaBriefly]:
        payload = self.payload(response)

        content = payload["content"]

        if content == []:
            raise MangaNotFound(MangaNotFound.__doc__)
        else:
            manga_data = content

        manga = self.parse_manga_briefly(manga_data)

        return manga

    def _manga_type(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_type: Optional[bool] = True,
    ) -> list[MangaMedium]:
        payload = self.payload(response)

        content = payload["content"]

        if content == []:
            raise MangaNotFound(MangaNotFound.__doc__)
        else:
            manga_data = content

        if primarily_type is not None and not primarily_type:
            manga_data = reverse(manga_data)
        manga_data = limit_offset(manga_data, offset, limit)

        manga = self.parse_manga_medium(manga_data)

        return manga

    def manga_new(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_new_manga: bool = True,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=primarily_new_manga,
        )

    def manga_latest_updated(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_latest_updated_manga: bool = True,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=primarily_latest_updated_manga,
        )

    def manga_rating(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_rating_manga: bool = True,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=primarily_rating_manga,
        )

    def manga_liked(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_liked_manga: bool = True,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=primarily_liked_manga,
        )

    def manga_viewed(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_viewed_manga: bool = True,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=primarily_viewed_manga,
        )

    def manga_count_chapters(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_count_chapters_manga: bool = True,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=primarily_count_chapters_manga,
        )

    def manga_random(
        self,
        response: Response,
        offset: int = 0,
        limit: Optional[int] = None,
    ) -> list[MangaMedium]:
        return self._manga_type(
            response=response,
            offset=offset,
            limit=limit,
            primarily_type=None,
        )

    def manga_info(self, response: Response) -> MangaHigh:
        payload = self.payload(response)

        content = payload["content"]

        if content == []:
            message: str = payload["msg"]

            if message.startswith("Контент для взрослых"):
                raise NeedAuthorizhationForViewManga(
                    NeedAuthorizhationForViewManga.__doc__,
                )
            raise MangaNotFound(MangaNotFound.__doc__)
        else:
            manga_data = content

        manga = self.parse_manga_high(manga_data)

        return manga

    def manga_chapters(
        self,
        response: Response,
        offset: int,
        limit: Optional[int] = None,
        primarily_new_chapters: bool = True,
    ) -> list[Chapter]:
        payload = self.payload(response)

        content = payload["content"]

        if content == []:
            raise ChaptersNotFound(ChaptersNotFound.__doc__)
        else:
            chapters_data = content

        if not primarily_new_chapters:
            chapters_data = reverse(chapters_data)
        chapters_data = limit_offset(chapters_data, offset, limit)

        chapters = self.parse_chapters(chapters_data)

        return chapters

    def chapter_pages(
        self,
        response: Response,
        offset: int,
        limit: Optional[int] = None,
        primarily_first_pages: bool = True,
    ):
        payload = self.payload(response)

        content = payload["content"]

        if content == []:
            raise ChapterNotFound(ChapterNotFound.__doc__)
        else:
            pages_data = content["pages"]

        if not primarily_first_pages:
            pages_data = reverse(pages_data)
        pages_data = limit_offset(pages_data, offset, limit)

        pages = self.parse_pages(pages_data)

        return pages

    def publisher_info(
        self,
        response: Response,
    ) -> PublisherHigh:
        payload = self.payload(response)

        content = payload["content"]

        if content == []:
            raise PublisherNotFound(PublisherNotFound.__doc__)
        else:
            publisher_data = content

        publisher = self.parse_publisher_high(publisher_data)

        return publisher
