from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    secret_key: str = "secret"
    access_token_expire_minutes: int = Field(alias='ACCESS_TOKEN_EXPIRE_MINUTES')
    database_url: str = Field(alias='DATABASE_URL')

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
