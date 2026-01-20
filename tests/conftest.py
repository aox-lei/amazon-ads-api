import os
from dotenv import load_dotenv
from ads_api import Credentials, set_proxy
import pytest

_ = load_dotenv()


@pytest.fixture(scope="session")
def credentials():
    set_proxy("http://127.0.0.1:8900")

    credentials = Credentials(
        client_id=os.getenv("ADS_CLIENT_ID", ""),
        client_secret=os.getenv("ADS_CLIENT_SECRET", ""),
        refresh_token=os.getenv("REFRESH_TOKEN", ""),
    )
    yield credentials


@pytest.fixture(scope="session")
def account_id():
    return os.getenv("ACCOUNT_ID", "")
