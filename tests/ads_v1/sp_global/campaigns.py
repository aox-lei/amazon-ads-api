import pytest

from ads_api.ads_v1.sp_global.campaigns import (
    CampaginGlobalApi,
    SPGlobalCampaignCreate,
    ListGlobalCampaignFilter,
    SPGlobalCampaignUpdate,
)
from ads_api import Credentials, enums, create_ads_client
from rich import inspect

from ads_api.ads_v1.sp_global.types.enums import (
    SPGlobalBidStrategy,
    SPGlobalPlacement,
    SPGlobalState,
    SPGlobalUpdateState,
)


@pytest.mark.asyncio
async def test_query(credentials: Credentials, account_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaginGlobalApi(ads_client, account_id)
    filter = ListGlobalCampaignFilter()
    res = await api.query(filter)
    inspect(res.unwrap())


@pytest.mark.asyncio
async def test_create(credentials: Credentials, account_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaginGlobalApi(ads_client, account_id)
    campaign_body = SPGlobalCampaignCreate.build(
        "测试广告活动", budget_settings={"UK": 1, "FR": 1}
    )
    optimization = SPGlobalCampaignCreate.build_marketplace_optimizations(
        bid_adjustments={
            SPGlobalPlacement.PRODUCT_PAGE: 1,
            SPGlobalPlacement.REST_OF_SEARCH: 2,
            SPGlobalPlacement.TOP_OF_SEARCH: 3,
        },
        bid_strategy=SPGlobalBidStrategy.MANUAL,
    )
    campaign_body.set_marketplace_configuration(
        "FR",
        name="测试广告活动(FR)",
        optimizations=optimization,
        state=SPGlobalState.ENABLED,
    )
    # inspect(campaign_body)
    res = await api.create([campaign_body])
    inspect(res)


@pytest.mark.asyncio
async def test_update(credentials: Credentials, account_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = CampaginGlobalApi(ads_client, account_id)

    campaign_body = SPGlobalCampaignUpdate.build("4999919260891723604")
    # _ = campaign_body.set_state(SPGlobalUpdateState.PAUSED)
    _ = campaign_body.set_marketplace_configuration("DE", state=SPGlobalState.PAUSED)
    res = await api.update([campaign_body])
    inspect(res.unwrap())
