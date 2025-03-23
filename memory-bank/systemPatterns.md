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

4. **Caching Strategy**: Two-tiered

   - In-memory cache for very high-frequency data
   - Redis for distributed caching across instances
   - Time-based expiration depending on data volatility

5. **Database Strategy**: Hybrid

   - Supabase/PostgreSQL for persistent storage
   - Separate tables for historical data vs. operational data

6. **Deployment Model**: Containerized Microservices
   - Separate services for REST API, GraphQL, Authentication, and Data Processing
   - Kubernetes orchestration for production

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

   - vnstock adapters: `adapters/`
   - Database repositories: `repositories/`
   - Responsibilities: Data retrieval, persistence

4. **Infrastructure Layer**
   - Authentication: `infrastructure/auth/`
   - Rate limiting: `infrastructure/throttling/`
   - Monitoring: `infrastructure/monitoring/`
   - Responsibilities: Cross-cutting concerns

### Data Flow

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Client  │─►  │Controller│─►  │ Service  │─►  │ Adapter  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                      ▲               │               │
                      │               ▼               ▼
                      │         ┌──────────┐    ┌──────────┐
                      └─────────│  Cache   │    │ vnstock  │
                                └──────────┘    └──────────┘
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
