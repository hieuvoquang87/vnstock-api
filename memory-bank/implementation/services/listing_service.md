# Listing Service

## Overview

The `ListingService` class provides a high-level interface for accessing listing data from various data sources. It uses the Data Source Factory pattern to create appropriate data source instances based on the requested source type.

## Class: ListingService

### Description

A service class that provides methods for retrieving listing data with standardized formatting and error handling. It acts as an abstraction over different data sources (VCI, TCBS, MSN).

### Location

`app/services/listing_service.py`

### Constructor

```python
def __init__(self, source: str = "vci")
```

**Parameters:**

- `source` (str): The data source to use. Default is "vci". Valid values are "vci", "tcbs", "msn".

**Description:**
Initializes the listing service with the specified data source. It creates the appropriate data source instance using the `DataSourceFactory`.

### Methods

#### \_format_response(self, data: Dict) -> Dict

**Description:**
Internal method to format response data with standardized fields like `totalCount` and `records`.

**Parameters:**

- `data` (Dict): The raw data from the data source

**Returns:**
A dictionary with standardized structure containing:

- `metadata`: Additional information about the data
- `totalCount`: Count of records in the response
- `records`: List of data records

#### async get_all_symbols(self, to_df: bool = False) -> Dict

**Description:**
Get a list of all available symbols with their details.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing all symbols with totalCount and records fields.

**Example:**

```python
service = ListingService()
symbols = await service.get_all_symbols()
print(f"Total symbols: {symbols['totalCount']}")
```

#### async get_symbols_by_industries(self, to_df: bool = False) -> Dict

**Description:**
Get symbols grouped by their respective industries.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing symbols organized by industries with totalCount and records fields.

**Example:**

```python
service = ListingService()
industry_symbols = await service.get_symbols_by_industries()
print(f"Total industries: {industry_symbols['totalCount']}")
```

#### async get_symbols_by_exchange(self, to_df: bool = False) -> Dict

**Description:**
Get symbols grouped by their respective exchanges.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing symbols organized by exchanges with totalCount and records fields.

**Example:**

```python
service = ListingService()
exchange_symbols = await service.get_symbols_by_exchange()
print(f"Total exchanges: {exchange_symbols['totalCount']}")
```

#### async get_symbols_by_group(self, group: str = 'VN30', to_df: bool = False) -> Dict

**Description:**
Get symbols that are part of a specific group like VN30, HNX30, etc.

**Parameters:**

- `group` (str): Group name (e.g., VN30, HNX30)
- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing symbols in the specified group with totalCount and records fields.

**Example:**

```python
service = ListingService()
vn30_symbols = await service.get_symbols_by_group(group="VN30")
print(f"Total VN30 symbols: {vn30_symbols['totalCount']}")
```

#### async get_industries_icb(self, to_df: bool = False) -> Dict

**Description:**
Get industry classification benchmark data.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing industry classification data with totalCount and records fields.

**Example:**

```python
service = ListingService()
industries = await service.get_industries_icb()
print(f"Total industries: {industries['totalCount']}")
```

#### async get_all_future_indices(self, to_df: bool = False) -> Dict

**Description:**
Get all available future indices.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing future indices data with totalCount and records fields.

**Example:**

```python
service = ListingService()
futures = await service.get_all_future_indices()
print(f"Total future indices: {futures['totalCount']}")
```

#### async get_all_covered_warrant(self, to_df: bool = False) -> Dict

**Description:**
Get all available covered warrants.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing covered warrants data with totalCount and records fields.

**Example:**

```python
service = ListingService()
warrants = await service.get_all_covered_warrant()
print(f"Total covered warrants: {warrants['totalCount']}")
```

#### async get_all_bonds(self, to_df: bool = False) -> Dict

**Description:**
Get all available bonds.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing bonds data with totalCount and records fields.

**Example:**

```python
service = ListingService()
bonds = await service.get_all_bonds()
print(f"Total bonds: {bonds['totalCount']}")
```

#### async get_all_government_bonds(self, to_df: bool = False) -> Dict

**Description:**
Get all available government bonds.

**Parameters:**

- `to_df` (bool): Whether internal processing should use DataFrame (client always gets JSON)

**Returns:**
A dictionary containing government bonds data with totalCount and records fields.

**Example:**

```python
service = ListingService()
gov_bonds = await service.get_all_government_bonds()
print(f"Total government bonds: {gov_bonds['totalCount']}")
```

## Notes

- The listing service handles errors gracefully and logs them for debugging
- It provides a consistent interface across different data sources
- The service adds value by standardizing response formats with totalCount and records fields
- Each method has proper error handling and will propagate exceptions with logged context
- The default data source is VCI, but it can be configured to use TCBS or MSN

## Important Implementation Considerations

- **Error Handling**: All public methods include try-except blocks with proper logging
- **Response Formatting**: The `_format_response` method ensures consistent response structure
- **Data Source Selection**: The service allows switching between data sources at initialization time
- **Not Implemented Methods**: Each method will propagate NotImplementedError from the data source if a method is not supported

## Examples

### Basic Usage

```python
# Create a service with the default VCI data source
service = ListingService()

# Get all symbols
symbols = await service.get_all_symbols()

# Get VN30 symbols
vn30 = await service.get_symbols_by_group("VN30")
```

### Using Different Data Sources

```python
# Create a service with the TCBS data source
tcbs_service = ListingService(source="tcbs")

# Get all symbols from TCBS
tcbs_symbols = await tcbs_service.get_all_symbols()
```
