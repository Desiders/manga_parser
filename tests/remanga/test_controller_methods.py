from manga_parser import RemangaController, RemangaParser, RemangaRequests
from manga_parser.utils.helper.remanga import (age_limit_by_raw,
                                               title_type_by_raw)

remanga_controller = RemangaController(
    requests=RemangaRequests(),
    parser=RemangaParser(),
)


class TestRemangaControllerMethods:
    def test_manga_search(self):
        manga = remanga_controller.manga_search(
            name="Клинок, рассекающий демонов",
            count=1,
        )

        assert isinstance(manga, list)
        assert len(manga) == 1

        manga = remanga_controller.manga_search(name="Клинок", count="10")

        assert isinstance(manga, list)
        assert len(manga) == 10

        manga = remanga_controller.manga_search(name="Клинок")

        assert isinstance(manga, list)
        assert len(manga) == 1

    def test_manga_new(self):
        manga_category_raw = "реинкарнация"
        manga_genre_id = 21
        manga_title_type = title_type_by_raw("manga")
        manga_age_limit_raw = "0+"
        manga_age_limit = age_limit_by_raw("16+")

        manga = remanga_controller.manga_new(
            page=1, offset=0, limit=None,
            primarily_new_manga=True,
            categories=[manga_category_raw],
            genres=[manga_genre_id],
            title_types=[manga_title_type],
            age_limits=[manga_age_limit_raw, manga_age_limit],
        )

        assert len(manga) == 30

        for manga_index in range(len(manga) - 1):
            now_manga = manga[manga_index]
            next_manga = manga[manga_index + 1]

            assert now_manga.id > next_manga.id
            assert manga_category_raw in {
                category.value
                for category in now_manga.categories
            }
            assert manga_genre_id in {
                genre.id
                for genre in now_manga.genres
            }
            assert manga_title_type == now_manga.title_type

        manga = remanga_controller.manga_new(
            page=1, offset=0, limit=None,
            primarily_new_manga=False,
        )

        assert len(manga) == 30

        for manga_index in range(len(manga) - 1):
            now_manga = manga[manga_index]
            next_manga = manga[manga_index + 1]

            assert now_manga.id < next_manga.id

        manga_f = remanga_controller.manga_new(
            page=1, offset=29, limit=10,
        )

        manga_s = remanga_controller.manga_new(
            page=2, offset=29, limit=40,
        )

        assert len(manga_f) == len(manga_s) == 1

        manga_f = remanga_controller.manga_new(
            page=1, limit=1,
            primarily_new_manga=False,
        )

        manga_s = remanga_controller.manga_new(
            page=2, limit=1,
            primarily_new_manga=True,
        )

        assert manga_f[0].id > manga_s[0].id

    def test_manga_latest_updated(self):
        manga_category_raw = "реинкарнация"
        manga_genre_id = 21
        manga_title_type = title_type_by_raw("manga")
        manga_age_limit_raw = "0+"
        manga_age_limit = age_limit_by_raw("16+")

        manga = remanga_controller.manga_latest_updated(
            page=1, offset=0, limit=None,
            categories=[manga_category_raw],
            genres=[manga_genre_id],
            title_types=[manga_title_type],
            age_limits=[manga_age_limit_raw, manga_age_limit],
        )

        assert len(manga) == 30

        for now_manga in manga:
            assert manga_category_raw in {
                category.value
                for category in now_manga.categories
            }
            assert manga_genre_id in {
                genre.id
                for genre in now_manga.genres
            }
            assert manga_title_type == now_manga.title_type

        manga_f = remanga_controller.manga_latest_updated(
            page=1, offset=29, limit=10,
        )

        manga_s = remanga_controller.manga_latest_updated(
            page=2, offset=29, limit=40,
        )

        assert len(manga_f) == len(manga_s) == 1

    def test_manga_rating(self):
        manga_category_raw = "реинкарнация"
        manga_genre_id = 21
        manga_title_type = title_type_by_raw("manga")
        manga_age_limit_raw = "0+"
        manga_age_limit = age_limit_by_raw("16+")
        
        manga = remanga_controller.manga_rating(
            page=1, offset=0, limit=None,
            primarily_rating_manga=True,
            categories=[manga_category_raw],
            genres=[manga_genre_id],
            title_types=[manga_title_type],
            age_limits=[manga_age_limit_raw, manga_age_limit],
        )

        assert len(manga) == 30

        # for manga_index in range(len(manga) - 1):
        #   `now_manga = manga[manga_index]`
        #   `next_manga = manga[manga_index + 1]`
        #   `assert now_manga.rating > next_manga.rating`
        #   isn't right expression,
        #   the site has its own algorithm for determining a place in the ranking

        for now_manga in manga:
            assert manga_category_raw in {
                category.value
                for category in now_manga.categories
            }
            assert manga_genre_id in {
                genre.id
                for genre in now_manga.genres
            }
            assert manga_title_type == now_manga.title_type

        manga = remanga_controller.manga_rating(
            page=1, offset=0, limit=None,
            primarily_rating_manga=False,
        )

        assert len(manga) == 30

        manga_f = remanga_controller.manga_rating(
            page=1, offset=29, limit=10,
        )

        manga_s = remanga_controller.manga_rating(
            page=2, offset=29, limit=40,
        )

        assert len(manga_f) == len(manga_s) == 1

    def test_manga_liked(self):
        manga_category_raw = "реинкарнация"
        manga_genre_id = 21
        manga_title_type = title_type_by_raw("manga")
        manga_age_limit_raw = "0+"
        manga_age_limit = age_limit_by_raw("16+")

        manga = remanga_controller.manga_liked(
            page=1, offset=0, limit=None,
            primarily_liked_manga=True,
            categories=[manga_category_raw],
            genres=[manga_genre_id],
            title_types=[manga_title_type],
            age_limits=[manga_age_limit_raw, manga_age_limit],
        )

        assert len(manga) == 30

        for manga_index in range(len(manga) - 1):
            now_manga = manga[manga_index]
            next_manga = manga[manga_index + 1]

            assert now_manga.liked > next_manga.liked
            assert manga_category_raw in {
                category.value
                for category in now_manga.categories
            }
            assert manga_genre_id in {
                genre.id
                for genre in now_manga.genres
            }
            assert manga_title_type == now_manga.title_type

        manga = remanga_controller.manga_liked(
            page=1, offset=0, limit=None,
            primarily_liked_manga=False,
        )

        assert len(manga) == 30

        for manga_index in range(len(manga) - 1):
            now_manga = manga[manga_index]
            next_manga = manga[manga_index + 1]

            assert now_manga.liked < next_manga.liked

        manga_f = remanga_controller.manga_liked(
            page=1, offset=29, limit=10,
        )

        manga_s = remanga_controller.manga_liked(
            page=2, offset=29, limit=40,
        )

        assert len(manga_f) == len(manga_s) == 1

        manga_f = remanga_controller.manga_liked(
            page=1, limit=1,
            primarily_liked_manga=False,
        )

        manga_s = remanga_controller.manga_liked(
            page=2, limit=1,
            primarily_liked_manga=True,
        )

        assert manga_f[0].liked > manga_s[0].liked

    def test_manga_viewed(self):
        manga_category_raw = "реинкарнация"
        manga_genre_id = 21
        manga_title_type = title_type_by_raw("manga")
        manga_age_limit_raw = "0+"
        manga_age_limit = age_limit_by_raw("16+")

        manga = remanga_controller.manga_viewed(
            page=1, offset=0, limit=None,
            primarily_viewed_manga=True,
            categories=[manga_category_raw],
            genres=[manga_genre_id],
            title_types=[manga_title_type],
            age_limits=[manga_age_limit_raw, manga_age_limit],
        )

        assert len(manga) == 30

        for manga_index in range(len(manga) - 1):
            now_manga = manga[manga_index]
            next_manga = manga[manga_index + 1]

            assert now_manga.views > next_manga.views
            assert manga_category_raw in {
                category.value
                for category in now_manga.categories
            }
            assert manga_genre_id in {
                genre.id
                for genre in now_manga.genres
            }
            assert manga_title_type == now_manga.title_type

        manga = remanga_controller.manga_viewed(
            page=1, offset=0, limit=None,
            primarily_viewed_manga=False,
        )

        assert len(manga) == 30

        for manga_index in range(len(manga) - 1):
            now_manga = manga[manga_index]
            next_manga = manga[manga_index + 1]

            assert now_manga.views < next_manga.views

        manga_f = remanga_controller.manga_viewed(
            page=1, offset=29, limit=10,
        )

        manga_s = remanga_controller.manga_viewed(
            page=2, offset=29, limit=40,
        )

        assert len(manga_f) == len(manga_s) == 1

        manga_f = remanga_controller.manga_viewed(
            page=1, limit=1,
            primarily_viewed_manga=False,
        )

        manga_s = remanga_controller.manga_viewed(
            page=2, limit=1,
            primarily_viewed_manga=True,
        )

        assert manga_f[0].views > manga_s[0].views
    
    def test_manga_count_chapters(self):
        manga_category_raw = "реинкарнация"
        manga_genre_id = 21
        manga_title_type = title_type_by_raw("manga")
        manga_age_limit_raw = "0+"
        manga_age_limit = age_limit_by_raw("16+")

        manga = remanga_controller.manga_count_chapters(
            page=1, offset=0, limit=None,
            primarily_count_chapters_manga=True,
            categories=[manga_category_raw],
            genres=[manga_genre_id],
            title_types=[manga_title_type],
            age_limits=[manga_age_limit_raw, manga_age_limit],
        )

        assert len(manga) == 30

        # it's funny, but the site doesn't return the count
        # of chapters in the manga (need another request)

        for now_manga in manga:
            assert manga_category_raw in {
                category.value
                for category in now_manga.categories
            }
            assert manga_genre_id in {
                genre.id
                for genre in now_manga.genres
            }
            assert manga_title_type == now_manga.title_type

        manga = remanga_controller.manga_count_chapters(
            page=1, offset=0, limit=None,
            primarily_count_chapters_manga=False,
        )

        assert len(manga) == 30

        manga_f = remanga_controller.manga_count_chapters(
            page=1, offset=29, limit=10,
        )

        manga_s = remanga_controller.manga_count_chapters(
            page=2, offset=29, limit=40,
        )

        assert len(manga_f) == len(manga_s) == 1

    def test_manga_info(self):
        manga_first = remanga_controller.manga_info(url=("https://remanga.org/manga/"
                                                         "the_beginning_after_the_end"))

        manga_second = remanga_controller.manga_info(url="the_beginning_after_the_end")

        assert manga_first.id == manga_second.id
        assert manga_first.url == manga_second.url
        assert manga_first.short_url == manga_second.short_url
        # assert manga_first == manga_second
        # this expression may be `False` because attributes like
        # `liked`, `views`, etc. are dynamic attributes

        # the last variable name don't have related with new tests
        manga = manga_first

        assert manga.age_limit.value == "0+"

        publishers = manga.publishers

        # it's the max `count_chapters` from the branches
        count_chapters = manga.count_chapters
        for branch in manga.branches:
            # branch's `count_chapters` might have a differ from `count_chapters` of other branches
            assert branch.count_chapters <= count_chapters

            for publisher in branch.publishers:
                assert publisher in publishers

    def test_manga_chapters(self):
        manga_chapters = remanga_controller.manga_chapters(
            branch=852,  # or `branch=manga.branches[i]`
            offset=0, limit=5, primarily_new_chapters=True,
        )

        for manga_chapter_index in range(4):
            next_manga_chapter_index = manga_chapter_index + 1

            now_manga_chapter = manga_chapters[manga_chapter_index]
            next_manga_chapter = manga_chapters[next_manga_chapter_index]

            assert now_manga_chapter.chapter_index > next_manga_chapter.chapter_index
            assert now_manga_chapter.upload_date > next_manga_chapter.upload_date

            if now_manga_chapter.is_paid or now_manga_chapter.free_date is not None:
                assert now_manga_chapter.price is not None

            if now_manga_chapter.free_date is not None:
                assert now_manga_chapter.upload_date < now_manga_chapter.free_date

        manga_chapters_new = remanga_controller.manga_chapters(
            branch=852, offset=0,
            limit=3, primarily_new_chapters=True,
        )

        manga_chapters_old = remanga_controller.manga_chapters(
            branch=852, offset=0,
            limit=3, primarily_new_chapters=False,
        )

        for manga_chapter_new, manga_chapter_old in zip(manga_chapters_new, manga_chapters_old,):
            manga_chapter_new.id != manga_chapter_old.id

        manga_chapters_f = remanga_controller.manga_chapters(
            branch=852, offset=0,
            limit=3, primarily_new_chapters=True,
        )

        manga_chapters_s = remanga_controller.manga_chapters(
            branch=852, offset=2,
            limit=1, primarily_new_chapters=True,
        )

        assert manga_chapters_f[2].id == manga_chapters_s[0].id

    def test_chapter_pages(self):
        chapter_pages_f = remanga_controller.chapter_pages(
            chapter_or_url=59059,  # or `chapter_or_url=chapters[i]`
            offset=0, limit=3,
            primarily_first_pages=True,
        )

        chapter_pages_s = remanga_controller.chapter_pages(
            chapter_or_url=("https://remanga.org/manga/"
                            "the_beginning_after_the_end/"
                            "ch59059"),
            offset=1, limit=2,
            primarily_first_pages=True,
        )

        assert chapter_pages_f[0].id != chapter_pages_s[0].id
        assert chapter_pages_f[1].id == chapter_pages_s[0].id
        assert chapter_pages_f[2].id == chapter_pages_s[1].id

        chapter_pages_t = remanga_controller.chapter_pages(
            chapter_or_url="ch59059",
            offset=1, limit=2,
            primarily_first_pages=False,
        )

        for page_f, page_s in zip(chapter_pages_s, chapter_pages_t):
            assert page_f.id != page_s.id

    def test_publisher_info(self):
        publisher_f = remanga_controller.publisher_info(
            url="https://remanga.org/team/assault_team",
        )

        publisher_s = remanga_controller.publisher_info(
            url="assault_team",
        )

        assert publisher_f.id == publisher_s.id
        assert publisher_f.url == publisher_s.url
        assert publisher_f.short_url == publisher_s.short_url

        # the last variable name don't have related with new tests
        publisher = publisher_f

        assert publisher.image in publisher.images
        assert publisher.image == publisher.images[0]

        subscription_data = publisher.subscription
        if subscription_data is not None:
            assert subscription_data.price > 0.0
