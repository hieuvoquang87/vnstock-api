from fastapi import HTTPException, status

class VNStockAPIException(HTTPException):
    """Base exception for all VNStock API exceptions."""
    
    def __init__(
        self,
        status_code: int,
        detail: str,
        error_code: str = None,
        headers: dict = None,
    ):
        super().__init__(
            status_code=status_code,
            detail={
                "error": {
                    "code": error_code or "INTERNAL_ERROR",
                    "message": detail,
                    "details": {}
                }
            },
            headers=headers,
        )

class StockSymbolNotFoundError(VNStockAPIException):
    """Exception raised when a stock symbol is not found."""
    
    def __init__(self, symbol: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Stock symbol '{symbol}' not found",
            error_code="STOCK_SYMBOL_NOT_FOUND",
        )

class DateRangeInvalidError(VNStockAPIException):
    """Exception raised when a date range is invalid."""
    
    def __init__(self, start_date: str = None, end_date: str = None):
        message = "Invalid date range"
        if start_date and end_date:
            message = f"Invalid date range: start_date ({start_date}) to end_date ({end_date})"
        elif start_date:
            message = f"Invalid start_date: {start_date}"
        elif end_date:
            message = f"Invalid end_date: {end_date}"
            
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
            error_code="DATE_RANGE_INVALID",
        )

class RateLimitExceededError(VNStockAPIException):
    """Exception raised when rate limit is exceeded."""
    
    def __init__(self, limit: int, reset_time: str):
        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Limit: {limit} requests per minute",
            error_code="RATE_LIMIT_EXCEEDED",
            headers={"X-RateLimit-Reset": reset_time},
        )

class ExternalAPIError(VNStockAPIException):
    """Exception raised when an external API returns an error."""
    
    def __init__(self, service: str, message: str):
        super().__init__(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Error from external service ({service}): {message}",
            error_code="EXTERNAL_API_ERROR",
        ) 