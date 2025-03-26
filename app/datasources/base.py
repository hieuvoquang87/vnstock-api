from abc import ABC, abstractmethod
from typing import Dict, List, Optional

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