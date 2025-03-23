import os
from typing import Optional, Dict, Any, List
from pydantic_settings import BaseSettings
from pydantic import field_validator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Helper function to parse comma-separated string to list
def parse_comma_separated_list(value: str) -> List[str]:
    if not value:
        return ["*"]
    return [x.strip() for x in value.split(",")]

class Settings(BaseSettings):
    """Application settings."""
    
    # API configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "VNStock API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "API wrapper for the vnstock Python library"
    
    # CORS - default to allow all
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Redis configuration
    REDIS_HOST: Optional[str] = None
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None
    
    # Cache settings
    CACHE_ENABLED: bool = True
    CACHE_DEFAULT_TIMEOUT: int = 3600  # 1 hour
    
    # Supabase configuration
    SUPABASE_URL: Optional[str] = None
    SUPABASE_KEY: Optional[str] = None
    
    # API rate limiting
    RATE_LIMIT_PER_MIN: int = 60
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    model_config = {
        "case_sensitive": True,
        "env_file": ".env",
    }

# Create settings instance
settings = Settings() 