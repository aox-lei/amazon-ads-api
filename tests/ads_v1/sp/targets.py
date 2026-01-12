import pytest

from ads_api.ads_v1.sp.targets import (
    TargetApi,
    ListTargetFilter,
)
from ads_api import Credentials, enums, create_ads_client
from returns.pipeline import is_successful
from pprint import pprint as print


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = TargetApi(ads_client, "1797199929863809")
    filter = ListTargetFilter()

    data = await api.query(filter)
    if not is_successful(data):
        print(data.failure())
        return
    data = data.unwrap()
    print(data.dict())
