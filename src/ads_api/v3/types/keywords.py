from typing import Optional
from ads_api.base import CamelCaseBaseModel


class KeywordGroup(CamelCaseBaseModel):
    description: Optional[str] = None
    id: str
    impact_summary: Optional[str] = None
    sample_keywords: Optional[list[str]] = None
    text: str


class SuggestedBid(CamelCaseBaseModel):
    bid_rec_id: Optional[str] = None
    range_end: Optional[float] = None
    range_start: Optional[float] = None
    suggested: Optional[float] = None
