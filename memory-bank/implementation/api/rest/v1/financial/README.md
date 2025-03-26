# Financial Reports REST API

## Overview

The Financial Reports REST API provides endpoints for retrieving financial information about Vietnamese companies, including financial statements, ratios, and other financial metrics. This API interacts with the service layer to fetch and transform data from various data sources.

## Endpoints

### Get Financial Statements

- **Method**: GET
- **Path**: `/api/v1/financial/{symbol}/statements`
- **Description**: Retrieves financial statements (income statement, balance sheet, cash flow) for a company.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `period` (query parameter, required): Financial period (quarterly/yearly)
  - `year` (query parameter, required): Year of the financial statement
  - `quarter` (query parameter, optional): Quarter number (1-4) for quarterly statements
  - `source` (query parameter, optional): Data source identifier. Default: "unified"
- **Example request**: `GET /api/v1/financial/VNM/statements?period=quarterly&year=2023&quarter=4`

### Get Financial Ratios

- **Method**: GET
- **Path**: `/api/v1/financial/{symbol}/ratios`
- **Description**: Retrieves key financial ratios for a company.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `period` (query parameter, required): Financial period (quarterly/yearly)
  - `year` (query parameter, required): Year of the financial ratios
  - `quarter` (query parameter, optional): Quarter number (1-4) for quarterly ratios
  - `source` (query parameter, optional): Data source identifier. Default: "unified"
- **Example request**: `GET /api/v1/financial/VNM/ratios?period=quarterly&year=2023&quarter=4`

### Get Financial Analysis

- **Method**: GET
- **Path**: `/api/v1/financial/{symbol}/analysis`
- **Description**: Retrieves financial analysis and metrics for a company.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `period` (query parameter, required): Financial period (quarterly/yearly)
  - `year` (query parameter, required): Year of the analysis
  - `quarter` (query parameter, optional): Quarter number (1-4) for quarterly analysis
  - `source` (query parameter, optional): Data source identifier. Default: "unified"
- **Example request**: `GET /api/v1/financial/VNM/analysis?period=quarterly&year=2023&quarter=4`

### Get Financial History

- **Method**: GET
- **Path**: `/api/v1/financial/{symbol}/history`
- **Description**: Retrieves historical financial data for a company.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `period` (query parameter, required): Financial period (quarterly/yearly)
  - `start_year` (query parameter, required): Start year of the historical data
  - `end_year` (query parameter, required): End year of the historical data
  - `source` (query parameter, optional): Data source identifier. Default: "unified"
- **Example request**: `GET /api/v1/financial/VNM/history?period=yearly&start_year=2020&end_year=2023`

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

The Financial Reports REST API is implemented using FastAPI's router mechanism. Each endpoint:

1. Receives the request with the stock symbol and required parameters
2. Uses dependency injection to get an instance of the FinancialService
3. Calls the appropriate service method to retrieve and transform the data
4. Formats the response with the standard data and metadata structure
5. Handles exceptions and returns appropriate error responses

The implementation uses async/await for all operations to ensure optimal performance.

## Future Enhancements

- Add filtering and pagination for historical data
- Implement caching to improve performance
- Add rate limiting to prevent abuse
- Support batch operations for multiple symbols
- Add more detailed financial metrics and analysis
- Support custom date ranges for historical data
- Add financial statement comparison features
