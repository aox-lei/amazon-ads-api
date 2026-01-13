from typing import Optional
from pydantic import BaseSettings
from .enums import Region

__all__ = [
    "settings",
]


class Settings(BaseSettings):
    AUTH_URL_NA: str = "https://api.amazon.com/auth/o2/token"  # 北美
    AUTH_URL_EU: str = "https://api.amazon.com/auth/o2/token"  # 欧洲
    AUTH_URL_FE: str = "https://api.amazon.com/auth/o2/token"  # 远东

    API_ENDPOINT_NA: str = "https://advertising-api.amazon.com"
    API_ENDPOINT_EU: str = "https://advertising-api-eu.amazon.com"
    API_ENDPOINT_FE: str = "https://advertising-api-fe.amazon.com"
    PROXY_URL: Optional[str] = None

    def get_auth_url(self, region: Region) -> Optional[str]:
        map_ = {
            Region.NA: self.AUTH_URL_NA,
            Region.EU: self.AUTH_URL_EU,
            Region.FE: self.AUTH_URL_FE,
        }
        return map_.get(region)

    def get_api_endpoint(self, region: Region) -> Optional[str]:
        map_ = {
            Region.NA: self.API_ENDPOINT_NA,
            Region.EU: self.API_ENDPOINT_EU,
            Region.FE: self.API_ENDPOINT_FE,
        }
        return map_.get(region)


settings = Settings()
