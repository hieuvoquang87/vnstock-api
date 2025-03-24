# System Patterns: vnstock-api

## Architecture Overview

The `vnstock-api` follows a layered architecture pattern to ensure separation of concerns and maintainability. The system is designed with the following key components:

```
┌─────────────────────────────────────────────────────────┐
│                      Client Layer                        │
│  (External applications consuming REST/GraphQL APIs)     │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    API Gateway Layer                     │
│     (Authentication, Rate Limiting, Request Routing)     │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                     Service Layer                        │
│      (Business Logic, Data Transformation, Caching)      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    Integration Layer                     │
│           (vnstock Library, External APIs)               │
└─────────────────────────────────────────────────────────┘
```

## Key Technical Decisions

1. **Framework Choice**: FastAPI

   - Reasons: High performance, automatic OpenAPI documentation, native async support, type hints
   - Alternatives considered: Flask, Django REST Framework

2. **API Design Approach**: Resource-based REST + GraphQL

   - REST: Follow RESTful principles with resource-based URLs and appropriate HTTP methods
   - GraphQL: Single endpoint with schema that mirrors vnstock library functionality

3. **Authentication Strategy**: API Key-based

   - Simple header-based authentication (X-API-Key)
   - Future expansion to support OAuth for enterprise integrations

4. **Caching Strategy**: External Managed Service

   - Redis Cloud for distributed caching across instances
   - Time-based expiration depending on data volatility
   - Optimize for serverless environment

5. **Database Strategy**: Managed Service

   - Supabase/PostgreSQL as Database-as-a-Service
   - Separate tables for historical data vs. operational data
   - Connection pooling optimized for serverless

6. **Deployment Model**: Serverless

   - AWS Lambda functions or similar serverless platform
   - API Gateway for routing and management
   - Infrastructure as Code (IaC) using Terraform/AWS CDK
   - Separate functions for high-load operations

7. **Documentation Strategy**: Code-Mirroring Documentation

   - Markdown documentation files that mirror the application structure
   - Each implementation file has an equivalent documentation file
   - Detailed function documentation with explanations, parameters, and examples
   - Living documentation that evolves with the code

## Design Patterns in Use

1. **Repository Pattern**

   - Abstract data access logic
   - Facilitate testing through mocking
   - Implementation: `repositories/` module

2. **Adapter Pattern**

   - Bridge between vnstock library and API
   - Standardize data formats
   - Implementation: `adapters/vnstock_adapter.py`

3. **Factory Pattern**

   - Create different types of response objects
   - Support various output formats
   - Implementation: `factories/response_factory.py`

4. **Decorator Pattern**

   - Add cross-cutting concerns (logging, caching, validation)
   - Separate core business logic
   - Implementation: Python decorators in `decorators/` module

5. **Strategy Pattern**
   - Different caching strategies based on data type
   - Pluggable rate limiting algorithms
   - Implementation: `strategies/` module

## Component Relationships

### Core Components

1. **API Controllers**

   - REST endpoints: `api/rest/`
   - GraphQL resolvers: `api/graphql/`
   - Responsibilities: Request validation, response formatting

2. **Service Layer**

   - Business logic: `services/`
   - Caching logic: `services/cache/`
   - Responsibilities: Orchestration, transformation

3. **Data Access Layer**

   - Data sources: `datasources/`
   - Database repositories: `repositories/`
   - Responsibilities: Data retrieval, persistence, and external system integration

4. **Infrastructure Layer**
   - Authentication: `infrastructure/auth/`
   - Rate limiting: `infrastructure/throttling/`
   - Monitoring: `infrastructure/monitoring/`
   - Responsibilities: Cross-cutting concerns

### Data Flow

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Client  │─►  │Controller│─►  │ Service  │─►  │DataSource│
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                      ▲               │               │
                      │               ▼               ▼
                      │         ┌──────────┐    ┌──────────┐
                      └─────────│  Cache   │    │ External │
                                └──────────┘    │  Systems │
                                               └──────────┘
```

## File Structure

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
│   ├── datasources/         # External data source integrations
│   │   ├── vnstock_adapter.py # Adapter for vnstock library
│   │   ├── external_api/    # External API integrations
│   │   ├── database/        # Database abstractions
│   │   └── realtime/        # Real-time data sources
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
├── docs/                    # Documentation
│   ├── implementation/      # Implementation documentation
│   │   ├── api/             # API documentation
│   │   │   ├── rest/        # REST API documentation
│   │   │   │   ├── v1/      # API v1 documentation
│   │   │   │   │   ├── stocks/ # Stock endpoints documentation
│   │   │   │   │   └── market/ # Market endpoints documentation
│   │   │   └── graphql/     # GraphQL documentation
│   │   │       └── resolvers/ # Resolvers documentation
│   │   ├── core/            # Core functionality documentation
│   │   ├── services/        # Services documentation
│   │   ├── datasources/     # Data sources documentation
│   │   ├── repositories/    # Repositories documentation
│   │   ├── models/          # Models documentation
│   │   └── infrastructure/  # Infrastructure documentation
│   └── guides/              # User and developer guides
├── functions/               # Serverless function handlers
│   ├── api_handler.py       # Main API handler
│   ├── background_jobs.py   # Background processing
│   └── ...                  # Other function handlers
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   │   ├── api/             # API tests
│   │   ├── services/        # Service tests
│   │   └── ...              # Other unit tests
│   ├── integration/         # Integration tests
│   │   ├── api/             # API integration tests
│   │   └── ...              # Other integration tests
│   └── conftest.py          # Test configuration
├── scripts/                 # Utility scripts
│   ├── deploy.sh            # Deployment script
│   └── ...                  # Other scripts
├── infrastructure/          # Infrastructure as Code
│   ├── terraform/           # Terraform configurations
│   │   ├── main.tf          # Main Terraform configuration
│   │   └── ...              # Other Terraform files
│   └── ...                  # Other IaC solutions
├── Dockerfile               # Docker configuration for local dev
├── docker-compose.yml       # Docker Compose for local services
├── Makefile                 # Command shortcuts
├── pyproject.toml           # Poetry configuration
├── README.md                # Project documentation
├── serverless.yml           # Serverless Framework configuration
└── .env.example             # Example environment variables
```

## Testing Strategy

1. **Unit Testing**

   - Focus on service and adapter layers
   - Mock external dependencies

2. **Integration Testing**

   - Test API endpoints with mocked vnstock
   - Test caching behavior

3. **End-to-End Testing**

   - Full API tests with real vnstock integration
   - Performance and load testing

4. **Serverless Testing**
   - Local serverless environment testing
   - Cloud-based testing in staging environment

## Documentation Strategy

1. **Implementation Documentation**

   - Mirror the application structure in `docs/implementation/`
   - Each implementation file (`.py`) has a corresponding documentation file (`.md`)
   - Document all functions, classes, and methods with parameters, return types, and examples
   - Keep documentation synchronized with code changes

2. **Documentation Format**

   - Function descriptions in Markdown format
   - Parameter and return type documentation
   - Usage examples and edge cases
   - Integration notes where applicable

3. **Documentation Maintenance**
   - Update documentation with each code change
   - Review documentation during code reviews
   - Automate documentation checks in CI pipeline

## Serverless Considerations

1. **Cold Start Optimization**

   - Keep dependencies minimal
   - Use lazy loading where appropriate
   - Optimize initialization code

2. **Statelessness**

   - Design functions to be stateless
   - Use external services for state management
   - Share common code through layers

3. **Function Sizing**
   - Break complex operations into smaller functions
   - Balance function size vs. cold start time
   - Consider provisioned concurrency for critical paths
