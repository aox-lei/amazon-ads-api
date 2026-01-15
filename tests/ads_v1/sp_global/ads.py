import pytest

from ads_api.ads_v1.sp_global.ads import AdsGlobalApi, ListGlobalAdFilter
from ads_api import Credentials, enums, create_ads_client


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = AdsGlobalApi(ads_client, "amzn1.ads-account.g.a8a482m7xu81z4dallvt606cc")
    filter = ListGlobalAdFilter()
    data = await api.query(filter)
    print(data)
