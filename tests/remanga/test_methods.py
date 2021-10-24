from manga_parser.manga import ReManga


client = ReManga()


class TestMethodsRemanga:
    def test_manga_search(self):
        manga = client.manga_search(
            name="Клинок",
            count=10,
        )
        assert len(manga) == 10

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

        assert manga_by_name_ru[0].id == manga_by_name_en[0].id
        assert (
            manga_by_name_ru[0].name_ru == manga_by_name_en[0].name_ru
                                        == "Клинок, рассекающий демонов"
        )
        assert (
            manga_by_name_ru[0].name_en == manga_by_name_en[0].name_en
                                        == "Blade of Demon Destruction"
        )

    def test_manga_info(self):
        manga_single = client.manga_search(
            name="Начало после конца",
            count=1,
        )[0]

        manga_info_by_short_url = client.manga_info(
            url=manga_single.short_url,
        )
        manga_info_by_url = client.manga_info(
            url=manga_single.url,
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

    def test_manga_chapters(self):
        manga_single = client.manga_search(
            name="Расхититель гробниц",
        )[0]

        manga_info = client.manga_info(
            url=manga_single.url,
        )

        chapters = client.manga_chapters(
            branch_id=manga_info.branches[0].id,
            count=1,
        )
        assert len(chapters) == 1

        chapters = client.manga_chapters(
            branch_id=manga_info.branches[0].id,
        )
        assert len(chapters) == manga_info.branches[0].count_chapters

        chapter_new = client.manga_chapters(
            branch_id=manga_info.branches[0].id,
            offset=0,
            count=1,
            primarily_new=True,
        )[0]
        chapter_old = client.manga_chapters(
            branch_id=manga_info.branches[0].id,
            offset=0,
            count=1,
            primarily_new=False,
        )[0]

        assert chapter_new != chapter_old
        assert chapter_new.index > chapter_old.index

        last_chapter = chapters.pop(0)
        for chapter in chapters:
            if chapter.price is not None:
                assert chapter.free_date is not None
            else:
                assert chapter.free_date is None

            assert last_chapter.index > chapter.index

            last_chapter = chapter

    def test_chapter_pages(self):
        manga_single = client.manga_search(
            name="Меч разящего грома",
        )[0]

        manga_info = client.manga_info(
            url=manga_single.url,
        )

        chapters = client.manga_chapters(
            branch_id=manga_info.branches[0].id,
            count=10,
            primarily_new=False,
        )

        pages = client.chapter_pages(
            chapter_id=chapters[0].id,
            count=1
        )
        assert len(pages) == 1

        for chapter in chapters:
            pages = client.chapter_pages(chapter_id=chapter.id)

            for page in pages:
                assert page.url.startswith("https://")

    def test_translator_info(self):
        translator_by_short_url = client.translator_info(
            url="891",
        )
        translator_by_url = client.translator_info(
            url="https://remanga.org/team/891",
        )

        assert (
            translator_by_short_url.name == translator_by_url.name
                                         == "ArticaProject"
        )

        assert (
            translator_by_short_url.liked > 1_800_000
            and
            translator_by_url.liked > 1_800_000
        )

        assert (
            translator_by_short_url.count_works > 5
            and
            translator_by_url.count_works > 5
        )

        translator = client.translator_info("otakudo")

        assert translator.count_works > 30

    def test_manga_by_url(self):
        manga = client.manga_by_url(client.URL_NEW)

        assert len(manga) == 20
        assert manga[0].id > manga[-1].id

        manga = client.manga_by_url(client.URL_NEW, count=10)

        assert len(manga) == 10
        assert manga[0].id > manga[-1].id

        for url in [
            client.URL_RECOMMENDATIONS, client.URL_VIEWS,
            client.URL_LIKED,
        ]:
            manga = client.manga_by_url(url, count=2)
            manga_second = client.manga_by_url(url, offset=1, count=1)

            assert manga_second[0].id == manga[1].id

    def test_manga_recommendations(self):
        manga_f = client.manga_recommendations(count=1)
        manga_s = client.manga_recommendations(offset=1, count=1)
        manga = client.manga_recommendations(count=2)

        assert (
            manga[0].id == manga_f[0].id and
            manga[1].id == manga_s[0].id
        )

    def test_manga_views(self):
        manga = client.manga_views(count=2)

        assert len(manga) == 2
        assert manga[0].views > manga[1].views

        manga_f = client.manga_views(count=3)
        manga_s = client.manga_views(offset=3, count=3)

        for manga_first, manga_second in zip(manga_f, manga_s):
            assert manga_first.views > manga_second.views

    def test_manga_liked(self):
        manga = client.manga_liked(count=2)

        assert len(manga) == 2
        assert manga[0].liked > manga[1].liked

        manga_f = client.manga_liked(count=3)
        manga_s = client.manga_liked(offset=3, count=3)

        for manga_first, manga_second in zip(manga_f, manga_s):
            assert manga_first.liked > manga_second.liked

    def test_manga_new(self):
        manga = client.manga_new(count=2)

        assert len(manga) == 2
        assert manga[0].id > manga[1].id

        manga_f = client.manga_new(count=3)
        manga_s = client.manga_new(offset=3, count=3)

        for manga_first, manga_second in zip(manga_f, manga_s):
            assert manga_first.id > manga_second.id


client.close()
