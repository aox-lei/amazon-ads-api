from ads_api.ads_v1.sp_global.ad_groups import (
    AdGroupsGlobalApi,
    SPGlobalAdGroupCreate,
    SPGlobalAdGroupUpdate,
    ListGlobalAdGroupFilter,
)
import pytest
from ads_api import Credentials, create_ads_client, Region
from rich import inspect

from ads_api.ads_v1.sp_global.types.enums import SPGlobalUpdateState


@pytest.mark.asyncio
async def test_query(credentials: Credentials, account_id: str):
    ads_client = create_ads_client(Region.EU, credentials)
    api = AdGroupsGlobalApi(ads_client, account_id)
    filter = ListGlobalAdGroupFilter(campaign_id_filter=["4999846175555759136"])
    res = await api.query(filter)
    inspect(res.unwrap())


@pytest.mark.asyncio
async def test_create(credentials: Credentials, account_id: str):
    ads_client = create_ads_client(Region.EU, credentials)
    api = AdGroupsGlobalApi(ads_client, account_id)
    ad_group = SPGlobalAdGroupCreate.build(
        campaign_id="4999941439445228797", name="测试广告组", country_codes=["UK", "FR"]
    )
    _ = ad_group.set_bid(default_bid=0.02, country_code="UK")
    _ = ad_group.set_bid(default_bid=0.03, country_code="FR")
    _ = ad_group.set_marketplace_configuration("UK", name="测试广告组UK")

    res = await api.create([ad_group])
    inspect(res.unwrap())


@pytest.mark.asyncio
async def test_update(credentials: Credentials, account_id: str):
    ads_client = create_ads_client(Region.EU, credentials)
    api = AdGroupsGlobalApi(ads_client, account_id)
    ad_group = SPGlobalAdGroupUpdate.build(ad_group_id="5000070297893591358")
    _ = ad_group.set_state(SPGlobalUpdateState.PAUSED)
    res = await api.update([ad_group])
    inspect(res.unwrap())
