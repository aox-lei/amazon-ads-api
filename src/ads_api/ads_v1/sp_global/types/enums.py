from enum import Enum


class SPGlobalCampaignStateFilter(str, Enum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    ARCHIVED = "ARCHIVED"


class SPGlobalCurrencyCode(str, Enum):
    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    MXP = "MXP"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"
    
class SPGlobalCurrencyCodeByCountryCode(Enum):
    AE = SPGlobalCurrencyCode.AED
    AU = SPGlobalCurrencyCode.AUD
    BE = SPGlobalCurrencyCode.EUR  # 比利时使用欧元
    BR = SPGlobalCurrencyCode.BRL
    CA = SPGlobalCurrencyCode.CAD
    DE = SPGlobalCurrencyCode.EUR  # 德国使用欧元
    EG = SPGlobalCurrencyCode.EGP
    ES = SPGlobalCurrencyCode.EUR  # 西班牙使用欧元
    FR = SPGlobalCurrencyCode.EUR  # 法国使用欧元
    GB = SPGlobalCurrencyCode.GBP
    UK = SPGlobalCurrencyCode.GBP
    IN = SPGlobalCurrencyCode.INR
    IT = SPGlobalCurrencyCode.EUR  # 意大利使用欧元
    JP = SPGlobalCurrencyCode.JPY
    MX = SPGlobalCurrencyCode.MXN  # 墨西哥使用墨西哥比索
    NL = SPGlobalCurrencyCode.EUR  # 荷兰使用欧元
    PL = SPGlobalCurrencyCode.PLN
    SA = SPGlobalCurrencyCode.SAR  # 沙特阿拉伯使用沙特里亚尔
    SE = SPGlobalCurrencyCode.SEK
    SG = SPGlobalCurrencyCode.SGD
    TR = SPGlobalCurrencyCode.TRY
    US = SPGlobalCurrencyCode.USD
    ZA = SPGlobalCurrencyCode.ZAR  # 南非使用南非兰特


class SPGlobalCountryCode(str, Enum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MK = "MK"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SPGlobalMarketplace(str, Enum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    UK = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SPGlobalBidStrategy(str, Enum):
    MANUAL = "MANUAL"  # 使用您设定的确切出价和任何排名调整，不受动态竞价的影响
    RULE_BASED = "RULE_BASED"  # 基于规则
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"  # 只向下调整
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"  # 实时调整出价，最大增减幅度为 100%。启用此设置后，当广告更有可能转化为销售时，出价会增加；当转化可能性较低时，出价会降低。


# region Placement 位置


class SPGlobalPlacement(str, Enum):
    PRODUCT_PAGE = "PRODUCT_PAGE"  # 产品页
    REST_OF_SEARCH = "REST_OF_SEARCH"  # 位于搜索结果首页中间或底部的广告位。也指位于搜索结果第二页及以后的广告位。
    TOP_OF_SEARCH = "TOP_OF_SEARCH"  # 在搜索结果首页顶部位置展示。


# endregion


# region 网站限制
class SPGlobalSiteRestriction(str, Enum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # 企业购
    AMAZON_HAUL = "AMAZON_HAUL"


# endregion


# region SPState
class SPGlobalState(str, Enum):
    ENABLED = "ENABLED"  # 活动
    PAUSED = "PAUSED"  # 暂停
    ARCHIVED = "ARCHIVED"  # 归档


class SPGlobalCreateState(str, Enum):
    ENABLED = "ENABLED"  # 活动
    PAUSED = "PAUSED"  # 暂停


class SPGlobalUpdateState(str, Enum):
    ENABLED = "ENABLED"  # 活动
    PAUSED = "PAUSED"  # 暂停
    ENABLING="ENABLING"


# endregion


# region SPDeliveryReason
class SPGlobalDeliveryReason(str, Enum):
    # --- 广告主级别 (ADVERTISER) ---
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"  # 广告主账号已归档
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"  # 广告主账户预算已耗尽
    ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT = (
        "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT"  # 超出后付费信用额度
    )
    ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET = (
        "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET"  # 超出后付费每月预算限制
    )
    ADVERTISER_OUT_OF_PREPAY_BALANCE = (
        "ADVERTISER_OUT_OF_PREPAY_BALANCE"  # 预付费余额不足
    )
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"  # 广告主账号已手动暂停
    ADVERTISER_PAYMENT_FAILURE = (
        "ADVERTISER_PAYMENT_FAILURE"  # 广告主支付方式失效或扣款失败
    )
    ADVERTISER_POLICING_PENDING_REVIEW = (
        "ADVERTISER_POLICING_PENDING_REVIEW"  # 广告主账号合规性审核中
    )
    ADVERTISER_POLICING_SUSPENDED = (
        "ADVERTISER_POLICING_SUSPENDED"  # 广告主账号因违反政策被暂停
    )

    # --- 广告活动级别 (CAMPAIGN) ---
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"  # 广告活动已归档
    CAMPAIGN_END_DATE_REACHED = (
        "CAMPAIGN_END_DATE_REACHED"  # 已达到广告活动设置的结束日期
    )
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"  # 广告活动信息设置不完整
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"  # 广告活动日预算已耗尽
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"  # 广告活动已手动暂停
    CAMPAIGN_PENDING_REVIEW = "CAMPAIGN_PENDING_REVIEW"  # 广告活动正在审核中
    CAMPAIGN_PENDING_START_DATE = (
        "CAMPAIGN_PENDING_START_DATE"  # 尚未到达广告活动开始日期
    )
    CAMPAIGN_REJECTED = "CAMPAIGN_REJECTED"  # 广告活动被拒绝

    # --- 广告组级别 (AD_GROUP) ---
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"  # 广告组已归档
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"  # 广告组设置不完整
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"  # 广告组出价过低，难以获得曝光
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"  # 广告组已手动暂停
    AD_GROUP_PENDING_REVIEW = "AD_GROUP_PENDING_REVIEW"  # 广告组审核中
    AD_GROUP_POLICING_PENDING_REVIEW = (
        "AD_GROUP_POLICING_PENDING_REVIEW"  # 广告组合规性审核中
    )
    AD_GROUP_REJECTED = "AD_GROUP_REJECTED"  # 广告组被拒绝

    # --- 广告级别 (AD) ---
    AD_ARCHIVED = "AD_ARCHIVED"  # 广告已归档
    AD_PAUSED = "AD_PAUSED"  # 广告已手动暂停
    AD_INELIGIBLE = "AD_INELIGIBLE"  # 广告不符合投放资格（通常与商品状态有关）
    AD_NOT_DELIVERING = "AD_NOT_DELIVERING"  # 广告当前未在投放
    AD_CREATION_FAILED = "AD_CREATION_FAILED"  # 广告创建失败
    AD_CREATION_IN_PROGRESS = "AD_CREATION_IN_PROGRESS"  # 广告正在创建中
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"  # 广告合规性审核中
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"  # 广告因违反政策被暂停
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"  # 广告缺少必要的装饰元素
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"  # 广告缺少图片素材

    # --- 创意/素材级别 (CREATIVE) ---
    CREATIVE_MISSING_ASSET = (
        "CREATIVE_MISSING_ASSET"  # 创意缺少必要的素材（如Logo或背景图）
    )
    CREATIVE_PENDING_REVIEW = "CREATIVE_PENDING_REVIEW"  # 创意审核中
    CREATIVE_REJECTED = "CREATIVE_REJECTED"  # 创意被审核拒绝

    # --- 商品/页面状态 (PRODUCT / ELIGIBILITY) ---
    BRAND_INELIGIBLE = "BRAND_INELIGIBLE"  # 品牌不符合投放资格
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"  # 落地页不符合投放资格
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"  # 落地页无法打开或不存在
    NOT_BUYABLE = "NOT_BUYABLE"  # 商品当前不可购买
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"  # 商品失去黄金购物车 (Buybox)
    NOT_IN_POLICY = "NOT_IN_POLICY"  # 不符合广告投放政策
    NO_INVENTORY = "NO_INVENTORY"  # 库房无货
    OUT_OF_STOCK = "OUT_OF_STOCK"  # 商品缺货
    NO_PURCHASABLE_OFFER = "NO_PURCHASABLE_OFFER"  # 没有可购买的报价

    # --- 审核政策原因 (MODERATION / POLICY) ---
    MODERATION_ADULT_NOVELTY_POLICY_VIOLATION = (
        "MODERATION_ADULT_NOVELTY_POLICY_VIOLATION"  # 违反成人新奇物品政策
    )
    MODERATION_ADULT_PRODUCT_POLICY_VIOLATION = (
        "MODERATION_ADULT_PRODUCT_POLICY_VIOLATION"  # 违反成人用品政策
    )
    MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION = (
        "MODERATION_ADULT_SOFTLINES_POLICY_VIOLATION"  # 违反成人轻纺产品政策
    )
    MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION = (
        "MODERATION_CLAIM_WEIGHTLOSS_POLICY_VIOLATION"  # 违反减肥声明政策
    )
    MODERATION_CONTENT_NUDITY_POLICY_VIOLATION = (
        "MODERATION_CONTENT_NUDITY_POLICY_VIOLATION"  # 违反裸露内容政策
    )
    MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION = (
        "MODERATION_CONTENT_PROVOCATIVE_POLICY_VIOLATION"  # 违反挑逗性内容政策
    )
    MODERATION_CONTENT_SMOKING_POLICY_VIOLATION = (
        "MODERATION_CONTENT_SMOKING_POLICY_VIOLATION"  # 违反吸烟内容政策
    )
    MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION = (
        "MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION"  # 违反重大敏感事件政策
    )
    MODERATION_ERROR_404 = "MODERATION_ERROR_404"  # 审核时落地页返回 404 错误
    MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION = (
        "MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION"  # 违反性暗示图像政策
    )
    MODERATION_HFSS_PRODUCT_POLICY_VIOLATION = (
        "MODERATION_HFSS_PRODUCT_POLICY_VIOLATION"  # 违反高油盐糖食品政策
    )
    MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION = (
        "MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION"  # 违反攻击性语言政策
    )
    MODERATION_NOT_COMPLIANT_TO_AD_POLICY = (
        "MODERATION_NOT_COMPLIANT_TO_AD_POLICY"  # 不符合通用广告政策
    )
    MODERATION_SMOKING_RELATED_POLICY_VIOLATION = (
        "MODERATION_SMOKING_RELATED_POLICY_VIOLATION"  # 违反吸烟相关产品政策
    )

    # --- 组合/定位/限制 (PORTFOLIO / TARGET / OTHER) ---
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"  # 广告组合已归档
    PORTFOLIO_END_DATE_REACHED = "PORTFOLIO_END_DATE_REACHED"  # 广告组合已结束
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"  # 广告组合预算已耗尽
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"  # 广告组合已暂停
    PORTFOLIO_PENDING_START_DATE = (
        "PORTFOLIO_PENDING_START_DATE"  # 广告组合尚未到达开始日期
    )
    TARGET_ARCHIVED = "TARGET_ARCHIVED"  # 投放目标（关键词/商品等）已归档
    TARGET_BLOCKED = "TARGET_BLOCKED"  # 投放目标被封锁
    TARGET_PAUSED = "TARGET_PAUSED"  # 投放目标已手动暂停
    TARGET_POLICING_SUSPENDED = "TARGET_POLICING_SUSPENDED"  # 投放目标因违规被暂停
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"  # 安全扫描审核中
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"  # 安全扫描未通过
    SPEND_LIMIT_EXCEEDED = "SPEND_LIMIT_EXCEEDED"  # 超出支出限制
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"  # 根据 PIR 规则被排除
    OUT_OF_REWARD_BUDGET = "OUT_OF_REWARD_BUDGET"  # 奖励预算耗尽
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"  # 状态不可用
    OTHER = "OTHER"  # 其他未知原因


# endregion


# region SPDeliveryStatus Model
class SPDeliveryStatus(str, Enum):
    DELIVERING = "DELIVERING"  # 正在交付
    NOT_DELIVERING = "NOT_DELIVERING"  # 未交付
    UNAVAILABLE = "UNAVAILABLE"  # 不可用


# endregion


# region SPAdGroupStateFilter


class SPGlobalAdGroupStateFilter(str, Enum):
    ENABLED = "ENABLED"  # 启用
    PAUSED = "PAUSED"  # 暂停
    ARCHIVED = "ARCHIVED"  # 归档


# endregion


# region SPAdStateFilter
class SPAdStateFilter(str, Enum):
    ENABLED = "ENABLED"  # 启用
    PAUSED = "PAUSED"  # 暂停
    ARCHIVED = "ARCHIVED"  # 归档


# endregion
