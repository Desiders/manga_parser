import json
import typing

import bs4

from .. import exceptions
from ..schemas import readmanga
from ..utils import edit_start, get_urls, limit_offset, urls_concat


class BaseUrls:
    """
    The base class of requests to the site https://readmanga.io
    """

    __hash__ = None
    __slots__ = ()

    URL_SITE = "https://readmanga.io"
    URL_SEARCH = "https://readmanga.io/search"
    URL_TRANSLATOR = "https://readmanga.io/list/person"
    URL_POPULAR = "https://readmanga.io/recommendations/top"
    URL_BEST = "https://readmanga.io/list?sortType=votes"
    URL_NEW = "https://readmanga.io/list?sortType=created"


class ReadMangaParser(BaseUrls):
    """
    The parser of site https://readmanga.io
    """

    __slots__ = ()

    def parse_manga_search(
        self,
        soup: bs4.BeautifulSoup,
        count: typing.Optional[int] = 1,
    ) -> typing.List[readmanga.MangaBriefly]:
        content = soup.find(class_="leftContent")\
                      .find(class_="tiles row")

        if content is None:
            raise exceptions.MangaNotFound((
                "The manga not found! "
                "Check the correctness of the name that you passed. "
                "You may have specified too large offset! "
            ))

        manga = []
        for tag in limit_offset(
            iterable=content.find_all(class_="img"),
            offset=0,
            limit=count,
        ):
            tag: bs4.element.Tag

            name = tag.find_next(name="h3").a.string

            short_url, url = get_urls(tag, self.URL_SITE)

            photo = tag.a.find_next()["data-original"]

            manga.append(
                readmanga.MangaBriefly(
                    name=name,
                    short_url=short_url,
                    url=url,
                    photo=photo,
                )
            )

        return manga

    def parse_manga_info(
        self,
        soup: bs4.BeautifulSoup,
        short_url: str,
        chapters_offset: int = 0,
        chapters_count: typing.Optional[int] = None,
        chapters_primarily_new: bool = True,
    ) -> readmanga.Manga:
        manga = {}

        left_content = soup.find(class_="leftContent")

        # name, url, description
        for page_element in left_content.find(
            name=["h1", "meta"],
            recursive=False,
        ).find_next_siblings(
            name="meta",
            recursive=False,
        ):
            manga[page_element["itemprop"]] = page_element["content"]

        for photo in left_content.find(class_="picture-fotorama")\
                                 .find_all(
            name="img",
            recursive=False,
        ):
            manga.setdefault("photo", []).append(photo["data-full"])

        subject = left_content.find(class_="col-sm-7")

        # votes, stars
        type_by_name = {"ratingCount": int, "ratingValue": float}
        for rating in subject.find(class_="user-rating")\
                             .find_all(
            name="meta",
            recursive=False,
            itemprop=type_by_name.keys(),
        ):
            name = rating["itemprop"]

            manga[name] = type_by_name[name](rating["content"])

        type_info = subject.find(class_="subject-meta")

        try:
            _, manga["status"] = type_info.find(
                name="p",
                recursive=False,
            ).text.rsplit(maxsplit=1)
        except ValueError:
            manga["status"] = "завершен"

        manga["elem_year"] = int(
            type_info.find(class_="elem_year").a.string
        )

        category = type_info.find(class_="elem_category")
        if category:
            manga["elem_category"] = category.a.string

        # genres, tags, etc
        for tag in type_info.find_all(
            class_=["elem_genre", "elem_another", "elem_tag"],
        ):
            tag: bs4.element.Tag

            manga.setdefault("tags", []).append(tag.a.string)

        # authors, screenwriters, illustrators
        for name in ["elem_author", "elem_screenwriter", "elem_illustrator"]:
            for tag in type_info.find_all(class_=name):
                tag: bs4.element.Tag

                manga.setdefault(name, []).append(tag.a.string)

        # publishers
        for publisher in type_info.find_all(class_="elem_publisher"):
            publisher: bs4.element.Tag

            manga.setdefault("elem_publisher", []).append(
                publisher.string.strip(", "),
            )

        # translators
        for translator in type_info.find_all(class_="elem_translator"):
            translator: bs4.element.Tag

            name = translator.a.string

            translator_short_url = translator.a["href"]
            translator_url = urls_concat([
                self.URL_SITE, translator_short_url,
            ])

            manga.setdefault("elem_translator", []).append(
                readmanga.TranslatorBriefly(
                    name=name,
                    short_url=translator_short_url[1:],  # without "/"
                    url=translator_url,
                ),
            )

        # chapters
        subject = left_content.find(class_="table table-hover")
        if subject:
            chapters = subject.find(
                lambda tag: tag.parent.name != "thead",
                recursive=False,
            ).find_next_siblings()

            manga["count_chapters"] = len(chapters)

            for page_element in limit_offset(
                iterable=edit_start(
                    iterable=chapters,
                    start_with_new=chapters_primarily_new,
                ),
                offset=chapters_offset,
                limit=chapters_count,
            ):
                page_element: bs4.element.Tag

                if page_element.td.has_attr("rowspan"):
                    page_element.td.decompose()

                name = page_element.a.text.strip(" \n")

                chapter_url = urls_concat([
                    self.URL_SITE, page_element.a["href"],
                ])

                title = page_element.a["title"]
                if title:
                    translator, _ = title.rsplit(maxsplit=1)
                else:
                    translator = None

                date = page_element.td.find_next()\
                                      .find_next().string.strip(" \n")

                manga.setdefault("chapters", []).append(
                    readmanga.Chapter(
                        name=name,
                        url=chapter_url,
                        translator=translator,
                        date=date,
                    )
                )

        for similar in soup.find(class_="rightContent")\
                           .find(name="ol", class_="mangaList")\
                           .find_all(name="li"):
            similar: bs4.element.Tag

            name = similar.a.text.strip()

            similar_short_url, similar_url = get_urls(tag, self.URL_SITE)

            photo = similar.span["rel"]

            manga.setdefault("similar", []).append(
                readmanga.MangaBriefly(
                    name=name,
                    short_url=similar_short_url,
                    url=similar_url,
                    photo=photo,
                )
            )

        return readmanga.Manga(
            short_url=short_url,
            **manga,
        )

    def parse_chapter_pages(
        self,
        soup: bs4.BeautifulSoup,
        offset: int = 0,
        count: typing.Optional[int] = None,
        primarily_first: bool = True,
    ) -> typing.List[readmanga.Page]:
        def check_script(tag: bs4.element.Tag) -> bool:
            if tag.name == "script":
                type = tag.get("type")
                if type is None or type != "text/javascript":
                    return False
                return tag.text.strip().startswith("var prevLink")

        script = soup.find(check_script)

        if script is None:
            raise exceptions.PagesNotFound((
                "The pages not found! "
                "Check the correctness of the url that you passed. "
            ))

        code = script.string

        pages_str = code[code.index("[["):code.index("]]") + 2]
        pages_json = json.loads(pages_str.replace("'", '"'))

        pages = []
        for page in limit_offset(
            iterable=edit_start(
                iterable=pages_json,
                start_with_new=primarily_first,
            ),
            offset=offset,
            limit=count,
        ):
            *url, width, height = page

            url = "".join(url)

            pages.append(
                readmanga.Page(
                    url=url,
                    width=width,
                    height=height,
                )
            )

        return pages

    def parse_translator_info(
        self,
        soup: bs4.BeautifulSoup,
        short_url: str,
        url: str,
    ) -> readmanga.Translator:
        translator = {}

        left_content = soup.find(class_="leftContent")

        # names
        for page_element in left_content.find(
            name="h1",
            recursive=False,
        ).find_all(
            name="span",
            recursive=False,
        ):
            page_element: bs4.element.Tag

            # name, eng-name, original-name = ...
            translator[page_element["class"][0]] = page_element.string

        subject = left_content.find(class_="flex-row")

        # votes, stars
        type_by_name = {"ratingCount": int, "ratingValue": float}
        for rating in subject.find(class_="user-rating")\
                             .find_all(
            name="meta",
            recursive=False,
            itemprop=type_by_name.keys(),
        ):
            name = rating["itemprop"]

            translator[name] = type_by_name[name](rating["content"])

        description = subject.find_next(class_="manga-description")
        if description:
            translator["manga-description"] = description.text.strip()

        date = subject.find(class_="subject-meta").find(
            name="p",
            recursive=False,
        )
        if date:
            translator["birthDate"] = date.time.string

        # vk / site / etc
        contact = left_content.find(target="_blank")
        if contact:
            translator["contact"] = urls_concat([
                self.URL_SITE, contact["href"],
            ])

        for work in left_content.find(class_="tiles row")\
                                .find_all(class_="img"):
            work: bs4.element.Tag

            name = work.find_next(name="h3").a.string

            work_short_url, work_url = get_urls(work, self.URL_SITE)

            photo = work.a.find_next()["data-original"]

            translator.setdefault("works", []).append(
                readmanga.MangaBriefly(
                    name=name,
                    short_url=work_short_url,
                    url=work_url,
                    photo=photo,
                )
            )

        return readmanga.Translator(
            short_url=short_url,
            url=url,
            **translator,
        )

    def parse_manga_popular(
        self,
        soup: bs4.BeautifulSoup,
        offset: int = 0,
        count: typing.Optional[int] = None,
    ) -> typing.List[readmanga.MangaBriefly]:
        popular = soup.find(class_="leftContent")\
                      .find(class_="tiles row")\
                      .find_all(class_="img")

        if popular == []:
            raise exceptions.MangaNotFound((
                "The manga not found! "
                "The source didn't return manga. "
            ))

        manga = []
        for popular in limit_offset(
            iterable=popular,
            offset=offset,
            limit=count,
        ):
            popular: bs4.element.Tag

            name = popular.find_next(name="h3").a.string

            short_url, url = get_urls(popular, self.URL_SITE)

            photo = popular.a.find_next()["data-original"]

            manga.append(
                readmanga.MangaBriefly(
                    name=name,
                    short_url=short_url,
                    url=url,
                    photo=photo,
                )
            )

        return manga

    def parse_manga_by_url(
        self,
        soup: bs4.BeautifulSoup,
        count: typing.Optional[int] = None,
    ) -> typing.List[readmanga.MangaBriefly]:
        content = soup.find(class_="leftContent")\
                      .find(class_="tiles row")\
                      .find_all(class_="img")

        if content == []:
            raise exceptions.MangaNotFound((
                "The manga not found! "
                "The source didn't return manga. "
            ))

        manga = []
        for manga_info in limit_offset(
            iterable=content,
            offset=0,
            limit=count,
        ):
            manga_info: bs4.element.Tag

            name = manga_info.find_next(name="h3").a.string

            short_url, url = get_urls(manga_info, self.URL_SITE)

            photo = manga_info.a.find_next()["data-original"]

            manga.append(
                readmanga.MangaBriefly(
                    name=name,
                    short_url=short_url,
                    url=url,
                    photo=photo,
                )
            )

        return manga
