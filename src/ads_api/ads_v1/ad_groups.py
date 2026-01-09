from typing import Optional
import pydantic
from returns.result import Failure, Success, Result
from ads_api.ads_v1.enums import SPAdGroupStateFilter
from ads_api.base import BaseWithProfileId, CamelCaseBaseModel
from typing_extensions import Literal
from .ad_groups_type import (
    SPAdGroup,
    SPAdGroupCreate,
    SPAdGroupMultiStatusSuccess,
    SPAdGroupUpdate,
)
from .common_type import ErrorsIndex


class AdGroupsApi(BaseWithProfileId):
    async def query(
        self, filter: "ListAdGroupFiler", next_token: Optional[str] = None
    ) -> Result["ListAdGroupsResponse", Exception]:
        body = filter.to_body(next_token)
        try:
            response = await self.client.post("/adsApi/v1/query/adGroups", json=body)
            response_data = response.json()
            return Success(ListAdGroupsResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def create(
        self, ad_groups: list[SPAdGroupCreate]
    ) -> Result["OperationAdGroupResponse", Exception]:
        body = {
            "adGroups": [
                item.dict(exclude_none=True, by_alias=True) for item in ad_groups
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/create/adGroups", json=body)
            response_data = response.json()
            return Success(OperationAdGroupResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def delete(
        self, ad_group_ids: list[str]
    ) -> Result["OperationAdGroupResponse", Exception]:
        body = {"adGroupIds": ad_group_ids}
        try:
            response = await self.client.post("/adsApi/v1/delete/adGroups", json=body)
            response_data = response.json()
            return Success(OperationAdGroupResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def update(
        self, ad_groups: list[SPAdGroupUpdate]
    ) -> Result["OperationAdGroupResponse", Exception]:
        body = {
            "adGroups": [
                item.dict(exclude_none=True, by_alias=True) for item in ad_groups
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/update/adGroups", json=body)
            response_data = response.json()
            return Success(OperationAdGroupResponse(**response_data))
        except Exception as e:
            return Failure(e)


# region ListAdGroupFilter
class ListAdGroupFiler(CamelCaseBaseModel):
    ad_group_id_filter: Optional[list[str]] = None
    ad_product_filter: list[Literal["SPONSORED_PRODUCTS"]] = ["SPONSORED_PRODUCTS"]
    campaign_id_filter: Optional[list[str]] = None
    max_results: int = 1000
    name_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    name_filter_query_term_match_type: Optional[
        Literal["EXACT_MATCH", "BROAD_MATCH"]
    ] = pydantic.Field(default=None, exclude=True)
    state_filter: Optional[list[SPAdGroupStateFilter]] = pydantic.Field(
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


# region ListAdGroupsResponse
class ListAdGroupsResponse(CamelCaseBaseModel):
    ad_groups: Optional[list[SPAdGroup]] = None
    next_token: Optional[str] = None


# endregion


# region OperationCampaignResponse
class OperationAdGroupResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]] = None
    success: Optional[list[SPAdGroupMultiStatusSuccess]] = None


# endregion
