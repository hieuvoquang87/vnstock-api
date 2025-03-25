from typing import Dict, List, Optional, Type
import logging
from app.datasources.base import CompanyDataSource, SOURCE_TCBS, SOURCE_VCI, SOURCE_ALL
from app.datasources.tcbs.company import TcbsCompanyDataSource
from app.datasources.vci.company import VciCompanyDataSource

logger = logging.getLogger(__name__)

class DataSourceFactory:
    """Factory for creating data sources"""

    _company_datasources: Dict[str, Type[CompanyDataSource]] = {
        SOURCE_TCBS: TcbsCompanyDataSource,
        SOURCE_VCI: VciCompanyDataSource
    }

    @classmethod
    def create_company_datasource(cls, source: str = SOURCE_TCBS) -> CompanyDataSource:
        """Create a company data source based on the specified source
        
        Args:
            source: The data source provider name, either "tcbs" or "vci"
            
        Returns:
            An instance of the appropriate CompanyDataSource implementation
        """
        if source not in cls._company_datasources:
            logger.warning(f"Unknown data source '{source}', defaulting to '{SOURCE_TCBS}'")
            source = SOURCE_TCBS
            
        return cls._company_datasources[source]()
    
    @classmethod
    def get_all_company_datasources(cls) -> Dict[str, CompanyDataSource]:
        """Get all available company data sources
        
        Returns:
            A dictionary of data source name to data source instance
        """
        return {name: source_class() for name, source_class in cls._company_datasources.items()} 