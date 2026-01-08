from datetime import datetime
from typing import Optional
from ads_api.base import CamelCaseBaseModel
from typing_extensions import Literal
from .enums import *
import pydantic


# region 自动创建
class SPAutoCreationSettings(CamelCaseBaseModel):
    """自动创建设置"""

    # 是否自动创建目标受众
    auto_create_targets: bool
    # 是否允许亚马逊管理您的广告系列生命周期
    auto_manage_campaign: Optional[bool] = None


class SPCreateAutoCreationSettings(CamelCaseBaseModel):
    # 是否自动创建目标受众
    auto_create_targets: bool
    # 是否允许亚马逊管理您的广告系列生命周期
    auto_manage_campaign: Optional[bool] = None


# endregion


# region 预算 Model
class SPMonetaryBudget(CamelCaseBaseModel):
    """货币预算"""

    currency_code: SPCurrencyCode
    # 应用预算规则后预算的货币金额
    rule_value: Optional[float] = None
    # 预算货币的上限金额
    value: float


class SPCreateMonetaryBudget(CamelCaseBaseModel):
    """货币预算(创建)"""

    value: float


class SPMonetaryBudgetValue(CamelCaseBaseModel):
    monetary_budget: SPMonetaryBudget


class SPCreateMonetaryBudgetValue(CamelCaseBaseModel):
    monetary_budget: SPCreateMonetaryBudget


class SPBudgetValue(CamelCaseBaseModel):
    """货币预算值"""

    monetary_budget_value: SPMonetaryBudgetValue


class SPCreateBudgetValue(CamelCaseBaseModel):
    """货币预算值(创建)"""

    monetary_budget_value: SPCreateMonetaryBudgetValue


class SPBudget(CamelCaseBaseModel):
    """预算"""

    budget_type: Literal["MONETARY"]  # 预算类型 货币
    budget_value: SPBudgetValue
    recurrence_time_period: Literal["DAILY"]  # 预算周期, 每日


class SPCreateBudget(CamelCaseBaseModel):
    budget_type: Literal["MONETARY"] = "MONETARY"
    budget_value: SPCreateBudgetValue
    recurrence_time_period: Literal["DAILY"] = "DAILY"


# endregion


# region 优化 Model
# --- 竞价设置 -------------------
class SPAudienceBidAdjustment(CamelCaseBaseModel):
    """观众出价调整"""

    audience_id: str
    percentage: int  # 百分比


class SPCreateAudienceBidAdjustment(CamelCaseBaseModel):
    """观众出价调整(创建)"""

    audience_id: str
    percentage: int  # 百分比


class SPCreativeBidAdjustment(CamelCaseBaseModel):
    """创意出价调整"""

    creative_type: Optional[Literal["SPOTLIGHT"]] = None  # 创意类型
    percentage: int  # 百分比


class SPCreateCreativeBidAdjustment(CamelCaseBaseModel):
    """创意出价调整(创建)"""

    creative_type: Optional[Literal["SPOTLIGHT"]] = None  # 创意类型
    percentage: int  # 百分比


class SPPlacementBidAdjustment(CamelCaseBaseModel):
    """竞价调整"""

    percentage: int
    placement: SPPlacement


class SPCreatePlacementBidAdjustment(CamelCaseBaseModel):
    """竞价调整(创建)"""

    percentage: int
    placement: SPPlacement


class SPBidAdjustments(CamelCaseBaseModel):
    # 观众出价调整
    audience_bid_adjustments: Optional[list[SPAudienceBidAdjustment]] = pydantic.Field(
        default=None, min_items=0, max_items=1
    )
    # 创意竞价调整
    creative_bid_adjustments: Optional[list[SPCreativeBidAdjustment]] = pydantic.Field(
        default=None, min_items=0, max_items=2
    )
    # 竞价调整
    placement_bid_adjustments: Optional[list[SPPlacementBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=4)
    )


class SPCreateBidAdjustments(CamelCaseBaseModel):
    # 观众出价调整
    audience_bid_adjustments: Optional[list[SPCreateAudienceBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=1)
    )
    # 创意竞价调整
    creative_bid_adjustments: Optional[list[SPCreateCreativeBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=2)
    )
    # 竞价调整
    placement_bid_adjustments: Optional[list[SPCreatePlacementBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=4)
    )


class SPUpdateBidAdjustments(CamelCaseBaseModel):
    # 观众出价调整
    audience_bid_adjustments: Optional[list[SPCreateAudienceBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=1)
    )
    # 创意竞价调整
    creative_bid_adjustments: Optional[list[SPCreateCreativeBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=2)
    )
    # 竞价调整
    placement_bid_adjustments: Optional[list[SPCreatePlacementBidAdjustment]] = (
        pydantic.Field(default=None, min_items=0, max_items=4)
    )


class SPBidSettings(CamelCaseBaseModel):
    """竞价设置"""

    bid_adjustments: Optional[SPBidAdjustments] = None
    bid_strategy: Optional[SPBidStrategy] = None


class SPCreateBidSettings(CamelCaseBaseModel):
    bid_adjustments: Optional[SPCreateBidAdjustments] = None
    bid_strategy: Optional[SPBidStrategy] = None


class SPUpdateBidSettings(CamelCaseBaseModel):
    bid_adjustments: Optional[SPUpdateBidAdjustments] = None
    bid_strategy: Optional[SPBidStrategy] = None


# --- end 竞价设置 -------------------
class SPBudgetSettings(CamelCaseBaseModel):
    """预算设置"""

    off_amazon_budget_control_strategy: Optional[SPOffAmazonBudgetControlStrategy] = (
        None
    )


class SPCreateBudgetSettings(CamelCaseBaseModel):
    """预算设置(创建)"""

    off_amazon_budget_control_strategy: Optional[SPOffAmazonBudgetControlStrategy] = (
        None
    )


class SPUpdateBudgetSettings(CamelCaseBaseModel):
    """预算设置(更新)"""

    off_amazon_budget_control_strategy: Optional[SPOffAmazonBudgetControlStrategy] = (
        None
    )


class SPCampaignOptimizations(CamelCaseBaseModel):
    """优化设置"""

    bid_settings: Optional[SPBidSettings] = None  # 竞价设置
    budget_settings: Optional[SPBudgetSettings] = None  # 预算设置


class SPCreateCampaignOptimizations(CamelCaseBaseModel):
    """优化设置(创建)"""

    bid_settings: Optional[SPCreateBidSettings] = None  # 竞价设置
    budget_settings: Optional[SPCreateBudgetSettings] = None  # 预算设置


class SPUpdateCampaignOptimizations(CamelCaseBaseModel):
    """优化设置(更新)"""

    bid_settings: Optional[SPUpdateBidSettings] = None  # 竞价设置
    budget_settings: Optional[SPUpdateBudgetSettings] = None  # 预算设置


# endregion


# region Tag Model
class SPCreateTag(CamelCaseBaseModel):
    key: str
    value: str


class SPTag(CamelCaseBaseModel):
    key: str
    value: str


# endregion


# region SPCampagin
class SPStatus(CamelCaseBaseModel):
    delivery_reasons: Optional[list[SPDeliveryReason]] = None
    delivery_status: SPDeliveryStatus


class SPCampaign(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"]
    auto_creation_settings: SPAutoCreationSettings
    budgets: list[SPBudget]  # 预算
    campaign_id: str  # 活动编号
    countries: Optional[list[SPCountryCode]] = pydantic.Field(
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
    status: Optional[SPStatus]  # 状态
    # 开放式标签, 自定义
    tags: Optional[list[SPTag]] = pydantic.Field(default=None)


# endregion


# region 创建活动


class SPCampaignCreate(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    auto_creation_settings: SPCreateAutoCreationSettings
    budgets: list[SPCreateBudget] = pydantic.Field(default=..., max_items=1)
    countries: Optional[list[SPCountryCode]] = pydantic.Field(default=None, max_items=1)
    end_datetime: Optional[datetime] = pydantic.Field(default=None, alias="endDateTime")
    marketplace_scope: Literal["SINGLE_MARKETPLACE"] = "SINGLE_MARKETPLACE"
    marketplaces: Optional[list[SPMarketplace]] = pydantic.Field(
        default=None, max_items=1
    )
    name: str
    optimizations: Optional[SPCreateCampaignOptimizations] = None
    protfolio_id: Optional[str] = None
    site_restrictions: Optional[list[SPSiteRestriction]] = pydantic.Field(
        default=None, max_items=1
    )
    start_datetime: datetime
    state: SPCreateState
    tags: Optional[SPCreateTag] = None


# endregion


# region 更新活动
class SPCampaignUpdate(CamelCaseBaseModel):
    budgets: Optional[list[SPCreateBudget]] = None
    campaign_id: str
    end_datetime: Optional[datetime] = pydantic.Field(default=None, alias="endDateTime")
    name: Optional[str] = None
    optimizations: Optional[SPUpdateCampaignOptimizations] = None
    portfolio_id: Optional[str] = None
    site_restrictions: Optional[list[SPSiteRestriction]] = None
    start_datetime: Optional[datetime] = pydantic.Field(
        default=None, alias="startDateTime"
    )
    state: Optional[SPUpdateState] = None
    tags: Optional[dict[str, str]]


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


# region SPCampaignMultiStatusSuccess Response
class SPCampaignMultiStatusSuccess(CamelCaseBaseModel):
    campaign: SPCampaign
    index: int


# endregion
