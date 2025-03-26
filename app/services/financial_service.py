from typing import Dict, List
from app.datasources.factory import DataSourceFactory
from app.datasources.base import SOURCE_TCBS
import logging
import asyncio
from datetime import datetime

logger = logging.getLogger(__name__)


class FinancialService:
    """Service for financial-related operations"""

    def __init__(self, source: str = SOURCE_TCBS):
        """Initialize the financial service
        
        Args:
            source: Data source identifier ("tcbs", "vci", or "unified")
        """
        self.data_source_factory = DataSourceFactory()
        self.source = source

    async def get_balance_sheet(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> List[Dict]:
        """Get balance sheet data for a company
        
        Args:
            symbol: Stock ticker symbol
            period: Period type ("year" or "quarter")
            lang: Language ("vi" or "en")
            dropna: Whether to drop rows with all NaN values
            to_df: Whether to return as DataFrame
            show_log: Whether to show debug logs
            
        Returns:
            Balance sheet data
        """
        try:
            return await self.data_source_factory.create_financial_datasource(self.source).get_balance_sheet(
                symbol=symbol,
                period=period,
                lang=lang,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
        except Exception as e:
            logger.error(f"Error getting balance sheet for {symbol}: {str(e)}")
            raise

    async def get_income_statement(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> List[Dict]:
        """Get income statement data for a company
        
        Args:
            symbol: Stock ticker symbol
            period: Period type ("year" or "quarter")
            lang: Language ("vi" or "en")
            dropna: Whether to drop rows with all NaN values
            to_df: Whether to return as DataFrame
            show_log: Whether to show debug logs
            
        Returns:
            Income statement data
        """
        try:
            return await self.data_source_factory.create_financial_datasource(self.source).get_income_statement(
                symbol=symbol,
                period=period,
                lang=lang,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
        except Exception as e:
            logger.error(f"Error getting income statement for {symbol}: {str(e)}")
            raise

    async def get_cash_flow(
        self,
        symbol: str,
        period: str = "year",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> List[Dict]:
        """Get cash flow data for a company
        
        Args:
            symbol: Stock ticker symbol
            period: Period type ("year" or "quarter")
            dropna: Whether to drop rows with all NaN values
            to_df: Whether to return as DataFrame
            show_log: Whether to show debug logs
            
        Returns:
            Cash flow data
        """
        try:
            return await self.data_source_factory.create_financial_datasource(self.source).get_cash_flow(
                symbol=symbol,
                period=period,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
        except Exception as e:
            logger.error(f"Error getting cash flow for {symbol}: {str(e)}")
            raise

    async def get_ratios(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> List[Dict]:
        """Get financial ratios data for a company
        
        Args:
            symbol: Stock ticker symbol
            period: Period type ("year" or "quarter")
            lang: Language ("vi" or "en")
            dropna: Whether to drop rows with all NaN values
            to_df: Whether to return as DataFrame
            show_log: Whether to show debug logs
            
        Returns:
            Financial ratios data
        """
        try:
            return await self.data_source_factory.create_financial_datasource(self.source).get_ratios(
                symbol=symbol,
                period=period,
                lang=lang,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
        except Exception as e:
            logger.error(f"Error getting ratios for {symbol}: {str(e)}")
            raise 