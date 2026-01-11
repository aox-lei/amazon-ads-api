from typing import Optional
from ads_api.base import CamelCaseBaseModel


class KeywordGroup(CamelCaseBaseModel):
    description: Optional[str] = None
    id: str
    impact_summary: Optional[str] = None
    sample_keywords: Optional[list[str]] = None
    text: str
