from typing import Optional


class BaseException(Exception):
    def __init__(self, message: str, code: Optional[str] = None):
        self.code = code
        self.message = message
        super().__init__(code, message)


class BadRequestException(BaseException):
    """400"""


class UnauthorizedException(BaseException):
    """401"""


class ForbidenException(BaseException):
    """403"""


class NotFoundException(BaseException):
    """404"""


class ContentTooLargeException(BaseException):
    """413"""


class TooManyRequestsException(BaseException):
    """429"""


class InternalServerException(BaseException):
    """500"""


class BadGatewayException(BaseException):
    """502"""


class ServiceUnavailableException(BaseException):
    """503"""


class GatewayTimeoutException(BaseException):
    """504"""
