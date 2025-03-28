from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, Path, Query, HTTPException
from datetime import datetime
import logging
from app.datasources.base import SOURCE_UNIFIED
from app.models.schemas.listing import ApiResponse, ApiErrorResponse
from app.services.company_service import CompanyService

# Set up logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(
    responses={
        404: {"model": ApiErrorResponse, "description": "Not found"},
        500: {"model": ApiErrorResponse, "description": "Internal server error"},
    },
)

async def get_company_service(source: str = Query(SOURCE_UNIFIED, description="Data source to use")):
    """Dependency to get the company service with the specified source."""
    try:
        return CompanyService(), source
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid source: {str(e)}")
    except Exception as e:
        logger.error(f"Error creating company service: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating company service")

@router.get(
    "/{symbol}",
    response_model=ApiResponse,
    summary="Get company info",
    description="Get comprehensive company information."
)
async def get_company_info(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get comprehensive company information."""
    service, source = service_and_source
    try:
        data = await service.get_company_info(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get company info not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_company_info for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve company information: {str(e)}"
        )

@router.get(
    "/{symbol}/profile",
    response_model=ApiResponse,
    summary="Get company profile",
    description="Get detailed company profile."
)
async def get_company_profile(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get detailed company profile."""
    service, source = service_and_source
    try:
        data = await service.get_company_profile(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get company profile not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_company_profile for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve company profile: {str(e)}"
        )

@router.get(
    "/{symbol}/officers",
    response_model=ApiResponse,
    summary="Get company officers",
    description="Get company management information."
)
async def get_company_officers(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get company management information."""
    service, source = service_and_source
    try:
        data = await service.get_company_officers(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get company officers not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_company_officers for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve company officers: {str(e)}"
        )

@router.get(
    "/{symbol}/shareholders",
    response_model=ApiResponse,
    summary="Get shareholders",
    description="Get major shareholders information."
)
async def get_shareholders(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get major shareholders information."""
    service, source = service_and_source
    try:
        data = await service.get_shareholders(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get shareholders not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_shareholders for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve shareholders: {str(e)}"
        )

@router.get(
    "/{symbol}/insider-trading",
    response_model=ApiResponse,
    summary="Get insider trading",
    description="Get insider trading information."
)
async def get_insider_trading(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get insider trading information."""
    service, source = service_and_source
    try:
        data = await service.get_insider_trading(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get insider trading not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_insider_trading for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve insider trading information: {str(e)}"
        )

@router.get(
    "/{symbol}/subsidiaries",
    response_model=ApiResponse,
    summary="Get subsidiaries",
    description="Get company subsidiaries."
)
async def get_subsidiaries(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get company subsidiaries."""
    service, source = service_and_source
    try:
        data = await service.get_subsidiaries(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get subsidiaries not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_subsidiaries for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve subsidiaries: {str(e)}"
        )

@router.get(
    "/{symbol}/events",
    response_model=ApiResponse,
    summary="Get company events",
    description="Get company events."
)
async def get_company_events(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get company events."""
    service, source = service_and_source
    try:
        data = await service.get_company_events(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get company events not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_company_events for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve company events: {str(e)}"
        )

@router.get(
    "/{symbol}/news",
    response_model=ApiResponse,
    summary="Get company news",
    description="Get company news."
)
async def get_company_news(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get company news."""
    service, source = service_and_source
    try:
        data = await service.get_company_news(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get company news not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_company_news for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve company news: {str(e)}"
        )

@router.get(
    "/{symbol}/dividends",
    response_model=ApiResponse,
    summary="Get dividends",
    description="Get dividend history."
)
async def get_dividends(
    symbol: str = Path(..., description="Company stock symbol"),
    service_and_source: tuple = Depends(get_company_service)
):
    """Get dividend history."""
    service, source = service_and_source
    try:
        data = await service.get_dividends(symbol, source)
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": source,
                "symbol": symbol
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get dividends not implemented for source {source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_dividends for {symbol}: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to retrieve dividends: {str(e)}"
        ) 