from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List, Optional
from datetime import datetime

router = APIRouter()

@router.get("/indices")
async def get_market_indices(
    source: Optional[str] = "vnstock"
) -> Dict:
    """
    Get market indices information
    """
    try:
        # Placeholder data until connected to actual service
        return {
            "data": [
                {
                    "index": "VN-Index",
                    "value": 1250.85,
                    "change": 12.34,
                    "change_percent": 0.99
                },
                {
                    "index": "HNX-Index",
                    "value": 230.45,
                    "change": 2.31,
                    "change_percent": 1.01
                }
            ],
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 