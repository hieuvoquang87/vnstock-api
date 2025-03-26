from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Dict, List, Optional
from app.services.financial_service import FinancialService
from app.datasources.base import SOURCE_UNIFIED, SOURCE_TCBS
from app.core.response import create_response

router = APIRouter(tags=["financial"])
financial_service = FinancialService(source=SOURCE_TCBS)


def get_financial_service() -> FinancialService:
    """Dependency injection for FinancialService"""
    return FinancialService()


@router.get("/{symbol}/balance-sheets")
async def get_balance_sheet(
    symbol: str,
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs")
) -> Dict:
    """Get balance sheet data for a company
    
    Args:
        symbol: Stock ticker symbol
        period: Period type (year or quarter)
        dropna: Drop rows with all NaN values
        to_df: Return as DataFrame
        show_log: Show debug logs
        
    Returns:
        Balance sheet data
    """
    try:
        data = await financial_service.get_balance_sheet(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return create_response(data=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{symbol}/income-statements")
async def get_income_statement(
    symbol: str,
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs")
) -> Dict:
    """Get income statement data for a company
    
    Args:
        symbol: Stock ticker symbol
        period: Period type (year or quarter)
        dropna: Drop rows with all NaN values
        to_df: Return as DataFrame
        show_log: Show debug logs
        
    Returns:
        Income statement data
    """
    try:
        data = await financial_service.get_income_statement(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return create_response(data=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{symbol}/cash-flows")
async def get_cash_flow(
    symbol: str,
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs")
) -> Dict:
    """Get cash flow data for a company
    
    Args:
        symbol: Stock ticker symbol
        period: Period type (year or quarter)
        dropna: Drop rows with all NaN values
        to_df: Return as DataFrame
        show_log: Show debug logs
        
    Returns:
        Cash flow data
    """
    try:
        data = await financial_service.get_cash_flow(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return create_response(data=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{symbol}/ratios")
async def get_ratios(
    symbol: str,
    period: str = Query("year", description="Period type (year or quarter)"),
    dropna: bool = Query(True, description="Drop rows with all NaN values"),
    to_df: bool = Query(True, description="Return as DataFrame"),
    show_log: bool = Query(False, description="Show debug logs")
) -> Dict:
    """Get financial ratios data for a company
    
    Args:
        symbol: Stock ticker symbol
        period: Period type (year or quarter)
        dropna: Drop rows with all NaN values
        to_df: Return as DataFrame
        show_log: Show debug logs
        
    Returns:
        Financial ratios data
    """
    try:
        data = await financial_service.get_ratios(
            symbol=symbol,
            period=period,
            dropna=dropna,
            to_df=to_df,
            show_log=show_log
        )
        return create_response(data=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 