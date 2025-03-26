from typing import Dict, List, Optional
from vnstock.common.data.data_explorer import Finance
from app.datasources.base import FinancialDataSource, SOURCE_TCBS
import logging

logger = logging.getLogger(__name__)


class TCBSFinancialDataSource(FinancialDataSource):
    """TCBS implementation of the FinancialDataSource interface"""

    SOURCE = SOURCE_TCBS

    def __init__(self):
        """Initialize the TCBS financial data source"""
        self._last_api_logs = None

    async def get_balance_sheet(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> List[Dict]:
        """Get balance sheet data from TCBS API"""
        try:
            finance = Finance(symbol=symbol, source=self.SOURCE)
            result = finance.balance_sheet(
                period=period,
                lang=lang,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
            return result.to_dict(orient='records')
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
        """Get income statement data from TCBS API"""
        try:
            finance = Finance(symbol=symbol, source=self.SOURCE)
            result = finance.income_statement(
                period=period,
                lang=lang,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
            return result.to_dict(orient='records')
            
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
        """Get cash flow data from TCBS API"""
        try:
            finance = Finance(symbol=symbol, source=self.SOURCE)
            result = finance.cash_flow(
                period=period,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
            return result.to_dict(orient='records')
            
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
        """Get financial ratios data from TCBS API"""
        try:
            finance = Finance(symbol=symbol, source=self.SOURCE)
            result = finance.ratio(
                period=period,
                lang=lang,
                dropna=dropna,
                to_df=to_df,
                show_log=show_log
            )
            return result.to_dict(orient='records')
            
        except Exception as e:
            logger.error(f"Error getting ratios for {symbol}: {str(e)}")
            raise 