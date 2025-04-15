# Listing Tools Implementation Plan

## Overview

This document outlines the implementation plan for `listing_tools.py`, which serves as an interface between the VNStock API's listing services and an LLM Agent. The tools will follow a consistent pattern to provide stock listing data in a format suitable for LLM consumption.

## Implementation Strategy

Each function in the `ListingService` class will have a corresponding function in `listing_tools.py` that:

1. Instantiates the ListingService
2. Calls the appropriate service method
3. Formats the response in a standardized structure with status and data fields
4. Handles exceptions gracefully

## Function Implementations

### 1. get_all_symbols()

**Status:** Already implemented  
**Purpose:** Retrieves all available stock symbols

```python
async def get_all_symbols() -> dict:
    """Get all available stock symbols from the vnstock API.

    Returns:
        dict: A dictionary containing:
            - metadata: Additional information about the request
            - totalCount: The total number of symbols available
            - records: List of symbol objects with their details

    Example response:
        {
            "metadata": {},
            "totalCount": 1602,
            "records": [
                {
                    "symbol": "AAA",
                    "exchange": "HOSE",
                    ...
                },
                ...
            ]
        }
    """
    try:
        listing_service = ListingService()
        result = await listing_service.get_all_symbols()
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error getting all symbols: {str(e)}"
        }
```

### 2. get_symbols_by_industries()

**Status:** To be implemented  
**Purpose:** Retrieves symbols grouped by industry

```python
async def get_symbols_by_industries() -> dict:
    """Get stock symbols grouped by industry from the vnstock API.

    Returns:
        dict: A dictionary containing:
            - metadata: Additional information about the request
            - totalCount: The total number of industry categories
            - records: List of industries with their symbols

    Example response:
        {
            "metadata": {},
            "totalCount": 30,
            "records": [
                {
                    "industryName": "Banking",
                    "symbols": ["TCB", "VCB", "MBB", ...]
                },
                ...
            ]
        }
    """
    try:
        listing_service = ListingService()
        result = await listing_service.get_symbols_by_industries()
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error getting symbols by industries: {str(e)}"
        }
```

### 3. get_symbols_by_exchange()

**Status:** To be implemented  
**Purpose:** Retrieves symbols grouped by exchange

```python
async def get_symbols_by_exchange() -> dict:
    """Get stock symbols grouped by exchange from the vnstock API.

    Returns:
        dict: A dictionary containing:
            - metadata: Additional information about the request
            - totalCount: The total number of exchanges
            - records: List of exchanges with their symbols

    Example response:
        {
            "metadata": {},
            "totalCount": 3,
            "records": [
                {
                    "exchange": "HOSE",
                    "symbols": ["TCB", "VCB", "MBB", ...]
                },
                ...
            ]
        }
    """
    try:
        listing_service = ListingService()
        result = await listing_service.get_symbols_by_exchange()
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error getting symbols by exchange: {str(e)}"
        }
```

### 4. get_symbols_by_group()

**Status:** To be implemented  
**Purpose:** Retrieves symbols in a specific group (e.g., VN30, HNX30)

```python
async def get_symbols_by_group(group: str = "VN30") -> dict:
    """Get stock symbols in a specific group from the vnstock API.

    Args:
        group: The stock group name (default: "VN30")

    Returns:
        dict: A dictionary containing:
            - metadata: Additional information about the request
            - totalCount: The total number of symbols in the group
            - records: List of symbols in the specified group

    Example response:
        {
            "metadata": {},
            "totalCount": 30,
            "records": [
                {
                    "symbol": "TCB",
                    "exchange": "HOSE",
                    ...
                },
                ...
            ]
        }
    """
    try:
        listing_service = ListingService()
        result = await listing_service.get_symbols_by_group(group=group)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error getting symbols by group: {str(e)}"
        }
```

### 5. get_industries_icb()

**Status:** To be implemented  
**Purpose:** Retrieves industry classification benchmark data

```python
async def get_industries_icb() -> dict:
    """Get industry classification benchmark data from the vnstock API.

    Returns:
        dict: A dictionary containing:
            - metadata: Additional information about the request
            - totalCount: The total number of industry classifications
            - records: List of industry classifications

    Example response:
        {
            "metadata": {},
            "totalCount": 114,
            "records": [
                {
                    "icbCode": "8000",
                    "icbName": "Financials",
                    ...
                },
                ...
            ]
        }
    """
    try:
        listing_service = ListingService()
        result = await listing_service.get_industries_icb()
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error getting industry classifications: {str(e)}"
        }
```

## Implementation Notes

1. All functions follow a consistent pattern to ensure uniformity and maintainability
2. Each function includes comprehensive docstrings with:
   - Function description
   - Parameter details
   - Return value structure
   - Example response format
3. Error handling is consistent across all functions
4. The response format is standardized with:
   - `status`: "success" or "error"
   - `data`: The actual data when successful
   - `error_message`: Error details when unsuccessful

## LLM Agent Integration Considerations

1. The response structure is designed to be easily parsed by LLM Agents
2. Error messages are descriptive to assist the agent in troubleshooting
3. Example responses help the agent understand the data structure
4. The metadata field provides context that may be useful for the agent

## Next Steps

1. Implement the remaining 5 functions in the `listing_tools.py` file
2. Write unit tests for each function
3. Document the tools in the API documentation
4. Create example usage patterns for LLM Agents
