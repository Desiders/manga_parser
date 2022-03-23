from manga_parser.urls.urls import Urls


class RemangaUrls(Urls):
    """
    Class with urls for parsing site remanga.org
    """

    SITE = "https://remanga.org"

    MANGA = "manga"
    PUBLISHERS = "team"


class RemangaApiUrls(Urls):
    """
    Class with urls for parsing api site remanga.org
    """

    SITE = "https://remanga.org/api"

    SEARCH = "search"
    MANGA = "titles"
    NEW = "search/catalog/?ordering=-id"
    LATEST_UPDATED = "search/catalog/?ordering=-chapter_date"
    RATING = "search/catalog/?ordering=-rating"
    LIKED = "search/catalog/?ordering=-votes"
    VIEWED = "search/catalog/?ordering=-views"
    COUNT_CHAPTERS = "search/catalog/?ordering=-count_chapters"
    RANDOM = "search/catalog/?ordering=-random"
    RECOMMENDATIONS = "search/catalog/recommendations"
    CHAPTERS = "titles/chapters"
    PUBLISHERS = "publishers"
