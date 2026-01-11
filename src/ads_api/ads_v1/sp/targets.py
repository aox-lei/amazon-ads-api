from typing import Optional
from returns.result import Failure, Success, Result
from ads_api.base import BaseWithProfileId, CamelCaseBaseModel
from typing_extensions import Literal
import pydantic
from .types.enums import MatchType, SPTargetType
from .types.targets import (
    SPTarget,
    SPTargetCreate,
    SPTargetMultiStatusSuccess,
    SPTargetUpdate,
)
from .types.common import ErrorsIndex


class TargetApi(BaseWithProfileId):
    async def query(
        self,
        filter: "ListTargetFilter",
        next_token: Optional[str] = None,
    ) -> Result["ListTargetResponse", Exception]:
        body = filter.to_body(next_token)
        try:
            response = await self.client.post("/adsApi/v1/query/targets", json=body)
            response_data = response.json()
            return Success(ListTargetResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def create(
        self, targets: list[SPTargetCreate]
    ) -> Result["OperationTargetResponse", Exception]:
        body = {
            "campaigns": [
                item.dict(exclude_none=True, by_alias=True) for item in targets
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/create/targets", json=body)
            response_data = response.json()
            return Success(OperationTargetResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def delete(
        self, target_ids: list[str]
    ) -> Result["OperationTargetResponse", Exception]:
        body = {"targetIds": target_ids}
        try:
            response = await self.client.post("/adsApi/v1/delete/targets", json=body)
            response_data = response.json()
            return Success(OperationTargetResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def update(
        self, targets: list[SPTargetUpdate]
    ) -> Result["OperationTargetResponse", Exception]:
        body = {
            "campaigns": [
                item.dict(exclude_none=True, by_alias=True) for item in targets
            ]
        }
        try:
            response = await self.client.post("/adsApi/v1/update/targets", json=body)
            response_data = response.json()
            return Success(OperationTargetResponse(**response_data))
        except Exception as e:
            return Failure(e)


class ListTargetFilter(CamelCaseBaseModel):
    ad_group_filter: Optional[list[str]] = None
    ad_product_filter: list[Literal["SPONSORED_PRODUCTS"]] = ["SPONSORED_PRODUCTS"]
    campaign_id_filter: Optional[list[str]] = None
    keyword_filter: Optional[list[str]] = None
    keyword_filter_query_term_match_type: Optional[
        Literal["EXACT_MATCH", "BROAD_MATCH"]
    ] = None
    match_type_filter: Optional[list[MatchType]] = None
    max_results: Optional[int] = pydantic.Field(default=None, lt=1, gt=5000)
    negative_filter: Optional[list[bool]] = None
    product_id_filter: Optional[list[str]] = None
    product_id_filter_query_term_match_type: Optional[
        Literal["EXACT_MATCH", "BROAD_MATCH"]
    ] = None
    state_filter: Optional[list[Literal["ENABLED", "PAUSED", "ARCHIVED"]]] = None
    target_id_filter: Optional[list[str]] = None
    target_type_filter: Optional[list[SPTargetType]] = None

    def to_body(self, next_token: Optional[str] = None):
        body = self.dict(exclude_none=True, by_alias=True)
        if self.ad_group_filter is not None:
            body["adGroupFilter"] = {"include": self.ad_group_filter}
        if self.campaign_id_filter is not None:
            body["campaignIdFilter"] = {"include": self.campaign_id_filter}
        if self.keyword_filter is not None:
            body["nameFilter"] = {
                "include": self.keyword_filter,
                "queryTermMatchType": self.keyword_filter_query_term_match_type,
            }
        if self.match_type_filter is not None:
            body["matchTypeFilter"] = {"include": self.match_type_filter}

        if self.negative_filter is not None:
            body["negativeFilter"] = {"include": self.negative_filter}
        if self.product_id_filter is not None:
            body["productIdFilter"] = {
                "include": self.product_id_filter,
                "query_term_match_type": self.product_id_filter_query_term_match_type,
            }
        if self.state_filter is not None:
            body["stateFilter"] = {"include": self.state_filter}
        if next_token is not None:
            body["nextToken"] = next_token
        if self.target_id_filter is not None:
            body["targetIdFilter"] = {"include": self.target_id_filter}
        if self.target_type_filter is not None:
            body["targetTypeFilter"] = {"include": self.target_type_filter}

        return body


class ListTargetResponse(CamelCaseBaseModel):
    targets: Optional[list[SPTarget]] = None
    next_token: Optional[str] = None


# region OperationCampaign Response
class OperationTargetResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]] = None
    success: Optional[list[SPTargetMultiStatusSuccess]] = None


# endregion
