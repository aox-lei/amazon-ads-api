import pytest
from ads_api.accounts.account import AccountApi, TestAccountApi
from ads_api import Credentials, enums, create_ads_client


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    profile_api = AccountApi(ads_client)
    profiles = await profile_api.query()
    print(profiles)

@pytest.mark.asyncio
async def test_test_account_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = TestAccountApi(ads_client)
    data = await api.query()
    print(data)
    
@pytest.mark.asyncio
async def test_test_account_create(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = TestAccountApi(ads_client)
    res = await api.create("AUTHOR", "UK")
    print(res)
    