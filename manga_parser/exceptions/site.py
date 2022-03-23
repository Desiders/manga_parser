class SiteException(BaseException):
    """
    Base class for site exceptions
    """


class ManyRequests(SiteException):
    """
    The site refused on the request, because from this
    computer many requests

    You may change the headers.
    """


class SiteInternalServerError(SiteException):
    """
    Problems with the site

    Perhaps use mirrors will solve this problem.
    """
