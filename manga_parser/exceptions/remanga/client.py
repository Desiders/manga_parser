from manga_parser.exceptions.client import ClientException


class RemangaClientException(ClientException):
    """
    Base class for client exceptions from remanga
    """


class NeedAuthorizhationForViewManga(RemangaClientException):
    """
    The site required to be authorized for view the manga
    """
