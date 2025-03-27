# Listing API Routes

## Overview

This module implements REST API endpoints for the listing service, providing access to stock listings and related information from different data sources (VCI, TCBS). It follows the standard API response format and includes proper error handling and logging.

## Router

The router is created with the prefix "/listing" and includes standard error responses.

## Dependencies

### get_listing_service

**Description:**
A FastAPI dependency function that creates and returns a ListingService instance with the specified data source.

**Parameters:**

- `source` (str): Data source to use (vci, tcbs), default is "vci"

**Returns:**
An instance of the ListingService.

**Raises:**

- HTTPException(400): If the source is invalid
- HTTPException(500): If there's an error creating the service

## Endpoints

### GET /api/v1/listing/symbols

**Description:**
Get a list of all available symbols including stock code, company name, exchange, industry, etc.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing the list of symbols.

**Example:**

```
GET /api/v1/listing/symbols?source=vci
```

### GET /api/v1/listing/symbols/by-industry

**Description:**
Get symbols organized by their respective industries.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing symbols grouped by industry.

**Example:**

```
GET /api/v1/listing/symbols/by-industry?source=vci
```

### GET /api/v1/listing/symbols/by-exchange

**Description:**
Get symbols organized by their respective exchanges.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing symbols grouped by exchange.

**Example:**

```
GET /api/v1/listing/symbols/by-exchange?source=vci
```

### GET /api/v1/listing/symbols/by-group/{group}

**Description:**
Get symbols that are part of a specific group like VN30, HNX30, etc.

**Parameters:**

- `group` (path, required): Group name (e.g., VN30, HNX30)
- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing symbols in the specified group.

**Example:**

```
GET /api/v1/listing/symbols/by-group/VN30?source=vci
```

### GET /api/v1/listing/industries/icb

**Description:**
Get industry classification benchmark data.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing industry classification benchmark data.

**Example:**

```
GET /api/v1/listing/industries/icb?source=vci
```

### GET /api/v1/listing/future-indices

**Description:**
Get all available future indices.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing future indices data.

**Example:**

```
GET /api/v1/listing/future-indices?source=vci
```

### GET /api/v1/listing/covered-warrants

**Description:**
Get all available covered warrants.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing covered warrants data.

**Example:**

```
GET /api/v1/listing/covered-warrants?source=vci
```

### GET /api/v1/listing/bonds

**Description:**
Get all available bonds.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing bonds data.

**Example:**

```
GET /api/v1/listing/bonds?source=vci
```

### GET /api/v1/listing/government-bonds

**Description:**
Get all available government bonds.

**Parameters:**

- `source` (query, optional): Data source to use (vci, tcbs)

**Returns:**
An ApiResponse containing government bonds data.

**Example:**

```
GET /api/v1/listing/government-bonds?source=vci
```

## Error Handling

All endpoints include standardized error handling:

- NotImplementedError: Returns a 501 status code for methods not implemented by the current data source
- General exceptions: Returns a 500 status code with the error message
- All errors are logged for debugging purposes

## Notes

- The API uses dependency injection to create and manage the listing service
- All endpoints support switching between different data sources via the query parameter
- Some endpoints may not be supported by all data sources and will return appropriate error responses
- Response data is converted to DataFrame format for consistent structure
