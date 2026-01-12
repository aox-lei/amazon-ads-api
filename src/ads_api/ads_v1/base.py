from typing import Callable, Optional, TypeVar
from collections.abc import Awaitable
from typing_extensions import ParamSpec
from enum import Enum
from returns.result import Success, Failure, Result
import httpx
from returns.pipeline import is_successful
from ads_api.ads_v1.exception import (
    BadGatewayException,
    BadRequestException,
    ContentTooLargeException,
    ForbidenException,
    GatewayTimeoutException,
    InternalServerException,
    NotFoundException,
    ServiceUnavailableException,
    TooManyRequestsException,
    UnauthorizedException,
    BaseException,
)
import pydantic
import functools


class ErrorCode(str, Enum):
    # --- 基础 HTTP/系统级别 ---
    BAD_REQUEST = "BAD_REQUEST"  # 请求格式错误或无效
    UNAUTHORIZED = "UNAUTHORIZED"  # 身份认证失败（Token 无效或过期）
    FORBIDDEN = "FORBIDDEN"  # 权限不足（无权访问该资源或账号）
    NOT_FOUND = "NOT_FOUND"  # 找不到请求的路径或资源
    CONFLICT = "CONFLICT"  # 资源状态冲突
    INTERNAL_ERROR = "INTERNAL_ERROR"  # 亚马逊服务器内部错误
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # 触发频率限制 (429 Rate Limit)
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # 请求体过大
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # 不支持该操作
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"  # 该功能已停用
    UNSUPPORTED_MARKETPLACE = "UNSUPPORTED_MARKETPLACE"  # 不支持该站点（Marketplace）

    # --- 资源 ID 与 归属问题 ---
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"  # 找不到指定的资源 ID
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = (
        "RESOURCE_DOES_NOT_BELONG_TO_PARENT"  # 资源不属于所提供的父级 ID
    )
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"  # 资源为空
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"  # 资源为 Null
    RESOURCE_IS_IN_TERMINAL_STATE = (
        "RESOURCE_IS_IN_TERMINAL_STATE"  # 资源处于终态（如已归档），不可操作
    )
    FIELD_VALUE_NOT_FOUND = "FIELD_VALUE_NOT_FOUND"  # 字段值未找到
    DUPLICATE_RESOURCE_ID_FOUND = "DUPLICATE_RESOURCE_ID_FOUND"  # 发现重复的资源 ID

    # --- 字段/格式验证 ---
    FIELD_VALUE_IS_INVALID = "FIELD_VALUE_IS_INVALID"  # 字段值无效
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"  # 字段值不能为空
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"  # 字段值为空
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"  # 字段值不唯一
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"  # 字段值不匹配
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = (
        "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"  # 字段值必须为空或 Null
    )
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"  # 该字段值不可编辑
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"  # 发现重复的字段值
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = (
        "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"  # 包含无效字符
    )
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = (
        "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"  # 包含黑名单违禁词
    )

    # --- 范围与限制 (Limits) ---
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"  # 字段值超出允许范围
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"  # 字段值高于最大上限
    )
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"  # 字段值低于最小下限
    )
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"  # 字段长度/大小超出范围
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"  # 字段长度超过最大值
    )
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"  # 字段长度低于最小值
    )
    TOTAL_RESOURCE_LIMIT_EXCEEDED = (
        "TOTAL_RESOURCE_LIMIT_EXCEEDED"  # 超出总资源配额限制
    )
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # 超出活动资源配额限制
    )
    GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT = (
        "GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT"  # 触发单个广告活动下广告组的数量限制
    )

    # --- 时间与日期 ---
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"  # 日期不能是过去的时间
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"  # 日期不能为空
    DATE_TOO_SOON = "DATE_TOO_SOON"  # 日期设置得太早（不符合最小提前量要求）
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"  # 持续时间太短

    # --- 父级与资源状态约束 ---
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # 父级已归档，无法创建子项
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # 父级已归档，无法编辑
    ARCHIVED_RESOURCE_CANNOT_EDIT = (
        "ARCHIVED_RESOURCE_CANNOT_EDIT"  # 资源已归档，无法编辑
    )
    AUTOCREATED_ENTITY_CANNOT_EDIT = (
        "AUTOCREATED_ENTITY_CANNOT_EDIT"  # 自动创建的实体不可编辑
    )

    # --- 业务逻辑与账号限制 ---
    PAYMENT_ISSUE = "PAYMENT_ISSUE"  # 支付账户问题
    PRODUCT_INELIGIBLE = "PRODUCT_INELIGIBLE"  # 产品不符合资格
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO = (
        "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO"  # 受组合限制，无法更新全局属性
    )
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE = (
        "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE"  # 受状态限制，无法更新全局属性
    )


class ErrorResponse(pydantic.BaseModel):
    code: Optional[ErrorCode] = None
    message: str


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
