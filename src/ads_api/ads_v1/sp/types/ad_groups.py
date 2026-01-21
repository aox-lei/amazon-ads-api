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
    status: Optional[SPStatus] = None
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
    state: SPCreateState = SPCreateState.ENABLED
    tags: Optional[list[SPCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )

    @classmethod
    def build(cls, campaign_id: str, name: str, default_bid: float):
        return cls(
            campaign_id=campaign_id,
            name=name,
            bid=SPCreateAdGroupBid(default_bid=default_bid),
        )

    def set_state(self, state: SPCreateState):
        self.state = state
        return self

    def set_tags(self, tags: dict[str, str]):
        self.tags = [SPCreateTag(key=key, value=value) for key, value in tags.items()]
        return self


# endregion


# region Update
class SPAdGroupUpdate(CamelCaseBaseModel):
    ad_group_id: str
    bid: Optional[SPUpdateAdGroupBid] = None
    state: Optional[SPUpdateState] = None
    tags: Optional[list[SPCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )

    @classmethod
    def build(cls, ad_group_id: str):
        return cls(ad_group_id=ad_group_id)

    def set_default_bid(self, default_bid: float):
        self.bid = SPUpdateAdGroupBid(default_bid=default_bid)
        return self

    def set_state(self, state: SPUpdateState):
        self.state = state
        return self

    def set_tags(self, tags: dict[str, str]):
        self.tags = [SPCreateTag(key=key, value=value) for key, value in tags.items()]
        return self


# endregion


# region SPAdGroupMultiStatusSuccess
class SPAdGroupMultiStatusSuccess(CamelCaseBaseModel):
    ad_group: SPAdGroup
    index: int


# endregion
