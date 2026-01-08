import pytest
import asyncio
import httpx
from ads_api import settings, enums, create_client, Credentials


@pytest.mark.asyncio
async def test_test(credentials: Credentials):
    httpx_client = create_client(enums.Region.EU, credentials)
    async with httpx_client as client:
        response = await client.get(
            f"{settings.API_ENDPOINT_EU}/v2/profiles"
        )
        print(response)
