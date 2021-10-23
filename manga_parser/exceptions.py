class MangaNotFound(Exception):
    """
    If the manga was not found
    """
    pass


class MangaNeedAuthorization(Exception):
    """
    If you need authorization to view the manga
    """
    pass


class TranslatorNotFound(Exception):
    """
    If the translator was not found
    """
    pass


class ChaptersNotFound(Exception):
    """
    If the chapters was not found.
    Maybe everything is correct, but the chapters aren't found
    or the wrong branch is specified
    """
    pass


class ChapterNotFound(Exception):
    """
    If the chapter was not found
    """
    pass


class PagesNotFound(Exception):
    """
    If the pages was not found
    """
    pass


class IncorrectProtocol(Exception):
    """
    If the protocol incorrect
    """
    pass


class MethodNotFound(Exception):
    """
    If the method not found
    """
    pass


class BadStatusCode(Exception):
    """
    If the status code in the response indicates an error
    """
    pass


class PaymentRequired(Exception):
    """
    If the site returns an status code about the need for payment
    """
    pass
