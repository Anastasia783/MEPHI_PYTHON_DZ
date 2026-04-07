from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    env: str

    jwt_secret: str
    jwt_alg: str
    access_token_expire_minutes: int

    sqlite_path: str

    openrouter_api_key: str = ""
    openrouter_base_url: str
    openrouter_model: str
    openrouter_site_url: str
    openrouter_app_name: str
    openrouter_timeout: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()