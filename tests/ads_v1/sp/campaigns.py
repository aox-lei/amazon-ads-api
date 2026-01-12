import pytest

from ads_api.ads_v1.sp.campaigns import (
    CampaignApi,
    ListCampaignFilter,
    SPCampaignStateFilter,
)
from ads_api.ads_v1.sp.types.campaigns import SPCampaignCreate
from ads_api import Credentials, enums, create_ads_client
from returns.pipeline import is_successful
from pprint import pprint as print


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaignApi(ads_client, "1797199929863809")
    filter = ListCampaignFilter(state_filter=[SPCampaignStateFilter.ENABLED])

    data = await api.query(filter)
    if not is_successful(data):
        print(data.failure())
        return
    data = data.unwrap()
    print(data.dict())


@pytest.mark.asyncio
async def test_create(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    budgets = SPCampaignCreate.set_budgets(budget_value=1000)
    api = CampaignApi(ads_client, "1797199929863809")
