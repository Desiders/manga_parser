def urls_concat(
    *urls: tuple[str],
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
