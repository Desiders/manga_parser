from typing import Optional, Union

from manga_parser.controllers.base import Controller
from manga_parser.parsers.remanga import RemangaParser
from manga_parser.requests.remanga import RemangaRequests
from manga_parser.schemas.remanga import (Chapter, MangaBriefly, MangaHigh,
                                          MangaMedium, Page, PublisherHigh)
from manga_parser.typehints.remanga import (AgeLimitsType, BranchOrIdType,
                                            CategoriesType,
                                            ChapterOrIdOrUrlType, GenresType,
                                            MangaOrUrlType, PublisherOrUrlType,
                                            StatusesType, TitleTypesType)


class RemangaController(Controller):
    def __init__(self, requests: RemangaRequests, parser: RemangaParser):
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
        count: Union[int, str] = 1,
    ) -> list[MangaBriefly]:
        """
        Search the manga by name

        Site doesn't responsibility to return the transmitted amount of manga.

        :name:
         The name by which the manga will be searched.
        :count:
         The amount of the manga required to return.
        """
        return self.parser.manga_search(
            response=self.requests.manga_search(
                name=name,
                count=count,
            ),
        )

    def manga_new(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_new_manga: bool = True,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the most new manga

        Returns a maximum of 30 results.
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_new_manga:
         The first of the manga is new.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_new(
            response=self.requests.manga_new(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
            primarily_new_manga=primarily_new_manga,
        )

    manga_most_new = manga_new

    def manga_latest_updated(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_latest_updated_manga: bool = True,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the most latest updated manga

        Returns a maximum of 30 results
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_latest_updated_manga:
         The first of the manga is latest updated.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_latest_updated(
            response=self.requests.manga_latest_updated(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
            primarily_latest_updated_manga=primarily_latest_updated_manga,
        )

    manga_most_latest_updated = manga_latest_updated

    def manga_rating(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_rating_manga: bool = True,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the most rating manga

        Returns a maximum of 30 results
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_rating_manga:
         The first of the manga is most rating.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_rating(
            response=self.requests.manga_rating(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
            primarily_rating_manga=primarily_rating_manga,
        )

    manga_most_rating = manga_rating

    def manga_liked(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_liked_manga: bool = True,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the most liked manga

        Returns a maximum of 30 results
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_liked_manga:
         The first of the manga is most liked.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_liked(
            response=self.requests.manga_liked(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
            primarily_liked_manga=primarily_liked_manga,
        )

    manga_most_liked = manga_liked

    def manga_viewed(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_viewed_manga: bool = True,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the most viewed manga

        Returns a maximum of 30 results
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_viewed_manga:
         The first of the manga is most viewed.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_viewed(
            response=self.requests.manga_viewed(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
            primarily_viewed_manga=primarily_viewed_manga,
        )

    manga_most_viewed = manga_viewed

    def manga_count_chapters(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_count_chapters_manga: bool = True,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the manga with most count chapters

        Returns a maximum of 30 results
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_count_chapters_manga:
         The first of the manga with most count chapters.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_count_chapters(
            response=self.requests.manga_count_chapters(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
            primarily_count_chapters_manga=primarily_count_chapters_manga,
        )

    manga_most_count_chapters = manga_count_chapters

    def manga_random(
        self,
        page: int = 1,
        offset: int = 0,
        limit: Optional[int] = None,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> list[MangaMedium]:
        """
        Return the random manga

        Returns a maximum of 30 results
        1 page = 30 results

        :page:
         The number of the page with results.
        :offset:
         The index of the manga to start with.
        :limit:
         The amount of the manga required to return.
        :categories:
         The categories by which the manga will be searched.
         (Category | Category.id | Category.value)
        :genres:
         The genres by which the manga will be searched.
         (Genre | Genre.id | Genre.value)
        :statuses:
         The statuses by which the manga will be searched.
         (Status | Status.id | Status.{lang_code}_value)
        :title_types:
         The title types by which the manga will be searched.
         (TitleType | TitleType.id | TitleType.{lang_code}_value)
        :age_limits:
         The age limits by which the manga will be searched.
         (AgeLimit | AgeLimit.id | AgeLimit.value)
        """
        return self.parser.manga_random(
            response=self.requests.manga_random(
                page=page,
                categories=categories,
                genres=genres,
                statuses=statuses,
                title_types=title_types,
                age_limits=age_limits,
            ),
            offset=offset,
            limit=limit,
        )

    def manga_info(self, manga_or_url: MangaOrUrlType) -> MangaHigh:
        """
        Return the manga's information

        :manga_or_url:
         The manga required to return the information.
         You can transmit url and short url, for example:
          `https://remanga.org/manga/the_beginning_after_the_end`,
          `the_beginning_after_the_end`.
         (Manga | Manga.url | Manga.short_url)
        """
        return self.parser.manga_info(
            response=self.requests.manga_info(
                manga_or_url=manga_or_url,
            ),
        )

    def manga_chapters(
        self,
        branch_or_id: BranchOrIdType,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_new_chapters: bool = True,
    ) -> list[Chapter]:
        """
        Return the manga's chapters

        :branch_or_id:
         The branch for return specifying the specific branch's chapters.
         Different teams can have different branches.
         (Branch | Branch.id)
        :offset:
         The index of the manga's chapter to start with.
        :limit:
         The amount of the manga required to return.
        :primarily_new_chapters:
         The first of the chapters is new.
        """
        return self.parser.manga_chapters(
            response=self.requests.manga_chapters(
                branch_or_id=branch_or_id,
            ),
            offset=offset,
            limit=limit,
            primarily_new_chapters=primarily_new_chapters,
        )

    def chapter_pages(
        self,
        chapter_or_id_or_url: ChapterOrIdOrUrlType,
        offset: int = 0,
        limit: Optional[int] = None,
        primarily_first_pages: bool = True,
    ) -> list[Page]:
        """
        Return the chapter's pages

        :chapter_or_id_or_url:
         The chapter of the manga to return the pages.
         You can transmit url and short url, for example:
          `https://remanga.org/manga/the_beginning_after_the_end/ch59059`,
          `ch59059`.
         (Chapter | Chapter.id)
        :offset:
         The index of the chapter's page to start with.
        :limit:
         The amount of the pages required to return.
        :primarily_first_pages:
         The first of the pages is first.
        """
        return self.parser.chapter_pages(
            response=self.requests.chapter_pages(
                chapter_or_id_or_url=chapter_or_id_or_url,
            ),
            offset=offset,
            limit=limit,
            primarily_first_pages=primarily_first_pages,
        )

    def publisher_info(
        self,
        publisher_or_url: PublisherOrUrlType,
    ) -> PublisherHigh:
        """
        Return the publisher's information

        :publisher_or_url:
         The publisher required to return the information.
         (Publisher | Publisher.url | Publisher.short_url)
        """
        return self.parser.publisher_info(
            response=self.requests.publisher_info(
                publisher_or_url=publisher_or_url,
            ),
        )
