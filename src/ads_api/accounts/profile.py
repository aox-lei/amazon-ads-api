from typing import Optional
from returns.result import Failure, Success, Result
from typing_extensions import Literal
from ads_api.base import Base, CamelCaseBaseModel
from ads_api import enums

__all__ = ["ProfileApi", "ListProfileFilter"]


class ProfileApi(Base):
    async def list(
        self, filter: Optional["ListProfileFilter"] = None
    ) -> Result[list["Profile"], Exception]:
        param = filter.to_param() if filter else None
        try:
            response = await self.client.get("/v2/profiles", params=param)
            response_data = response.json()
            return Success([Profile(**item) for item in response_data])
        except Exception as e:
            return Failure(e)


# region 获取配置文件过滤器


class ListProfileFilter(CamelCaseBaseModel):
    # 仅包含具有指定广告 API 程序权限的用户配置文件
    api_program: Optional[
        list[
            Literal[
                "billing",
                "campaign",
                "paymentMethod",
                "store",
                "report",
                "account",
                "post",
            ]
        ]
    ] = ["campaign"]

    # 仅包含具有指定访问级别的用户配置文件
    access_level: Optional[list[Literal["edit", "view"]]] = ["edit"]
    # 只包含指定类型的列表中的画像
    profile_type_filter: Optional[list[Literal["seller", "vendor", "agency"]]] = None
    # 默认返回所有, 设置则只返回包含此字段或不包含此字段
    valid_payment_method_filter: Optional[bool] = None

    def to_param(self):
        param = self.dict(exclude_none=True, by_alias=True)
        if self.api_program is not None:
            param["apiProgram"] = ",".join(self.api_program)
        if self.access_level is not None:
            param["accessLevel"] = ",".join(self.access_level)
        if self.profile_type_filter is not None:
            param["profileTypeFilter"] = ",".join(self.profile_type_filter)
        return param


# endregion


# region Profile Model Response
class AccountInfo(CamelCaseBaseModel):
    # 市场id
    marketplace_string_id: str
    # 卖家和供应商的标识符, 此值并非唯一, 在不同的市场平台中可能相同
    id: str
    type: Literal["vendor", "seller", "agency"]
    name: str
    # 子类型
    sub_type: Optional[Literal["KDP_AUTHOR", "AMAZON_ATTRIBUTION"]] = None
    # 是否设置有效的支付方式
    valid_payment_method: bool


class Profile(CamelCaseBaseModel):
    profile_id: int
    country_code: enums.CountryCode
    currency_code: enums.CurrencyCode
    # 此字段只适用于卖家类型账户的赞助商品推广
    daily_budget: Optional[float]
    timezone: enums.TimeZone
    account_info: AccountInfo


# endregion
