from typing import Optional
import pytest
import asyncio
import httpx
import pydantic
from ads_api import settings, enums, create_ads_client, Credentials

class A(pydantic.BaseModel):
    name: str
    age: Optional[int] = None
    
    def set_age(self, age:int):
        self.age = age
        return self


@pytest.mark.asyncio
async def test_test():
    a= A(name="zhangsan")
    _ = a.set_age(10)
    print(a)
