# Technical Context: vnstock-api

## Technologies Used

### Core Technologies

1. **Python 3.12**

   - Primary programming language
   - Leverages type hints for better code quality
   - Uses the latest Python features for performance

2. **FastAPI**

   - Modern, high-performance web framework
   - Native async support for high concurrency
   - Automatic OpenAPI documentation generation

3. **GraphQL (Strawberry)**

   - Type-first GraphQL library for Python
   - Code-first schema generation
   - Integration with FastAPI
   - Exposes GraphQL Explorer for interactive queries

4. **Poetry**

   - Dependency management and packaging
   - Reproducible builds and environments
   - Virtual environment management

5. **Pydantic**
   - Data validation and settings management
   - Schema definition and parsing
   - Used for request/response models

### Data Storage & Caching

1. **Supabase/PostgreSQL**

   - Database-as-a-service for persistent storage
   - Stores user information, API keys, usage metrics
   - Keeps historical data to reduce third-party API calls
   - Managed service with scaling capabilities

2. **Redis Cloud**
   - Managed Redis service
   - Used for distributed caching
   - Supports rate limiting implementation
   - Pub/sub for event-driven features
   - Cache-as-a-service optimized for serverless

### Testing & Quality

1. **Pytest**

   - Testing framework
   - Support for fixtures and parametrization
   - Coverage reporting

2. **Mypy**

   - Static type checking
   - Ensures type safety

3. **Flake8/Black**
   - Code style enforcement
   - Automatic formatting

### CI/CD & Deployment

1. **GitHub Actions**

   - Continuous integration
   - Automated testing
   - Deployment pipelines

2. **Serverless Framework**

   - Deploying serverless functions
   - Managing infrastructure as code
   - Multi-cloud deployment capability

3. **AWS Lambda / Azure Functions**

   - Serverless compute platform
   - Pay-per-use pricing model
   - Auto-scaling capabilities

4. **Docker**

   - Local development environment
   - CI/CD pipeline testing

5. **Terraform / AWS CDK**
   - Infrastructure as Code
   - Automated environment provisioning
   - Consistent infrastructure management

## Development Setup

### Local Development

```
vnstock-api/
├── .github/                 # GitHub Actions workflows
│   └── workflows/           # CI/CD workflow definitions
├── app/                     # Main application package
│   ├── api/                 # API routes and handlers
│   │   ├── rest/            # REST API endpoints
│   │   │   ├── v1/          # API version 1
│   │   │   │   ├── stocks/  # Stock-related endpoints
│   │   │   │   ├── market/  # Market-related endpoints
│   │   │   │   └── ...      # Other resource endpoints
│   │   │   └── __init__.py  # REST API package initialization
│   │   └── graphql/         # GraphQL schema and resolvers
│   │       ├── resolvers/   # GraphQL resolvers
│   │       ├── schema.py    # GraphQL schema definition
│   │       └── __init__.py  # GraphQL package initialization
│   ├── core/                # Core functionality
│   │   ├── config.py        # Configuration settings
│   │   ├── exceptions.py    # Custom exceptions
│   │   └── logging.py       # Logging configuration
│   ├── services/            # Business logic layer
│   │   ├── stock_service.py # Stock-related business logic
│   │   ├── market_service.py# Market-related business logic
│   │   ├── cache_service.py # Caching service
│   │   └── ...              # Other services
│   ├── adapters/            # Integration with vnstock
│   │   ├── vnstock_adapter.py # Main adapter for vnstock
│   │   └── ...              # Other adapters
│   ├── repositories/        # Data access layer
│   │   ├── stock_repo.py    # Stock data repository
│   │   ├── user_repo.py     # User data repository
│   │   └── ...              # Other repositories
│   ├── models/              # Data models (Pydantic)
│   │   ├── domain/          # Domain models
│   │   ├── schemas/         # Request/Response schemas
│   │   └── entities/        # Database entities
│   └── infrastructure/      # Infrastructure components
│       ├── auth/            # Authentication
│       │   ├── api_key.py   # API key handling
│       │   └── ...          # Other auth related
│       ├── cache/           # Caching
│       │   ├── redis.py     # Redis client
│       │   └── ...          # Other cache related
│       └── database/        # Database connections
│           ├── supabase.py  # Supabase client
│           └── ...          # Other database related
├── functions/               # Serverless function handlers
│   ├── api_handler.py       # Main API handler
│   ├── background_jobs.py   # Background processing
│   └── ...                  # Other function handlers
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── conftest.py          # Test configuration
├── scripts/                 # Utility scripts
├── infrastructure/          # Infrastructure as Code
│   ├── terraform/           # Terraform configurations
│   └── ...                  # Other IaC solutions
├── Dockerfile               # Docker configuration for local dev
├── docker-compose.yml       # Docker Compose for local services
├── Makefile                 # Command shortcuts
├── pyproject.toml           # Poetry configuration
├── README.md                # Project documentation
├── serverless.yml           # Serverless Framework configuration
└── .env.example             # Example environment variables
```

### Prerequisites

- Python 3.12+
- Poetry
- Docker & Docker Compose (for local development)
- Make (optional, for command shortcuts)
- AWS CLI or equivalent cloud provider CLI (for deployment)

### Environment Setup

```bash
# Clone repository
git clone https://github.com/yourusername/vnstock-api.git
cd vnstock-api

# Install dependencies
poetry install

# Activate virtual environment
poetry shell

# Set up local services (Redis, PostgreSQL)
docker-compose up -d

# Run development server
make dev
```

## Technical Constraints

1. **Performance Requirements**

   - Response time: <200ms for non-cached requests
   - Response time: <50ms for cached requests
   - Throughput: Support 100+ requests per second
   - Cold start time: <1s for serverless functions

2. **Compatibility**

   - Support for all major vnstock library versions
   - Graceful handling of upstream API changes
   - Support for multiple Python runtime versions

3. **Security**

   - API key rotation
   - Rate limiting
   - Input validation
   - Protection against common attacks (injection, CSRF)

4. **Scalability**

   - Serverless auto-scaling
   - Connection pooling for database
   - Cache optimization

5. **Serverless Constraints**
   - Function timeout limits
   - Memory limitations
   - Cold start considerations
   - State management

## Dependencies

### Production Dependencies

```toml
[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.104.0"
uvicorn = "^0.23.2"
pydantic = "^2.4.2"
strawberry-graphql = "^0.211.1"
redis = "^5.0.1"
asyncpg = "^0.28.0"
vnstock = "^0.2.7"
httpx = "^0.25.0"
python-jose = "^3.3.0"
mangum = "^0.17.0"  # AWS Lambda handler for ASGI apps
supabase = "^2.0.0"
```

### Development Dependencies

```toml
[tool.poetry.dev-dependencies]
pytest = "^7.4.2"
pytest-cov = "^4.1.0"
mypy = "^1.6.1"
flake8 = "^6.1.0"
black = "^23.9.1"
isort = "^5.12.0"
docker-compose = "^1.29.2"
serverless = "^3.34.0"
terraform-local = "^0.0.1"
```

## Third-Party Integrations

1. **vnstock Library**

   - Core library being wrapped
   - All functionality exposed through API
   - Requires monitoring for upstream changes

2. **Supabase**

   - User management
   - API key storage
   - Usage metrics
   - Database-as-a-service

3. **Redis Cloud**

   - Managed Redis service
   - Caching and rate limiting

4. **AWS/Azure/GCP**

   - Serverless platform
   - API Gateway
   - Storage services

5. **Optional: Sentry**
   - Error tracking and monitoring
   - Performance metrics

## Deployment Architecture

```
┌─────────────────┐     ┌────────────────┐     ┌────────────────┐
│  Client Request │────►│  API Gateway   │────►│ Lambda Function│
└─────────────────┘     └────────────────┘     └────────┬───────┘
                                                        │
                        ┌────────────────┐              │
                        │  Redis Cloud   │◄─────────────┤
                        └────────────────┘              │
                                                        │
                        ┌────────────────┐              │
                        │   Supabase     │◄─────────────┘
                        └────────────────┘
```

## Development Workflow

1. **Local Development**

   - Run server using FastAPI's built-in server
   - Use Docker for local dependencies (Redis, PostgreSQL)
   - Test endpoints with Swagger UI or GraphQL Explorer

2. **Testing**

   - Run unit tests with pytest
   - Integration tests using local serverless emulator

3. **Deployment**

   - CI/CD pipeline with GitHub Actions
   - Infrastructure provisioning with Terraform/CDK
   - Deployment using Serverless Framework
   - Staged deployments (dev, staging, production)

4. **Monitoring**
   - CloudWatch Logs or equivalent
   - Serverless metrics dashboard
   - Sentry for error tracking
