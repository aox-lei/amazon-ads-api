from datetime import datetime
from typing import Optional
from typing_extensions import Literal
from .enums import (
    SPGlobalCreateState,
    SPGlobalCurrencyCode,
    SPGlobalCurrencyCodeByCountryCode,
    SPGlobalMarketplace,
    SPGlobalState,
)
from ads_api.base import CamelCaseBaseModel
from .common import (
    SPGlobalCreateTag,
    SPTag,
    SPGlobalStatus,
    SPGlobalTag,
    Error,
)
from .enums import SPGlobalUpdateState
import pydantic


# region 出价
class SPGlobalAdGroupBidMarketplaceSetting(CamelCaseBaseModel):
    currency_code: SPGlobalCurrencyCode
    default_bid: float
    marketplace: SPGlobalMarketplace


class SPGlobalCreateAdGroupBidMarketplaceSetting(CamelCaseBaseModel):
    currency_code: SPGlobalCurrencyCode
    default_bid: float
    marketplace: SPGlobalMarketplace


class SPGlobalAdGroupBid(CamelCaseBaseModel):
    marketplace_settings: Optional[list[SPGlobalAdGroupBidMarketplaceSetting]]


class SPGlobalCreateAdGroupBid(CamelCaseBaseModel):
    marketplace_settings: list[SPGlobalCreateAdGroupBidMarketplaceSetting] = []


class SPGlobalUpdateAdGroupBid(CamelCaseBaseModel):
    marketplace_settings: Optional[list[SPGlobalCreateAdGroupBidMarketplaceSetting]] = (
        None
    )


# endregion


class SPGlobalMarketplaceAdGroupFieldOverrides(CamelCaseBaseModel):
    name: Optional[str]
    state: Optional[SPGlobalState]
    tags: Optional[list[SPGlobalTag]] = pydantic.Field(default=None, max_items=50)


# region SPGlobalMarketplaceAdGroupConfigurations
class SPGlobalMarketplaceAdGroupConfigurations(CamelCaseBaseModel):
    ad_group_id: Optional[str] = None
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalMarketplaceAdGroupFieldOverrides


# endregion


# region SPGlobalAdGroup
class SPGlobalAdGroup(CamelCaseBaseModel):
    ad_group_id: str
    ad_product: Literal["SPONSORED_PRODUCTS"]
    bid: SPGlobalAdGroupBid
    campaign_id: str
    creation_datetime: datetime = pydantic.Field(default=..., alias="creationDateTime")
    last_updated_datetime: datetime = pydantic.Field(
        default=..., alias="lastUpdatedDateTime"
    )
    marketplace_configurations: Optional[
        list[SPGlobalMarketplaceAdGroupConfigurations]
    ] = None
    marketplace_scope: Literal["GLOBAL"]
    marketplaces: list[SPGlobalMarketplace]
    name: str
    state: SPGlobalState
    status: Optional[SPGlobalStatus] = None
    tags: Optional[list[SPTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )


# endregion


# region SPGlobalCreateMarketplaceAdGroupConfigurations
class SPGlobalCreateMarketplaceAdGroupFieldOverrides(CamelCaseBaseModel):
    name: Optional[str] = None
    state: Optional[SPGlobalState] = None
    tags: Optional[list[SPGlobalCreateTag]] = None


class SPGlobalCreateMarketplaceAdGroupConfigurations(CamelCaseBaseModel):
    marketplace: SPGlobalMarketplace
    overrides: SPGlobalCreateMarketplaceAdGroupFieldOverrides


# endregion


# region SPGlobalAdGroupCreate
class SPGlobalAdGroupCreate(CamelCaseBaseModel):
    ad_product: Literal["SPONSORED_PRODUCTS"] = "SPONSORED_PRODUCTS"
    bid: SPGlobalCreateAdGroupBid
    campaign_id: str
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceAdGroupConfigurations]
    ] = None
    marketplace_scope: Literal["GLOBAL"] = "GLOBAL"
    marketplaces: list[SPGlobalMarketplace]
    name: str
    state: SPGlobalCreateState
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )

    @classmethod
    def build(cls, campaign_id: str, name: str, country_codes: list[str]):
        marketplaces = [
            SPGlobalMarketplace[country_code] for country_code in country_codes
        ]
        return cls(
            bid=SPGlobalCreateAdGroupBid(),
            campaign_id=campaign_id,
            name=name,
            marketplaces=marketplaces,
            state=SPGlobalCreateState.ENABLED,
        )

    def set_bid(
        self, default_bid: float, country_code: str, currency_code: Optional[str] = None
    ):
        marketplace = SPGlobalMarketplace[country_code]
        if currency_code is None:
            currency_code = SPGlobalCurrencyCodeByCountryCode[country_code].value
        else:
            currency_code = SPGlobalCurrencyCode[currency_code]
        self.bid.marketplace_settings.append(
            SPGlobalCreateAdGroupBidMarketplaceSetting(
                currency_code=currency_code,
                default_bid=default_bid,
                marketplace=marketplace,
            )
        )
        return self

    def set_marketplace_configuration(
        self,
        country_code: str,
        *,
        name: Optional[str] = None,
        state: Optional[SPGlobalState] = None,
        tags: Optional[dict[str, str]] = None,
    ):
        self.marketplace_configurations = self.marketplace_configurations or []
        self.marketplace_configurations.append(
            SPGlobalCreateMarketplaceAdGroupConfigurations(
                marketplace=SPGlobalMarketplace[country_code],
                overrides=SPGlobalCreateMarketplaceAdGroupFieldOverrides(
                    name=name,
                    state=state,
                    tags=(
                        [
                            SPGlobalCreateTag(key=key, value=value)
                            for key, value in tags.items()
                        ]
                        if tags
                        else None
                    ),
                ),
            )
        )
        return self

    def set_tag(self, key: str, value: str):
        self.tags = self.tags or []
        self.tags.append(SPGlobalCreateTag(key=key, value=value))
        return self


# endregion


# region SPAdGroupUpdate
class SPGlobalAdGroupUpdate(CamelCaseBaseModel):
    ad_group_id: str
    bid: Optional[SPGlobalUpdateAdGroupBid] = None
    marketplace_configurations: Optional[
        list[SPGlobalCreateMarketplaceAdGroupConfigurations]
    ] = pydantic.Field(default=None, min_items=0, max_items=50)
    marketplaces: Optional[list[SPGlobalMarketplace]] = None
    name: Optional[str] = None
    state: Optional[SPGlobalUpdateState] = None
    tags: Optional[list[SPGlobalCreateTag]] = pydantic.Field(
        default=None, min_items=0, max_items=50
    )

    @classmethod
    def build(cls, ad_group_id: str):
        return cls(ad_group_id=ad_group_id)

    def set_bid(
        self, default_bid: float, country_code: str, currency_code: Optional[str] = None
    ):
        self.bid = self.bid or SPGlobalUpdateAdGroupBid(marketplace_settings=[])
        self.bid.marketplace_settings = self.bid.marketplace_settings or []
        marketplace = SPGlobalMarketplace[country_code]
        if currency_code is None:
            currency_code = SPGlobalCurrencyCodeByCountryCode[country_code].value
        else:
            currency_code = SPGlobalCurrencyCode[currency_code]
        self.bid.marketplace_settings.append(
            SPGlobalCreateAdGroupBidMarketplaceSetting(
                currency_code=currency_code,
                default_bid=default_bid,
                marketplace=marketplace,
            )
        )
        return self

    def set_marketplace_configuration(
        self,
        country_code: str,
        *,
        name: Optional[str] = None,
        state: Optional[SPGlobalState] = None,
        tags: Optional[dict[str, str]] = None,
    ):
        self.marketplace_configurations = self.marketplace_configurations or []
        self.marketplace_configurations.append(
            SPGlobalCreateMarketplaceAdGroupConfigurations(
                marketplace=SPGlobalMarketplace[country_code],
                overrides=SPGlobalCreateMarketplaceAdGroupFieldOverrides(
                    name=name,
                    state=state,
                    tags=(
                        [
                            SPGlobalCreateTag(key=key, value=value)
                            for key, value in tags.items()
                        ]
                        if tags
                        else None
                    ),
                ),
            )
        )
        return self

    def set_tag(self, key: str, value: str):
        self.tags = self.tags or []
        self.tags.append(SPGlobalCreateTag(key=key, value=value))
        return self

    def set_state(self, state: SPGlobalUpdateState):
        self.state = state
        return self


# endregion


# region SPGlobalAdGroupPartialIndex
class SPGlobalAdGroupPartialIndex(CamelCaseBaseModel):
    ad_group: SPGlobalAdGroup
    errors: list[Error]
    index: int


# endregion


# region SPGlobalAdGroupMultiStatusSuccess
class SPGlobalAdGroupMultiStatusSuccess(CamelCaseBaseModel):
    ad_group: SPGlobalAdGroup
    index: int


# endregion
