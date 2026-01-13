from .setting import settings
from .base import create_ads_client, Credentials, BaseWithProfileId

__all__ = ["settings", "create_ads_client", "Credentials", "BaseWithProfileId"]


def set_proxy(proxy_url: str):
    settings.PROXY_URL = proxy_url
