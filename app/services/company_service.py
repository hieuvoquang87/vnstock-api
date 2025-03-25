from typing import Dict, List, Optional, Any
from app.datasources.factory import DataSourceFactory
from app.datasources.base import CompanyDataSource, SOURCE_ALL
import logging
import asyncio
from functools import reduce

logger = logging.getLogger(__name__)


class CompanyService:
    """Service for company-related operations"""

    def __init__(self, data_source_factory=DataSourceFactory()):
        self.data_source_factory = data_source_factory

    async def get_company_info(self, symbol: str, source: str = SOURCE_ALL) -> Dict:
        """Get comprehensive company information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Comprehensive company information
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_company_info(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_company_info(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_info(symbol)
                return self._transform_company_info(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_company_info: {e}")
            raise

    async def get_company_profile(self, symbol: str, source: str = SOURCE_ALL) -> Dict:
        """Get company profile information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Company profile information
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_company_profile(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_company_profile(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_profile(symbol)
                return self._transform_company_profile(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_company_profile: {e}")
            raise

    async def get_company_officers(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get company officers information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Company officers information
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_company_officers(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_company_officers(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_officers(symbol)
                return self._transform_company_officers(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_company_officers: {e}")
            raise

    async def get_shareholders(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get major shareholders information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Major shareholders information
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_shareholders(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_shareholders(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_shareholders(symbol)
                return self._transform_shareholders(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_shareholders: {e}")
            raise

    async def get_insider_trading(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get insider trading information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Insider trading information
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_insider_trading(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_insider_trading(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_insider_trading(symbol)
                return self._transform_insider_trading(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_insider_trading: {e}")
            raise

    async def get_subsidiaries(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get company subsidiaries information
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Company subsidiaries information
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_subsidiaries(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_subsidiaries(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_subsidiaries(symbol)
                return self._transform_subsidiaries(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_subsidiaries: {e}")
            raise

    async def get_company_events(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get company events
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Company events
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_company_events(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_company_events(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_events(symbol)
                return self._transform_company_events(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_company_events: {e}")
            raise

    async def get_company_news(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get company news
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Company news
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_company_news(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_company_news(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_company_news(symbol)
                return self._transform_company_news(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_company_news: {e}")
            raise

    async def get_dividends(self, symbol: str, source: str = SOURCE_ALL) -> List[Dict]:
        """Get dividend history
        
        Args:
            symbol: Stock ticker symbol
            source: Data source identifier ("tcbs", "vci", or "all")
            
        Returns:
            Dividend history
        """
        try:
            if source == SOURCE_ALL:
                # Get data from all sources
                datasources = self.data_source_factory.get_all_company_datasources()
                
                # Gather results from all data sources asynchronously
                tasks = {name: ds.get_dividends(symbol) for name, ds in datasources.items()}
                results = await asyncio.gather(*tasks.values(), return_exceptions=True)
                
                # Combine results from all sources with source identification
                combined_data = {}
                for (name, _), result in zip(tasks.items(), results):
                    if isinstance(result, Exception):
                        logger.error(f"Error fetching data from {name}: {result}")
                        continue
                    combined_data[name] = result
                
                return self._transform_combined_dividends(combined_data)
            else:
                # Get data from a specific source
                data_source = self.data_source_factory.create_company_datasource(source)
                data = await data_source.get_dividends(symbol)
                return self._transform_dividends(data, source)
        except Exception as e:
            logger.error(f"Error in company service get_dividends: {e}")
            raise

    # Single-source transformation methods
    
    def _transform_company_info(self, data: Dict, source: str) -> Dict:
        """Transform company info data to standard format"""
        try:
            # Add source information to the data
            return {**data, "source": source}
        except Exception as e:
            logger.error(f"Error transforming company info: {e}")
            return {**data, "source": source}

    def _transform_company_profile(self, data: Dict, source: str) -> Dict:
        """Transform company profile data to standard format"""
        try:
            # Add source information to the data
            return {**data, "source": source}
        except Exception as e:
            logger.error(f"Error transforming company profile: {e}")
            return {**data, "source": source}

    def _transform_company_officers(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform company officers data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming company officers: {e}")
            return [{**item, "source": source} for item in data]

    def _transform_shareholders(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform shareholders data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming shareholders: {e}")
            return [{**item, "source": source} for item in data]

    def _transform_insider_trading(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform insider trading data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming insider trading: {e}")
            return [{**item, "source": source} for item in data]

    def _transform_subsidiaries(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform subsidiaries data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming subsidiaries: {e}")
            return [{**item, "source": source} for item in data]

    def _transform_company_events(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform company events data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming company events: {e}")
            return [{**item, "source": source} for item in data]

    def _transform_company_news(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform company news data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming company news: {e}")
            return [{**item, "source": source} for item in data]

    def _transform_dividends(self, data: List[Dict], source: str) -> List[Dict]:
        """Transform dividends data to standard format"""
        try:
            # Add source information to each item in the list
            return [{**item, "source": source} for item in data]
        except Exception as e:
            logger.error(f"Error transforming dividends: {e}")
            return [{**item, "source": source} for item in data]
            
    # Combined data transformation methods
    
    def _transform_combined_company_info(self, data: Dict[str, Dict]) -> Dict:
        """Transform combined company info data to unified format"""
        try:
            # Create a unified structure with data from all sources
            return {
                "unified": self._unify_company_info(data),
                "sources": data
            }
        except Exception as e:
            logger.error(f"Error transforming combined company info: {e}")
            return {"sources": data}
    
    def _transform_combined_company_profile(self, data: Dict[str, Dict]) -> Dict:
        """Transform combined company profile data to unified format"""
        try:
            # Unify data from all sources
            if not data:
                return {}
                
            # For simplicity, use the first source's data as the unified view
            # In a real implementation, you might use more sophisticated merging logic
            first_source = next(iter(data))
            return {
                "unified": data[first_source],
                "sources": data
            }
        except Exception as e:
            logger.error(f"Error transforming combined company profile: {e}")
            return {"sources": data}
    
    def _transform_combined_company_officers(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined company officers data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, officers in data.items():
                # Add source information to each officer
                for officer in officers:
                    result.append({**officer, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined company officers: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _transform_combined_shareholders(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined shareholders data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, shareholders in data.items():
                # Add source information to each shareholder
                for shareholder in shareholders:
                    result.append({**shareholder, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined shareholders: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _transform_combined_insider_trading(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined insider trading data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, trades in data.items():
                # Add source information to each trade
                for trade in trades:
                    result.append({**trade, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined insider trading: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _transform_combined_subsidiaries(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined subsidiaries data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, subsidiaries in data.items():
                # Add source information to each subsidiary
                for subsidiary in subsidiaries:
                    result.append({**subsidiary, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined subsidiaries: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _transform_combined_company_events(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined company events data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, events in data.items():
                # Add source information to each event
                for event in events:
                    result.append({**event, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined company events: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _transform_combined_company_news(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined company news data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, news_items in data.items():
                # Add source information to each news item
                for news in news_items:
                    result.append({**news, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined company news: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _transform_combined_dividends(self, data: Dict[str, List[Dict]]) -> List[Dict]:
        """Transform combined dividends data to unified format"""
        try:
            # Unify data from all sources
            result = []
            for source_name, dividends in data.items():
                # Add source information to each dividend
                for dividend in dividends:
                    result.append({**dividend, "source": source_name})
            return result
        except Exception as e:
            logger.error(f"Error transforming combined dividends: {e}")
            # Fallback to concatenating all sources
            return [item for items in data.values() for item in items]
    
    def _unify_company_info(self, data: Dict[str, Dict]) -> Dict:
        """Unify company info data from multiple sources"""
        # This is a placeholder implementation
        # In a real implementation, you would merge data from different sources intelligently
        
        # If no data available, return empty dict
        if not data:
            return {}
            
        # If only one source, use it as the unified view
        if len(data) == 1:
            return next(iter(data.values()))
        
        # Example implementation - combine all sources
        # For each section, prioritize data from the most "complete" source
        try:
            unified = {}
            
            # For profile, use the first one available (could be more sophisticated)
            for source_name in data:
                if "profile" in data[source_name] and data[source_name]["profile"]:
                    unified["profile"] = data[source_name]["profile"]
                    unified["profile_source"] = source_name
                    break
            
            # For officers, combine all
            all_officers = []
            for source_name in data:
                if "listKeyOfficer" in data[source_name] and data[source_name]["listKeyOfficer"]:
                    for officer in data[source_name]["listKeyOfficer"]:
                        all_officers.append({**officer, "source": source_name})
            unified["listKeyOfficer"] = all_officers
            
            # Similar approach for other sections
            all_shareholders = []
            for source_name in data:
                if "listShareHolder" in data[source_name] and data[source_name]["listShareHolder"]:
                    for shareholder in data[source_name]["listShareHolder"]:
                        all_shareholders.append({**shareholder, "source": source_name})
            unified["listShareHolder"] = all_shareholders
            
            # And for the rest of the sections
            for section in ["listInsiderDealing", "listSubCompany", "listEventNews", "listActivityNews", "listDividendPaymentHis"]:
                all_items = []
                for source_name in data:
                    if section in data[source_name] and data[source_name][section]:
                        for item in data[source_name][section]:
                            all_items.append({**item, "source": source_name})
                unified[section] = all_items
            
            return unified
            
        except Exception as e:
            logger.error(f"Error unifying company info: {e}")
            # Fallback - use the first source's data
            return next(iter(data.values())) if data else {} 