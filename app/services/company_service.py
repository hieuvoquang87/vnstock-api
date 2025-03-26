from typing import Dict, List, Optional, Any
from app.datasources.factory import DataSourceFactory
from app.datasources.base import CompanyDataSource, SOURCE_UNIFIED, SOURCE_TCBS, SOURCE_VCI
import logging
import asyncio
from functools import reduce

logger = logging.getLogger(__name__)


class CompanyService:
    """Service for company-related operations"""

    def __init__(self, data_source_factory=DataSourceFactory()):
        self.data_source_factory = data_source_factory

    async def get_company_info(self, symbol: str, source: str = SOURCE_UNIFIED) -> Dict:
        """Get comprehensive company information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Comprehensive company information
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_company_info(symbol),
                    vci_source.get_company_info(symbol),
                    return_exceptions=True
                )
                
                # Combine data
                return self._unify_company_info({
                    SOURCE_TCBS: tcbs_data if not isinstance(tcbs_data, Exception) else None,
                    SOURCE_VCI: vci_data if not isinstance(vci_data, Exception) else None
                })
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_info(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_company_info: {e}")
            raise

    async def get_company_profile(self, symbol: str, source: str = SOURCE_UNIFIED) -> Dict:
        """Get company profile information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Company profile information
        """
        try:
            print(f"Getting company profile for {symbol} from {source}")
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_company_profile(symbol),
                    vci_source.get_company_profile(symbol),
                    return_exceptions=True
                )
                
                # Merge data from both sources if available
                if isinstance(tcbs_data, Dict) and isinstance(vci_data, Dict):
                    # Combine properties from both sources, with TCBS taking precedence for duplicates
                    return {**tcbs_data, **vci_data}
                # Prioritize TCBS data if available, otherwise use VCI
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                elif not isinstance(vci_data, Exception):
                    return vci_data
                else:
                    # Both failed
                    raise Exception("Failed to get company profile from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_profile(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_company_profile: {e}")
            raise

    async def get_company_officers(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get company officers information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Company officers information
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_company_officers(symbol),
                    vci_source.get_company_officers(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get company officers from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_officers(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_company_officers: {e}")
            raise

    async def get_shareholders(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get major shareholders information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Major shareholders information
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_shareholders(symbol),
                    vci_source.get_shareholders(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get shareholders from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_shareholders(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_shareholders: {e}")
            raise

    async def get_insider_trading(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get insider trading information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Insider trading information
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_insider_trading(symbol),
                    vci_source.get_insider_trading(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get insider trading from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_insider_trading(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_insider_trading: {e}")
            raise

    async def get_subsidiaries(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get company subsidiaries information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Company subsidiaries information
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_subsidiaries(symbol),
                    vci_source.get_subsidiaries(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get subsidiaries from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_subsidiaries(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_subsidiaries: {e}")
            raise

    async def get_company_events(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get company events
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Company events
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_company_events(symbol),
                    vci_source.get_company_events(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get company events from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_events(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_company_events: {e}")
            raise

    async def get_company_news(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get company news
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Company news
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_company_news(symbol),
                    vci_source.get_company_news(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get company news from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_news(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_company_news: {e}")
            raise

    async def get_dividends(self, symbol: str, source: str = SOURCE_UNIFIED) -> List[Dict]:
        """Get dividend history
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Dividend history
        """
        try:
            if source == SOURCE_UNIFIED:
                # Get data sources
                tcbs_source = self.data_source_factory.create_company_datasource(SOURCE_TCBS)
                vci_source = self.data_source_factory.create_company_datasource(SOURCE_VCI)
                
                # Get data from both sources
                tcbs_data, vci_data = await asyncio.gather(
                    tcbs_source.get_dividends(symbol),
                    vci_source.get_dividends(symbol),
                    return_exceptions=True
                )
                
                # Use VCI data if available, otherwise fall back to TCBS
                if not isinstance(vci_data, Exception):
                    return vci_data
                elif not isinstance(tcbs_data, Exception):
                    return tcbs_data
                else:
                    raise Exception("Failed to get dividends from any source")
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_dividends(symbol)
                return data
        except Exception as e:
            logger.error(f"Error in company service get_dividends: {e}")
            raise
    
    def _unify_company_info(self, data: Dict[str, Dict]) -> Dict:
        """Unify company info data from multiple sources"""
        try:
            # If no valid data available, return empty dict
            if not data or (data[SOURCE_TCBS] is None and data[SOURCE_VCI] is None):
                return {}
                
            # If only TCBS data available
            if data[SOURCE_TCBS] is not None and data[SOURCE_VCI] is None:
                return data[SOURCE_TCBS]
            
            # If only VCI data available
            if data[SOURCE_VCI] is not None and data[SOURCE_TCBS] is None:
                return data[SOURCE_VCI]
            
            # If both sources available, merge them
            result = {}
            
            # For profile, merge properties from both sources with TCBS taking precedence
            result["profile"] = {}
            if "profile" in data[SOURCE_VCI] and data[SOURCE_VCI]["profile"]:
                result["profile"].update(data[SOURCE_VCI]["profile"])
            if "profile" in data[SOURCE_TCBS] and data[SOURCE_TCBS]["profile"]:
                result["profile"].update(data[SOURCE_TCBS]["profile"])
            
            # For list sections, combine from both sources
            for section in ["listKeyOfficer", "listShareHolder", "listInsiderDealing", 
                          "listSubCompany", "listEventNews", "listActivityNews", 
                          "listDividendPaymentHis"]:
                result[section] = []
                
                # Add TCBS data
                if section in data[SOURCE_TCBS] and data[SOURCE_TCBS][section]:
                    result[section].extend(data[SOURCE_TCBS][section])
                
                # Add VCI data
                if section in data[SOURCE_VCI] and data[SOURCE_VCI][section]:
                    result[section].extend(data[SOURCE_VCI][section])
            
            return result
            
        except Exception as e:
            logger.error(f"Error unifying company info: {e}")
            # Return first non-None source's data as fallback
            if data[SOURCE_TCBS] is not None:
                return data[SOURCE_TCBS]
            elif data[SOURCE_VCI] is not None:
                return data[SOURCE_VCI]
            else:
                return {} 