def urls_concat(
    *urls: str,
    sep: str = "", end: str = "",
) -> str:
    return sep.join(map(str, urls)) + end


def is_url(value: str) -> bool:
    return value.startswith("http")


def get_short_url(url: str) -> str:
    *_, short_url = url.rsplit("/", maxsplit=1)

    return short_url


def get_chapter_id_from_url(url: str) -> str:
    _, chapter_id = url.rsplit("/ch", maxsplit=1)

    return chapter_id


def is_chapter_url(value: str) -> bool:
    return value.startswith("ch")


def get_chapter_id_from_chapter_url(chapter_url: str) -> str:
    return chapter_url[2:]  # without "ch"


def get_en_genre_from_short_url(short_url: str) -> str:
    *_, en_genre = short_url.rsplit("/", maxsplit=1)

    return en_genre


def get_short_publisher_url_from_href(href: str) -> str:
    *_, short_publisher_url = href.rsplit("/", maxsplit=1)

    return short_publisher_url


def get_short_url_from_href(href: str) -> str:
    return href[1:]  # without "/"
