import pytest

from ads_api.ads_v1.campaigns import (
    CampaignApi,
    ListCampaignFilter,
    SPCampaignStateFilter,
)
from ads_api import Credentials, enums, create_ads_client


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaignApi(ads_client, "1797199929863809")
    filter = ListCampaignFilter(state_filter=[SPCampaignStateFilter.ENABLED])

    data = await api.query(filter)
    print(data)
