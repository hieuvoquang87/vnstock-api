# exceptions

## Overview

This module defines custom exceptions for the VNStock API. It provides a consistent error handling approach that follows RFC 7807 (Problem Details for HTTP APIs) with standardized error responses.

## Classes

### VNStockAPIException

**Description:**
Base exception class for all VNStock API exceptions. Extends FastAPI's HTTPException with a structured error format.

**Parameters:**

- `status_code` (int): HTTP status code to return
- `detail` (str): Human-readable error message
- `error_code` (str, optional): Machine-readable error code, defaults to "INTERNAL_ERROR"
- `headers` (dict, optional): Additional HTTP headers to include in the response

**Returns:**
An HTTPException with a structured response body containing error details.

**Example:**

```python
from app.core.exceptions import VNStockAPIException

# Raise a custom API exception
raise VNStockAPIException(
    status_code=400,
    detail="Something went wrong with your request",
    error_code="CUSTOM_ERROR"
)

# Response body:
# {
#   "error": {
#     "code": "CUSTOM_ERROR",
#     "message": "Something went wrong with your request",
#     "details": {}
#   }
# }
```

### StockSymbolNotFoundError

**Description:**
Exception raised when a stock symbol is not found.

**Parameters:**

- `symbol` (str): The stock symbol that was not found

**Returns:**
A VNStockAPIException with status code 404 and appropriate error message.

**Example:**

```python
from app.core.exceptions import StockSymbolNotFoundError

# Raise a stock symbol not found exception
raise StockSymbolNotFoundError(symbol="INVALID")

# Response body:
# {
#   "error": {
#     "code": "STOCK_SYMBOL_NOT_FOUND",
#     "message": "Stock symbol 'INVALID' not found",
#     "details": {}
#   }
# }
```

### DateRangeInvalidError

**Description:**
Exception raised when a date range is invalid.

**Parameters:**

- `start_date` (str, optional): The invalid start date
- `end_date` (str, optional): The invalid end date

**Returns:**
A VNStockAPIException with status code 400 and appropriate error message.

**Example:**

```python
from app.core.exceptions import DateRangeInvalidError

# Raise a date range invalid exception
raise DateRangeInvalidError(start_date="2023-01-01", end_date="2022-01-01")

# Response body:
# {
#   "error": {
#     "code": "DATE_RANGE_INVALID",
#     "message": "Invalid date range: start_date (2023-01-01) to end_date (2022-01-01)",
#     "details": {}
#   }
# }
```

### RateLimitExceededError

**Description:**
Exception raised when rate limit is exceeded.

**Parameters:**

- `limit` (int): The rate limit that was exceeded
- `reset_time` (str): When the rate limit will reset

**Returns:**
A VNStockAPIException with status code 429 and appropriate error message and headers.

**Example:**

```python
from app.core.exceptions import RateLimitExceededError

# Raise a rate limit exceeded exception
raise RateLimitExceededError(limit=60, reset_time="2023-01-01T12:00:00Z")

# Response body:
# {
#   "error": {
#     "code": "RATE_LIMIT_EXCEEDED",
#     "message": "Rate limit exceeded. Limit: 60 requests per minute",
#     "details": {}
#   }
# }
#
# Response headers:
# X-RateLimit-Reset: 2023-01-01T12:00:00Z
```

### ExternalAPIError

**Description:**
Exception raised when an external API returns an error.

**Parameters:**

- `service` (str): The name of the external service that returned an error
- `message` (str): The error message from the external service

**Returns:**
A VNStockAPIException with status code 502 and appropriate error message.

**Example:**

```python
from app.core.exceptions import ExternalAPIError

# Raise an external API error exception
raise ExternalAPIError(service="vnstock", message="Connection timeout")

# Response body:
# {
#   "error": {
#     "code": "EXTERNAL_API_ERROR",
#     "message": "Error from external service (vnstock): Connection timeout",
#     "details": {}
#   }
# }
```

## Notes

- All exceptions follow RFC 7807 (Problem Details for HTTP APIs) format
- Exceptions include machine-readable error codes for clients to handle programmatically
- The base exception can be extended for additional custom exceptions as needed
- Some exceptions add custom headers to provide additional information (e.g., RateLimitExceededError adds X-RateLimit-Reset)
