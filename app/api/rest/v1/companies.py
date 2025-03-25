from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Dict, List, Optional
import logging
from app.services.company_service import CompanyService
from app.datasources.base import SOURCE_ALL, SOURCE_TCBS, SOURCE_VCI
from datetime import datetime

router = APIRouter()
logger = logging.getLogger(__name__)

async def get_company_service():
    """Dependency for CompanyService"""
    return CompanyService()

@router.get("/{symbol}/info")
async def get_company_info(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get comprehensive company information
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_company_info(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/profile")
async def get_company_profile(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get company profile information
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_company_profile(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/officers")
async def get_company_officers(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get company officers information
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_company_officers(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/shareholders")
async def get_shareholders(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get major shareholders information
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_shareholders(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/insider-trading")
async def get_insider_trading(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get insider trading information
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_insider_trading(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/subsidiaries")
async def get_subsidiaries(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get company subsidiaries information
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_subsidiaries(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/events")
async def get_company_events(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get company events
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_company_events(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/news")
async def get_company_news(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get company news
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_company_news(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}/dividends")
async def get_dividends(
    symbol: str,
    source: Optional[str] = Query(SOURCE_ALL, description=f"Data source: '{SOURCE_TCBS}', '{SOURCE_VCI}', or '{SOURCE_ALL}' for combined data"),
    company_service: CompanyService = Depends(get_company_service)
) -> Dict:
    """
    Get dividend history
    
    - **symbol**: Stock ticker symbol
    - **source**: Data source to use (tcbs, vci, or all)
    """
    try:
        data = await company_service.get_dividends(symbol, source)
        return {
            "data": data,
            "meta": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 