from datetime import datetime
import pydantic
from typing import Optional
from typing_extensions import Literal
from ads_api.base import CamelCaseBaseModel
from .enums import *
from .common import SPStatus, SPTag, SPCreateTag


# region 出价 Model
class SPAdGroupBid(CamelCaseBaseModel):
    """出价 Model"""

    currency_code: SPCurrencyCode
    default_bid: float  # 默认出价


class SPCreateAdGroupBid(CamelCaseBaseModel):
    default_bid: float  # 默认出价


class SPUpdateAdGroupBid(CamelCaseBaseModel):
    default_bid: float  # 默认出价


# endregion


# region SPAdGroup Model
class SPAdGroup(CamelCaseBaseModel):
    ad_group_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"]
    bid: SPAdGroupBid  # 出价
    campaign_id: str
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    global_ad_group_id: Optional[str] = None
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_scope: Literal["SINGLE_MARKETPLACE"]
    marketplaces: list[SPMarketplace]
    name: str
    state: SPState
    status: SPStatus
    tags: Optional[list[SPTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region Create
class SPAdGroupCreate(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    bid: SPCreateAdGroupBid
    campaign_id: str
    name: str
    state: SPCreateState
    tags: Optional[list[SPCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region Update
class SPAdGroupUpdate(CamelCaseBaseModel):
    ad_group_id: str
    bid: SPUpdateAdGroupBid
    state: SPUpdateState
    tags: Optional[list[SPCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region SPAdGroupMultiStatusSuccess
class SPAdGroupMultiStatusSuccess(CamelCaseBaseModel):
    ad_group: SPAdGroup
    index: int


# endregion
