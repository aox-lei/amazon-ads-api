import pytest
import asyncio
from ads_api import settings, enums


def test_settings():
    url = settings.get_auth_url(enums.Region.EU)
    print(url)
