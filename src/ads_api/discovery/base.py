from collections import Awaitable
import functools
from typing import Callable, TypeVar
import httpx
import pydantic
from returns.pipeline import is_successful
from returns.result import Failure, Result, Success
from typing_extensions import ParamSpec
from .exception import *


P = ParamSpec("P")
R_SUCCESS = TypeVar("R_SUCCESS", bound=pydantic.BaseModel)
R_ERROR = TypeVar("R_ERROR", bound=httpx.Response)


def handle_api_errors(
    func: Callable[P, Awaitable[Result[R_SUCCESS, R_ERROR]]],
) -> Callable[P, Awaitable[Result[R_SUCCESS, BaseException]]]:
    @functools.wraps(func)
    async def wrapper(
        *args: P.args, **kwargs: P.kwargs
    ) -> Result[R_SUCCESS, BaseException]:
        result = await func(*args, **kwargs)
        if is_successful(result):
            return Success(result.unwrap())

        response = result.failure()
        error_map = {
            400: BadRequestException,
            401: UnauthorizedException,
            403: ForbidenException,
            404: NotFoundException,
            413: ContentTooLargeException,
            429: TooManyRequestsException,
            500: InternalServerException,
            502: BadGatewayException,
            503: ServiceUnavailableException,
            504: GatewayTimeoutException,
        }
        if error_map.get(response.status_code):
            response_data = response.json()
            _response_class = error_map[response.status_code]
            return Failure(
                _response_class(
                    message=response_data.get("message"),
                    code=response_data.get("code"),
                )
            )
        else:
            return Failure(BaseException(message="Unknown Error"))

    return wrapper
