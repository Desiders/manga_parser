class ClientException(BaseException):
    """
    Base class for client exceptions
    """


class DefaultClientNotInstalled(ClientException):
    """
    The default client is not installed

    For solve this problem, install: {default_client} {default_client_version}
    Installing: `pip install {default_client}~={default_client_version}`
    """


class NeedPaymentForUsingSite(ClientException):
    """
    The site doesn't want to be parsed

    Perhaps authorization will solve this exception or
    just try set random headers
    """
