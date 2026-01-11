from datetime import datetime
from typing import Optional
from typing_extensions import Literal
from .enums import (
    SPGlobalCreateState,
    SPGlobalCurrencyCode,
    SPGlobalMarketplace,
    SPGlobalState,
)
from ads_api.base import CamelCaseBaseModel
from .common import (
    SPGlobalCreateTag,
    SPTag,
    SPGlobalStatus,
    SPGlobalTag,
    Error,
)
from .enums import SPGlobalUpdateState
import pydantic


# region 出价
class SPGlobalAdGroupBidMarketplaceSetting(CamelCaseBaseModel):
    currency_code: SPGlobalCurrencyCode
    default_bid: float
    marketplace: SPGlobalMarketplace


class SPGlobalCreateAdGroupBidMarketplaceSetting(CamelCaseBaseModel):
    currency_code: SPGlobalCurrencyCode
    default_bid: float
    marketplace: SPGlobalMarketplace


class SPGlobalAdGroupBid(CamelCaseBaseModel):
    marketplace_settings: Optional[list[SPGlobalAdGroupBidMarketplaceSetting]]


class SPGlobalCreateAdGroupBid(CamelCaseBaseModel):
    marketplace_settings: Optional[list[SPGlobalCreateAdGroupBidMarketplaceSetting]]


class SPGlobalUpdateAdGroupBid(CamelCaseBaseModel):
    marketplace_settings: Optional[list[SPGlobalCreateAdGroupBidMarketplaceSetting]]


# endregion


class SPGlobalMarketplaceAdGroupFieldOverrides(CamelCaseBaseModel):
    name: Optional[str]
    state: Optional[SPGlobalState]
    tags: Optional[list[SPGlobalTag]] = pydantic.Field(default=None, max_items=50)


# region SPGlobalMarketplaceAdGroupConfigurations
class SPGlobalMarketplaceAdGroupConfigurations(str, CamelCaseBaseModel):
    ad_group_id: str
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalMarketplaceAdGroupFieldOverrides


# endregion


# region SPGlobalAdGroup
class SPGlobalAdGroup(CamelCaseBaseModel):
    ad_group_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"]
    bid: SPGlobalAdGroupBid
    campaign_id: str
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_configurations: Optional[
        list[SPGlobalMarketplaceAdGroupConfigurations]
    ] = None
    marketplace_scope: Literal["GLOBAL"]
    marketplaces: list[SPGlobalMarketplace]
    name: str
    state: SPGlobalState
    status: SPGlobalStatus
    tags: Optional[list[SPTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region SPGlobalCreateMarketplaceAdGroupConfigurations
class SPGlobalCreateMarketplaceAdGroupFieldOverrides(CamelCaseBaseModel):
    name: Optional[str] = None
    state: Optional[SPGlobalState] = None
    tags: Optional[list[SPGlobalCreateTag]] = None


class SPGlobalCreateMarketplaceAdGroupConfigurations(CamelCaseBaseModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceAdGroupFieldOverrides


# endregion


# region SPGlobalAdGroupCreate
class SPGlobalAdGroupCreate(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    bid: SPGlobalCreateAdGroupBid
    campaign_id: str
    marketplace_configurations: SPGlobalCreateMarketplaceAdGroupConfigurations
    marketplace_scope: Literal["GLOBAL"] = "GLOBAL"
    marketplaces: list[SPGlobalMarketplace]
    name: str
    state: SPGlobalCreateState
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region SPAdGroupUpdate
class SPGlobalAdGroupUpdate(CamelCaseBaseModel):
    ad_group_id: str
    bid: Optional[SPGlobalUpdateAdGroupBid] = None
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceAdGroupConfigurations]
    ] = pydantic.Field(default=None, min_items=0, max_items=50)
    marketplaces: Optional[list[SPGlobalMarketplace]] = None
    name: Optional[str] = None
    state: Optional[SPGlobalUpdateState] = None
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region SPGlobalAdGroupPartialIndex
class SPGlobalAdGroupPartialIndex(CamelCaseBaseModel):
    ad_group: SPGlobalAdGroup
    errors: list[Error]
    index: int


# endregion


# region SPGlobalAdGroupMultiStatusSuccess
class SPGlobalAdGroupMultiStatusSuccess(CamelCaseBaseModel):
    ad_group: SPGlobalAdGroup
    index: int


# endregion
