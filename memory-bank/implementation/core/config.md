# config

## Overview

This module manages application configuration and environment variables using Pydantic settings. It provides a centralized place for all application settings and environment variable handling.

## Classes

### Settings

**Description:**
A Pydantic settings class that loads and validates environment variables for the application.

**Attributes:**

- `API_V1_STR` (str): The base path for API version 1 endpoints, defaults to "/api/v1"
- `PROJECT_NAME` (str): The name of the project, defaults to "VNStock API"
- `VERSION` (str): The API version, defaults to "0.1.0"
- `DESCRIPTION` (str): The API description, defaults to "API wrapper for the vnstock Python library"
- `ALLOWED_HOSTS` (List[str]): List of allowed hosts for CORS, defaults to ["*"]
- `REDIS_HOST` (Optional[str]): Redis server host, loaded from env var "REDIS_HOST"
- `REDIS_PORT` (int): Redis server port, loaded from env var "REDIS_PORT", defaults to 6379
- `REDIS_PASSWORD` (Optional[str]): Redis server password, loaded from env var "REDIS_PASSWORD"
- `CACHE_ENABLED` (bool): Whether caching is enabled, loaded from env var "CACHE_ENABLED", defaults to True
- `CACHE_DEFAULT_TIMEOUT` (int): Default cache timeout in seconds, loaded from env var "CACHE_DEFAULT_TIMEOUT", defaults to 3600 (1 hour)
- `SUPABASE_URL` (Optional[str]): Supabase URL, loaded from env var "SUPABASE_URL"
- `SUPABASE_KEY` (Optional[str]): Supabase API key, loaded from env var "SUPABASE_KEY"
- `RATE_LIMIT_PER_MIN` (int): API rate limit per minute, loaded from env var "RATE_LIMIT_PER_MIN", defaults to 60
- `ENVIRONMENT` (str): Application environment, loaded from env var "ENVIRONMENT", defaults to "development"
- `DEBUG` (bool): Debug mode flag, loaded from env var "DEBUG", defaults to True

**Example:**

```python
from app.core.config import settings

# Access configuration
api_path = settings.API_V1_STR
is_debug = settings.DEBUG

# Use settings in application initialization
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
)
```

## Variables

### settings

**Description:**
A pre-instantiated Settings object that can be imported and used throughout the application.

**Type:**
`Settings`

**Example:**

```python
from app.core.config import settings

# Use settings in other modules
if settings.CACHE_ENABLED:
    # Set up caching
    pass
```

## Notes

- The module uses `python-dotenv` to load environment variables from a `.env` file
- Default values are provided for most settings, but can be overridden through environment variables
- Boolean environment variables can be set using "true", "1", or "t" (case-insensitive) for True
- Settings are case-sensitive by default
- Environment variables take precedence over values defined in the `.env` file
