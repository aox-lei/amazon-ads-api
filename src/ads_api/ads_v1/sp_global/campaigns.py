from typing import Optional
from typing_extensions import Literal
from ads_api.base import BaseWithAccountId, CamelCaseBaseModel
from .types.enums import SPGlobalCampaignStateFilter
import pydantic
from returns.result import Result, Failure, Success
from .types.campaigns import (
    SPGlobalCampaign,
    SPGlobalCampaignPartialIndex,
    SPGlobalCampaignMultiStatusSuccess,
    SPGlobalCampaignCreate,
    SPGlobalCampaignUpdate,
)
from .types.common import ErrorsIndex


class CampaginGlobalApi(BaseWithAccountId):
    async def query(
        self,
        filter: "ListGlobalCampaignFilter",
        next_token: Optional[str] = None,
    ) -> Result["ListGlobalCampaignResponse", Exception]:
        body = filter.to_body(next_token)
        try:
            response = await self.client.post("/adsApi/v1/query/campaigns", json=body)
            response_data = response.json()
            return Success(ListGlobalCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def create(
        self, campaigns: list["SPGlobalCampaignCreate"]
    ) -> Result["OperationGlobalCampaignResponse", Exception]:
        body = {
            "campaigns": [
                item.dict(exclude_none=True, by_alias=True) for item in campaigns
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/create/campaigns", json=body)
            response_data = response.json()
            return Success(OperationGlobalCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def delete(
        self, campaign_ids: list[str]
    ) -> Result["OperationGlobalCampaignResponse", Exception]:
        body = {"campaignIds": campaign_ids}
        try:
            response = await self.client.post("/adsApi/v1/delete/campaigns", json=body)
            response_data = response.json()
            return Success(OperationGlobalCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def update(
        self, campaigns: list[SPGlobalCampaignUpdate]
    ) -> Result["OperationGlobalCampaignResponse", Exception]:
        body = {
            "campaigns": [
                item.dict(exclude_none=True, by_alias=True) for item in campaigns
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/update/campaigns", json=body)
            response_data = response.json()
            return Success(OperationGlobalCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)


# region ListCampaginFilter
class ListGlobalCampaignFilter(CamelCaseBaseModel):
    ad_product_filter: Optional[list[Literal["SPONSORED_PRODUCTS"]]] = [
        "SPONSORED_PRODUCTS"
    ]
    campaign_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=1000
    )
    marketplaces_scope_filter: list[Literal["GLOBAL"]] = ["GLOBAL"]
    max_results: int = 1000
    name_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    name_filter_query_term_match_type: Optional[
        Literal["EXACT_MATCH", "BROAD_MATCH"]
    ] = pydantic.Field(default=None, exclude=True)
    protfolio_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    state_filter: Optional[list[SPGlobalCampaignStateFilter]] = pydantic.Field(
        default=None, min_items=0, max_items=3
    )

    def to_body(self, next_token: Optional[str] = None):
        body = self.dict(exclude_none=True, by_alias=True)
        body["marketplaceScopeFilter"] = {"include": self.marketplaces_scope_filter}
        if self.ad_product_filter is not None:
            body["adProductFilter"] = {"include": self.ad_product_filter}
        if self.campaign_id_filter is not None:
            body["campaignIdFilter"] = {"include": self.campaign_id_filter}
        if self.name_filter is not None:
            body["nameFilter"] = {
                "include": self.name_filter,
                "queryTermMatchType": self.name_filter_query_term_match_type,
            }
        if self.protfolio_id_filter is not None:
            body["portfolioIdFilter"] = {"include": self.protfolio_id_filter}
        if self.state_filter is not None:
            body["stateFilter"] = {"include": self.state_filter}
        if next_token is not None:
            body["nextToken"] = next_token

        return body


# endregion


# region ListGlobalCampaign Response
class ListGlobalCampaignResponse(CamelCaseBaseModel):
    campaigns: Optional[list[SPGlobalCampaign]] = None
    next_token: Optional[str] = None


# endregion


# region OperationGlobalCampaign Response
class OperationGlobalCampaignResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]] = None
    partial_success: Optional[list[SPGlobalCampaignPartialIndex]] = None
    success: Optional[list[SPGlobalCampaignMultiStatusSuccess]] = None


# endregion
