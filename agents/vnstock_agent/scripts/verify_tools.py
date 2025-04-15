#!/usr/bin/env python3
"""
Verification script for listing_tools.py
"""

import asyncio
import sys
import os
import json

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
tools_dir = os.path.join(parent_dir, 'tools')
sample_data_dir = os.path.join(current_dir, 'sample-data')
sys.path.insert(0, parent_dir)

# Ensure sample data directory exists
os.makedirs(sample_data_dir, exist_ok=True)

# Import the tools module
from agents.vnstock_agent.tools.listing_tools import (
    get_all_symbols,
    get_symbols_by_industries,
    get_symbols_by_exchange,
    get_symbols_by_group,
    get_industries_icb,
)

def save_to_json(data, function_name):
    """Save data to a JSON file named after the function."""
    file_path = os.path.join(sample_data_dir, f"{function_name}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved data to {file_path}")

async def verify_tools():
    """Verify all listing tools functions and save results to JSON files."""
    print("Verifying listing_tools.py...")
    
    # Test get_all_symbols
    print("\nTesting get_all_symbols...")
    result = await get_all_symbols()
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        data = result['data']
        print(f"Total symbols: {data['totalCount']}")
        if data['records']:
            print(f"First symbol: {json.dumps(data['records'][0], indent=2)}")
        save_to_json(result, "get_all_symbols")
    else:
        print(f"Error: {result['error_message']}")
    
    # Test get_symbols_by_industries
    print("\nTesting get_symbols_by_industries...")
    result = await get_symbols_by_industries()
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        data = result['data']
        print(f"Total industry categories: {data['totalCount']}")
        save_to_json(result, "get_symbols_by_industries")
    else:
        print(f"Error: {result['error_message']}")
    
    # Test get_symbols_by_exchange
    print("\nTesting get_symbols_by_exchange...")
    result = await get_symbols_by_exchange()
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        data = result['data']
        print(f"Total exchanges: {data['totalCount']}")
        save_to_json(result, "get_symbols_by_exchange")
    else:
        print(f"Error: {result['error_message']}")
    
    # Test get_symbols_by_group
    print("\nTesting get_symbols_by_group...")
    result = await get_symbols_by_group(group="VN30")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        data = result['data']
        print(f"Total symbols in VN30: {data['totalCount']}")
        save_to_json(result, "get_symbols_by_group")
    else:
        print(f"Error: {result['error_message']}")
    
    # Test get_industries_icb
    print("\nTesting get_industries_icb...")
    result = await get_industries_icb()
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        data = result['data']
        print(f"Total industry classifications: {data['totalCount']}")
        save_to_json(result, "get_industries_icb")
    else:
        print(f"Error: {result['error_message']}")
    
    print("\nAll data has been saved to JSON files in the sample-data directory.")

if __name__ == "__main__":
    asyncio.run(verify_tools()) 