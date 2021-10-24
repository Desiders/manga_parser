import typing

import bs4

from .. import exceptions
from ..schemas import remanga
from ..utils import edit_start, limit_offset, urls_concat


class BaseUrls:
    """
    The base class of requests to the site https://remanga.org
    """

    __hash__ = None
    __slots__ = ()

    URL_SITE = "https://remanga.org"
    URL_SEARCH = "https://remanga.org/api/search"
    URL_MANGA = "https://remanga.org/manga"
    URL_MANGA_API = "https://remanga.org/api/titles"
    URL_CHAPTERS = "https://api.remanga.org/api/titles/chapters"
    URL_TEAM = "https://remanga.org/team"
    URL_TEAM_API = "https://remanga.org/api/publishers"
    URL_RECOMMENDATIONS = "https://remanga.org/api/titles/recommendations"
    URL_VIEWS = "https://remanga.org/api/titles/?ordering=-total_views"
    URL_LIKED = "https://remanga.org/api/titles/?ordering=-total_votes"
    URL_NEW = "https://remanga.org/api/titles/?ordering=-id"


class ReMangaParser(BaseUrls):
    """
    The parser of site https://remanga.org
    """

    __slots__ = ()

    def parse_manga_search(
        self,
        manga_json: typing.Dict[str, typing.Any],
    ) -> typing.List[remanga.MangaBriefly]:
        content = manga_json["content"]

        if content == []:
            raise exceptions.MangaNotFound((
                "The manga not found! "
                "Check the correctness of the name that you passed. "
            ))

        manga = []
        for manga_info in content:
            manga_short_url = manga_info["dir"]
            manga_url = urls_concat([self.URL_MANGA, manga_short_url], sep="/")

            photo_url = urls_concat([self.URL_SITE, manga_info["img"]["high"]])

            manga.append(
                remanga.MangaBriefly(
                    rus_name=manga_info["rus_name"],
                    en_name=manga_info["en_name"],
                    dir=manga_short_url,
                    url=manga_url,
                    img=photo_url,
                    id=manga_info["id"],
                    avg_rating=float(manga_info["avg_rating"]),
                    issue_year=manga_info["issue_year"],
                    count_chapters=manga_info["count_chapters"],
                )
            )

        return manga

    def parse_manga_info(
        self,
        manga_json: typing.Dict[str, typing.Any],
        short_url: str,
    ) -> remanga.Manga:
        content = manga_json["content"]

        if content == []:
            message: str = manga_json["msg"]
            if message.startswith("Контент для взрослых"):
                raise exceptions.MangaNeedAuthorization((
                    "Needs authorization to view this manga! "
                    "The manga unavailable for viewing by minors. "
                    "You can change the headers and set token. "
                ))
            raise exceptions.MangaNotFound((
                "The manga not found! "
                "Check the correctness of the short_url that you passed. "
            ))

        genres = [
            genre["name"]
            for genre in content["genres"]
        ]

        translators = []
        for translator in content["publishers"]:
            translator_short_url = translator["dir"]
            url = urls_concat(
                urls=[self.URL_TEAM, translator_short_url],
                sep="/",
            )

            translators.append(
                remanga.TranslatorBriefly(
                    name=translator["name"],
                    tagline=translator["tagline"],
                    dir=translator_short_url,
                    url=url,
                )
            )

        branches = []
        for branch_info in content["branches"]:
            branch_translators = []
            for translator in branch_info["publishers"]:
                translator_short_url = translator["dir"]
                url = urls_concat(
                    urls=[self.URL_TEAM, translator_short_url],
                    sep="/",
                )

                branch_translators.append(
                    remanga.TranslatorBriefly(
                        name=translator["name"],
                        tagline=translator["tagline"],
                        dir=translator_short_url,
                        url=url,
                    )
                )

            photo_short_url = branch_info["img"]
            if photo_short_url:
                photo_url = urls_concat([self.URL_SITE, photo_short_url])
            else:
                photo_url = None

            branches.append(
                remanga.Branch(
                    id=branch_info["id"],
                    img=photo_url,
                    publishers=translators,
                    total_votes=branch_info["total_votes"],
                    count_chapters=branch_info["count_chapters"],
                )
            )

        manga_url = urls_concat([self.URL_MANGA, short_url], sep="/")

        soup = bs4.BeautifulSoup(content["description"], "lxml")
        description = soup.text

        photo_url = urls_concat([self.URL_SITE, content["img"]["high"]])

        return remanga.Manga(
            rus_name=content["rus_name"],
            en_name=content["en_name"],
            dir=short_url,
            url=manga_url,
            id=content["id"],
            description=description,
            img=photo_url,
            count_rating=content["count_rating"],
            avg_rating=content["avg_rating"],
            count_bookmarks=content["count_bookmarks"],
            total_votes=content["total_votes"],
            total_views=content["total_views"],
            status=content["status"]["name"],
            issue_year=content["issue_year"],
            type=content["type"]["name"],
            genres=genres,
            publishers=translators,
            branches=branches,
            count_chapters=content["count_chapters"],
        )

    def parse_manga_chapters(
        self,
        chapters_json: typing.Dict[str, typing.Any],
        offset: int = 0,
        count: typing.Optional[int] = None,
        primarily_new: bool = True,
    ) -> typing.List[remanga.Chapter]:
        content: list = chapters_json["content"]

        if content == []:
            raise exceptions.ChaptersNotFound((
                "The chapters was not found! "
                "Check the correctness of the branch_id that you passed. "
                "Maybe everything is correct, but the chapters aren't found. "
            ))

        chapters = []
        for chapter_info in limit_offset(
            iterable=edit_start(
                iterable=content,
                start_with_new=primarily_new,
            ),
            offset=offset,
            limit=count,
        ):
            translators = [
                translator["name"]
                for translator in chapter_info["publishers"]
            ]

            price = chapter_info["price"]
            if price:
                price = float(price)

            chapters.append(
                remanga.Chapter(
                    name=chapter_info["name"] or None,
                    id=chapter_info["id"],
                    tome=chapter_info["tome"],
                    chapter=chapter_info["chapter"],
                    index=chapter_info["index"],
                    score=chapter_info["score"],
                    is_free=not chapter_info["is_paid"],
                    price=price,
                    pub_date=chapter_info["pub_date"],
                    upload_date=chapter_info["upload_date"],
                    publishers=translators,
                )
            )

        return chapters

    def parse_chapter_pages(
        self,
        pages_json: typing.Dict[str, typing.Any],
        offset: int = 0,
        count: typing.Optional[int] = None,
        primarily_first: bool = True,
    ) -> typing.List[remanga.Page]:
        content: typing.Dict[list, dict] = pages_json["content"]

        if content == []:
            raise exceptions.ChapterNotFound((
                "The chapter was not found! "
                "Check the correctness of the chapter_id that you passed. "
            ))

        pages = []
        for page in limit_offset(
            iterable=edit_start(
                iterable=content["pages"],
                start_with_new=primarily_first,
            ),
            offset=offset,
            limit=count,
        ):
            pages.append(
                remanga.Page(
                    link=page["link"],
                    height=page["height"],
                    width=page["width"],
                    count_comments=page["count_comments"],
                )
            )

        return pages

    def parse_translator_info(
        self,
        translator_json: typing.Dict[str, typing.Any],
        short_url: str,
    ) -> remanga.Translator:
        content: typing.Dict[list, dict] = translator_json["content"]

        if content == []:
            raise exceptions.TranslatorNotFound((
                "The translator not found! "
                "Check the correctness of the short_url that you passed. "
            ))

        contacts = {
            source: link
            for source, link in content["links"].items()
            if link != ""
        }

        soup = bs4.BeautifulSoup(content["description"], "lxml")
        description = soup.text

        photo_url = urls_concat([self.URL_SITE, content["img"]["high"]])

        translator_url = urls_concat([self.URL_TEAM, short_url], "/")

        return remanga.Translator(
            name=content["name"],
            tagline=content["tagline"],
            description=description,
            img=photo_url,
            dir=short_url,
            url=translator_url,
            rank=content["rank"]["name"],
            count_titles=content["count_titles"],
            count_votes=content["count_votes"],
            count_period_chapters=content["count_period_chapters"],
            links=contacts,
        )

    def parse_manga_by_url(
        self,
        manga_json: typing.Dict[str, typing.Any],
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[remanga.MangaAverage]:
        content = manga_json["content"]

        if content == []:
            raise exceptions.MangaNotFound((
                "The manga not found! "
                "The source didn't return manga. "
            ))

        manga = []
        for manga_info in limit_offset(
            iterable=content,
            offset=offset,
            limit=count,
        ):
            genres = manga_info["genres"]
            if genres is not None:
                genres = [
                    genre["name"]
                    for genre in manga_info["genres"]
                ]
            else:
                genres = []

            manga_short_url = manga_info["dir"]
            manga_url = urls_concat([self.URL_MANGA, manga_short_url], sep="/")

            photo_url = urls_concat([self.URL_SITE, manga_info["img"]["high"]])

            manga.append(
                remanga.MangaAverage(
                    rus_name=manga_info["rus_name"],
                    en_name=manga_info["en_name"],
                    dir=manga_short_url,
                    url=manga_url,
                    id=manga_info["id"],
                    img=photo_url,
                    avg_rating=float(manga_info["avg_rating"]),
                    total_votes=manga_info["total_votes"],
                    total_views=manga_info["total_views"],
                    issue_year=manga_info["issue_year"],
                    type=manga_info["type"],
                    genres=genres,
                    count_chapters=manga_info["count_chapters"],
                )
            )

        return manga
