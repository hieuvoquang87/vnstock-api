from app.services.listing_service import ListingService

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

