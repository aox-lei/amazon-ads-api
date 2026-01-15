from typing import Optional

from returns.result import Failure, Success, Result

from ads_api.base import BaseWithAccountId, CamelCaseBaseModel
import pydantic
from typing_extensions import Literal
from .types.enums import SPAdStateFilter
from .types.common import ErrorsIndex
from .types.ads import (
    SPGlobalAdPartialIndex,
    SPGlobalAdMultiStatusSuccess,
    SPGlobalAd,
    SPGlobalAdCreate,
    SPGlobalAdUpdate,
)
from ads_api.ads_v1.base import handle_api_errors
from httpx import Response


class AdsGlobalApi(BaseWithAccountId):

    @handle_api_errors
    async def query(
        self, filter: "ListGlobalAdFilter", next_token: Optional[str] = None
    ) -> Result["ListGlobalAdResponse", Response]:
        body = filter.to_body(next_token)
        response = await self.client.post("/adsApi/v1/query/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(ListGlobalAdResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def create(
        self, ads: list[SPGlobalAdCreate]
    ) -> Result["OperationGlobalAdResponse", Response]:
        body = {"ads": [item.dict(exclude_none=True, by_alias=True) for item in ads]}
        response = await self.client.post("/adsApi/v1/create/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationGlobalAdResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def delete(
        self, ad_ids: list[str]
    ) -> Result["OperationGlobalAdResponse", Response]:
        body = {"adIds": ad_ids}
        response = await self.client.post("/adsApi/v1/delete/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationGlobalAdResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def update(
        self, ads: list[SPGlobalAdUpdate]
    ) -> Result["OperationGlobalAdResponse", Response]:
        body = {"ads": [item.dict(exclude_none=True, by_alias=True) for item in ads]}
        response = await self.client.post("/adsApi/v1/update/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationGlobalAdResponse(**response_data))
        return Failure(response)


class ListGlobalAdFilter(CamelCaseBaseModel):
    ad_group_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    ad_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    ad_product_filter: list[Literal["SPONSORED_PRODUCTS"]] = ["SPONSORED_PRODUCTS"]
    marketplace_scope_filter: list[Literal["GLOBAL"]] = ["GLOBAL"]
    max_results: int = 1000
    state_filter: Optional[list[SPAdStateFilter]] = pydantic.Field(
        default=None, min_items=0, max_items=3
    )

    def to_body(self, next_token: Optional[str] = None):
        body = self.dict(exclude_none=True, by_alias=True)
        body["adProductFilter"] = {"include": self.ad_product_filter}
        body["marketplaceScopeFilter"] = {"include": self.marketplace_scope_filter}
        if self.ad_group_id_filter is not None:
            body["adGroupIdFilter"] = {"include": self.ad_group_id_filter}
        if self.ad_id_filter is not None:
            body["adIdFilter"] = {"include": self.ad_id_filter}
        if self.state_filter is not None:
            body["stateFilter"] = {"include": self.state_filter}
        if next_token is not None:
            body["nextToken"] = next_token

        return body


# region ListAdResponse
class ListGlobalAdResponse(CamelCaseBaseModel):
    ads: Optional[list[SPGlobalAd]] = None
    next_token: Optional[str] = None


# endregion


# region OperationAdResponse
class OperationGlobalAdResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]] = None
    partial_success: Optional[list[SPGlobalAdPartialIndex]] = None
    success: Optional[list[SPGlobalAdMultiStatusSuccess]] = None


# endregion
