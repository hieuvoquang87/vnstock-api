from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, Path, Query, HTTPException
from app.datasources.base import SOURCE_UNIFIED
from app.models.schemas.response import create_api_response, create_error_response
from app.services.company_service import CompanyService

router = APIRouter()


@router.get("/{symbol}")
async def get_company_info(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get comprehensive company information.
    """
    try:
        service = CompanyService()
        data = await service.get_company_info(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="COMPANY_INFO_ERROR",
            message=f"Failed to retrieve company information: {str(e)}"
        )


@router.get("/{symbol}/profile")
async def get_company_profile(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get detailed company profile.
    """
    try:
        service = CompanyService()
        data = await service.get_company_profile(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="COMPANY_PROFILE_ERROR",
            message=f"Failed to retrieve company profile: {str(e)}"
        )


@router.get("/{symbol}/officers")
async def get_company_officers(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get company management information.
    """
    try:
        service = CompanyService()
        data = await service.get_company_officers(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="COMPANY_OFFICERS_ERROR",
            message=f"Failed to retrieve company officers: {str(e)}"
        )


@router.get("/{symbol}/shareholders")
async def get_shareholders(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get major shareholders information.
    """
    try:
        service = CompanyService()
        data = await service.get_shareholders(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="SHAREHOLDERS_ERROR",
            message=f"Failed to retrieve shareholders: {str(e)}"
        )


@router.get("/{symbol}/insider-trading")
async def get_insider_trading(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get insider trading information.
    """
    try:
        service = CompanyService()
        data = await service.get_insider_trading(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="INSIDER_TRADING_ERROR",
            message=f"Failed to retrieve insider trading information: {str(e)}"
        )


@router.get("/{symbol}/subsidiaries")
async def get_subsidiaries(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get company subsidiaries.
    """
    try:
        service = CompanyService()
        data = await service.get_subsidiaries(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="SUBSIDIARIES_ERROR",
            message=f"Failed to retrieve subsidiaries: {str(e)}"
        )


@router.get("/{symbol}/events")
async def get_company_events(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get company events.
    """
    try:
        service = CompanyService()
        data = await service.get_company_events(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="COMPANY_EVENTS_ERROR",
            message=f"Failed to retrieve company events: {str(e)}"
        )


@router.get("/{symbol}/news")
async def get_company_news(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get company news.
    """
    try:
        service = CompanyService()
        data = await service.get_company_news(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="COMPANY_NEWS_ERROR",
            message=f"Failed to retrieve company news: {str(e)}"
        )


@router.get("/{symbol}/dividends")
async def get_dividends(
    symbol: str = Path(..., description="Company stock symbol"),
    source: str = Query(SOURCE_UNIFIED, description="Data source to use")
):
    """
    Get dividend history.
    """
    try:
        service = CompanyService()
        data = await service.get_dividends(symbol, source)
        return create_api_response(data)
    except Exception as e:
        return create_error_response(
            code="DIVIDENDS_ERROR",
            message=f"Failed to retrieve dividends: {str(e)}"
        ) 