class ReadmangaMangaException(BaseException):
    """
    Base class for manga exceptions from remanga
    """


class MangaNotFound(ReadmangaMangaException):
    """
    The manga not found
    """
