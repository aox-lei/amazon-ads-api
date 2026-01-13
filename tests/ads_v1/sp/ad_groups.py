import pytest

from ads_api.ads_v1.sp.ad_groups import AdGroupsApi, ListAdGroupFiler
from ads_api import Credentials, enums, create_ads_client


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = AdGroupsApi(ads_client, "1797199929863809")
    filter = ListAdGroupFiler(
        
    )
    data = await api.query(filter)
    print(data)
