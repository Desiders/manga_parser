import itertools
import typing

import bs4


def edit_start(
    iterable,
    start_with_new: bool,
):
    if start_with_new:
        return iterable
    return iterable[::-1]


def limit_offset(
    iterable,
    offset: int,
    limit: typing.Optional[int],
) -> itertools.islice:
    return itertools.islice(
        itertools.islice(iterable, offset, None),
        limit,
    )


def urls_concat(
    urls: typing.List[typing.Any],
    sep: str = "",
) -> str:
    if urls == []:
        return ""

    full_url = urls.pop(0)
    for url in urls:
        url_with_sep = f"{sep}{url}"
        full_url += url_with_sep

    return full_url


def get_short_url(url: str) -> str:
    if url.startswith("http"):
        _, short_url = url.rsplit("/", maxsplit=1)
    else:
        short_url = url
    return short_url


def get_urls(
    tag: bs4.element.Tag,
    url_concat: str,
) -> typing.Tuple[str, str]:
    href: str = tag.a["href"]
    if href.startswith("/"):
        short_url = href[1:]  # without "/"
        url = urls_concat([url_concat, href])
    else:
        *_, short_url = href.rsplit("/", maxsplit=1)

        url = href
    return short_url, url
