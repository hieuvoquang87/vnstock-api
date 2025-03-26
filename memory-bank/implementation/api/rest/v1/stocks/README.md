# Stocks REST API

## Overview

The Stocks REST API provides endpoints for retrieving information about Vietnamese stocks, including price data, historical price data, and other stock-related information. This API interacts with the service layer to fetch and transform data from various data sources, primarily the VNStock library.

## Endpoints

### Get Stock Price

- **Method**: GET
- **Path**: `/api/v1/stocks/{symbol}/price`
- **Description**: Retrieves the current price and basic trading information for a stock.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/stocks/VNM/price`

## Response Format

All endpoints follow a standard response format:

```json
{
  "data": {
    // The actual response data
    // Structure varies depending on the endpoint
  },
  "meta": {
    "timestamp": "2023-05-01T12:34:56.789Z",
    "version": "1.0"
  }
}
```

## Error Responses

Errors are returned with appropriate HTTP status codes and follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

Common error status codes:

- 400: Bad Request - The request was malformed
- 404: Not Found - The requested resource was not found
- 500: Internal Server Error - Something went wrong on the server

## Implementation Details

The Stocks REST API is implemented using FastAPI's router mechanism. Each endpoint:

1. Receives the request with the stock symbol and optional source parameter
2. Uses dependency injection to get an instance of the StockService (to be implemented)
3. Calls the appropriate service method to retrieve and transform the data
4. Formats the response with the standard data and metadata structure
5. Handles exceptions and returns appropriate error responses

The implementation uses async/await for all operations to ensure optimal performance.

## Future Enhancements

- Implement historical price data endpoints
- Add technical analysis endpoints
- Add stock screening functionality
- Implement watchlist functionality
- Add portfolio analysis capabilities
