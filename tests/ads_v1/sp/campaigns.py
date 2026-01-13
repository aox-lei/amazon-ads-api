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
    budgets = SPCampaignCreate.create_budgets(budget_value=1)
    bid_settings = SPCampaignCreate.create_bid_settings(
        audience_adjustment=SPCampaignCreate.create_audience_adjustment(
            audience_id="409816952926330179", percentage=10
        ),
        placement_adjustment=[
            SPCampaignCreate.create_placement_adjustment(SPPlacement.PRODUCT_PAGE, 10)
        ],
        bid_strategy=SPBidStrategy.MANUAL,
    )
    budget_settings = SPCampaignCreate.create_budget_settings(
        off_amazon_budget_control_strategy=SPOffAmazonBudgetControlStrategy.MAXIMIZE_REACH
    )
    campaign = SPCampaignCreate(
        ad_product="SPONSORED_PRODUCTS",
        auto_creation_settings=SPCampaignCreate.create_auto_creation_settings(),
        budgets=budgets,
        countries=[SPCountryCode.GB],
        name="测试广告活动",
        optimizations=SPCampaignCreate.create_optimizations(
            bid_settings=bid_settings, budget_settings=budget_settings
        ),
    )

    api = CampaignApi(ads_client, "1797199929863809")
    response = await api.create([campaign])
    print(response)


@pytest.mark.asyncio
async def test_delete(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaignApi(ads_client, "1797199929863809")
    response = await api.delete(campaign_ids=["83761549527322"])
    print(response)


@pytest.mark.asyncio
async def test_update(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaignApi(ads_client, "1797199929863809")

    body = SPCampaignUpdate(campaign_id="83761549527322", state=SPUpdateState.ENABLED)
    response = await api.update(campaigns=[body])
    print(response)
