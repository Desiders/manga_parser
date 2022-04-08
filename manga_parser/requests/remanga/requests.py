from typing import Callable, Optional, Union

from manga_parser.client.base import Response
from manga_parser.exceptions.client import NeedPaymentForUsingSite
from manga_parser.exceptions.remanga.client import \
    NeedAuthorizhationForViewManga
from manga_parser.parsers.remanga.helper import (age_limit_id_by_raw,
                                                 category_id_by_raw,
                                                 genre_id_by_raw,
                                                 status_id_by_raw,
                                                 title_type_id_by_raw)
from manga_parser.requests.requests import Requests
from manga_parser.schemas.remanga import (AgeLimit, Branch, Category, Chapter,
                                          Genre, Manga, Publisher, Status,
                                          TitleType)
from manga_parser.typehints.remanga import (AgeLimitsIdsType, AgeLimitsType,
                                            BranchIdType, BranchOrIdType,
                                            CategoriesIdsType, CategoriesType,
                                            ChapterIdType,
                                            ChapterOrIdOrUrlType,
                                            GenresIdsType, GenresType,
                                            MangaOrUrlType, MangaShortUrlType,
                                            PublisherOrUrlType,
                                            PublisherShortUrlType,
                                            StatusesIdsType, StatusesType,
                                            TitleTypesIdsType, TitleTypesType)
from manga_parser.urls.remanga import RemangaApiUrls, RemangaUrls
from manga_parser.urls.urls import (get_chapter_id_from_chapter_url,
                                    get_chapter_id_from_url, get_short_url,
                                    is_chapter_url, is_url, urls_concat)


def unpacking_params_to_ids(
    fn: Callable[
        ["RemangaRequests",
         str, int,
         CategoriesIdsType,
         GenresIdsType,
         StatusesIdsType,
         TitleTypesIdsType,
         AgeLimitsIdsType],
        Response,
    ],
):
    def wrap(
        *args,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
        **kwargs,
    ):
        if categories:
            categories_ids = []
            for category in categories:
                if isinstance(category, int):
                    category_id = category
                elif isinstance(category, str):
                    category_id = category_id_by_raw(category)
                elif isinstance(category, Category):
                    category_id = category.id
                categories_ids.append(category_id)
        else:
            categories_ids = None

        if genres:
            genres_ids = []
            for genre in genres:
                if isinstance(genre, int):
                    genre_id = genre
                elif isinstance(genre, str):
                    genre_id = genre_id_by_raw(genre)
                elif isinstance(genre, Genre):
                    genre_id = genre.id
                genres_ids.append(genre_id)
        else:
            genres_ids = None

        if statuses:
            statuses_ids = []
            for status in statuses:
                if isinstance(status, int):
                    status_id = status
                elif isinstance(status, str):
                    status_id = status_id_by_raw(status)
                elif isinstance(status, Status):
                    status_id = status.id
                statuses_ids.append(status_id)
        else:
            statuses_ids = None

        if title_types:
            title_types_ids = []
            for title_type in title_types:
                if isinstance(title_type, int):
                    title_type_id = title_type
                elif isinstance(title_type, str):
                    title_type_id = title_type_id_by_raw(title_type)
                elif isinstance(title_type, TitleType):
                    title_type_id = title_type.id
                title_types_ids.append(title_type_id)
        else:
            title_types_ids = None

        if age_limits:
            age_limits_ids = []
            for age_limit in age_limits:
                if isinstance(age_limit, int):
                    age_limit_id = age_limit
                elif isinstance(age_limit, str):
                    age_limit_id = age_limit_id_by_raw(age_limit)
                elif isinstance(age_limit, AgeLimit):
                    age_limit_id = age_limit.id
                age_limits_ids.append(age_limit_id)
        else:
            age_limits_ids = None

        return fn(
            *args,
            **kwargs,
            categories_ids=categories_ids,
            genres_ids=genres_ids,
            statuses_ids=statuses_ids,
            title_types_ids=title_types_ids,
            age_limits_ids=age_limits_ids,
        )
    return wrap


def unpacking_manga_to_id(
    fn: Callable[
        ["RemangaRequests",
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


def unpacking_branch_to_id(
    fn: Callable[
        ["RemangaRequests",
         BranchIdType],
        Response,
    ],
):
    def wrap(
        *args,
        branch_or_id: BranchOrIdType,
        **kwargs,
    ):
        if isinstance(branch_or_id, Branch):
            branch_id = branch_or_id.id
        else:
            branch_id = branch_or_id

        return fn(
            *args,
            **kwargs,
            branch_id=branch_id,
        )
    return wrap


def unpacking_chapter_to_id(
    fn: Callable[
        ["RemangaRequests",
         ChapterIdType],
        Response,
    ],
):
    def wrap(
        *args,
        chapter_or_id_or_url: ChapterOrIdOrUrlType,
        **kwargs,
    ):

        if isinstance(chapter_or_id_or_url, Chapter):
            chapter_id = chapter_or_id_or_url.id
        else:
            if isinstance(chapter_or_id_or_url, str):
                if is_chapter_url(chapter_or_id_or_url):
                    chapter_id = get_chapter_id_from_chapter_url(
                        chapter_or_id_or_url,
                    )
                elif is_url(chapter_or_id_or_url):
                    chapter_id = get_chapter_id_from_url(chapter_or_id_or_url)
                else:
                    chapter_id = chapter_or_id_or_url
            else:
                chapter_id = chapter_or_id_or_url

        return fn(
            *args,
            **kwargs,
            chapter_id=chapter_id,
        )
    return wrap


def unpacking_publisher_to_id(
    fn: Callable[
        ["RemangaRequests",
         PublisherShortUrlType],
        Response,
    ],
):
    def wrap(
        *args,
        publisher_or_url: PublisherOrUrlType,
        **kwargs,
    ):
        if isinstance(publisher_or_url, Publisher):
            short_url = publisher_or_url.short_url
        else:
            if is_url(publisher_or_url):
                short_url = get_short_url(publisher_or_url)
            else:
                short_url = publisher_or_url

        return fn(
            *args,
            **kwargs,
            short_url=short_url,
        )
    return wrap


class RemangaRequests(Requests):
    urls = RemangaUrls
    urls_api = RemangaApiUrls

    def handle_exceptions(self, status_code: int) -> None:
        super().handle_exceptions(status_code)

        if 400 <= status_code < 500:
            if status_code == 401:
                raise NeedAuthorizhationForViewManga(
                    NeedAuthorizhationForViewManga.__doc__,
                )
            if status_code == 402:
                raise NeedPaymentForUsingSite(
                    NeedPaymentForUsingSite.__doc__,
                )

    def request(
        self,
        url: str,
        method: Optional[str] = "GET",
        **kwargs,
    ) -> Response:
        response = super().request(url=url, method=method, **kwargs)

        self.handle_exceptions(response.status_code)

        return response

    def manga_search(self, name: str, count: Union[int, str] = 1) -> Response:
        """
        Search the manga by name

        Site doesn't responsibility to return the transmitted amount of manga.

        :name:
        :count:
        """
        return self.request(
            url=urls_concat(
                self.urls_api.SITE.value,
                self.urls_api.SEARCH.value,
                sep="/", end="/",
            ),
            method="GET",
            params={"query": name, "count": count},
        )

    @unpacking_params_to_ids
    def _manga_type(
        self,
        search_type: str,
        page: int = 1,
        categories_ids: CategoriesIdsType = None,
        genres_ids: GenresIdsType = None,
        statuses_ids: StatusesIdsType = None,
        title_types_ids: TitleTypesIdsType = None,
        age_limits_ids: AgeLimitsIdsType = None,
    ) -> Response:
        """
        Return the manga

        Returns a maximum of 30 results
        1 page - 30 results

        :search_type:
        :page:
        :categories_ids:
        :genres_ids:
        :statuses_ids:
        :title_types_ids:
        :age_limits_ids:
        """
        return self.request(
            url=urls_concat(
                self.urls_api.SITE.value,
                search_type,
                sep="/",
            ),
            method="GET",
            params={
                "page": page,
                "categories": categories_ids,
                "genres": genres_ids,
                "status": statuses_ids,
                "types": title_types_ids,
                "age_limit": age_limits_ids,
            },
        )

    def manga_new(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.NEW.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    def manga_latest_updated(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.LATEST_UPDATED.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    def manga_rating(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.RATING.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    def manga_liked(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.LIKED.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    def manga_viewed(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.VIEWED.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    def manga_count_chapters(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.COUNT_CHAPTERS.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    def manga_random(
        self,
        page: int = 1,
        categories: CategoriesType = None,
        genres: GenresType = None,
        statuses: StatusesType = None,
        title_types: TitleTypesType = None,
        age_limits: AgeLimitsType = None,
    ) -> Response:
        return self._manga_type(
            search_type=self.urls_api.RANDOM.value,
            page=page,
            categories=categories,
            genres=genres,
            statuses=statuses,
            title_types=title_types,
            age_limits=age_limits,
        )

    @unpacking_manga_to_id
    def manga_info(self, short_url: MangaShortUrlType) -> Response:
        """
        Return the manga's information

        :short_url:
        """
        return self.request(
            url=urls_concat(
                self.urls_api.SITE.value,
                self.urls_api.MANGA.value,
                short_url,
                sep="/", end="/",
            ),
            method="GET",
        )

    @unpacking_branch_to_id
    def manga_chapters(self, branch_id: BranchIdType) -> Response:
        """
        Return the manga's chapters

        :branch_id:
        """
        return self.request(
            url=urls_concat(
                self.urls_api.SITE.value,
                self.urls_api.CHAPTERS.value,
                sep="/", end="/",
            ),
            method="GET",
            params={"branch_id": branch_id},
        )

    @unpacking_chapter_to_id
    def chapter_pages(self, chapter_id: ChapterIdType) -> Response:
        """
        Return the chapter's pages

        :chapter_id:
        """
        return self.request(
            url=urls_concat(
                self.urls_api.SITE.value,
                self.urls_api.CHAPTERS.value,
                chapter_id,
                sep="/", end="/",
            ),
            method="GET",
        )

    @unpacking_publisher_to_id
    def publisher_info(self, short_url: PublisherShortUrlType) -> Response:
        """
        Return the publisher's information

        :short_url:
        """
        return self.request(
            url=urls_concat(
                self.urls_api.SITE.value,
                self.urls_api.PUBLISHERS.value,
                short_url,
                sep="/", end="/",
            ),
            method="GET",
        )
