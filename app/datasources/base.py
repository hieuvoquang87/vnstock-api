from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Source constants
SOURCE_TCBS = "tcbs"
SOURCE_VCI = "vci"
SOURCE_UNIFIED = "unified"

class CompanyDataSource(ABC):
    """Abstract interface for company data sources"""

    @abstractmethod
    async def get_company_info(self, symbol: str) -> Dict:
        """Get comprehensive company information"""
        pass

    @abstractmethod
    async def get_company_profile(self, symbol: str) -> Dict:
        """Get company profile information"""
        pass

    @abstractmethod
    async def get_company_officers(self, symbol: str) -> List[Dict]:
        """Get company officers information"""
        pass

    @abstractmethod
    async def get_shareholders(self, symbol: str) -> List[Dict]:
        """Get major shareholders information"""
        pass

    @abstractmethod
    async def get_insider_trading(self, symbol: str) -> List[Dict]:
        """Get insider trading information"""
        pass

    @abstractmethod
    async def get_subsidiaries(self, symbol: str) -> List[Dict]:
        """Get company subsidiaries information"""
        pass

    @abstractmethod
    async def get_company_events(self, symbol: str) -> List[Dict]:
        """Get company events"""
        pass

    @abstractmethod
    async def get_company_news(self, symbol: str) -> List[Dict]:
        """Get company news"""
        pass

    @abstractmethod
    async def get_dividends(self, symbol: str) -> List[Dict]:
        """Get dividend history"""
        pass

class FinancialDataSource(ABC):
    """Abstract interface for financial data sources"""

    @abstractmethod
    async def get_balance_sheet(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> Dict:
        """Get balance sheet data"""
        pass

    @abstractmethod
    async def get_income_statement(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> Dict:
        """Get income statement data"""
        pass

    @abstractmethod
    async def get_cash_flow(
        self,
        symbol: str,
        period: str = "year",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> Dict:
        """Get cash flow data"""
        pass

    @abstractmethod
    async def get_ratios(
        self,
        symbol: str,
        period: str = "year",
        lang: str = "vi",
        dropna: bool = True,
        to_df: bool = True,
        show_log: bool = False
    ) -> Dict:
        """Get financial ratios data"""
        pass

class ListingDataSource(ABC):
    """Abstract interface for listing data sources."""

    @abstractmethod
    async def get_all_symbols(self, show_log: bool = False) -> Dict:
        """Get list of all available symbols."""
        pass


    @abstractmethod
    async def get_symbols_by_industries(self, 
                                        show_log: bool = False) -> Dict:
        """Get symbols grouped by industry."""
        pass

    @abstractmethod
    async def get_symbols_by_exchange(self, 
                                     show_log: bool = False) -> Dict:
        """Get symbols grouped by exchange."""
        pass

    @abstractmethod
    async def get_symbols_by_group(self, group: str = 'VN30', 
                                  show_log: bool = False) -> Dict:
        """Get symbols in a specific group like VN30, HNX30, etc."""
        pass

    @abstractmethod
    async def get_industries_icb(self, 
                                show_log: bool = False) -> Dict:
        """Get industry classification benchmark data."""
        pass

    @abstractmethod
    async def get_all_future_indices(self, 
                                    show_log: bool = False) -> Dict:
        """Get all future indices."""
        pass

    @abstractmethod
    async def get_all_covered_warrant(self, 
                                     show_log: bool = False) -> Dict:
        """Get all covered warrants."""
        pass

    @abstractmethod
    async def get_all_bonds(self, 
                           show_log: bool = False) -> Dict:
        """Get all bonds."""
        pass

    @abstractmethod
    async def get_all_government_bonds(self, 
                                      show_log: bool = False) -> Dict:
        """Get all government bonds."""
        pass

class DataSourceFactory:
    """Factory class for creating data source instances."""

    @staticmethod
    def create_listing_datasource(source: str = "vci"):
        """Create a listing data source.
        
        Args:
            source: The source type identifier (default: "vci").
                   Possible values: "vci", "tcbs", "msn".
        
        Returns:
            An instance of a class implementing the ListingDataSource interface.
        """
        source = source.lower()
        if source == "vci":
            # Import here to avoid circular imports
            from app.datasources.vci.listing import VCIListingDataSource
            return VCIListingDataSource()
        elif source == "tcbs":
            # Import here to avoid circular imports
            from app.datasources.tcbs.listing import TCBSListingDataSource
            return TCBSListingDataSource()
        else:
            raise ValueError(f"Unsupported source: {source}")