# Companies REST API

## Overview

The Companies REST API provides endpoints for retrieving information about Vietnamese companies, including company profiles, officers, shareholders, insider trading, subsidiaries, corporate events, news, and dividends. This API interacts with the service layer to fetch and transform data from various data sources, primarily the VNStock library.

## Endpoints

### Get Company Information

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/info`
- **Description**: Retrieves comprehensive information about a company including profile, officers, shareholders, etc.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/info`

### Get Company Profile

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/profile`
- **Description**: Retrieves the profile information for a company.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/profile`

### Get Company Officers

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/officers`
- **Description**: Retrieves information about company officers.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/officers`

### Get Shareholders

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/shareholders`
- **Description**: Retrieves information about major shareholders.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/shareholders`

### Get Insider Trading

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/insider-trading`
- **Description**: Retrieves insider trading information.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/insider-trading`

### Get Subsidiaries

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/subsidiaries`
- **Description**: Retrieves information about company subsidiaries.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/subsidiaries`

### Get Company Events

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/events`
- **Description**: Retrieves corporate events information.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/events`

### Get Company News

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/news`
- **Description**: Retrieves news related to the company.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/news`

### Get Dividends

- **Method**: GET
- **Path**: `/api/v1/companies/{symbol}/dividends`
- **Description**: Retrieves dividend payment history.
- **Parameters**:
  - `symbol` (path parameter, required): Stock symbol/ticker for the company
  - `source` (query parameter, optional): Data source identifier. Default: "vnstock"
- **Example request**: `GET /api/v1/companies/VNM/dividends`

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

The Companies REST API is implemented using FastAPI's router mechanism. Each endpoint:

1. Receives the request with the stock symbol and optional source parameter
2. Uses dependency injection to get an instance of the CompanyService
3. Calls the appropriate service method to retrieve and transform the data
4. Formats the response with the standard data and metadata structure
5. Handles exceptions and returns appropriate error responses

The implementation uses async/await for all operations to ensure optimal performance.

## Future Enhancements

- Add filtering and pagination for list endpoints
- Implement caching to improve performance
- Add rate limiting to prevent abuse
- Support batch operations for multiple symbols
- Add more detailed company financial data endpoints
