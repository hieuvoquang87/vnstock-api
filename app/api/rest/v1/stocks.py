from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List, Optional
from datetime import datetime

router = APIRouter()

@router.get("/{symbol}/price")
async def get_stock_price(
    symbol: str,
    source: Optional[str] = "vnstock"
) -> Dict:
    """
    Get stock price information
    """
    try:
        # Placeholder data until connected to actual service
        return {
            "data": {
                "symbol": symbol,
                "price": 62000,
                "change": 1000,
                "change_percent": 1.64,
                "volume": 1243500
            },
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 