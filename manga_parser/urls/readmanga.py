from manga_parser.urls.base import Urls


class ReadmangaUrls(Urls):
    """
    Class with urls for parsing site readmanga.io
    """

    SITE = "https://readmanga.io"

    MANGA = ""
    SEARCH = "search"
    PUBLISHERS = "list/person"
    POPULAR = "recommendations/top"
    NEW = "list?sortType=created"
    RATING = "list?sortType=votes"
    RANDOM = "internal/random"
