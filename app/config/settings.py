from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    """
    Application configuration settings.

    These settings are automatically loaded from environment variables
    or an optional `.env` file, using Pydantic's BaseSettings class.
    """

    openai_api_key: str  # API key for OpenAI models
    ydc_api_key: str     # API key for You.com Data Collector (or similar external service)
    app_version: str = "1.0.0"  # Application version identifier
    debug: bool = False         # Debug flag to control logging or error verbosity

    class Config:
        # Specify a .env file from which to load variables if not set in the environment
        env_file = ".env"

# Instantiate the settings object which can be imported throughout the application
settings = AppSettings()
