from fastapi import APIRouter, Depends, HTTPException, Query, Path
from typing import Dict, List, Optional
from datetime import datetime
import logging
from app.services.financial_service import FinancialService
from app.datasources.base import SOURCE_UNIFIED, SOURCE_TCBS
from app.models.schemas.listing import ApiResponse, ApiErrorResponse

# Set up logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(
    responses={
        404: {"model": ApiErrorResponse, "description": "Not found"},
        500: {"model": ApiErrorResponse, "description": "Internal server error"},
    },
)

async def get_financial_service(source: str = Query(SOURCE_TCBS, description="Data source to use")) -> FinancialService:
    """Dependency injection for FinancialService"""
    try:
        return FinancialService(source=source)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid source: {str(e)}")
    except Exception as e:
        logger.error(f"Error creating financial service: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating financial service")


@router.get(
    "/{symbol}/balance-sheets",
    response_model=ApiResponse,
    summary="Get balance sheet data",
    description="Get balance sheet data for a company"
)
async def get_balance_sheet(
    symbol: str = Path(..., description="Stock ticker symbol"),
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs"),
    service: FinancialService = Depends(get_financial_service)
) -> Dict:
    """Get balance sheet data for a company"""
    try:
        data = await service.get_balance_sheet(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
                "symbol": symbol,
                "period": period
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get balance sheet not implemented for source {service.source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_balance_sheet for {symbol}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{symbol}/income-statements",
    response_model=ApiResponse,
    summary="Get income statement data",
    description="Get income statement data for a company"
)
async def get_income_statement(
    symbol: str = Path(..., description="Stock ticker symbol"),
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs"),
    service: FinancialService = Depends(get_financial_service)
) -> Dict:
    """Get income statement data for a company"""
    try:
        data = await service.get_income_statement(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
                "symbol": symbol,
                "period": period
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get income statement not implemented for source {service.source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_income_statement for {symbol}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{symbol}/cash-flows",
    response_model=ApiResponse,
    summary="Get cash flow data",
    description="Get cash flow data for a company"
)
async def get_cash_flow(
    symbol: str = Path(..., description="Stock ticker symbol"),
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs"),
    service: FinancialService = Depends(get_financial_service)
) -> Dict:
    """Get cash flow data for a company"""
    try:
        data = await service.get_cash_flow(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
                "symbol": symbol,
                "period": period
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get cash flow not implemented for source {service.source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_cash_flow for {symbol}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{symbol}/ratios",
    response_model=ApiResponse,
    summary="Get financial ratios data",
    description="Get financial ratios data for a company"
)
async def get_ratios(
    symbol: str = Path(..., description="Stock ticker symbol"),
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs"),
    service: FinancialService = Depends(get_financial_service)
) -> Dict:
    """Get financial ratios data for a company"""
    try:
        data = await service.get_ratios(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return ApiResponse(
            data={"records": data} if isinstance(data, list) else data,
            meta={
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "source": service.source,
                "symbol": symbol,
                "period": period
            }
        )
    except NotImplementedError as e:
        logger.warning(f"Get ratios not implemented for source {service.source}: {str(e)}")
        raise HTTPException(
            status_code=501, 
            detail=f"Not implemented for this source: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in get_ratios for {symbol}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 