import httpx
import pydantic
from .enums import Region
from .setting import settings
from returns.result import Result, Success, Failure


class Credentials(pydantic.BaseModel):
    client_id: str
    client_secret: str
    refresh_token: str


class AccessTokenResponse(pydantic.BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str


async def get_access_token(
    region: Region, credentials: Credentials
) -> Result[AccessTokenResponse, Exception]:
    url = settings.get_auth_url(region)
    if url is None:
        return Failure(ValueError("Invalid region"))
    req_data = {
        "grant_type": "refresh_token",
        "refresh_token": credentials.refresh_token,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, data=req_data)
        except Exception as e:
            return Failure(e)

        if response.status_code != 200:
            return Failure(ValueError("Failed to get access token"))
        return Success(AccessTokenResponse.model_validate(response.json()))
