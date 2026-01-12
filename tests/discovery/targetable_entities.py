import pytest

from ads_api.discovery.targetable_entities import (
    TargetableEntitiesApi,
    ListTargetableEntitiesFilter,
)
from ads_api.discovery.types.enums import AdProduct
from ads_api import Credentials, enums, create_ads_client
from returns.pipeline import is_successful
from pprint import pprint as print


@pytest.mark.asyncio
async def test_list(credentials: Credentials):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = TargetableEntitiesApi(ads_client, "1797199929863809")
    filter = ListTargetableEntitiesFilter(ad_product=AdProduct.SPONSORED_PRODUCTS)

    data = await api.query(filter)
    if not is_successful(data):
        print(data.failure())
        return
    data = data.unwrap()
    print(data.dict())
