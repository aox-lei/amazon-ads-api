from enum import Enum


# region 区域
class Region(str, Enum):
    NA = "NA"  # 北美
    EU = "EU"  # 欧洲
    FE = "FE"  # 远东


# endregion


# region 国家代码
class CountryCode(str, Enum):
    US = "US"  # 美国
    CA = "CA"  # 加拿大
    DE = "DE"  # 德国
    FR = "FR"  # 法兰
    IT = "IT"  # 意大利
    ES = "ES"  # 西班牙
    JP = "JP"  # 日本
    UK = "UK"  # 英格兰
    AU = "AU"  # 澳大利亚
    BR = "BR"  # 巴西
    MX = "MX"  # 墨西哥
    AE = "AE"  # 阿联酋
    BE = "BE"  # 比利时
    EG = "EG"  # 埃及
    IE = "IE"  # 爱尔兰
    IN = "IN"  # 印度
    NL = "NL"  # 荷兰
    PL = "PL"  # 波兰
    SA = "SA"  # 沙特阿拉伯
    SE = "SE"  # 瑞典
    TR = "TR"  # 土耳其
    SG = "SG"  # 新加坡
    ZA = "ZA"  # 南非


# endregion


# region 货币代码
class CurrencyCode(str, Enum):
    BRL = "BRL"  # 巴西雷亚尔
    CAD = "CAD"  # 加拿大元
    MXN = "MXN"  # 墨西哥比索
    USD = "USD"  # 美元
    AED = "AED"  # 阿联酋迪拉姆
    EUR = "EUR"  # 欧元
    EGP = "EGP"  # 埃及镑
    INR = "INR"  # 印度卢比
    PLN = "PLN"  # 波兰兹罗提
    SAR = "SAR"  # 沙特里亚尔
    SEK = "SEK"  # 瑞典克朗
    TRY = "TRY"  # 土耳其里拉
    GBP = "GBP"  # 英镑
    AUD = "AUD"  # 澳大利亚元
    JPY = "JPY"  # 日元
    SGD = "SGD"  # 新加坡元


# endregion


# region 时区
class TimeZone(str, Enum):
    AFRICA_CAIRO = "Africa/Cairo"  # 非洲/开罗
    AMERICA_SAO_PAULO = "America/Sao_Paulo"  # 美洲/圣保罗
    AMERICA_LOS_ANGELES = "America/Los_Angeles"  # 美洲/洛杉矶
    ASIA_DUBAI = "Asia/Dubai"  # 亚洲/迪拜
    ASIA_KOLKATA = "Asia/Kolkata"  # 亚洲/加尔各答
    ASIA_RIYADH = "Asia/Riyadh"  # 亚洲/利雅得
    ASIA_SINGAPORE = "Asia/Singapore"  # 亚洲/新加坡
    ASIA_TOKYO = "Asia/Tokyo"  # 亚洲/东京
    AUSTRALIA_SYDNEY = "Australia/Sydney"  # 澳洲/悉尼
    EUROPE_AMSTERDAM = "Europe/Amsterdam"  # 欧洲/阿姆斯特丹
    EUROPE_DUBLIN = "Europe/Dublin"  # 欧洲/都柏林
    EUROPE_ISTANBUL = "Europe/Istanbul"  # 欧洲/伊斯坦布尔
    EUROPE_LONDON = "Europe/London"  # 欧洲/伦敦
    EUROPE_PARIS = "Europe/Paris"  # 欧洲/巴黎
    EUROPE_STOCKHOLM = "Europe/Stockholm"  # 欧洲/斯德哥尔摩
    EUROPE_WARSAW = "Europe/Warsaw"  # 欧洲/华沙
    EUROPE_BRUSSELS = "Europe/Brussels"  # 欧洲/布鲁塞尔
    AFRICA_JOHANNESBURG = "Africa/Johannesburg"  # 非洲/约翰内斯堡


# endregion
