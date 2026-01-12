from enum import Enum


class AdProduct(str, Enum):
    SPONSORED_BRANDS = "SPONSORED_BRANDS"
    SPONSORED_DISPLAY = "SPONSORED_DISPLAY"
    SPONSORED_PRODUCTS = "SPONSORED_PRODUCTS"
    SPONSORED_TELEVISION = "SPONSORED_TELEVISION"


class Locale(str, Enum):
    ar_AE = "ar_AE"
    de_DE = "de_DE"
    en_AE = "en_AE"
    en_AU = "en_AU"
    en_CA = "en_CA"
    en_GB = "en_GB"
    en_IN = "en_IN"
    en_SG = "en_SG"
    en_US = "en_US"
    en_ZA = "en_ZA"
    es_ES = "es_ES"
    es_MX = "es_MX"
    fr_CA = "fr_CA"
    fr_FR = "fr_FR"
    hi_IN = "hi_IN"
    it_IT = "it_IT"
    ja_JP = "ja_JP"
    ko_KR = "ko_KR"
    nl_NL = "nl_NL"
    pl_PL = "pl_PL"
    pt_BR = "pt_BR"
    sv_SE = "sv_SE"
    ta_IN = "ta_IN"
    th_TH = "th_TH"
    tr_TR = "tr_TR"
    vi_VN = "vi_VN"
    zh_CN = "zh_CN"


class TargetType(str, Enum):
    AUDIENCE = "AUDIENCE"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    PRODUCT_CATEGORY = "PRODUCT_CATEGORY"
    PRODUCT_CATEGORY_AUDIENCE = "PRODUCT_CATEGORY_AUDIENCE"
