"""Configuration settings for the application"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    app_name: str = "FastAPI Application"
    app_version: str = "0.1.0"
    debug: bool = False
    api_prefix: str = "/api/v1"
    
    # Database settings (if needed)
    database_url: Optional[str] = None
    
    # Server settings
    host: str = "127.0.0.1"
    port: int = 8000
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
