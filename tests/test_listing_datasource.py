import asyncio
import json
from app.datasources.base import DataSourceFactory

async def test_vci_listing_datasource():
    """Test VCIListingDataSource functionality."""
    print("\n--- Testing VCI Listing DataSource ---")
    
    # Create data source using factory
    datasource = DataSourceFactory.create_listing_datasource("vci")
    
    # Test get_all_symbols
    print("\nFetching all symbols...")
    all_symbols = await datasource.get_all_symbols()
    print(f"Retrieved {len(all_symbols['records'])} symbols")
    
    # Note: search_symbols and get_symbol_details are not supported by VCI
    # and have been removed from the implementation
    
    # Test get_symbols_by_industries
    print("\nGetting symbols by industries...")
    industry_symbols = await datasource.get_symbols_by_industries()
    print(f"Retrieved {len(industry_symbols['records'])} industry categories")
    
    # Test get_symbols_by_group
    print("\nGetting VN30 symbols...")
    vn30_symbols = await datasource.get_symbols_by_group(group="VN30")
    print(f"Retrieved {len(vn30_symbols['records'])} symbols in VN30")

async def test_tcbs_listing_datasource():
    """Test TCBSListingDataSource functionality."""
    print("\n--- Testing TCBS Listing DataSource ---")
    
    # Create data source using factory
    datasource = DataSourceFactory.create_listing_datasource("tcbs")
    
    # Test get_all_symbols
    print("\nFetching all symbols...")
    all_symbols = await datasource.get_all_symbols()
    print(f"Retrieved {len(all_symbols['records'])} symbols")
    
    # Test search_symbols
    print("\nSearching for 'TCB'...")
    search_results = await datasource.search_symbols(query="TCB")
    print(f"Found {len(search_results['records'])} matches")
    
    # Test get_symbol_details
    print("\nGetting details for 'TCB'...")
    symbol_details = await datasource.get_symbol_details(symbol="TCB")
    print(f"Symbol details: {json.dumps(symbol_details, indent=2)[:200]}...")
    
    # Test methods that might not be supported by TCBS
    print("\nTesting potentially unsupported methods...")
    try:
        industry_symbols = await datasource.get_symbols_by_industries()
        print(f"Retrieved {len(industry_symbols['records'])} industry categories")
    except NotImplementedError as e:
        print(f"get_symbols_by_industries: {str(e)}")

async def main():
    """Main function to run all tests."""
    try:
        await test_vci_listing_datasource()
        await test_tcbs_listing_datasource()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 