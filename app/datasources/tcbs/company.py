from typing import Dict, List, Optional
from datetime import datetime, date
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
            company_overview = company.overview()
            return company_overview.to_dict(orient='records')
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
            # TODO: Implement connection to vnstock with TCBS source
            # Example: import vnstock; result = await vnstock.shareholders(symbol, source=self.SOURCE)
            
            # Placeholder data using TCBS format
            return [
                {
                    "no": 1,
                    "ticker": "SCIC",
                    "name": "State Capital Investment Corporation",
                    "ownPercent": 0.35
                },
                {
                    "no": 2,
                    "ticker": "F&N",
                    "name": "Foreign Investor Group",
                    "ownPercent": 0.20
                }
            ]
        except Exception as e:
            logger.error(f"Error getting shareholders for {symbol} from TCBS: {e}")
            raise

    async def get_insider_trading(self, symbol: str) -> List[Dict]:
        """Get insider trading information from TCBS data source"""
        try:
            # TODO: Implement connection to vnstock with TCBS source
            # Example: import vnstock; result = await vnstock.insider_trading(symbol, source=self.SOURCE)
            
            # Placeholder data using TCBS format
            today = date.today().strftime("%y/%m/%d")
            return [
                {
                    "no": 1,
                    "ticker": symbol,
                    "anDate": today,
                    "dealingMethod": 1,
                    "dealingAction": "0",
                    "quantity": 5000,
                    "price": 25000,
                    "ratio": -0.008
                }
            ]
        except Exception as e:
            logger.error(f"Error getting insider trading for {symbol} from TCBS: {e}")
            raise

    async def get_subsidiaries(self, symbol: str) -> List[Dict]:
        """Get company subsidiaries information from TCBS data source"""
        try:
            # TODO: Implement connection to vnstock with TCBS source
            # Example: import vnstock; result = await vnstock.subsidiaries(symbol, source=self.SOURCE)
            
            # Placeholder data using TCBS format
            return [
                {
                    "no": 1,
                    "ticker": symbol,
                    "companyName": f"{symbol} Solutions",
                    "ownPercent": 1.0
                },
                {
                    "no": 2,
                    "ticker": symbol,
                    "companyName": f"{symbol} Trading",
                    "ownPercent": 0.75
                }
            ]
        except Exception as e:
            logger.error(f"Error getting subsidiaries for {symbol} from TCBS: {e}")
            raise

    async def get_company_events(self, symbol: str) -> List[Dict]:
        """Get company events from TCBS data source"""
        try:
            # TODO: Implement connection to vnstock with TCBS source
            # Example: import vnstock; result = await vnstock.company_events(symbol, source=self.SOURCE)
            
            # Placeholder data using TCBS format
            today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            next_month = (datetime.now().replace(month=datetime.now().month % 12 + 1)).strftime("%Y-%m-%d %H:%M:%S")
            
            return [
                {
                    "id": 1,
                    "ticker": symbol,
                    "price": 60000,
                    "priceChange": 1000,
                    "priceChangeRatio": 0.017,
                    "priceChangeRatio1M": 0.025,
                    "eventName": f"{symbol} - Annual Shareholders Meeting",
                    "eventCode": "AGME",
                    "notifyDate": today,
                    "exerDate": next_month,
                    "regFinalDate": "2023-03-15 00:00:00",
                    "exRigthDate": "2023-03-10 00:00:00",
                    "eventDesc": f"Annual Shareholders Meeting for {symbol}"
                }
            ]
        except Exception as e:
            logger.error(f"Error getting company events for {symbol} from TCBS: {e}")
            raise

    async def get_company_news(self, symbol: str) -> List[Dict]:
        """Get company news from TCBS data source"""
        try:
            # TODO: Implement connection to vnstock with TCBS source
            # Example: import vnstock; result = await vnstock.company_news(symbol, source=self.SOURCE)
            
            # Placeholder data using TCBS format
            today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            return [
                {
                    "rsi": 50.6,
                    "rs": 47,
                    "ticker": symbol,
                    "price": 61800,
                    "priceChange": -500,
                    "priceChangeRatio": -0.008,
                    "priceChangeRatio1M": 0.018,
                    "id": 11500855,
                    "title": f"{symbol}: Quarterly financial report",
                    "source": "HOSE",
                    "publishDate": today
                }
            ]
        except Exception as e:
            logger.error(f"Error getting company news for {symbol} from TCBS: {e}")
            raise

    async def get_dividends(self, symbol: str) -> List[Dict]:
        """Get dividend history from TCBS data source"""
        try:
            # TODO: Implement connection to vnstock with TCBS source
            # Example: import vnstock; result = await vnstock.dividends(symbol, source=self.SOURCE)
            
            # Placeholder data using TCBS format
            return [
                {
                    "exerciseDate": "26/12/24",
                    "cashYear": 2023,
                    "cashDividendPercentage": 0.05,
                    "issueMethod": "cash",
                    "no": 1,
                    "ticker": symbol
                }
            ]
        except Exception as e:
            logger.error(f"Error getting dividends for {symbol} from TCBS: {e}")
            raise 