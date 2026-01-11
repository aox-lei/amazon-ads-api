from typing import Optional

from returns.result import Failure, Success, Result
from .types.campaigns_type import (
    SPCampaign,
    SPCampaignCreate,
    SPCampaignMultiStatusSuccess,
    SPCampaignUpdate,
)
from ads_api.base import BaseWithProfileId, CamelCaseBaseModel
from typing_extensions import Literal
from .types.common_type import ErrorsIndex
import pydantic
from .types.enums import SPCampaignStateFilter

__all__ = ["CampaignApi", "ListCampaignFilter", "SPCampaignStateFilter"]


# region CampaignApi
class CampaignApi(BaseWithProfileId):
    async def query(
        self,
        filter: "ListCampaignFilter",
        next_token: Optional[str] = None,
    ) -> Result["ListCampaignResponse", Exception]:
        body = filter.to_body(next_token)
        try:
            response = await self.client.post("/adsApi/v1/query/campaigns", json=body)
            response_data = response.json()
            return Success(ListCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def create(
        self, campaigns: list[SPCampaignCreate]
    ) -> Result["OperationCampaignResponse", Exception]:
        body = {
            "campaigns": [
                item.dict(exclude_none=True, by_alias=True) for item in campaigns
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/create/campaigns", json=body)
            response_data = response.json()
            return Success(OperationCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def delete(
        self, campaign_ids: list[str]
    ) -> Result["OperationCampaignResponse", Exception]:
        body = {"campaignIds": campaign_ids}
        try:
            response = await self.client.post("/adsApi/v1/delete/campaigns", json=body)
            response_data = response.json()
            return Success(OperationCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def update(
        self, campaigns: list[SPCampaignUpdate]
    ) -> Result["OperationCampaignResponse", Exception]:
        body = {
            "campaigns": [
                item.dict(exclude_none=True, by_alias=True) for item in campaigns
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/update/campaigns", json=body)
            response_data = response.json()
            return Success(OperationCampaignResponse(**response_data))
        except Exception as e:
            return Failure(e)


# endregion


# region ListCampaginFilter
class ListCampaignFilter(CamelCaseBaseModel):
    ad_product_filter: Optional[list[Literal["SPONSORED_PRODUCTS"]]] = [
        "SPONSORED_PRODUCTS"
    ]
    campaign_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=1000
    )
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
    state_filter: Optional[list[SPCampaignStateFilter]] = pydantic.Field(
        default=None, min_items=0, max_items=3
    )

    def to_body(self, next_token: Optional[str] = None):
        body = self.dict(exclude_none=True, by_alias=True)
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


# region ListCampaign Response
class ListCampaignResponse(CamelCaseBaseModel):
    campaigns: Optional[list[SPCampaign]] = None
    next_token: Optional[str] = None


# endregion


# region OperationCampaign Response
class OperationCampaignResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]] = None
    success: Optional[list[SPCampaignMultiStatusSuccess]] = None


# endregion
