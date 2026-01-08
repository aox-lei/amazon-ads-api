import os
from dotenv import load_dotenv
from ads_api import Credentials
import pytest

_ = load_dotenv()


@pytest.fixture(scope="session")
def credentials():
    credentials = Credentials(
        client_id=os.getenv("ADS_CLIENT_ID", ""),
        client_secret=os.getenv("ADS_CLIENT_SECRET", ""),
        refresh_token=os.getenv("REFRESH_TOKEN", ""),
        profile_id=os.getenv("PROFILE_ID"),
    )
    yield credentials
