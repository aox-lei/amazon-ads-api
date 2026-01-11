import pydantic
from ads_api.base import CamelCaseBaseModel, BaseWithProfileId
from typing import Any, Optional, Union
from typing_extensions import Literal
from returns.result import Failure, Success, Result
from .types.keywords import KeywordGroup, SuggestedBid

__all__ = ["RecommendationApi", "KeywordForAsinFilter", "KeywordForAdGroupFilter"]


class RecommendationApi(BaseWithProfileId):
    """关键词推荐"""

    async def keyword_groups(
        self,
        asins: list[str],
        country_code: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> Result["KeywordGroupResponse", Exception]:

        body: dict[str, Any] = {
            "asins": asins,
        }
        if country_code:
            body["countryCode"] = country_code
        if next_token:
            body["nextToken"] = next_token

        try:
            response = await self.client.post(
                "/sp/targeting/recommendations/keywordGroups", json=body
            )
            response_data = response.json()
            return Success(KeywordGroupResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def keyword(
        self, filter: Union["KeywordForAsinFilter", "KeywordForAdGroupFilter"]
    ) -> Result[list["KeywordItemResponse"], Exception]:
        body = filter.dict(exclude_none=True, by_alias=True)
        try:
            response = await self.client.post(
                "/sp/targets/keywords/recommendations",
                json=body,
                headers={
                    "Content-Type": "application/vnd.spkeywordsrecommendation.v3+json"
                },
            )
            response_data = response.json()
            data = [KeywordItemResponse(**item) for item in response_data]
            return Success(data)
        except Exception as e:
            return Failure(e)


# region KeywordFilter
class KeywordTargetFilter(CamelCaseBaseModel):
    bid: Optional[float] = None
    keyword: Optional[str] = None
    match_type: Optional[Literal["BROAD", "EXACT", "PHRASE"]] = None
    user_selected_keyword: Optional[bool] = None


class KeywordFilterBase(CamelCaseBaseModel):
    targets: Optional[list[KeywordTargetFilter]] = None
    locale: Optional[str] = None
    max_recommendations: int = 200
    sort_dimension: Optional[Literal["CLICKS", "CONVERSIONS", "DEFAULT"]] = None


class KeywordForAsinFilter(KeywordFilterBase):
    asins: list[str] = pydantic.Field(default=..., max_items=50)
    recommendation_type: str = "KEYWORDS_FOR_ASINS"

    @classmethod
    def by_asins(cls, asins: list[str]):
        return cls(asins=asins)


class KeywordForAdGroupFilter(KeywordFilterBase):
    ad_group_id: str
    campaign_id: str
    recommendation_type: str = "KEYWORDS_FOR_ADGROUP"


# endregion


# region KeywordGroupResponse
class KeywordGroupResponse(CamelCaseBaseModel):
    """
    KeywordGroupResponse
    """

    country_code: Optional[str] = None
    keyword_groups: Optional[list[KeywordGroup]] = None
    next_token: Optional[str] = None


# endregion


# region KeywordResponse
class KeywordItemResponse(CamelCaseBaseModel):
    rank: Optional[int] = None
    suggested_bid: Optional[SuggestedBid] = None
    translation: Optional[str] = None
    bid: Optional[float] = None
    keyword: Optional[str] = None
    match_type: Optional[Literal["BROAD", "EXACT", "PHRASE"]] = None
    user_selected_keyword: Optional[bool] = None


# endregion
