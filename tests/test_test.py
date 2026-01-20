from enum import Enum
from typing import Optional
import pytest
import asyncio
import httpx
import pydantic
from ads_api import Region
from datetime import datetime, timezone
import pendulum

class A(str, Enum):
    US = "US"
    CA = "CA"

@pytest.mark.asyncio
async def test_test():
    country_code = "NA"
    print(A[country_code])
