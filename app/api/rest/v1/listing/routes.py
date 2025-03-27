from fastapi import APIRouter, Depends, Query, Path, HTTPException
from typing import Optional, Dict
import logging
from datetime import datetime

from app.services.listing_service import ListingService
from app.models.schemas.listing import ApiResponse, ApiErrorResponse, ResponseModel

# Set up logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(
    prefix="/listing",
    tags=["listing"],
    responses={
        404: {"model": ApiErrorResponse, "description": "Not found"},
        500: {"model": ApiErrorResponse, "description": "Internal server error"},
    },
)

async def get_listing_service(source: str = Query("vci", description="Data source to use (vci, tcbs)")):
    """Dependency to get the listing service with the specified source."""
    try:
        return ListingService(source=source)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid source: {str(e)}")
    except Exception as e:
        logger.error(f"Error creating listing service: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating listing service")

@router.get(
    "/symbols",
    response_model=ApiResponse,
    summary="Get all symbols",
    description="Get a list of all available symbols including stock code, company name, exchange, industry, etc.",
)
async def get_all_symbols(
    service: ListingService = Depends(get_listing_service)
):
    """Get all available symbols."""
    try:
        data = await service.get_all_symbols()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_all_symbols: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/symbols/by-industry",
    response_model=ApiResponse,
    summary="Get symbols by industry",
    description="Get symbols organized by their respective industries.",
)
async def get_symbols_by_industries(
    service: ListingService = Depends(get_listing_service)
):
    """Get symbols grouped by industry."""
    try:
        data = await service.get_symbols_by_industries()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_symbols_by_industries: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/symbols/by-exchange",
    response_model=ApiResponse,
    summary="Get symbols by exchange",
    description="Get symbols organized by their respective exchanges.",
)
async def get_symbols_by_exchange(
    service: ListingService = Depends(get_listing_service)
):
    """Get symbols grouped by exchange."""
    try:
        data = await service.get_symbols_by_exchange()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_symbols_by_exchange: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/symbols/by-group/{group}",
    response_model=ApiResponse,
    summary="Get symbols by group",
    description="Get symbols that are part of a specific group like VN30, HNX30, etc.",
)
async def get_symbols_by_group(
    group: str = Path(..., description="Group name (e.g., VN30, HNX30)"),
    service: ListingService = Depends(get_listing_service)
):
    """Get symbols in a specific group."""
    try:
        data = await service.get_symbols_by_group(group=group)
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
                "group": group,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_symbols_by_group: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/industries/icb",
    response_model=ApiResponse,
    summary="Get industries ICB",
    description="Get industry classification benchmark data.",
)
async def get_industries_icb(
    service: ListingService = Depends(get_listing_service)
):
    """Get industry classification benchmark data."""
    try:
        data = await service.get_industries_icb()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_industries_icb: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/future-indices",
    response_model=ApiResponse,
    summary="Get all future indices",
    description="Get all available future indices.",
)
async def get_all_future_indices(
    service: ListingService = Depends(get_listing_service)
):
    """Get all future indices."""
    try:
        data = await service.get_all_future_indices()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_all_future_indices: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/covered-warrants",
    response_model=ApiResponse,
    summary="Get all covered warrants",
    description="Get all available covered warrants.",
)
async def get_all_covered_warrant(
    service: ListingService = Depends(get_listing_service)
):
    """Get all covered warrants."""
    try:
        data = await service.get_all_covered_warrant()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_all_covered_warrant: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/bonds",
    response_model=ApiResponse,
    summary="Get all bonds",
    description="Get all available bonds.",
)
async def get_all_bonds(
    service: ListingService = Depends(get_listing_service)
):
    """Get all bonds."""
    try:
        data = await service.get_all_bonds()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_all_bonds: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/government-bonds",
    response_model=ApiResponse,
    summary="Get all government bonds",
    description="Get all available government bonds.",
)
async def get_all_government_bonds(
    service: ListingService = Depends(get_listing_service)
):
    """Get all government bonds."""
    try:
        data = await service.get_all_government_bonds()
        return ApiResponse(
            data=data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
            }
        )
    except NotImplementedError as e:
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_all_government_bonds: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 