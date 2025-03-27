import logging
import pandas as pd
from typing import Dict, Optional
from vnstock.common.data.data_explorer import Listing
from app.datasources.base import ListingDataSource, SOURCE_TCBS

# Set up logging
logger = logging.getLogger(__name__)

class TCBSListingDataSource(ListingDataSource):
    """TCBS implementation of the ListingDataSource interface."""

    def __init__(self):
        """Initialize TCBS listing data source."""
        self.listing = Listing(source=SOURCE_TCBS)

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
        """Get list of all available symbols from TCBS API."""
        try:
            df = self.listing.all_symbols(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting all symbols from TCBS: {str(e)}")
            raise

    async def search_symbols(self, query: str, exchange: Optional[str] = None, 
                            industry: Optional[str] = None, 
                            show_log: bool = False) -> Dict:
        """Search for symbols based on criteria from TCBS API."""
        try:
            df = self.listing.search_symbols(
                query=query, 
                exchange=exchange, 
                industry=industry, 
                to_df=True, 
                show_log=show_log
            )
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error searching symbols from TCBS: {str(e)}")
            raise

    async def get_symbol_details(self, symbol: str, 
                                show_log: bool = False) -> Dict:
        """Get detailed information for a specific symbol from TCBS API."""
        try:
            df = self.listing.symbol_details(
                symbol=symbol, 
                to_df=True, 
                show_log=show_log
            )
            return self._convert_df_to_dict(df)
        except Exception as e:
            logger.error(f"Error getting symbol details from TCBS: {str(e)}")
            raise

    # Note: The following methods might have limited functionality in TCBS
    # Implementation will forward to the vnstock library but may raise NotImplementedError
    
    async def get_symbols_by_industries(self, 
                                        show_log: bool = False) -> Dict:
        """Get symbols grouped by industry from TCBS API."""
        try:
            df = self.listing.symbols_by_industries(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'symbols_by_industries' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting symbols by industries from TCBS: {str(e)}")
            raise

    async def get_symbols_by_exchange(self, 
                                     show_log: bool = False) -> Dict:
        """Get symbols grouped by exchange from TCBS API."""
        try:
            df = self.listing.symbols_by_exchange(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'symbols_by_exchange' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting symbols by exchange from TCBS: {str(e)}")
            raise

    async def get_symbols_by_group(self, group: str = 'VN30', 
                                  show_log: bool = False) -> Dict:
        """Get symbols in a specific group from TCBS API."""
        try:
            df = self.listing.symbols_by_group(group=group, to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'symbols_by_group' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting symbols by group from TCBS: {str(e)}")
            raise

    async def get_industries_icb(self, 
                                show_log: bool = False) -> Dict:
        """Get industry classification benchmark data from TCBS API."""
        try:
            df = self.listing.industries_icb(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'industries_icb' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting industries ICB from TCBS: {str(e)}")
            raise

    async def get_all_future_indices(self, 
                                    show_log: bool = False) -> Dict:
        """Get all future indices from TCBS API."""
        try:
            df = self.listing.all_future_indices(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'all_future_indices' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting future indices from TCBS: {str(e)}")
            raise

    async def get_all_covered_warrant(self, 
                                     show_log: bool = False) -> Dict:
        """Get all covered warrants from TCBS API."""
        try:
            df = self.listing.all_covered_warrant(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'all_covered_warrant' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting covered warrants from TCBS: {str(e)}")
            raise

    async def get_all_bonds(self, 
                           show_log: bool = False) -> Dict:
        """Get all bonds from TCBS API."""
        try:
            df = self.listing.all_bonds(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'all_bonds' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting bonds from TCBS: {str(e)}")
            raise

    async def get_all_government_bonds(self, 
                                      show_log: bool = False) -> Dict:
        """Get all government bonds from TCBS API."""
        try:
            df = self.listing.all_government_bonds(to_df=True, show_log=show_log)
            return self._convert_df_to_dict(df)
        except AttributeError:
            logger.error("Method 'all_government_bonds' not supported by TCBS")
            raise NotImplementedError("This method is not supported by TCBS data source")
        except Exception as e:
            logger.error(f"Error getting government bonds from TCBS: {str(e)}")
            raise 