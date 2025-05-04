from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Application configuration pulled from environment or `.env` file.
    """
    openai_api_key: str
    ydc_api_key: str
    app_version: str = "1.0.0"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = AppSettings()
