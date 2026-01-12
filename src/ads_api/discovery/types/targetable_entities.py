from ads_api.base import CamelCaseBaseModel
from typing import Optional
from .enums import TargetType


class TargetableEntity(CamelCaseBaseModel):
    audience_id: Optional[str] = None
    audience_resolved: Optional[str] = None  # audience_id的解析名称
    audience_tooltip: Optional[str] = None  # audience_id的提示信息
    content_category_id: Optional[str] = None  # 类型目标的标识符
    content_category_resolved: Optional[str] = None  # content_category_id的解析名称
    path: list[str]  # 目标实体在亚马逊分类体系中的位置。
    product_category_id: Optional[str] = (
        None  # PRODUCT_CATEGORY 或者 PRODUCT_CATEGORY_AUDIENCE
    )
    product_category_resolved: Optional[str] = None  # product_category_id的解析名称
    target_type: TargetType
