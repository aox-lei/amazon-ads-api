from datetime import datetime
from typing import Optional
from ads_api.base import CamelCaseBaseModel
from typing_extensions import Literal
from .enums import *
from .common_type import SPStatus, SPTag, SPCreateTag
import pydantic


# region 创意
class SPVideo(CamelCaseBaseModel):
    asset_id: str  # 资源id
    asset_version: str  # 视频版本
    description: Optional[str] = None  # 描述
    headline: Optional[str] = None  # 视频的标题


class SPCreateVideo(CamelCaseBaseModel):
    asset_id: str  # 资源id
    asset_version: str  # 视频版本
    description: Optional[str] = None  # 描述
    headline: Optional[str] = None  # 视频的标题


class SPSpotlightVideoSettings(CamelCaseBaseModel):
    optimize_text: bool  # 是否希望亚马逊对提供的文本进行优化
    videos: list[SPVideo]


class SPCreateSpotlightVideoSettings(CamelCaseBaseModel):
    optimize_text: bool  # 是否希望亚马逊对提供的文本进行优化
    videos: list[SPCreateVideo]


class SPUpdateSpotlightVideoSettings(CamelCaseBaseModel):
    optimize_text: bool  # 是否希望亚马逊对提供的文本进行优化
    videos: list[SPCreateVideo]


class SPGlobalStoreSettings(CamelCaseBaseModel):
    catalog_source_marketplace: Optional[SPMarketplace] = None
    product_id: str
    product_id_type: Literal["ASIN", "SKU"]
    resolved_product_id: str  # 与广告产品关联的产品标识符。这是一个只读字段。
    resolved_product_id_type: Optional[Literal["ASIN", "SKU"]]  # 已解析的产品 ID 类


class SPCreateGlobalStoreSettings(CamelCaseBaseModel):
    catalog_source_marketplace: Optional[SPMarketplace] = None
    product_id: str
    product_id_type: Literal["ASIN", "SKU"]


class SPAdvertisedProducts(CamelCaseBaseModel):
    global_store_settings: Optional[SPGlobalStoreSettings] = None
    product_id: str  # 广告产品的标识符
    product_id_type: Literal["ASIN", "SKU"]
    resolved_product_id: str  # 与广告产品关联的产品标识符。这是一个只读字段。
    resolved_product_id_type: Optional[Literal["ASIN", "SKU"]]  # 已解析的产品 ID 类


class SPCreateAdvertisedProducts(CamelCaseBaseModel):
    global_store_settings: Optional[SPCreateGlobalStoreSettings] = None
    product_id: str  # 广告产品的标识符
    product_id_type: Literal["ASIN", "SKU"]


class SPProductCreativeSettings(CamelCaseBaseModel):
    advertised_product: SPAdvertisedProducts
    headline: Optional[str] = None  # 与广告创意关联的标题/自定义文本。
    spotlight_videos: Optional[SPSpotlightVideoSettings] = None


class SPCreateProductCreativeSettings(CamelCaseBaseModel):
    advertised_product: SPCreateAdvertisedProducts
    headline: Optional[str] = None  # 与广告创意关联的标题/自定义文本。
    spotlight_videos: Optional[SPCreateSpotlightVideoSettings] = None


class SPUpdateProductCreativeSettings(CamelCaseBaseModel):
    spotlight_videos: Optional[SPUpdateSpotlightVideoSettings] = None


class SPProductCreative(CamelCaseBaseModel):
    product_creative_settings: SPProductCreativeSettings


class SPCreateProductCreative(CamelCaseBaseModel):
    product_creative_settings: SPCreateProductCreativeSettings


class SPUpdateProductCreative(CamelCaseBaseModel):
    product_creative_settings: SPUpdateProductCreativeSettings


class SPCreative(CamelCaseBaseModel):
    product_creative: SPProductCreative


class SPCreateCreative(CamelCaseBaseModel):
    product_creative: SPCreateProductCreative


class SPUpdateCreative(CamelCaseBaseModel):
    product_creative: SPUpdateProductCreative


# endregion

# region SPAd


class SPAd(CamelCaseBaseModel):
    ad_group_id: str
    ad_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"]
    ad_type: Literal["PRODUCT_AD"]
    campaign_id: str
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    creative: SPCreative
    global_ad_id: Optional[str] = None
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_scope: Literal["SINGLE_MARKETPLACE"]
    marketplaces: list[SPMarketplace]
    state: SPState
    status: SPStatus
    tags: Optional[list[SPTag]] = pydantic.Field(default=None)


# endregion


# region 创建Ad
class SPAdCreate(CamelCaseBaseModel):
    ad_group_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    ad_type: Literal["PRODUCT_AD"] = "PRODUCT_AD"
    creative: SPCreateCreative
    state: SPCreateState
    tags: Optional[list[SPCreateTag]] = pydantic.Field(default=None)


# endregion


# region 更新Ad
class SPAdUpdate(CamelCaseBaseModel):
    ad_id: str
    creative: Optional[SPUpdateCreative] = None
    state: Optional[SPUpdateState] = None
    tags: Optional[list[SPCreateTag]] = pydantic.Field()


# endregion
