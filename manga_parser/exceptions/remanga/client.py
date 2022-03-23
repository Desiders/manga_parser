from manga_parser.exceptions.client import ClientException


class RemangaClientException(ClientException):
    """
    Base class for client exceptions from remanga
    """


class NeedAuthorizhationForViewManga(RemangaClientException):
    """
    The site required to be authorized for view the manga
    """


class NeedPaymentForUsingSite(RemangaClientException):
    """
    The site doesn't want to be parsed

    Perhaps authorization will solve this exception.
    """
