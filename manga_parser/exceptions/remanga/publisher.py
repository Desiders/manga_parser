class RemangaPublisherException(BaseException):
    """
    Base class for publisher exceptions from remanga
    """


class PublisherNotFound(RemangaPublisherException):
    """
    The publisher not found
    """
