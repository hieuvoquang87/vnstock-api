import logging
import pandas as pd
from typing import Dict, Optional
from vnstock.common.data.data_explorer import Listing
from app.datasources.base import ListingDataSource, SOURCE_VCI

# Set up logging
logger = logging.getLogger(__name__)

class VCIListingDataSource(ListingDataSource):
    """VCI implementation of the ListingDataSource interface."""

    def __init__(self):
        """Initialize VCI listing data source."""
        self.listing = Listing(source=SOURCE_VCI)

    def _convert_df_to_dict(self, df: pd.DataFrame) -> Dict:
        """Convert DataFrame to dictionary format."""
        if not isinstance(df, pd.DataFrame):
            return df
        
        records = df.to_dict(orient='records')
        
        return {
            'totalCount': list(df.shape)[0],
            'records': records
        }

    async def get_all_symbols(self, show_log: bool = False) -> Dict:
        """Get list of all available symbols from VCI API."""
        try:
            df = self.listing.all_symbols(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting all symbols from VCI: {str(e)}")
            raise

    # Note: VCI does not support search_symbols and get_symbol_details
    # These methods are handled by the base class which raises NotImplementedError

    async def get_symbols_by_industries(self, show_log: bool = False) -> Dict:
        """Get symbols grouped by industry from VCI API."""
        try:
            df = self.listing.symbols_by_industries(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting symbols by industries from VCI: {str(e)}")
            raise

    async def get_symbols_by_exchange(self, show_log: bool = False) -> Dict:
        """Get symbols grouped by exchange from VCI API."""
        try:
            df = self.listing.symbols_by_exchange(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting symbols by exchange from VCI: {str(e)}")
            raise

    async def get_symbols_by_group(self, group: str = 'VN30', show_log: bool = False) -> Dict:
        """Get symbols in a specific group from VCI API."""
        try:
            df = self.listing.symbols_by_group(group=group, to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting symbols by group from VCI: {str(e)}")
            raise

    async def get_industries_icb(self, show_log: bool = False) -> Dict:
        """Get industry classification benchmark data from VCI API."""
        try:
            df = self.listing.industries_icb(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting industries ICB from VCI: {str(e)}")
            raise

    async def get_all_future_indices(self, show_log: bool = False) -> Dict:
        """Get all future indices from VCI API."""
        try:
            df = self.listing.all_future_indices(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting future indices from VCI: {str(e)}")
            raise

    async def get_all_covered_warrant(self, show_log: bool = False) -> Dict:
        """Get all covered warrants from VCI API."""
        try:
            df = self.listing.all_covered_warrant(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting covered warrants from VCI: {str(e)}")
            raise

    async def get_all_bonds(self, show_log: bool = False) -> Dict:
        """Get all bonds from VCI API."""
        try:
            df = self.listing.all_bonds(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting bonds from VCI: {str(e)}")
            raise

    async def get_all_government_bonds(self, show_log: bool = False) -> Dict:
        """Get all government bonds from VCI API."""
        try:
            df = self.listing.all_government_bonds(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting government bonds from VCI: {str(e)}")
            raise 