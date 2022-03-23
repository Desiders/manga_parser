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
