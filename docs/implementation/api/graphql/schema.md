# GraphQL Schema

## Overview

The GraphQL schema defines the types and resolvers for the vnstock API's GraphQL interface. Currently, the implementation uses hard-coded mock data to facilitate development and testing while the REST API is being finalized.

## Usage Note

As per the project decision, the GraphQL implementation is currently using mock data. We will revisit and implement the actual data source integration after the REST API is finalized. This allows for proper alignment between the REST and GraphQL interfaces and prevents duplication of effort during early development.

## Schema Structure

The schema follows a resource-based structure that mirrors the data available through the vnstock library:

- Query type with fields for various stock data
- Type definitions for structured responses
- Mock resolvers that return representative data

## Types

The schema includes the following primary types:

- `CompanyProfile`: Company overview information
- `CompanyOfficer`: Information about company management
- `Shareholder`: Major shareholders data
- `InsiderTrading`: Insider trading activity
- `Subsidiary`: Company subsidiaries
- `CompanyEvent`: Corporate events
- `CompanyNews`: Company news articles
- `Dividend`: Dividend payment history
- `DataSource`: Enum for data source selection

## Resolvers

All resolvers currently return mock data for development purposes. The primary resolvers include:

### company_profile(symbol: String!)

**Description:**
Returns mock company profile information for a given symbol.

**Parameters:**

- `symbol` (String!): The stock ticker symbol

**Returns:**
A CompanyProfile object with mock data for the requested symbol.

### company_officers(symbol: String!)

**Description:**
Returns mock company officers for a given symbol.

**Parameters:**

- `symbol` (String!): The stock ticker symbol

**Returns:**
A list of CompanyOfficer objects with mock data.

### shareholders(symbol: String!)

**Description:**
Returns mock major shareholders for a given symbol.

**Parameters:**

- `symbol` (String!): The stock ticker symbol

**Returns:**
A list of Shareholder objects with mock data.

### insider_trading(symbol: String!)

**Description:**
Returns mock insider trading data for a given symbol.

**Parameters:**

- `symbol` (String!): The stock ticker symbol

**Returns:**
A list of InsiderTrading objects with mock data.

## Example Queries

```graphql
# Get company profile
query {
  companyProfile(symbol: "FPT") {
    symbol
    companyName
    exchange
    industry
    website
    businessSummary
  }
}

# Get company officers
query {
  companyOfficers(symbol: "FPT") {
    name
    position
    age
    nationality
    shares
  }
}
```

## Future Enhancements

When implementing the final GraphQL API with real data sources:

1. Connect resolvers to the actual data services
2. Add pagination for list responses
3. Implement filtering capabilities
4. Add DataLoader for efficient data fetching
5. Integrate with Redis for caching
6. Add error handling and validation

## Notes

- All field names follow camelCase naming convention in GraphQL responses
- The DataSource enum allows selecting the data provider in future implementations
- Mock data provides representative examples of the data structure
