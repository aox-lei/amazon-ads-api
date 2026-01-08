import pytest

from ads_api.accounts.profile import ProfileApi, ListProfileFilter
from ads_api import Credentials, enums, create_ads_client


@pytest.mark.asyncio
async def test_profile(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    profile_api = ProfileApi(ads_client)
    filter = ListProfileFilter()
    profiles = await profile_api.query(filter)
    print(profiles)
