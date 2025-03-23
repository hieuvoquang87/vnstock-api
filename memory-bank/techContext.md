# Technical Context: vnstock-api

## Technologies Used

### Core Technologies

1. **Python 3.8+**

   - Primary programming language
   - Leverages type hints for better code quality

2. **FastAPI**

   - Modern, high-performance web framework
   - Native async support for high concurrency
   - Automatic OpenAPI documentation generation

3. **GraphQL (Strawberry)**

   - Type-first GraphQL library for Python
   - Code-first schema generation
   - Integration with FastAPI

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

   - Primary database for persistent storage
   - Stores user information, API keys, usage metrics
   - Keeps historical data to reduce third-party API calls

2. **Redis**
   - In-memory data structure store
   - Used for distributed caching
   - Supports rate limiting implementation
   - Pub/sub for event-driven features

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

### CI/CD

1. **GitHub Actions**

   - Continuous integration
   - Automated testing
   - Deployment pipelines

2. **Docker**
   - Containerization
   - Consistent environments

## Development Setup

### Local Development

```
vnstock-api/
├── .venv/                   # Virtual environment (created by Poetry)
├── .github/                 # GitHub Actions workflows
├── app/                     # Main application package
│   ├── api/                 # API routes and handlers
│   │   ├── rest/            # REST API endpoints
│   │   └── graphql/         # GraphQL schema and resolvers
│   ├── core/                # Core functionality
│   │   ├── config.py        # Configuration settings
│   │   ├── exceptions.py    # Custom exceptions
│   │   └── logging.py       # Logging configuration
│   ├── services/            # Business logic layer
│   ├── adapters/            # Integration with vnstock
│   ├── repositories/        # Data access layer
│   ├── models/              # Data models (Pydantic)
│   │   ├── domain/          # Domain models
│   │   ├── schemas/         # Request/Response schemas
│   │   └── entities/        # Database entities
│   └── infrastructure/      # Infrastructure components
│       ├── auth/            # Authentication
│       ├── cache/           # Caching
│       └── database/        # Database connections
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── conftest.py          # Test configuration
├── scripts/                 # Utility scripts
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── Makefile                 # Command shortcuts
├── pyproject.toml           # Poetry configuration
└── README.md                # Project documentation
```

### Prerequisites

- Python 3.8+
- Poetry
- Docker & Docker Compose (for local services)
- Make (optional, for command shortcuts)

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

2. **Compatibility**

   - Support for all major vnstock library versions
   - Graceful handling of upstream API changes

3. **Security**

   - API key rotation
   - Rate limiting
   - Input validation
   - Protection against common attacks (injection, CSRF)

4. **Scalability**
   - Horizontal scaling for API servers
   - Connection pooling for database
   - Load balancing across instances

## Dependencies

### Production Dependencies

```toml
[tool.poetry.dependencies]
python = "^3.8"
fastapi = "^0.95.0"
uvicorn = "^0.21.1"
pydantic = "^1.10.7"
strawberry-graphql = "^0.175.1"
redis = "^4.5.4"
asyncpg = "^0.27.0"
vnstock = "^0.2.7"
httpx = "^0.24.0"
python-jose = "^3.3.0"
```

### Development Dependencies

```toml
[tool.poetry.dev-dependencies]
pytest = "^7.3.1"
pytest-cov = "^4.1.0"
mypy = "^1.2.0"
flake8 = "^6.0.0"
black = "^23.3.0"
isort = "^5.12.0"
docker-compose = "^1.29.2"
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

3. **Optional: Sentry**
   - Error tracking and monitoring
   - Performance metrics
