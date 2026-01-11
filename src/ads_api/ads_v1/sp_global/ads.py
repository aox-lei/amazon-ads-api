from typing import Optional

from returns.result import Failure, Success, Result

from ads_api.base import BaseWithProfileId, CamelCaseBaseModel
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


class AdsGlobalApi(BaseWithProfileId):
    async def query(
        self, filter: "ListGlobalAdFilter", next_token: Optional[str] = None
    ) -> Result["ListGlobalAdResponse", Exception]:
        body = filter.to_body(next_token)
        try:
            response = await self.client.post("/adsApi/v1/query/ads", json=body)
            response_data = response.json()
            return Success(ListGlobalAdResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def create(
        self, ads: list[SPGlobalAdCreate]
    ) -> Result["OperationGlobalAdResponse", Exception]:
        body = {"ads": [item.dict(exclude_none=True, by_alias=True) for item in ads]}
        try:
            response = await self.client.post("/adsApi/v1/create/ads", json=body)
            response_data = response.json()
            return Success(OperationGlobalAdResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def delete(
        self, ad_ids: list[str]
    ) -> Result["OperationGlobalAdResponse", Exception]:
        body = {"adIds": ad_ids}
        try:
            response = await self.client.post("/adsApi/v1/delete/ads", json=body)
            response_data = response.json()
            return Success(OperationGlobalAdResponse(**response_data))
        except Exception as e:
            return Failure(e)

    async def update(
        self, ads: list[SPGlobalAdUpdate]
    ) -> Result["OperationGlobalAdResponse", Exception]:
        body = {"ads": [item.dict(exclude_none=True, by_alias=True) for item in ads]}
        try:
            response = await self.client.post("/adsApi/v1/update/ads", json=body)
            response_data = response.json()
            return Success(OperationGlobalAdResponse(**response_data))
        except Exception as e:
            return Failure(e)


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
