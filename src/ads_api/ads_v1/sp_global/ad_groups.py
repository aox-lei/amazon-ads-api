from typing import Optional
import pydantic
from typing_extensions import Literal
from types.common import ErrorsIndex
from ads_api.base import BaseWithAccountId, CamelCaseBaseModel
from returns.result import Result, Success, Failure
from .types.enums import SPGlobalAdGroupStateFilter
from .types.ad_groups import (
    SPGlobalAdGroup,
    SPGlobalAdGroupCreate,
    SPGlobalAdGroupPartialIndex,
    SPGlobalAdGroupMultiStatusSuccess,
    SPGlobalAdGroupUpdate
)
from ads_api.ads_v1.base import handle_api_errors
from httpx import Response


class AdGroupsGlobalApi(BaseWithAccountId):
    @handle_api_errors
    async def query(
        self, filter: "ListGlobalAdGroupFilter", next_token: Optional[str] = None
    ) -> Result["ListGlobalAdGroupsGlobalResponse", Response]:
        body = filter.to_body(next_token)
        response = await self.client.post("/adsApi/v1/query/adGroups", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(ListGlobalAdGroupsGlobalResponse(**response_data))
        return Failure(response)
        

    @handle_api_errors
    async def create(
        self, ad_groups: list[SPGlobalAdGroupCreate]
    ) -> Result["OperationGlobalAdGroupResponse", Response]:
        body = {
            "adGroups": [
                item.dict(exclude_none=True, by_alias=True) for item in ad_groups
            ]
        }
        response = await self.client.post("/adsApi/v1/create/adGroups", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationGlobalAdGroupResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def delete(
        self, ad_group_ids: list[str]
    ) -> Result["OperationGlobalAdGroupResponse", Response]:
        body = {"adGroupIds": ad_group_ids}
        response = await self.client.post("/adsApi/v1/delete/adGroups", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationGlobalAdGroupResponse(**response_data))
        return Failure(response)


    @handle_api_errors
    async def update(
        self, ad_groups: list[SPGlobalAdGroupUpdate]
    ) -> Result["OperationGlobalAdGroupResponse", Response]:
        body = {
            "adGroups": [
                item.dict(exclude_none=True, by_alias=True) for item in ad_groups
            ]
        }
        response = await self.client.post("/adsApi/v1/update/adGroups", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationGlobalAdGroupResponse(**response_data))
        return Failure(response)


# region ListGlobalAdGroupFilter
class ListGlobalAdGroupFilter(CamelCaseBaseModel):
    ad_product_filter: list[Literal["SPONSORED_PRODUCTS"]] = ["SPONSORED_PRODUCTS"]
    campaign_id_filter: Optional[list[str]] = None
    marketplace_scope_filter: Optional[list[Literal["GLOBAL"]]] = None
    max_results: int = 1000
    name_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    name_filter_query_term_match_type: Optional[
        Literal["EXACT_MATCH", "BROAD_MATCH"]
    ] = pydantic.Field(default=None, exclude=True)
    state_filter: Optional[list[SPGlobalAdGroupStateFilter]] = pydantic.Field(
        default=None, min_items=0, max_items=3
    )

    def to_body(self, next_token: Optional[str] = None):
        body = self.dict(exclude_none=True, by_alias=True)
        body["adProductFilter"] = {"include": self.ad_product_filter}

        if self.campaign_id_filter is not None:
            body["campaignIdFilter"] = {"include": self.campaign_id_filter}
        if self.name_filter is not None:
            body["nameFilter"] = {
                "include": self.name_filter,
                "queryTermMatchType": self.name_filter_query_term_match_type,
            }
        if self.state_filter is not None:
            body["stateFilter"] = {"include": self.state_filter}
        if next_token is not None:
            body["nextToken"] = next_token

        return body


# endregion


# region ListGlobalAdGroupsGlobalResponse
class ListGlobalAdGroupsGlobalResponse(CamelCaseBaseModel):
    ad_groups: Optional[list[SPGlobalAdGroup]] = None
    next_token: Optional[str] = None


# endregion


# region OperationGlobalAdGroupResponse
class OperationGlobalAdGroupResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]] = None
    partial_success: Optional[list[SPGlobalAdGroupPartialIndex]] = None
    success: Optional[list[SPGlobalAdGroupMultiStatusSuccess]] = None


# endregion
