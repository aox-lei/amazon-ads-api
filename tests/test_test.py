from typing import Optional
import pytest
import asyncio
import httpx
import pydantic
from ads_api import settings, enums, create_ads_client, Credentials
from datetime import datetime, timezone
import pendulum


class A(pydantic.BaseModel):
    starttime: datetime = pydantic.Field(default_factory=lambda:datetime.now(timezone.utc))
    
    @pydantic.validator("starttime", always=True)
    def validate_starttime(cls, v:datetime):
        return pendulum.instance(v).format("YYYY-MM-DDTHH:mm:ss[Z]")

@pytest.mark.asyncio
async def test_test():
    a = A()
    print(type(a.starttime))
