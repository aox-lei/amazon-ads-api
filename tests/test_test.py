import asyncio
import json
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

import httpx
import pendulum
import pydantic
import pytest

from ads_api import Region
from ads_api.ads_v1.sp_global.campaigns import ListGlobalCampaignResponse


def test_test():
    with open("1.json", "r") as f:
        data = json.load(f)

    print(ListGlobalCampaignResponse(**data))