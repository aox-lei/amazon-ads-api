import pytest
from ads_api.accounts.account import AccountApi
from ads_api import Credentials, enums, create_ads_client


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    profile_api = AccountApi(ads_client)
    profiles = await profile_api.query()
    print(profiles)
