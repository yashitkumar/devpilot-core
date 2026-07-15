from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Application configurations with default values
    app_name: str = "devPilot-Core"
    app_version: str = "0.1.0"
    debug: bool = False
    description: str
    environment: str = "development"  # Options: development, staging, production
    
    # Required variables (will throw an error if missing from environment/.env)
    database_url: str
    jwt_secret_key: str

    # Automatically load environment variables from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instantiate a single global settings object
settings = Settings()
