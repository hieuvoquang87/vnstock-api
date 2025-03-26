from typing import Dict, List
import logging
from vnstock.common.data.data_explorer import Company
from app.datasources.base import CompanyDataSource, SOURCE_TCBS

logger = logging.getLogger(__name__)



class TcbsCompanyDataSource(CompanyDataSource):
    """TCBS implementation of the CompanyDataSource interface"""

    # Define the source as a class attribute
    SOURCE = SOURCE_TCBS

    async def get_company_info(self, symbol: str) -> Dict:
        """Get comprehensive company information from TCBS data source"""
        try:
            # Gather all individual data points
            profile = await self.get_company_profile(symbol)
            officers = await self.get_company_officers(symbol)
            shareholders = await self.get_shareholders(symbol)
            insider_transactions = await self.get_insider_trading(symbol)
            subsidiaries = await self.get_subsidiaries(symbol)
            events = await self.get_company_events(symbol)
            news = await self.get_company_news(symbol)
            dividends = await self.get_dividends(symbol)
            
            # Combine into comprehensive info
            return {
                "profile": profile,
                "listKeyOfficer": officers,
                "listShareHolder": shareholders,
                "listInsiderDealing": insider_transactions,
                "listSubCompany": subsidiaries,
                "listEventNews": events,
                "listActivityNews": news,
                "listDividendPaymentHis": dividends
            }
        except Exception as e:
            logger.error(f"Error getting company info for {symbol} from TCBS: {e}")
            raise

    async def get_company_profile(self, symbol: str) -> Dict:
        """Get company profile information from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            result = company.overview()
            company_overviews = result.to_dict(orient='records')
            return company_overviews[0]
        except Exception as e:
            logger.error(f"Error getting company profile for {symbol} from TCBS: {e}")
            raise

    async def get_company_officers(self, symbol: str) -> List[Dict]:
        """Get company officers information from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            company_officers = company.officers()
            return company_officers.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting company officers for {symbol} from TCBS: {e}")
            raise

    async def get_shareholders(self, symbol: str) -> List[Dict]:
        """Get major shareholders information from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            shareholders = company.shareholders()
            return shareholders.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting shareholders for {symbol} from TCBS: {e}")
            raise

    async def get_insider_trading(self, symbol: str) -> List[Dict]:
        """Get insider trading information from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            insider_trading = company.insider_transactions()
            return insider_trading.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting insider trading for {symbol} from TCBS: {e}")
            raise

    async def get_subsidiaries(self, symbol: str) -> List[Dict]:
        """Get company subsidiaries information from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            subsidiaries = company.subsidiaries()
            return subsidiaries.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting subsidiaries for {symbol} from TCBS: {e}")
            raise

    async def get_company_events(self, symbol: str) -> List[Dict]:
        """Get company events from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            events = company.events()
            return events.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting company events for {symbol} from TCBS: {e}")
            raise

    async def get_company_news(self, symbol: str) -> List[Dict]:
        """Get company news from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            news = company.news()
            return news.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting company news for {symbol} from TCBS: {e}")
            raise

    async def get_dividends(self, symbol: str) -> List[Dict]:
        """Get dividend history from TCBS data source"""
        try:
            company = Company(symbol=symbol, source=self.SOURCE)
            dividends = company.dividends()
            return dividends.to_dict(orient='records')
        except Exception as e:
            logger.error(f"Error getting dividends for {symbol} from TCBS: {e}")
            raise 