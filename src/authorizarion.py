from fastapi import Security
from fastapi.exceptions import HTTPException
from fastapi.security.api_key import APIKey, APIKeyHeader

from settings import env_config

api_key_header = APIKeyHeader(name=env_config.api_key_name)


async def check_authorization(
    api_key_header_value: str = Security(api_key_header),
) -> str:
    if api_key_header_value == env_config.api_key_secret:
        return api_key_header_value
    raise HTTPException(status_code=403, detail="invalid credentials")
