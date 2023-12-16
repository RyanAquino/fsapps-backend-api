from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str = "secret"
    access_token_minutes: int = 5
    database_url: str = "local"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
