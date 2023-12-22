from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    secret_key: str = Field(alias='SECRET_KEY')
    access_token_expire_minutes: int = Field(alias='ACCESS_TOKEN_EXPIRE_MINUTES')
    database_url: str = Field(alias='DATABASE_URL')
    host: str = Field(alias='HOST')
    port: int = Field(alias='PORT')
    reload: bool = Field(alias='RELOAD')

    model_config = SettingsConfigDict(env_file="../.env")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
