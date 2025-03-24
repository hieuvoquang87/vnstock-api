# Data Sources

## Overview

The `datasources` directory contains all modules that interact with external data providers or systems. This layer serves as a clean abstraction for all data access, isolating the rest of the application from the specific implementation details of various data sources.

## Purpose

The datasources layer has several key responsibilities:

1. **Abstraction**: Isolate the rest of the application from the implementation details of external data sources
2. **Standardization**: Provide consistent interfaces, error handling, and response formats
3. **Optimization**: Implement caching, batching, and retry logic
4. **Resilience**: Handle failures and ensure robust operation when external systems are unavailable
5. **Monitoring**: Capture performance metrics and availability information

## Types of Data Sources

The application interacts with various types of data sources:

| Type            | Purpose                      | Examples                                         |
| --------------- | ---------------------------- | ------------------------------------------------ |
| VNStock Library | Vietnamese stock market data | Price data, company information, market indices  |
| External APIs   | Supplementary financial data | International markets, news, economic indicators |
| Databases       | Persistent storage           | User data, cached results, analytics             |
| WebSockets      | Real-time updates            | Live price feeds, market alerts                  |
| File Systems    | Imports and exports          | CSV files, reports, batch data                   |

## Directory Structure

```
datasources/
├── vnstock_adapter.py      # Adapter for vnstock library
├── external_api/           # External API integrations
│   ├── news_api.py         # News data source
│   └── forex_api.py        # Foreign exchange data
├── database/               # Database abstractions
│   ├── supabase.py         # Supabase client
│   └── models.py           # Database models
└── realtime/               # Real-time data sources
    └── websocket.py        # WebSocket client
```

## Implementation Patterns

Each data source module should follow these patterns:

1. **Functional Interface**: Provide simple function-based interfaces for common operations
2. **Class-Based API**: Offer a class for more complex usage with state management
3. **Error Handling**: Convert external errors to application-specific exceptions
4. **Response Normalization**: Transform external data formats to application models
5. **Caching**: Implement appropriate caching strategies based on data characteristics
6. **Retry Logic**: Handle transient failures with configurable retry policies
7. **Logging**: Include comprehensive logging for troubleshooting

## Usage Guidelines

When implementing or using data sources:

1. Always use dependency injection for services that depend on data sources
2. Add appropriate unit tests with mocked external dependencies
3. Include integration tests for critical data flows
4. Document all public interfaces, including parameters and return values
5. Add examples for common usage patterns
6. Consider rate limiting and quotas for external services
7. Implement appropriate error handling at the service layer
