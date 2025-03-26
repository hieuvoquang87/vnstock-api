from typing import Dict, Type, Optional
from app.datasources.base import CompanyDataSource, FinancialDataSource, SOURCE_TCBS, SOURCE_VCI, SOURCE_UNIFIED
from app.datasources.tcbs.company import TcbsCompanyDataSource
from app.datasources.tcbs.financial import TCBSFinancialDataSource
from app.datasources.vci.company import VciCompanyDataSource
from app.datasources.vci.financial import VCIFinancialDataSource
import logging

logger = logging.getLogger(__name__)


class DataSourceFactory:
    """Factory for creating data sources"""

    _company_datasources: Dict[str, Type[CompanyDataSource]] = {
        SOURCE_TCBS: TcbsCompanyDataSource,
        SOURCE_VCI: VciCompanyDataSource
    }

    _financial_datasources: Dict[str, Type[FinancialDataSource]] = {
        SOURCE_TCBS: TCBSFinancialDataSource,
        SOURCE_VCI: VCIFinancialDataSource
    }

    _valid_sources = {SOURCE_TCBS, SOURCE_VCI, SOURCE_UNIFIED}

    def create_company_datasource(self, source: str) -> CompanyDataSource:
        """Create a company data source
        
        Args:
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Company data source instance
        """
        if source not in self._valid_sources:
            logger.warning(f"Unknown data source '{source}', defaulting to '{SOURCE_TCBS}'")
            source = SOURCE_TCBS

        datasource_class = self._company_datasources.get(source)
        if not datasource_class:
            raise ValueError(f"Unsupported data source: {source}")

        return datasource_class()

    def create_financial_datasource(self, source: str) -> FinancialDataSource:
        """Create a financial data source
        
        Args:
            source: Data source identifier ("tcbs", "vci", or "unified")
            
        Returns:
            Financial data source instance
        """
        if source not in self._valid_sources:
            logger.warning(f"Unknown data source '{source}', defaulting to '{SOURCE_TCBS}'")
            source = SOURCE_TCBS

        datasource_class = self._financial_datasources.get(source)
        if not datasource_class:
            raise ValueError(f"Unsupported data source: {source}")

        return datasource_class()

    @classmethod
    def get_all_company_datasources(cls) -> Dict[str, CompanyDataSource]:
        """Get all available company data sources
        
        Returns:
            A dictionary of data source name to data source instance
        """
        return {name: source_class() for name, source_class in cls._company_datasources.items()}

    @staticmethod
    def create_company_datasource(source: str = SOURCE_TCBS) -> CompanyDataSource:
        """Create a company data source based on the specified source type"""
        if source == SOURCE_TCBS:
            return TcbsCompanyDataSource()
        elif source == SOURCE_VCI:
            return VciCompanyDataSource()
        else:
            raise ValueError(f"Unsupported data source: {source}")

    @staticmethod
    def create_financial_datasource(source: str = SOURCE_TCBS) -> FinancialDataSource:
        """Create a financial data source based on the specified source type"""
        if source == SOURCE_TCBS:
            return TCBSFinancialDataSource()
        elif source == SOURCE_VCI:
            return VCIFinancialDataSource()
        else:
            raise ValueError(f"Unsupported data source: {source}") 