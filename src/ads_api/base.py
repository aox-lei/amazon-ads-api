from typing_extensions import override
import httpx
from .setting import settings
from .enums import Region
from typing import Any
import pydantic
from returns.result import Result, Success, Failure
from cachetools import TTLCache
from returns.pipeline import is_successful
from .util import to_camel

__all__ = [
    "create_ads_client",
    "Credentials",
    "Base",
    "CamelCaseBaseModel",
    "BaseWithProfileId",
]


class Credentials(pydantic.BaseModel):
    client_id: str
    client_secret: str
    refresh_token: str


class AccessTokenResponse(pydantic.BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str


token_cache: TTLCache[Any, Any] = TTLCache(maxsize=10 * 10000, ttl=3500)


class AccessTokenAuth(httpx.Auth):
    def __init__(self, region: Region, credentials: Credentials):
        self.region = region
        self.credentials = credentials

    @override
    async def async_auth_flow(self, request: httpx.Request):
        auth_result = await self.get_access_token()
        if not is_successful(auth_result):
            raise httpx.RequestError("请求认证接口失败")
        access_token = auth_result.unwrap().access_token
        request.headers["Authorization"] = f"Bearer {access_token}"
        yield request

    async def get_access_token(self) -> Result[AccessTokenResponse, Exception]:
        if token_cache.get(self.credentials.refresh_token):
            return Success(
                token_cache.get(self.credentials.refresh_token)
            )  # type:ignore

        url = settings.get_auth_url(self.region)
        if url is None:
            return Failure(ValueError("Invalid region"))
        req_data = {
            "grant_type": "refresh_token",
            "refresh_token": self.credentials.refresh_token,
            "client_id": self.credentials.client_id,
            "client_secret": self.credentials.client_secret,
        }
        async with httpx.AsyncClient(
            verify=False, proxy=settings.PROXY_URL, timeout=30.0
        ) as client:
            try:
                response = await client.post(url, data=req_data)
            except Exception as e:
                return Failure(e)

            if response.status_code != 200:
                return Failure(ValueError("Failed to get access token"))
        token_cache[self.credentials.refresh_token] = AccessTokenResponse(
            **response.json()
        )
        return Success(token_cache[self.credentials.refresh_token])


def create_ads_client(region: Region, credentials: Credentials):
    api_endpoint = settings.get_api_endpoint(region)
    if api_endpoint is None:
        raise ValueError("Invalid region")
    access_token = AccessTokenAuth(region, credentials)
    headers = {"Amazon-Advertising-API-ClientId": credentials.client_id}

    return httpx.AsyncClient(
        base_url=api_endpoint,
        auth=access_token,
        headers=headers,
        verify=False,
        timeout=30.0,
        proxy=settings.PROXY_URL,
    )


class Base:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client


class BaseWithProfileId(Base):
    def __init__(self, client: httpx.AsyncClient, profile_id: str):
        client.headers.update({"Amazon-Advertising-API-Scope": profile_id})
        super().__init__(client)


class BaseWithAccountId(Base):
    def __init__(self, client: httpx.AsyncClient, account_id: str):
        client.headers.update({"Amazon-Ads-AccountId": account_id})
        super().__init__(client)


class CamelCaseBaseModel(pydantic.BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
