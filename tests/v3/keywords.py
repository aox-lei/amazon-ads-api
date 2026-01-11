from ads_api import Credentials, enums, create_ads_client
from ads_api.v3.keywords import RecommendationApi, KeywordForAsinFilter
import pytest
import os


@pytest.mark.asyncio
async def test_keyword_groups(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = RecommendationApi(ads_client, os.getenv("PROFILE_ID", ""))
    response = await api.keyword_groups(["B0FS5SQDYN"], "UK")
    print(response)


@pytest.mark.asyncio
async def test_keyword(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = RecommendationApi(ads_client, os.getenv("PROFILE_ID", ""))

    filter = KeywordForAsinFilter.by_asins(["B0FS5SQDYN"])
    response = await api.keyword(filter)
    print(response)
