# vnstock_adapter

## Overview

This module provides adapter functions that interface with the vnstock library. It wraps the original library functions with standardized error handling, response formatting, and caching support.

## Functions

### get_stock_price(symbol: str, start_date: str = None, end_date: str = None) -> dict

**Description:**
Retrieves the stock price data for a specified symbol within an optional date range.

**Parameters:**

- `symbol` (str): The stock symbol to retrieve price data for
- `start_date` (str, optional): Start date in "YYYY-MM-DD" format. If not provided, retrieves data from 30 days ago.
- `end_date` (str, optional): End date in "YYYY-MM-DD" format. If not provided, uses the current date.

**Returns:**
Dictionary containing stock price data with the following structure:

```json
{
  "data": [
    {
      "date": "YYYY-MM-DD",
      "open": 123.45,
      "high": 126.78,
      "low": 122.45,
      "close": 125.67,
      "volume": 1234567
    },
    ...
  ],
  "meta": {
    "symbol": "XXX",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
}
```

**Example:**

```python
from app.adapters.vnstock_adapter import get_stock_price

# Get stock price for VNM from 2023-01-01 to 2023-01-31
price_data = get_stock_price("VNM", "2023-01-01", "2023-01-31")
```

**Notes:**

- Returns cached data when available and within cache expiration
- Raises `StockSymbolNotFoundError` if the symbol doesn't exist
- Raises `DateRangeInvalidError` if the date range is invalid
- Handles network errors and retries up to 3 times

### get_stock_info(symbol: str) -> dict

**Description:**
Retrieves detailed information for a specific stock symbol.

**Parameters:**

- `symbol` (str): The stock symbol to retrieve information for

**Returns:**
Dictionary containing company information with the following structure:

```json
{
  "data": {
    "symbol": "XXX",
    "company_name": "Company Full Name",
    "exchange": "HOSE",
    "industry": "Industry Name",
    "market_cap": 1234567890,
    "company_profile": "Description of the company...",
    "financial_indicators": {
      "pe_ratio": 12.34,
      "pb_ratio": 2.34,
      "dividend_yield": 0.045,
      ...
    }
  },
  "meta": {
    "retrieved_at": "YYYY-MM-DD HH:MM:SS"
  }
}
```

**Example:**

```python
from app.adapters.vnstock_adapter import get_stock_info

# Get information for VNM
stock_info = get_stock_info("VNM")
company_name = stock_info["data"]["company_name"]
```

**Notes:**

- Cache expiration is longer for company information (24 hours)
- Raises `StockSymbolNotFoundError` if the symbol doesn't exist

### get_market_overview() -> dict

**Description:**
Retrieves an overview of the current market status including indexes and top movers.

**Parameters:**
None

**Returns:**
Dictionary containing market overview data with the following structure:

```json
{
  "data": {
    "indexes": [
      {
        "code": "VNINDEX",
        "name": "VN Index",
        "value": 1234.56,
        "change": 12.34,
        "percent_change": 1.23
      },
      ...
    ],
    "top_gainers": [...],
    "top_losers": [...],
    "top_volume": [...]
  },
  "meta": {
    "timestamp": "YYYY-MM-DD HH:MM:SS"
  }
}
```

**Example:**

```python
from app.adapters.vnstock_adapter import get_market_overview

# Get current market overview
market_data = get_market_overview()
vn_index = next(idx for idx in market_data["data"]["indexes"] if idx["code"] == "VNINDEX")
```

**Notes:**

- Cache expiration is short (5 minutes) due to frequently changing data
- This is a high-volume endpoint and may be subject to more aggressive rate limiting

## Classes

### VnstockAdapter

**Description:**
Class-based interface to the vnstock library that maintains session information and provides access to all adapter functions.

**Methods:**

- `__init__(cache_service=None, retry_count=3)`: Initialize the adapter with optional caching and retry configuration
- `get_stock_price(symbol, start_date=None, end_date=None)`: Get stock price data
- `get_stock_info(symbol)`: Get company information
- `get_market_overview()`: Get market overview

**Example:**

```python
from app.adapters.vnstock_adapter import VnstockAdapter
from app.services.cache_service import CacheService

cache_service = CacheService()
adapter = VnstockAdapter(cache_service=cache_service)

# Use the adapter to get stock data
stock_data = adapter.get_stock_price("VNM")
```

**Notes:**

- The class-based approach is preferred for dependency injection and testing
- The functional interface calls the class methods with a shared instance
- Cache service is optional but recommended for production use
