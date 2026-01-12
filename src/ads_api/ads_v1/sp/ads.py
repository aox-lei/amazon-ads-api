from typing import Optional

from returns.result import Failure, Success, Result

from .types.common import ErrorsIndex
from ads_api.base import BaseWithProfileId, CamelCaseBaseModel
import pydantic
from typing_extensions import Literal
from .types.enums import SPAdStateFilter
from .types.ads import SPAd, SPAdCreate, SPAdUpdate, SPAdMultiStatusSuccess
from ads_api.ads_v1.base import handle_api_errors
from httpx import Response


class AdsApi(BaseWithProfileId):
    @handle_api_errors
    async def query(
        self, filter: "ListAdFilter", next_token: Optional[str] = None
    ) -> Result["ListAdResponse", Response]:
        body = filter.to_body(next_token)
        response = await self.client.post("/adsApi/v1/query/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(ListAdResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def create(
        self, ads: list[SPAdCreate]
    ) -> Result["OperationAdResponse", Response]:
        body = {"ads": [item.dict(exclude_none=True, by_alias=True) for item in ads]}
        response = await self.client.post("/adsApi/v1/create/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationAdResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def delete(
        self, ad_ids: list[str]
    ) -> Result["OperationAdResponse", Response]:
        body = {"adIds": ad_ids}

        response = await self.client.post("/adsApi/v1/delete/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationAdResponse(**response_data))
        return Failure(response)

    @handle_api_errors
    async def update(
        self, ads: list[SPAdUpdate]
    ) -> Result["OperationAdResponse", Response]:
        body = {"ads": [item.dict(exclude_none=True, by_alias=True) for item in ads]}

        response = await self.client.post("/adsApi/v1/update/ads", json=body)
        if response.is_success:
            response_data = response.json()
            return Success(OperationAdResponse(**response_data))
        return Failure(response)


class ListAdFilter(CamelCaseBaseModel):
    ad_group_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    ad_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    ad_product_filter: list[Literal["SPONSORED_PRODUCTS"]] = ["SPONSORED_PRODUCTS"]
    campaign_id_filter: Optional[list[str]] = pydantic.Field(
        default=None, min_items=0, max_items=100
    )
    max_results: int = 1000
    state_filter: Optional[list[SPAdStateFilter]] = pydantic.Field(
        default=None, min_items=0, max_items=3
    )

    def to_body(self, next_token: Optional[str] = None):
        body = self.dict(exclude_none=True, by_alias=True)
        body["adProductFilter"] = {"include": self.ad_product_filter}
        if self.ad_group_id_filter is not None:
            body["adGroupIdFilter"] = {"include": self.ad_group_id_filter}
        if self.ad_id_filter is not None:
            body["adIdFilter"] = {"include": self.ad_id_filter}
        if self.campaign_id_filter is not None:
            body["campaignIdFilter"] = {"include": self.campaign_id_filter}
        if self.state_filter is not None:
            body["stateFilter"] = {"include": self.state_filter}
        if next_token is not None:
            body["nextToken"] = next_token

        return body


# region ListAdResponse
class ListAdResponse(CamelCaseBaseModel):
    ads: Optional[list[SPAd]] = None
    next_token: Optional[str] = None


# endregion


# region OperationAdResponse
class OperationAdResponse(CamelCaseBaseModel):
    error: Optional[list[ErrorsIndex]]
    success: Optional[list[SPAdMultiStatusSuccess]]


# endregion
