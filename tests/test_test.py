from typing import Optional
import pytest
import asyncio
import httpx
import pydantic
from ads_api import settings, enums, create_ads_client, Credentials


class A(pydantic.BaseModel):
    a: str


class B(pydantic.BaseModel):
    b: str


class C(pydantic.BaseModel):
    a: Optional[A] = None
    b: Optional[B] = None


@pytest.mark.asyncio
async def test_test(credentials: Credentials):
    httpx_client = create_ads_client(enums.Region.EU, credentials)
    async with httpx_client as client:
        response = await client.get(f"{settings.API_ENDPOINT_EU}/v2/profiles")
        print(response)
