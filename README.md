# vnstock-api

A comprehensive API wrapper for the `vnstock` Python library that provides both REST and GraphQL APIs for accessing Vietnamese stock market data.

## Project Overview

This project aims to create a robust API service that exposes the functionality of the `vnstock` Python library through standardized REST and GraphQL interfaces. It includes authentication via API keys, rate limiting, and comprehensive documentation.

## Features

- **REST API**: Access all vnstock library functions through RESTful endpoints
- **GraphQL API**: Flexible data querying with GraphQL
- **API Key Authentication**: Track usage and implement rate limiting
- **Caching**: Redis-based caching for frequently accessed data
- **Data Persistence**: Historical data stored in Supabase/PostgreSQL
- **Documentation**: Comprehensive OpenAPI documentation
- **High Test Coverage**: Maintaining >85% code coverage

## Project Phases

### Phase 1: MVP (Current Focus)

- Implementation of REST API endpoints exposing vnstock functionality
- OpenAPI documentation
- Testing with >85% code coverage

### Phase 2: Expansion

- GraphQL API implementation
- Schema design and resolvers
- GraphQL documentation

### Phase 3: Performance Optimization

- Redis integration for caching frequently accessed data
- Supabase/PostgreSQL for historical data persistence
- Query optimization

### Phase 4: AI Capabilities

- MCP server integration for LLM interaction with the API
- AI-powered analytics and insights

### Phase 5: Productionization

- API key management system
- User registration and management
- Usage tracking and analytics
- Rate limiting and throttling

## Tech Stack

- **Python**: Core programming language
- **Poetry**: Dependency management
- **FastAPI**: API framework
- **GraphQL**: Query language and runtime
- **Supabase/PostgreSQL**: Database for persistence
- **Redis**: Caching layer
- **Pytest**: Testing framework
- **Makefile**: Command management

## Getting Started

### Prerequisites

- Python 3.8+
- Poetry
- Docker (optional, for containerization)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/vnstock-api.git
cd vnstock-api

# Install dependencies
make install

# Run development server
make dev
```

## Documentation

API documentation is available at `/docs` (Swagger UI) or `/redoc` (ReDoc) when the server is running.

## License

[MIT License](LICENSE)
