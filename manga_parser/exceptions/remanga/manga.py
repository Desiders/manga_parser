class RemangaMangaException(BaseException):
    """
    Base class for manga exceptions from remanga
    """


class MangaNotFound(RemangaMangaException):
    """
    The manga not found
    """


class ChaptersNotFound(RemangaMangaException):
    """
    The manga's chapters not found
    """


class ChapterNotFound(RemangaMangaException):
    """
    The manga's chapter not found
    """
