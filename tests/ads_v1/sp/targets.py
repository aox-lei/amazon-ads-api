import pytest

from ads_api.ads_v1.sp.targets import (
    TargetApi,
    ListTargetFilter,
)
from ads_api.ads_v1.sp.types.enums import SPMatchType, SPTargetType
from ads_api import Credentials, enums, create_ads_client
from rich import inspect


@pytest.mark.asyncio
async def test_query(credentials: Credentials, profile_id: str):
    ads_client = create_ads_client(enums.Region.EU, credentials)
    api = TargetApi(ads_client, profile_id)
    filter = ListTargetFilter(match_type_filter=[SPMatchType.BROAD], keyword_filter=["apple"], keyword_filter_query_term_match_type="EXACT_MATCH")

    data = await api.query(filter)
    inspect(data.unwrap())
