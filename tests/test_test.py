from typing import Optional
import pytest
import asyncio
import httpx
import pydantic
from ads_api import Region
from datetime import datetime, timezone
import pendulum


@pytest.mark.asyncio
async def test_test():
    print(Region.by_country_code("US"))
