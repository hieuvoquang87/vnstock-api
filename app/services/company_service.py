from typing import Dict, List, Optional, Any
from app.datasources.company_datasource import CompanyDataSource, DataSourceFactory
import logging

logger = logging.getLogger(__name__)


class CompanyService:
    """Service for company-related operations"""

    def __init__(self, data_source_factory=DataSourceFactory()):
        self.data_source_factory = data_source_factory

    async def get_company_info(self, symbol: str, source: str = "vnstock") -> Dict:
        """Get comprehensive company information"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_company_info(symbol)
            return self._transform_company_info(data)
        except Exception as e:
            logger.error(f"Error in company service get_company_info: {e}")
            raise

    async def get_company_profile(self, symbol: str, source: str = "vnstock") -> Dict:
        """Get company profile information"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_company_profile(symbol)
            return self._transform_company_profile(data)
        except Exception as e:
            logger.error(f"Error in company service get_company_profile: {e}")
            raise

    async def get_company_officers(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get company officers information"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_company_officers(symbol)
            return self._transform_company_officers(data)
        except Exception as e:
            logger.error(f"Error in company service get_company_officers: {e}")
            raise

    async def get_shareholders(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get major shareholders information"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_shareholders(symbol)
            return self._transform_shareholders(data)
        except Exception as e:
            logger.error(f"Error in company service get_shareholders: {e}")
            raise

    async def get_insider_trading(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get insider trading information"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_insider_trading(symbol)
            return self._transform_insider_trading(data)
        except Exception as e:
            logger.error(f"Error in company service get_insider_trading: {e}")
            raise

    async def get_subsidiaries(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get company subsidiaries information"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_subsidiaries(symbol)
            return self._transform_subsidiaries(data)
        except Exception as e:
            logger.error(f"Error in company service get_subsidiaries: {e}")
            raise

    async def get_company_events(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get company events"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_company_events(symbol)
            return self._transform_company_events(data)
        except Exception as e:
            logger.error(f"Error in company service get_company_events: {e}")
            raise

    async def get_company_news(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get company news"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_company_news(symbol)
            return self._transform_company_news(data)
        except Exception as e:
            logger.error(f"Error in company service get_company_news: {e}")
            raise

    async def get_dividends(self, symbol: str, source: str = "vnstock") -> List[Dict]:
        """Get dividend history"""
        try:
            data_source = self.data_source_factory.create_company_datasource(source)
            data = await data_source.get_dividends(symbol)
            return self._transform_dividends(data)
        except Exception as e:
            logger.error(f"Error in company service get_dividends: {e}")
            raise

    def _transform_company_info(self, data: Dict) -> Dict:
        """Transform company info data to standard format"""
        try:
            # The data is already in the right format with all required fields
            # We may implement additional transformations if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming company info: {e}")
            return data

    def _transform_company_profile(self, data: Dict) -> Dict:
        """Transform company profile data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming company profile: {e}")
            return data

    def _transform_company_officers(self, data: List[Dict]) -> List[Dict]:
        """Transform company officers data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming company officers: {e}")
            return data

    def _transform_shareholders(self, data: List[Dict]) -> List[Dict]:
        """Transform shareholders data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming shareholders: {e}")
            return data

    def _transform_insider_trading(self, data: List[Dict]) -> List[Dict]:
        """Transform insider trading data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming insider trading: {e}")
            return data

    def _transform_subsidiaries(self, data: List[Dict]) -> List[Dict]:
        """Transform subsidiaries data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming subsidiaries: {e}")
            return data

    def _transform_company_events(self, data: List[Dict]) -> List[Dict]:
        """Transform company events data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming company events: {e}")
            return data

    def _transform_company_news(self, data: List[Dict]) -> List[Dict]:
        """Transform company news data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming company news: {e}")
            return data

    def _transform_dividends(self, data: List[Dict]) -> List[Dict]:
        """Transform dividends data to standard format"""
        try:
            # Already in the right format based on TCBS structure
            # Add any additional transformation logic here if needed
            return data
        except Exception as e:
            logger.error(f"Error transforming dividends: {e}")
            return data 