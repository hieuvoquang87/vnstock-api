from typing import Dict, Optional, List
import logging
from app.datasources.base import DataSourceFactory, ListingDataSource

logger = logging.getLogger(__name__)

class ListingService:
    """Service for retrieving listing data from various sources."""

    def __init__(self, source: str = "vci"):
        """Initialize the listing service.
        
        Args:
            source: The data source to use (default: "vci")
        """
        self.source = source
        self.datasource = DataSourceFactory.create_listing_datasource(source)

    async def _format_response(self, data: Dict) -> Dict:
        """Format the response data with totalCount and records fields.
        
        Args:
            data: The raw data from the datasource
            
        Returns:
            Formatted data with totalCount and records fields
        """
        if "records" in data:
            # Already formatted, just ensure totalCount is present
            if "totalCount" not in data:
                data["totalCount"] = len(data["records"])
            return data
        
        # Format response with records and totalCount
        records = data.get("data", [])
        if isinstance(records, list):
            total_count = len(records)
        else:
            # If data is not a list, use 1 as count (e.g., for single item responses)
            records = [records] if records else []
            total_count = 1 if records else 0
            
        return {
            "metadata": data.get("metadata", {}),
            "totalCount": total_count,
            "records": records
        }

    async def get_all_symbols(self) -> Dict:
        """Get list of all available symbols.
        
        Returns:
            Dictionary containing all symbols with totalCount and records fields
        """
        try:
            data = await self.datasource.get_all_symbols()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_all_symbols: {str(e)}")
            raise

    async def get_symbols_by_industries(self) -> Dict:
        """Get symbols grouped by industry.
        
        Returns:
            Dictionary containing symbols organized by industries with totalCount and records fields
        """
        try:
            data = await self.datasource.get_symbols_by_industries()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_symbols_by_industries: {str(e)}")
            raise

    async def get_symbols_by_exchange(self) -> Dict:
        """Get symbols grouped by exchange.
        
        Returns:
            Dictionary containing symbols organized by exchanges with totalCount and records fields
        """
        try:
            data = await self.datasource.get_symbols_by_exchange()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_symbols_by_exchange: {str(e)}")
            raise

    async def get_symbols_by_group(self, group: str = 'VN30') -> Dict:
        """Get symbols in a specific group.
        
        Args:
            group: Group name (e.g., VN30, HNX30)
            
        Returns:
            Dictionary containing symbols in the specified group with totalCount and records fields
        """
        try:
            data = await self.datasource.get_symbols_by_group(group=group)
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_symbols_by_group: {str(e)}")
            raise

    async def get_industries_icb(self) -> Dict:
        """Get industry classification benchmark data.
        
        Returns:
            Dictionary containing industry classification data with totalCount and records fields
        """
        try:
            data = await self.datasource.get_industries_icb()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_industries_icb: {str(e)}")
            raise

    async def get_all_future_indices(self) -> Dict:
        """Get all future indices.
        
        Returns:
            Dictionary containing future indices data with totalCount and records fields
        """
        try:
            data = await self.datasource.get_all_future_indices()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_all_future_indices: {str(e)}")
            raise

    async def get_all_covered_warrant(self) -> Dict:
        """Get all covered warrants.
        
        Returns:
            Dictionary containing covered warrants data with totalCount and records fields
        """
        try:
            data = await self.datasource.get_all_covered_warrant()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_all_covered_warrant: {str(e)}")
            raise

    async def get_all_bonds(self) -> Dict:
        """Get all bonds.
        
        Returns:
            Dictionary containing bonds data with totalCount and records fields
        """
        try:
            data = await self.datasource.get_all_bonds()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_all_bonds: {str(e)}")
            raise

    async def get_all_government_bonds(self) -> Dict:
        """Get all government bonds.
        
        Returns:
            Dictionary containing government bonds data with totalCount and records fields
        """
        try:
            data = await self.datasource.get_all_government_bonds()
            return await self._format_response(data)
        except Exception as e:
            logger.error(f"Error in get_all_government_bonds: {str(e)}")
            raise 