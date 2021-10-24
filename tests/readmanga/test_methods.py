from manga_parser.manga import ReadManga


client = ReadManga(client_kwargs={
    "headers": {
        'User-Agent': 'MozihppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
    },
})


class TestMethodsReadManga:
    def test_manga_search(self):
        manga = client.manga_search(
            name="Клинок",
            count=10,
        )
        assert len(manga) == 10

        manga = client.manga_search(
            name="Клинок",
            count=60,
        )
        assert len(manga) == 50

        manga_by_name_ru = client.manga_search(
            name="Клинок, рассекающий демонов",
            count=1,
        )
        assert len(manga_by_name_ru) == 1

        manga_by_name_en = client.manga_search(
            name="Blade of Demon Destruction",
            count=1,
        )
        assert len(manga_by_name_en) == 1

        assert (
            manga_by_name_ru != manga_by_name_en or
            manga_by_name_ru == manga_by_name_en
        )

    def test_manga_info(self):
        manga_single = client.manga_search(
            name="Начало после конца",
            count=1,
        )[0]

        manga_info_by_short_url = client.manga_info(
            url=manga_single.short_url,
            chapters_count=0,
        )
        manga_info_by_url = client.manga_info(
            url=manga_single.url,
            chapters_count=0,
        )

        assert (
            manga_info_by_short_url.short_url == manga_info_by_url.short_url
                                              == manga_single.short_url
        )
        assert (
            manga_info_by_short_url.url == manga_info_by_url.url
                                        == manga_single.url
        )

        manga = client.manga_search(
            name="Клинок, рассекающий демонов",
            count=5,
        )

        for manga_single in manga:
            manga_info = client.manga_info(
                url=manga_single.short_url,
            )

            if manga_info.status.lower() == "закончен":
                assert manga_info.count_chapters > 0

    def test_chapter_pages(self):
        manga_single = client.manga_search(
            name="Меч разящего грома",
        )[0]

        manga_info = client.manga_info(
            url=manga_single.url,
            chapters_count=3,
            chapters_primarily_new=False,
        )

        pages = client.chapter_pages(
            url=manga_info.chapters[0].url,
            count=1,
        )
        assert len(pages) == 1

        for chapter in manga_info.chapters:
            pages = client.chapter_pages(url=chapter.url)

            for page in pages:
                assert page.url.startswith("https://")

    def test_translator_info(self):
        translator_by_short_url = client.translator_info(
            url="assley_team",
        )
        translator_by_url = client.translator_info(
            url="https://readmanga.io/list/person/assley_team",
        )

        assert translator_by_short_url == translator_by_url

    def test_manga_liked(self):
        manga_f = client.manga_popular(count=5)
        manga_s = client.manga_popular(offset=5, count=5)

        urls = [
            manga.url
            for manga in (*manga_f, *manga_s)
        ]

        assert len(urls) == 10

        manga = client.manga_popular()

        assert len(manga) == 30

    def test_manga_by_url(self):
        manga = client.manga_by_url(client.URL_NEW)

        assert len(manga) == 70

        manga_s = client.manga_by_url(client.URL_NEW, count=10)
        manga_f = client.manga_by_url(client.URL_BEST, count=10)

        assert manga_s != manga_f
        assert len(manga_s) + len(manga_f) == 20

    def test_manga_new(self):
        manga = client.manga_new()

        assert len(manga) == 70

        manga_f = client.manga_new(count=3)
        manga_s = client.manga_new(offset=3, count=3)

        assert manga_f != manga_s

    def test_manga_best(self):
        manga = client.manga_best()

        assert len(manga) == 70

        manga_f = client.manga_best(count=3)
        manga_s = client.manga_best(offset=3, count=3)

        assert manga_f != manga_s


client.close()
