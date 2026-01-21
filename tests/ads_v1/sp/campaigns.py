import pytest

from ads_api.ads_v1.sp.campaigns import (
    CampaignApi,
    ListCampaignFilter,
    SPCampaignStateFilter,
)
from ads_api.ads_v1.sp.types.campaigns import SPCampaignCreate, SPCampaignUpdate
from ads_api import Credentials, enums, create_ads_client
from returns.pipeline import is_successful
from pprint import pprint as print

from ads_api.ads_v1.sp.types.enums import (
    SPPlacement,
    SPBidStrategy,
    SPOffAmazonBudgetControlStrategy,
    SPCountryCode,
    SPUpdateState,
)
from rich import inspect


@pytest.mark.asyncio
async def test_list(credentials: Credentials):

    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaignApi(ads_client, "1797199929863809")
    filter = ListCampaignFilter(state_filter=[SPCampaignStateFilter.ENABLED])

    data = await api.query(filter)
    if not is_successful(data):
        return
    data = data.unwrap()
    print(data.dict())


@pytest.mark.asyncio
async def test_create(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    campaign = SPCampaignCreate.build(
        "测试广告活动", budget_value=1.0, country_code="UK"
    )

    api = CampaignApi(ads_client, "1797199929863809")
    response = await api.create([campaign])
    inspect(response.unwrap())


@pytest.mark.asyncio
async def test_update(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    campaign_update = SPCampaignUpdate.build("264982843807609", "测试广告活动UK")
    _ = campaign_update.set_state(SPUpdateState.PAUSED)
    _ = campaign_update.set_budget_settings(
        SPOffAmazonBudgetControlStrategy.MAXIMIZE_REACH
    )
    _ = campaign_update.set_tags({"tag1": "tag1"})
    api = CampaignApi(ads_client, "1797199929863809")
    res = await api.update(campaigns=[campaign_update])
    inspect(res.unwrap())


@pytest.mark.asyncio
async def test_delete(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaignApi(ads_client, "1797199929863809")
    response = await api.delete(campaign_ids=["83761549527322"])
    print(response)
