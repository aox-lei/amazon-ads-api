from typing import Any, Literal, Optional

from returns.result import Success, Result, Failure
from ads_api.base import Base, CamelCaseBaseModel
from enum import Enum

__all__ = ["AccountApi"]


# region 账号相关
class AccountApi(Base):
    async def query(
        self, max_results: int = 100, next_token: Optional[str] = None
    ) -> Result["ListReponse", Exception]:
        """列出与访问令牌关联的用户的所有广告帐户"""
        body: dict[str, Any] = {"maxResults": max_results}
        if next_token is not None:
            body["nextToken"] = next_token
        try:
            response = await self.client.post("/adsAccounts/list", json=body)
            response_data = response.json()

            return Success(ListReponse(**response_data))
        except Exception as e:
            return Failure(e)


# region Account账号数据
class Status(str, Enum):
    CREATED = "CREATED"
    DISABLED = "DISABLED"
    PARTIALLY_CREATED = "PARTIALLY_CREATED"
    PENDING = "PENDING"


class AlternateId(CamelCaseBaseModel):
    country_code: Optional[str] = None
    entity_id: Optional[str] = None
    profile_id: Optional[str] = None


class AdsAccountWithMetaData(CamelCaseBaseModel):
    account_name: Optional[str] = None
    ads_account_id: str
    alternate_ids: Optional[list[AlternateId]] = None
    country_codes: Optional[list[str]] = None
    errors: Any
    status: Optional[Status] = None


class ListReponse(CamelCaseBaseModel):
    ads_accounts: Optional[list[AdsAccountWithMetaData]] = None
    next_token: Optional[str] = None


# endregion


# region 测试账号
class TestAccountApi(Base):
    async def create(
        self,
        account_type: Literal["AUTHOR", "VENDOR"],
        country_code: str,
        vendor_code: Optional[str] = None,
    ) -> Result[bool, Exception]:
        """创建测试账号"""
        body = {
            "accountType": account_type,
            "countryCode": country_code,
        }
        if vendor_code is not None:
            body["accountMetaData"] = {  # type:ignore
                "vendorCode": vendor_code,
            }
        try:
            _ = await self.client.post("/testAccounts", json=body)
            return Success(True)
        except Exception as e:
            return Failure(e)

    async def query(self):
        try:
            res = await self.client.get("/testAccounts")
            return Success(res.json())
        except Exception as e:
            return Failure(e)


# endregion
