from ads_api.base import CamelCaseBaseModel, BaseWithProfileId
from typing import Any, Optional
from returns.result import Failure, Success, Result
from types.keywords import KeywordGroup


class Recommendation(BaseWithProfileId):
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


# region KeywordGroupResponse
class KeywordGroupResponse(CamelCaseBaseModel):
    """
    KeywordGroupResponse
    """

    country_code: Optional[str] = None
    keyword_groups: Optional[list[KeywordGroup]] = None
    next_token: Optional[str] = None


# endregion
