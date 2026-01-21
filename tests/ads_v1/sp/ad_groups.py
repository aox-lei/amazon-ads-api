import pytest

from ads_api.ads_v1.sp.ad_groups import (
    AdGroupsApi,
    ListAdGroupFiler,
    SPAdGroupCreate,
    SPAdGroupUpdate,
)
from ads_api import Credentials, enums, create_ads_client
from rich import inspect

from ads_api.ads_v1.sp.types.enums import SPUpdateState


@pytest.mark.asyncio
async def test_query(credentials: Credentials, profile_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = AdGroupsApi(ads_client, profile_id)
    filter = ListAdGroupFiler(max_results=10)
    data = await api.query(filter)
    inspect(data.unwrap())


@pytest.mark.asyncio
async def test_create(credentials: Credentials, profile_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = AdGroupsApi(ads_client, profile_id)

    ad_group = SPAdGroupCreate.build("264982843807609", "测试广告组", 0.02)
    data = await api.create([ad_group])
    inspect(data.unwrap())


@pytest.mark.asyncio
async def test_update(credentials: Credentials, profile_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = AdGroupsApi(ads_client, profile_id)

    ad_group = SPAdGroupUpdate.build("445914762331229")
    _ = ad_group.set_state(SPUpdateState.ENABLED)
    data = await api.update([ad_group])
    inspect(data.unwrap())
