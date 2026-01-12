from httpx import Response
import pydantic
from ads_api.base import BaseWithProfileId, CamelCaseBaseModel
from typing import Any, Optional
from .base import handle_api_errors
from returns.result import Failure, Success, Result
from .types.enums import AdProduct, Locale, TargetType
from .types.targetable_entities import TargetableEntity

__all__=["TargetableEntitiesApi", "ListTargetableEntitiesFilter"]

class TargetableEntitiesApi(BaseWithProfileId):
    @handle_api_errors
    async def query(
        self, filter: "ListTargetableEntitiesFilter", next_token: Optional[str] = None
    ) -> Result["ListTargetableEntitiesResponse", Response]:
        body = filter.to_body(next_token)
        response = await self.client.post("/targetableEntities/list", json=body)
        response_data = response.json()
        if response.is_success:
            return Success(ListTargetableEntitiesResponse(**response_data))
        return Failure(response)


class ListTargetableEntitiesFilter(CamelCaseBaseModel):
    ad_product: AdProduct
    local: Optional[Locale] = None
    max_results: Optional[int] = pydantic.Field(default=None, lt=1, gt=250)
    paths_filter: Optional[str] = None
    search_query_filter: Optional[str] = None
    target_type_filter: Optional[TargetType] = None

    def to_body(self, next_token: Optional[str] = None) -> dict[str, Any]:
        body = self.dict(exclude_none=True, by_alias=True)
        body["nextToken"] = next_token
        return body


# region ListTargetableEntitiesResponse
class ListTargetableEntitiesResponse(CamelCaseBaseModel):
    next_token: Optional[str] = None
    targetable_entities: Optional[list[TargetableEntity]] = None
    total_results: Optional[int] = None


# endregion
