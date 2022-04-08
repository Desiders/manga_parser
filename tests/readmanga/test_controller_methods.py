import logging
import time

from httpx import Client
from manga_parser import (ReadmangaController, ReadmangaParser,
                          ReadmangaRequests)

logger = logging.getLogger(__name__)

readmanga = ReadmangaController(
    requests=ReadmangaRequests(
        client=Client(
            headers={
                'User-Agent': (
                    'MozihppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/68.0.3440.75 Safari/537.36'
                ),
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US;q=0.5,en;q=0.3',
                'Cache-Control': 'max-age=0',
                'DNT': '1',
                'Upgrade-Insecure-Requests': '1',
            },
            timeout=30,
        ),
    ),
    parser=ReadmangaParser(),
)


def logging_execution_time(fn):
    def wrap(*args, **kwargs):
        start = time.monotonic()
        fn(*args, **kwargs)
        end = time.monotonic()

        logger.info(
            f"execution time: {end - start} s.\n"
        )
    return wrap


class TestReadmangaControllerMethods:
    @logging_execution_time
    def test_manga_search(self):
        manga = readmanga.manga_search(
            name="Клинок, рассекающий демонов",
            limit=1,
        )

        assert isinstance(manga, list)
        assert 0 <= len(manga) <= 1

        manga = readmanga.manga_search(name="Клинок, рассекающий демонов")

        assert isinstance(manga, list)
        assert 0 <= len(manga) <= 50
