from typing import Any, Dict, Optional
from datetime import datetime


def create_response(
    data: Any,
    meta: Optional[Dict] = None,
    error: Optional[Dict] = None
) -> Dict:
    """Create a standardized API response
    
    Args:
        data: The response data
        meta: Optional metadata about the response
        error: Optional error information
        
    Returns:
        A standardized response dictionary
    """
    response = {
        "data": data,
        "meta": meta or {
            "timestamp": datetime.utcnow().isoformat(),
            "version": "1.0"
        }
    }
    
    if error:
        response["error"] = error
        
    return response 