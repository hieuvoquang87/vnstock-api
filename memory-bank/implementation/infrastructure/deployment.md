# Deployment

## Overview

This document outlines the deployment strategy for the vnstock-api project using Vercel.

## Vercel Deployment

### Configuration

The project uses Vercel for serverless deployment with the following configuration in `vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app/main.py",
      "use": "@vercel/python",
      "config": {
        "runtime": "python3.12"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/main.py"
    }
  ]
}
```

### Python Runtime

The project uses Python 3.12 as specified in the `vercel.json` file's runtime configuration.

### Dependencies

The project uses a minimal set of dependencies for deployment:

- `fastapi`: Web framework for building APIs
- `uvicorn`: ASGI server for FastAPI
- `pydantic`: Data validation library
- `python-dotenv`: Environment variable management
- `redis`: Caching and rate limiting
- `pydantic-settings`: Settings management
- `vnstock`: Core library for Vietnamese stock data

Development dependencies (not included in deployment):

- Testing tools: `pytest`, `pytest-cov`
- Code quality tools: `flake8`, `mypy`, `black`, `isort`
- GraphQL: `strawberry-graphql` (to be added to production when needed)
- HTTP client: `httpx` (to be added to production when needed)

Dependencies are managed through Poetry and exported to `requirements.txt` for Vercel deployment.

### Environment Variables

Environment variables are defined in the Vercel dashboard or through the `.env` file for local development. The following variables are required:

- `REDIS_HOST`: Redis server hostname
- `REDIS_PORT`: Redis server port
- `REDIS_PASSWORD`: Redis server password
- `CACHE_ENABLED`: Enable/disable caching
- `CACHE_DEFAULT_TIMEOUT`: Default cache timeout in seconds
- `SUPABASE_URL`: Supabase URL
- `SUPABASE_KEY`: Supabase API key
- `RATE_LIMIT_PER_MIN`: API rate limit per minute
- `DEBUG`: Enable/disable debug mode

### Deployment Process

1. Ensure all dependencies are listed in `requirements.txt`
2. Commit changes to the repository
3. Connect the repository to Vercel
4. Configure environment variables in the Vercel dashboard
5. Deploy the project

Vercel automatically detects the Python FastAPI application and deploys it as a serverless function.

### Regions

The deployment is configured to use Vercel's global edge network for optimal performance.
