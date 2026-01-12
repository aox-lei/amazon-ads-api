from typing import Optional

from ads_api.base import CamelCaseBaseModel

from .enums import (
    SPDeliveryReason,
    SPDeliveryStatus,
)
from ads_api.ads_v1.base import ErrorCode


# region 状态
class SPStatus(CamelCaseBaseModel):
    delivery_reasons: Optional[list[SPDeliveryReason]] = None
    delivery_status: SPDeliveryStatus


# endregion


# region Tags
class SPTag(CamelCaseBaseModel):
    key: str
    value: str


class SPCreateTag(CamelCaseBaseModel):
    key: str
    value: str


class SPGlobalCreateTag(CamelCaseBaseModel):
    key: str
    value: str


class SPGlobalTag(CamelCaseBaseModel):
    key: str
    value: str


# endregion


# region ErrorsIndex Response
class Error(CamelCaseBaseModel):
    code: ErrorCode
    field_location: Optional[str] = None
    message: str


class ErrorsIndex(CamelCaseBaseModel):
    errors: list[Error]
    index: int


# endregion
