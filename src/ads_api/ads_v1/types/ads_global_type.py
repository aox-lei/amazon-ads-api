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
from .common_type import (
    SPGlobalCreateTag,
    SPTag,
    SPGlobalStatus,
    SPGlobalTag,
    Error,
)
from .enums import SPGlobalUpdateState
import pydantic


# region 创意
class SPGlobalGlobalStoreSettings(CamelCaseBaseModel):
    catalog_source_marketplace: Optional[SPGlobalMarketplace] = None


class SPGlobalCreateGlobalStoreSettings(CamelCaseBaseModel):
    catalog_source_marketplace: Optional[SPGlobalMarketplace] = None


class SPGlobalAdvertisedProductMarketplaceSetting(CamelCaseBaseModel):
    global_store_setting: Optional[SPGlobalGlobalStoreSettings]
    marketplace: SPGlobalMarketplace
    product_id: str
    resolved_product_id: Optional[str] = None


class SPGlobalCreateAdvertisedProductMarketplaceSetting(CamelCaseBaseModel):
    global_store_setting: Optional[SPGlobalCreateGlobalStoreSettings]
    marketplace: SPGlobalMarketplace
    product_id: str


class SPGlobalAdvertisedProducts(CamelCaseBaseModel):
    marketplace_settings: Optional[list[SPGlobalAdvertisedProductMarketplaceSetting]]
    product_id_type: Literal["ASIN", "SKU"]
    resolved_product_id_type: Optional[Literal["ASIN", "SKU"]]


class SPGlobalCreateAdvertisedProducts(CamelCaseBaseModel):
    marketplace_settings: Optional[
        list[SPGlobalCreateAdvertisedProductMarketplaceSetting]
    ]
    product_id_type: Literal["ASIN", "SKU"]


class SPGlobalProductCreativeSettings(CamelCaseBaseModel):
    advertised_product: SPGlobalAdvertisedProducts


class SPGlobalCreateProductCreativeSettings(CamelCaseBaseModel):
    advertised_product: SPGlobalCreateAdvertisedProducts


class SPGlobalProductCreative(CamelCaseBaseModel):
    product_creative_settings: SPGlobalProductCreativeSettings


class SPGlobalCreateProductCreative(CamelCaseBaseModel):
    product_creative_settings: SPGlobalCreateProductCreativeSettings


class SPGlobalCreative(CamelCaseBaseModel):
    product_creative: SPGlobalProductCreative


class SPGlobalCreateCreative(CamelCaseBaseModel):
    product_creative: SPGlobalCreateProductCreative


# endregion
# region SPGlobalAd
class SPGlobalAd(CamelCaseBaseModel):
    ad_group_id: str
    ad_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"]
    ad_type: Literal["PRODUCT_AD"]
    campaign_id: str
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    creative: SPGlobalCreative
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_scope: Literal["GLOBAL"]
    marketplaces: list[SPGlobalMarketplace]
    state: SPGlobalState
    status: SPGlobalStatus
    tags: Optional[list[SPGlobalTag]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )


# endregion


# region SPGlobalCreateMarketplaceAdConfigurations
class SPGlobalCreateMarketplaceAdFieldOverrides(CamelCaseBaseModel):
    state: Optional[SPGlobalState]
    tags: Optional[list[SPGlobalTag]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )


class SPGlobalCreateMarketplaceAdConfigurations(CamelCaseBaseModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceAdFieldOverrides


# endregion


# region 创建Ad
class SPGlobalAdCreate(CamelCaseBaseModel):
    ad_group_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    ad_type: Literal["PRODUCT_AD"] = "PRODUCT_AD"
    creative: SPGlobalCreateCreative
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceAdConfigurations]
    ] = None
    marketplace_scope: Literal["GLOBAL"] = "GLOBAL"
    marketplaces: list[SPGlobalMarketplace]
    state: SPGlobalCreateState
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )


# endregion


# region 更新Ad
class SPGlobalAdUpdate(CamelCaseBaseModel):
    ad_id: str
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceAdConfigurations]
    ] = None
    marketplaces: Optional[list[SPGlobalMarketplace]] = None
    state: Optional[SPGlobalUpdateState] = None
    tags: Optional[list[SPTag]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )


# endregion


# region SPGlobalAdPartialIndex
class SPGlobalAdPartialIndex(CamelCaseBaseModel):
    ad: SPGlobalAd
    errors: list[Error]
    index: int


# endregion


# region SPGlobalAdMultiStatusSuccess
class SPGlobalAdMultiStatusSuccess(CamelCaseBaseModel):
    ad: SPGlobalAd
    index: int


# endregion
