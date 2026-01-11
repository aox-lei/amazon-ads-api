from datetime import datetime
from typing import Optional
import pydantic
from typing_extensions import Literal
from ads_api.base import CamelCaseBaseModel
from .enums import *
from .common_type import Error, SPGlobalStatus, SPGlobalTag, SPGlobalCreateTag


# region 预算 Model
class SPGlobalMonetaryBudget(CamelCaseBaseModel):
    currency_code: SPGlobalCurrencyCode
    rule_value: Optional[float] = None
    # 预算货币的上限金额
    value: float


class SPGlobalCreateMonetaryBudget(CamelCaseBaseModel):
    value: float


class SPGlobalMonetaryBudgetMarketplaceSetting(CamelCaseBaseModel):
    marketplace: SPGlobalMarketplace
    monetary_budget: SPGlobalMonetaryBudget


class SPGlobalCreateMonetaryBudgetMarketplaceSetting(CamelCaseBaseModel):
    marketplace: SPGlobalMarketplace
    monetary_budget: SPGlobalCreateMonetaryBudget


class SPGlobalMonetaryBudgetValue(CamelCaseBaseModel):
    marketplace_settings: list[SPGlobalMonetaryBudgetMarketplaceSetting]


class SPGlobalCreateMonetaryBudgetValue(CamelCaseBaseModel):
    marketplace_settings: list[SPGlobalCreateMonetaryBudgetMarketplaceSetting]


class SPGlobalBudgetValue(CamelCaseBaseModel):
    monetary_budget_value: SPGlobalMonetaryBudgetValue


class SPGlobalCreateBudgetValue(CamelCaseBaseModel):
    monetary_budget_value: SPGlobalCreateMonetaryBudgetValue


class SPGlobalBudget(CamelCaseBaseModel):
    budget_type: Literal["MONETARY"]  # 预算类型 货币
    budget_value: SPGlobalBudgetValue
    recurrence_time_period: Literal["DAILY"]  # 预算周期, 每日


class SPGlobalCreateBudget(CamelCaseBaseModel):
    """预算(创建)"""

    budget_type: Literal["MONETARY"] = "MONETARY"  # 预算类型 货币
    budget_value: SPGlobalCreateBudgetValue
    recurrence_time_period: Literal["DAILY"] = "DAILY"


# endregion


# region 优化 Model
class SPGlobalPlacementBidAdjustment(CamelCaseBaseModel):
    percentage: int
    placement: SPGlobalPlacement


class SPGlobalCreatePlacementBidAdjustment(CamelCaseBaseModel):
    percentage: int
    placement: SPGlobalPlacement


class SPGlobalBidAdjustments(CamelCaseBaseModel):
    placement_bid_adjustments: Optional[list[SPGlobalPlacementBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=3)
    )


class SPGlobalCreateBidAdjustments(CamelCaseBaseModel):
    placement_bid_adjustments: Optional[list[SPGlobalCreatePlacementBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=3)
    )


class SPGlobalBidSettings(CamelCaseBaseModel):
    bid_adjustments: Optional[SPGlobalBidAdjustments] = None
    bid_strategy: Optional[SPGlobalBidStrategy] = None


class SPGlobalCreateBidSettings(CamelCaseBaseModel):
    bid_adjustments: Optional[SPGlobalCreateBidAdjustments] = None
    bid_strategy: Optional[SPGlobalBidStrategy] = None


class SPCampaignOptimizations(CamelCaseBaseModel):
    """优化设置"""

    bid_settings: Optional[SPGlobalBidSettings] = None  # 竞价设置


class SPGlobalCreateCampaignOptimizations(CamelCaseBaseModel):
    """优化设置(创建)"""

    bid_settings: Optional[SPGlobalCreateBidSettings] = None  # 竞价设置


# endregion


# region 自动创建设置
class SPGlobalAutoCreationSettings(CamelCaseBaseModel):
    auto_create_targets: bool


class SPGlobalCreateAutoCreationSettings(CamelCaseBaseModel):
    auto_create_targets: bool


# endregion

# region SPGlobalCampaign


class SPGlobalCampaign(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"]
    auto_creation_settings: SPGlobalAutoCreationSettings
    budgets: list[SPGlobalBudget]  # 预算
    campaign_id: str  # 活动编号
    countries: Optional[list[SPGlobalCountryCode]] = pydantic.Field(
        default=None, min_items=0, max_items=1
    )
    # 创建时间
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    # 结束时间
    end_datetime: Optional[datetime] = pydantic.Field(default=None, alias="endDateTime")
    global_campaign_id: Optional[str] = None  # 全球活动编号
    # 上次更新日期
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_scope: Literal["SINGLE_MARKETPLACE"]  # 市场范围， 单一市场
    marketplaces: Optional[list[SPMarketplace]] = pydantic.Field(
        default=None, min_items=0, max_items=1
    )
    name: str  # 活动名称
    optimizations: Optional[SPCampaignOptimizations] = None  # 优化
    protfolio_id: Optional[str] = None  # 组合编号
    site_restrictions: Optional[SPSiteRestriction] = None  # 网站限制
    # 活动开始时间
    start_datetime: datetime = pydantic.Field(default=..., alias="startDateTime")
    state: SPState  # 状态
    status: Optional[SPGlobalStatus]  # 状态
    # 开放式标签, 自定义
    tags: Optional[list["SPGlobalTag"]] = pydantic.Field(default=None, max_items=50)


# endregion


# region 创建全球活动


class SPGlobalCreateMarketplaceCampaignFieldOverrides(CamelCaseBaseModel):
    end_datetime: Optional[datetime] = pydantic.Field(default=None, alias="endDateTime")
    name: Optional[str] = None
    optimizations: Optional[SPGlobalCreateCampaignOptimizations]
    start_datetime: Optional[datetime] = pydantic.Field(
        default=None, alias="startDateTime"
    )
    state: Optional[SPGlobalState]
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(default=None, max_items=50)


class SPGlobalCreateMarketplaceCampaignConfigurations(CamelCaseBaseModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceCampaignFieldOverrides


class SPGlobalCampaignCreate(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    auto_creation_settings: SPGlobalCreateAutoCreationSettings
    budgets: list[SPGlobalCreateBudget]
    countries: Optional[list[SPGlobalCountryCode]] = pydantic.Field(
        default=None, max_items=1
    )
    end_datetime: Optional[datetime] = pydantic.Field(default=None, alias="endDateTime")
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceCampaignConfigurations]
    ] = None
    marketplace_scope: Literal["GLOBAL"] = "GLOBAL"
    marketplaces: Optional[list[SPGlobalMarketplace]] = None
    name: str
    optimizations: Optional[SPGlobalCreateCampaignOptimizations] = None
    portfolio_id: Optional[str] = None
    site_restrictions: Optional[SPGlobalSiteRestriction] = None
    start_datetime: datetime = pydantic.Field(default=..., alias="startDateTime")
    state: SPGlobalCreateState
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(default=None, max_items=50)


# endregion


# region 更新全球广告活动
class SPGlobalCampaignUpdate(CamelCaseBaseModel):
    budgets: Optional[list[SPGlobalCreateBudget]] = None
    campaign_id: str
    countries: Optional[list[SPGlobalCountryCode]] = None
    end_datetime: Optional[datetime] = pydantic.Field(default=None, alias="endDateTime")
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceCampaignConfigurations]
    ] = None
    marketplaces: Optional[list[SPGlobalMarketplace]] = None
    name: Optional[str] = None
    optimizations: Optional[SPGlobalCreateCampaignOptimizations] = None
    portfolio_id: Optional[str] = None
    site_restrictions: Optional[SPGlobalSiteRestriction] = None
    start_datetime: Optional[datetime] = pydantic.Field(
        default=None, alias="startDateTime"
    )
    state: Optional[SPGlobalUpdateState] = None
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(default=None, max_items=50)


# endregion


# region Operation Global Campaign
class SPGlobalCampaignPartialIndex(CamelCaseBaseModel):
    campaign: SPGlobalCampaign
    errors: list[Error]
    index: int


class SPGlobalCampaignMultiStatusSuccess(CamelCaseBaseModel):
    campaign: SPGlobalCampaign
    index: int
