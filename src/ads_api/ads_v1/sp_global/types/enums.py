from enum import Enum


class SPCampaignStateFilter(str, Enum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    ARCHIVED = "ARCHIVED"


class SPCurrencyCode(str, Enum):
    AED = "AED"  # 阿联酋迪拉姆
    AUD = "AUD"  # 澳大利亚元
    BRL = "BRL"  # 巴西雷亚尔
    CAD = "CAD"  # 加拿大元
    CHF = "CHF"  # 瑞士法郎
    CNY = "CNY"  # 人民币
    DKK = "DKK"  # 丹麦克朗
    EGP = "EGP"  # 埃及镑
    EUR = "EUR"  # 欧元
    GBP = "GBP"  # 英镑
    INR = "INR"  # 印度卢比
    JPY = "JPY"  # 日元
    MXN = "MXN"  # 墨西哥比索
    MXP = "MXP"  # 墨西哥比索(旧)
    NGN = "NGN"  # 尼日利亚奈拉
    NOK = "NOK"  # 挪威克朗
    NZD = "NZD"  # 新西兰元
    PLN = "PLN"  # 波兰兹罗提
    SAR = "SAR"  # 沙特里亚尔
    SEK = "SEK"  # 瑞典克朗
    SGD = "SGD"  # 新加坡元
    TRY = "TRY"  # 土耳其里拉
    USD = "USD"  # 美元
    ZAR = "ZAR"  # 南非兰特


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


class SPCountryCode(str, Enum):
    """Amazon广告支持的国家/地区代码枚举"""

    AE = "AE"  # 阿联酋
    AU = "AU"  # 澳大利亚
    BE = "BE"  # 比利时
    BR = "BR"  # 巴西
    CA = "CA"  # 加拿大
    DE = "DE"  # 德国
    EG = "EG"  # 埃及
    ES = "ES"  # 西班牙
    FR = "FR"  # 法国
    GB = "GB"  # 英国
    IE = "IE"  # 爱尔兰
    IN = "IN"  # 印度
    IT = "IT"  # 意大利
    JP = "JP"  # 日本
    MX = "MX"  # 墨西哥
    NL = "NL"  # 荷兰
    PL = "PL"  # 波兰
    SA = "SA"  # 沙特阿拉伯
    SE = "SE"  # 瑞典
    SG = "SG"  # 新加坡
    TR = "TR"  # 土耳其
    US = "US"  # 美国
    ZA = "ZA"  # 南非


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


class SPMarketplace(str, Enum):
    """Amazon广告支持的国家/地区代码枚举"""

    AE = "AE"  # 阿联酋
    AU = "AU"  # 澳大利亚
    BE = "BE"  # 比利时
    BR = "BR"  # 巴西
    CA = "CA"  # 加拿大
    DE = "DE"  # 德国
    EG = "EG"  # 埃及
    ES = "ES"  # 西班牙
    FR = "FR"  # 法国
    GB = "GB"  # 英国
    IE = "IE"  # 爱尔兰
    IN = "IN"  # 印度
    IT = "IT"  # 意大利
    JP = "JP"  # 日本
    MX = "MX"  # 墨西哥
    NL = "NL"  # 荷兰
    PL = "PL"  # 波兰
    SA = "SA"  # 沙特阿拉伯
    SE = "SE"  # 瑞典
    SG = "SG"  # 新加坡
    TR = "TR"  # 土耳其
    US = "US"  # 美国
    ZA = "ZA"  # 南非


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


class SPBidStrategy(str, Enum):
    MANUAL = "MANUAL"  # 使用您设定的确切出价和任何排名调整，不受动态竞价的影响
    RULE_BASED = "RULE_BASED"  # 基于规则
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"  # 只向下调整
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"  # 实时调整出价，最大增减幅度为 100%。启用此设置后，当广告更有可能转化为销售时，出价会增加；当转化可能性较低时，出价会降低。


class SPGlobalBidStrategy(str, Enum):
    MANUAL = "MANUAL"  # 使用您设定的确切出价和任何排名调整，不受动态竞价的影响
    RULE_BASED = "RULE_BASED"  # 基于规则
    SALES_DOWN_ONLY = "SALES_DOWN_ONLY"  # 只向下调整
    SALES_UP_AND_DOWN = "SALES_UP_AND_DOWN"  # 实时调整出价，最大增减幅度为 100%。启用此设置后，当广告更有可能转化为销售时，出价会增加；当转化可能性较低时，出价会降低。


# region Placement 位置
class SPPlacement(str, Enum):
    PRODUCT_PAGE = "PRODUCT_PAGE"  # 产品页
    REST_OF_SEARCH = "REST_OF_SEARCH"  # 位于搜索结果首页中间或底部的广告位。也指位于搜索结果第二页及以后的广告位。
    SITE_AMAZON_BUSINESS = "SITE_AMAZON_BUSINESS"  # 亚马逊企业购网站广告位。
    TOP_OF_SEARCH = "TOP_OF_SEARCH"  # 在搜索结果首页顶部位置展示。


class SPGlobalPlacement(str, Enum):
    PRODUCT_PAGE = "PRODUCT_PAGE"  # 产品页
    REST_OF_SEARCH = "REST_OF_SEARCH"  # 位于搜索结果首页中间或底部的广告位。也指位于搜索结果第二页及以后的广告位。
    TOP_OF_SEARCH = "TOP_OF_SEARCH"  # 在搜索结果首页顶部位置展示。


# endregion


# region 亚马逊预算控制策略
class SPOffAmazonBudgetControlStrategy(str, Enum):
    """亚马逊预算控制策略"""

    MAXIMIZE_REACH = "MAXIMIZE_REACH"  # 最大搜索
    MINIMIZE_SPEND = "MINIMIZE_SPEND"  # 最小花费


# endregion


# region 网站限制
class SPSiteRestriction(str, Enum):
    """网站限制"""

    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # 企业购
    AMAZON_HAUL = "AMAZON_HAUL"


class SPGlobalSiteRestriction(str, Enum):
    AMAZON_BUSINESS = "AMAZON_BUSINESS"  # 企业购
    AMAZON_HAUL = "AMAZON_HAUL"


# endregion


# region SPState
class SPState(str, Enum):
    """活动状态"""

    ENABLED = "ENABLED"  # 活动
    PAUSED = "PAUSED"  # 暂停
    ARCHIVED = "ARCHIVED"  # 归档


class SPCreateState(str, Enum):
    ENABLED = "ENABLED"  # 活动
    PAUSED = "PAUSED"  # 暂停


class SPUpdateState(str, Enum):
    ENABLED = "ENABLED"  # 活动
    PAUSED = "PAUSED"  # 暂停


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


# endregion


# region SPDeliveryReason
class SPDeliveryReason(str, Enum):
    # --- 广告主级别 (ADVERTISER) ---
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"  # 广告主账号已归档
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"  # 广告主预算耗尽
    ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT = (
        "ADVERTISER_OUT_OF_POSTPAY_CREDIT_LIMIT"  # 超出后付费信用额度
    )
    ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET = (
        "ADVERTISER_OUT_OF_POSTPAY_MONTHLY_BUDGET"  # 超出后付费每月预算
    )
    ADVERTISER_OUT_OF_PREPAY_BALANCE = (
        "ADVERTISER_OUT_OF_PREPAY_BALANCE"  # 预付费余额不足
    )
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"  # 广告主账号已暂停
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"  # 支付失败
    ADVERTISER_POLICING_PENDING_REVIEW = (
        "ADVERTISER_POLICING_PENDING_REVIEW"  # 账号政策审核中
    )
    ADVERTISER_POLICING_SUSPENDED = (
        "ADVERTISER_POLICING_SUSPENDED"  # 账号因违反政策被停用
    )

    # --- 广告活动级别 (CAMPAIGN) ---
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"  # 广告活动已归档
    CAMPAIGN_END_DATE_REACHED = "CAMPAIGN_END_DATE_REACHED"  # 已到达广告活动结束日期
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"  # 广告活动设置不完整
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"  # 广告活动预算耗尽
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"  # 广告活动已暂停
    CAMPAIGN_PENDING_REVIEW = "CAMPAIGN_PENDING_REVIEW"  # 广告活动审核中
    CAMPAIGN_PENDING_START_DATE = (
        "CAMPAIGN_PENDING_START_DATE"  # 尚未到达广告活动开始日期
    )
    CAMPAIGN_REJECTED = "CAMPAIGN_REJECTED"  # 广告活动被拒绝

    # --- 广告组级别 (AD_GROUP) ---
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"  # 广告组已归档
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"  # 广告组不完整
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"  # 广告组出价过低
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"  # 广告组已暂停
    AD_GROUP_PENDING_REVIEW = "AD_GROUP_PENDING_REVIEW"  # 广告组审核中
    AD_GROUP_POLICING_PENDING_REVIEW = (
        "AD_GROUP_POLICING_PENDING_REVIEW"  # 广告组政策审核中
    )
    AD_GROUP_REJECTED = "AD_GROUP_REJECTED"  # 广告组被拒绝

    # --- 广告/创意级别 (AD / CREATIVE) ---
    AD_ARCHIVED = "AD_ARCHIVED"  # 广告已归档
    AD_PAUSED = "AD_PAUSED"  # 广告已暂停
    AD_INELIGIBLE = "AD_INELIGIBLE"  # 广告不符合投放资格
    AD_NOT_DELIVERING = "AD_NOT_DELIVERING"  # 广告未在投放
    AD_CREATION_FAILED = "AD_CREATION_FAILED"  # 广告创建失败
    AD_CREATION_IN_PROGRESS = "AD_CREATION_IN_PROGRESS"  # 广告创建中
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"  # 广告政策审核中
    AD_POLICING_SUSPENDED = "AD_POLICING_SUSPENDED"  # 广告因政策原因被暂停
    AD_MISSING_DECORATION = "AD_MISSING_DECORATION"  # 广告缺少装饰元素
    AD_MISSING_IMAGE = "AD_MISSING_IMAGE"  # 广告缺少图片
    CREATIVE_MISSING_ASSET = "CREATIVE_MISSING_ASSET"  # 创意缺少素材
    CREATIVE_PENDING_REVIEW = "CREATIVE_PENDING_REVIEW"  # 创意审核中
    CREATIVE_REJECTED = "CREATIVE_REJECTED"  # 创意被拒绝

    # --- 广告扩展 (AD_EXTENSION) ---
    AD_EXTENSION_ARCHIVED = "AD_EXTENSION_ARCHIVED"  # 广告扩展已归档
    AD_EXTENSION_PAUSED = "AD_EXTENSION_PAUSED"  # 广告扩展已暂停
    AD_EXTENSION_POLICING_PENDING_REVIEW = (
        "AD_EXTENSION_POLICING_PENDING_REVIEW"  # 广告扩展政策审核中
    )
    AD_EXTENSION_POLICING_SUSPENDED = (
        "AD_EXTENSION_POLICING_SUSPENDED"  # 广告扩展因政策原因被暂停
    )

    # --- 投放目标级别 (TARGET) ---
    TARGET_ARCHIVED = "TARGET_ARCHIVED"  # 投放目标已归档
    TARGET_PAUSED = "TARGET_PAUSED"  # 投放目标已暂停
    TARGET_BLOCKED = "TARGET_BLOCKED"  # 投放目标被封锁
    TARGET_POLICING_SUSPENDED = "TARGET_POLICING_SUSPENDED"  # 投放目标因政策原因被暂停

    # --- 产品/页面/库存状态 (PRODUCT / INVENTORY) ---
    BRAND_INELIGIBLE = "BRAND_INELIGIBLE"  # 品牌不符合资格
    LANDING_PAGE_INELIGIBLE = "LANDING_PAGE_INELIGIBLE"  # 落地页不符合资格
    LANDING_PAGE_NOT_AVAILABLE = "LANDING_PAGE_NOT_AVAILABLE"  # 落地页无法访问
    NOT_BUYABLE = "NOT_BUYABLE"  # 产品不可购买
    NOT_IN_BUYBOX = "NOT_IN_BUYBOX"  # 产品不在黄金购物车 (Buybox)
    NOT_IN_POLICY = "NOT_IN_POLICY"  # 不符合政策
    NO_INVENTORY = "NO_INVENTORY"  # 无库存
    OUT_OF_STOCK = "OUT_OF_STOCK"  # 缺货
    NO_PURCHASABLE_OFFER = "NO_PURCHASABLE_OFFER"  # 没有可购买的报价

    # --- 政策审核与合规 (MODERATION / POLICY) ---
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
        "MODERATION_CRITICAL_EVENTS_POLICY_VIOLATION"  # 违反重大事件政策
    )
    MODERATION_ERROR_404 = "MODERATION_ERROR_404"  # 审核时落地页 404
    MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION = (
        "MODERATION_GRAPHICAL_SEXUAL_IMAGES_POLICY_VIOLATION"  # 违反性暗示图像政策
    )
    MODERATION_HFSS_PRODUCT_POLICY_VIOLATION = (
        "MODERATION_HFSS_PRODUCT_POLICY_VIOLATION"  # 违反高油盐糖食品政策
    )
    MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION = (
        "MODERATION_LANGUAGE_OFFENSIVE_POLICY_VIOLATION"  # 违反冒犯性语言政策
    )
    MODERATION_NOT_COMPLIANT_TO_AD_POLICY = (
        "MODERATION_NOT_COMPLIANT_TO_AD_POLICY"  # 不符合广告通用政策
    )
    MODERATION_SMOKING_RELATED_POLICY_VIOLATION = (
        "MODERATION_SMOKING_RELATED_POLICY_VIOLATION"  # 违反吸烟相关政策
    )

    # --- 组合/其他 (PORTFOLIO / OTHER) ---
    PORTFOLIO_ARCHIVED = "PORTFOLIO_ARCHIVED"  # 广告组合已归档
    PORTFOLIO_END_DATE_REACHED = "PORTFOLIO_END_DATE_REACHED"  # 广告组合已过期
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"  # 广告组合预算耗尽
    PORTFOLIO_PAUSED = "PORTFOLIO_PAUSED"  # 广告组合已暂停
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"  # 广告组合尚未开始
    SECURITY_SCAN_PENDING_REVIEW = "SECURITY_SCAN_PENDING_REVIEW"  # 安全扫描审核中
    SECURITY_SCAN_REJECTED = "SECURITY_SCAN_REJECTED"  # 安全扫描未通过
    SPEND_LIMIT_EXCEEDED = "SPEND_LIMIT_EXCEEDED"  # 超出支出限制
    PIR_RULE_EXCLUDED = "PIR_RULE_EXCLUDED"  # 被 PIR 规则排除
    OUT_OF_REWARD_BUDGET = "OUT_OF_REWARD_BUDGET"  # 奖励预算耗尽
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"  # 状态不可用
    OTHER = "OTHER"  # 其他状态


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


# region ErrorCode
class ErrorCode(str, Enum):
    # --- 基础 HTTP/系统级别 ---
    BAD_REQUEST = "BAD_REQUEST"  # 请求格式错误或无效
    UNAUTHORIZED = "UNAUTHORIZED"  # 身份认证失败（Token 无效或过期）
    FORBIDDEN = "FORBIDDEN"  # 权限不足（无权访问该资源或账号）
    NOT_FOUND = "NOT_FOUND"  # 找不到请求的路径或资源
    CONFLICT = "CONFLICT"  # 资源状态冲突
    INTERNAL_ERROR = "INTERNAL_ERROR"  # 亚马逊服务器内部错误
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # 触发频率限制 (429 Rate Limit)
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # 请求体过大
    ACTION_NOT_SUPPORTED = "ACTION_NOT_SUPPORTED"  # 不支持该操作
    FEATURE_DISCONTINUED = "FEATURE_DISCONTINUED"  # 该功能已停用
    UNSUPPORTED_MARKETPLACE = "UNSUPPORTED_MARKETPLACE"  # 不支持该站点（Marketplace）

    # --- 资源 ID 与 归属问题 ---
    RESOURCE_ID_NOT_FOUND = "RESOURCE_ID_NOT_FOUND"  # 找不到指定的资源 ID
    RESOURCE_DOES_NOT_BELONG_TO_PARENT = (
        "RESOURCE_DOES_NOT_BELONG_TO_PARENT"  # 资源不属于所提供的父级 ID
    )
    RESOURCE_IS_EMPTY = "RESOURCE_IS_EMPTY"  # 资源为空
    RESOURCE_IS_NULL = "RESOURCE_IS_NULL"  # 资源为 Null
    RESOURCE_IS_IN_TERMINAL_STATE = (
        "RESOURCE_IS_IN_TERMINAL_STATE"  # 资源处于终态（如已归档），不可操作
    )
    FIELD_VALUE_NOT_FOUND = "FIELD_VALUE_NOT_FOUND"  # 字段值未找到
    DUPLICATE_RESOURCE_ID_FOUND = "DUPLICATE_RESOURCE_ID_FOUND"  # 发现重复的资源 ID

    # --- 字段/格式验证 ---
    FIELD_VALUE_IS_INVALID = "FIELD_VALUE_IS_INVALID"  # 字段值无效
    FIELD_VALUE_IS_NULL = "FIELD_VALUE_IS_NULL"  # 字段值不能为空
    FIELD_VALUE_IS_EMPTY = "FIELD_VALUE_IS_EMPTY"  # 字段值为空
    FIELD_VALUE_NOT_UNIQUE = "FIELD_VALUE_NOT_UNIQUE"  # 字段值不唯一
    FIELD_VALUE_MISMATCH = "FIELD_VALUE_MISMATCH"  # 字段值不匹配
    FIELD_VALUE_MUST_BE_EMPTY_OR_NULL = (
        "FIELD_VALUE_MUST_BE_EMPTY_OR_NULL"  # 字段值必须为空或 Null
    )
    FIELD_VALUE_CANNOT_EDIT = "FIELD_VALUE_CANNOT_EDIT"  # 该字段值不可编辑
    DUPLICATE_FIELD_VALUE_FOUND = "DUPLICATE_FIELD_VALUE_FOUND"  # 发现重复的字段值
    FIELD_VALUE_CONTAINS_INVALID_CHARACTERS = (
        "FIELD_VALUE_CONTAINS_INVALID_CHARACTERS"  # 包含无效字符
    )
    FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS = (
        "FIELD_VALUE_CONTAINS_BLOCKLISTED_WORDS"  # 包含黑名单违禁词
    )

    # --- 范围与限制 (Limits) ---
    FIELD_VALUE_IS_OUT_OF_RANGE = "FIELD_VALUE_IS_OUT_OF_RANGE"  # 字段值超出允许范围
    FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_VALUE_IS_ABOVE_MAXIMUM_LIMIT"  # 字段值高于最大上限
    )
    FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_VALUE_IS_BELOW_MINIMUM_LIMIT"  # 字段值低于最小下限
    )
    FIELD_SIZE_IS_OUT_OF_RANGE = "FIELD_SIZE_IS_OUT_OF_RANGE"  # 字段长度/大小超出范围
    FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT = (
        "FIELD_SIZE_IS_ABOVE_MAXIMUM_LIMIT"  # 字段长度超过最大值
    )
    FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT = (
        "FIELD_SIZE_IS_BELOW_MINIMUM_LIMIT"  # 字段长度低于最小值
    )
    TOTAL_RESOURCE_LIMIT_EXCEEDED = (
        "TOTAL_RESOURCE_LIMIT_EXCEEDED"  # 超出总资源配额限制
    )
    ACTIVE_RESOURCE_LIMIT_EXCEEDED = (
        "ACTIVE_RESOURCE_LIMIT_EXCEEDED"  # 超出活动资源配额限制
    )
    GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT = (
        "GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT"  # 触发单个广告活动下广告组的数量限制
    )

    # --- 时间与日期 ---
    DATE_CANNOT_BE_IN_PAST = "DATE_CANNOT_BE_IN_PAST"  # 日期不能是过去的时间
    DATE_CANNOT_BE_NULL = "DATE_CANNOT_BE_NULL"  # 日期不能为空
    DATE_TOO_SOON = "DATE_TOO_SOON"  # 日期设置得太早（不符合最小提前量要求）
    DURATION_TOO_SHORT = "DURATION_TOO_SHORT"  # 持续时间太短

    # --- 父级与资源状态约束 ---
    ARCHIVED_PARENT_CANNOT_CREATE = (
        "ARCHIVED_PARENT_CANNOT_CREATE"  # 父级已归档，无法创建子项
    )
    ARCHIVED_PARENT_CANNOT_EDIT = "ARCHIVED_PARENT_CANNOT_EDIT"  # 父级已归档，无法编辑
    ARCHIVED_RESOURCE_CANNOT_EDIT = (
        "ARCHIVED_RESOURCE_CANNOT_EDIT"  # 资源已归档，无法编辑
    )
    AUTOCREATED_ENTITY_CANNOT_EDIT = (
        "AUTOCREATED_ENTITY_CANNOT_EDIT"  # 自动创建的实体不可编辑
    )

    # --- 业务逻辑与账号限制 ---
    PAYMENT_ISSUE = "PAYMENT_ISSUE"  # 支付账户问题
    PRODUCT_INELIGIBLE = "PRODUCT_INELIGIBLE"  # 产品不符合资格
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO = (
        "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO"  # 受组合限制，无法更新全局属性
    )
    GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE = (
        "GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE"  # 受状态限制，无法更新全局属性
    )


# endregion


# region SPAdGroupStateFilter
class SPAdGroupStateFilter(str, Enum):
    """
    AdGroup 状态
    """

    ENABLED = "ENABLED"  # 启用
    PAUSED = "PAUSED"  # 暂停
    ARCHIVED = "ARCHIVED"  # 归档


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


class AdProduct(str, Enum):
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"
    AMAZON_DSP = "AMAZON_DSP"


class MatchType(str, Enum):
    # --- 传统关键词匹配 (Keyword Match Types) ---
    BROAD = "BROAD"  # 广泛匹配：包含关键词、同义词或相关词汇
    PHRASE = "PHRASE"  # 短语匹配：包含精确短语或其紧密变体
    EXACT = "EXACT"  # 精确匹配：必须与搜索词完全一致（含单复数变体）

    # --- 自动投放策略 (SP Auto Targeting Groups) ---
    KEYWORDS_CLOSE_MATCH = (
        "KEYWORDS_CLOSE_MATCH"  # 紧密匹配：买家使用与商品高度相关的搜索词
    )
    KEYWORDS_LOOSE_MATCH = (
        "KEYWORDS_LOOSE_MATCH"  # 宽泛匹配：买家使用与商品相关度较低的搜索词
    )
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"  # 代替品：买家查看与您商品类似的详情页
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"  # 互补品：买家查看与您商品配套的详情页

    # --- 商品与类目投放 (Product Targeting) ---
    PRODUCT_EXACT = "PRODUCT_EXACT"  # 精确商品投放：针对特定的 ASIN 进行投放
    PRODUCT_SIMILAR = "PRODUCT_SIMILAR"  # 相似商品：针对与广告商品相似的商品进行投放

    # --- 展示型推广与再营销 (SD Targeting & Remarketing) ---
    INTERESTED_AUDIENCE = "INTERESTED_AUDIENCE"  # 兴趣受众：基于买家长期浏览兴趣的投放
    PRODUCT_REMARKETING = (
        "PRODUCT_REMARKETING"  # 商品再营销：针对看过您商品或类似商品的买家
    )
    PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS = "PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS"  # 类似广告商品的商品（常用于SD上下文投放）

    # --- 品牌推广与 AI/动态建议策略 (SB/SD Dynamic/Themed Keywords) ---
    KEYWORDS_RELATED_TO_YOUR_BRAND = (
        "KEYWORDS_RELATED_TO_YOUR_BRAND"  # 品牌相关词：与您品牌相关的关键词
    )
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"  # 类目相关词：与您产品类目相关的关键词
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = (
        "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"  # 竞品类目相关词
    )
    KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES = "KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES"  # 落地页相关词：基于您设定的落地页生成的词

    # --- 季节性与特殊策略 (Seasonal & Advanced) ---
    KEYWORDS_RELATED_TO_GIFTS = (
        "KEYWORDS_RELATED_TO_GIFTS"  # 礼品相关词：针对礼品属性搜索的词
    )
    KEYWORDS_RELATED_TO_PRIME_DAY = (
        "KEYWORDS_RELATED_TO_PRIME_DAY"  # Prime Day 相关词：大促期间的特定投放
    )
    MULTISIGNAL_BROAD = (
        "MULTISIGNAL_BROAD"  # 多信号广泛匹配：结合多种用户行为信号的增强型广泛投放
    )


class SPTargetType(str, Enum):
    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    LOCATION = "LOCATION"
    THEME = "THEME"


class SPThemeMatchType(str, Enum):
    KEYWORDS_CLOSE_MATCH = "KEYWORDS_CLOSE_MATCH"
    KEYWORDS_LOOSE_MATCH = "KEYWORDS_LOOSE_MATCH"
    KEYWORDS_RELATED_TO_GIFTS = "KEYWORDS_RELATED_TO_GIFTS"
    KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY = (
        "KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY"
    )
    KEYWORDS_RELATED_TO_PRIME_DAY = "KEYWORDS_RELATED_TO_PRIME_DAY"
    KEYWORDS_RELATED_TO_YOUR_BRAND = "KEYWORDS_RELATED_TO_YOUR_BRAND"
    KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY = (
        "KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY"
    )
    PRODUCT_COMPLEMENTS = "PRODUCT_COMPLEMENTS"
    PRODUCT_SUBSTITUTES = "PRODUCT_SUBSTITUTES"
