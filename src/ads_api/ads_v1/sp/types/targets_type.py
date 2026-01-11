from ads_api.base import CamelCaseBaseModel
from typing import Literal, Optional
import pydantic
from datetime import datetime
from .enums import (
    SPMarketplace,
    SPState,
    SPCurrencyCode,
    SPThemeMatchType,
    SPCreateState,
    SPTargetType,
    SPUpdateState
)
from .common_type import SPStatus, SPTag,SPCreateTag


# region 出价
class SPTargetBid(CamelCaseBaseModel):
    bid: Optional[float] = None
    curency_code: SPCurrencyCode


class SPCreateTargetBid(CamelCaseBaseModel):
    bid: Optional[float] = None
    
class SPUpdateTargetBid(CamelCaseBaseModel):
    bid: Optional[float] = None


# endregion

# region SPKeywordTarget


class SPKeywordTarget(CamelCaseBaseModel):
    keyword: str
    match_type: Literal["EXACT", "PHRASE", "BROAD"]
    native_language_keyword: Optional[str] = None  # 本地化的语言关键词
    native_language_local: Optional[Literal["zh_CN"]]


class SPCreateKeywordTarget(CamelCaseBaseModel):
    keyword: str
    match_type: Literal["EXACT", "PHRASE", "BROAD"]
    native_language_keyword: Optional[str] = None  # 本地化的语言关键词
    native_language_local: Optional[Literal["zh_CN"]]


# endregion

# region SPLocationTarget


class SPLocationTarget(CamelCaseBaseModel):
    location_id: str


class SPCreateLocationTarget(CamelCaseBaseModel):
    location_id: str


# endregion

# region SPProductCategoryTarget


class SPProductCategoryRefinement(CamelCaseBaseModel):
    product_age_range_id: Optional[str] = None  # 年龄范围id
    product_age_range_id_resolved: Optional[str] = None  # 解析的年龄范围id
    product_brand_id: Optional[str] = None  # 品牌id
    product_brand_id_resolved: Optional[str] = None
    product_category_id: Optional[str] = None  # 分类id
    product_category_id_resolved: Optional[str] = None
    product_genre_id: Optional[str] = None  # 产品类型id
    product_genre_id_resolved: Optional[str] = None
    product_price_greater_than: Optional[float] = None  # 价格>x
    product_price_less_than: Optional[float] = None  # 价格<x
    product_prime_shipping_eligible: Optional[bool] = None  # 是否符合prime配送条件
    product_rating_greater_than: Optional[float] = None  # 评分>x
    product_rating_less_than: Optional[float] = None  # 评分<x


class SPCreateProductCategoryRefinement(CamelCaseBaseModel):
    product_age_range_id: Optional[str] = None  # 年龄范围id
    product_age_range_id_resolved: Optional[str] = None  # 解析的年龄范围id
    product_brand_id: Optional[str] = None  # 品牌id
    product_brand_id_resolved: Optional[str] = None
    product_category_id: Optional[str] = None  # 分类id
    product_category_id_resolved: Optional[str] = None
    product_genre_id: Optional[str] = None  # 产品类型id
    product_genre_id_resolved: Optional[str] = None
    product_price_greater_than: Optional[float] = None  # 价格>x
    product_price_less_than: Optional[float] = None  # 价格<x
    product_prime_shipping_eligible: Optional[bool] = None  # 是否符合prime配送条件
    product_rating_greater_than: Optional[float] = None  # 评分>x
    product_rating_less_than: Optional[float] = None  # 评分<x


class SPProductCategoryRefinementValue(CamelCaseBaseModel):
    product_category_refinement: SPProductCategoryRefinement


class SPCreateProductCategoryRefinementValue(CamelCaseBaseModel):
    product_category_refinement: SPCreateProductCategoryRefinement


class SPProductCategoryTarget(CamelCaseBaseModel):
    product_category_refinement: SPProductCategoryRefinementValue


class SPCreateProductCategoryTarget(CamelCaseBaseModel):
    product_category_refinement: SPCreateProductCategoryRefinementValue


# endregion

# region SPProductTarget


class SPProductValue(CamelCaseBaseModel):
    product_id: str


class SPCreateProductValue(CamelCaseBaseModel):
    product_id: str


class SPProductTarget(CamelCaseBaseModel):
    match_type: Literal["PRODUCT_EXACT", "PRODUCT_SIMILAR"]
    product: SPProductValue
    product_type: Literal["ASIN", "SKU"]


class SPCreateProductTarget(CamelCaseBaseModel):
    match_type: Literal["PRODUCT_EXACT", "PRODUCT_SIMILAR"]
    product: SPCreateProductValue
    product_type: Literal["ASIN", "SKU"]


# endregion

# region SPThemeTarget


class SPThemeTarget(CamelCaseBaseModel):
    match_type: SPThemeMatchType


class SPCreateThemeTarget(CamelCaseBaseModel):
    match_type: SPThemeMatchType


# endregion

# region SPTargetDetails


class SPTargetDetails(CamelCaseBaseModel):
    keyword_target: Optional[SPKeywordTarget] = None
    locaition_target: Optional[SPLocationTarget] = None
    product_category_target: Optional[SPProductCategoryTarget] = None
    product_target: Optional[SPProductTarget] = None
    theme_target: Optional[SPThemeTarget] = None


class SPCreateTargetDetails(CamelCaseBaseModel):
    keyword_target: Optional[SPCreateKeywordTarget] = None
    locaition_target: Optional[SPCreateLocationTarget] = None
    product_category_target: Optional[SPCreateProductCategoryTarget] = None
    product_target: Optional[SPCreateProductTarget] = None
    theme_target: Optional[SPCreateThemeTarget] = None


# endregion

# region SPTarget


class SPTarget(CamelCaseBaseModel):
    ad_group_id: Optional[str] = None
    ad_product: Literal["SPONSORED_PRODUCTS"]
    bid: Optional[SPTargetBid] = None
    campaign_id: Optional[str] = None
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_scope: Literal["SINGLE_MARKETPLACE"]
    marketplaces: SPMarketplace
    negative: bool
    state: SPState
    status: Optional[SPStatus] = None
    tags: Optional[list[SPTag]] = pydantic.Field(default=None)
    target_details: SPTargetDetails
    target_id: str
    target_level: Literal["AD_GROUP", "CAMPAIGN"]
    target_type: SPTargetType


# endregion


# region TargetCreate
class SPTargetCreate(CamelCaseBaseModel):
    ad_group_id: Optional[str] = None
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    bid: Optional[SPCreateTargetBid] = None
    campaign_id: Optional[str] = None
    nagative: bool
    state: SPCreateState
    tags: Optional[list[SPTag]] = None
    target_details: SPCreateTargetDetails
    targett_type: SPTargetType


# endregion


# region SPTargetUpdate
class SPTargetUpdate(CamelCaseBaseModel):
    bid: Optional[SPUpdateTargetBid] = None
    state: Optional[SPUpdateState] = None
    tags: Optional[list[SPCreateTag]] = None
    target_id: str


# endregion


# region SPTargetMultiStatusSuccess
class SPTargetMultiStatusSuccess(CamelCaseBaseModel):
    index: int
    target: SPTarget


# endregion
