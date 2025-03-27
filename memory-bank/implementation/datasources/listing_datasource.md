# Listing Data Source

## Overview

This module provides the data source layer for retrieving listing data from different sources (VCI, TCBS, MSN). It defines an abstract interface for listing data sources and provides implementations that access listing data through the vnstock library.

## Interfaces

### ListingDataSource (Abstract Class)

An abstract interface that defines methods for retrieving listing data.

#### Methods

- `async get_all_symbols(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get list of all available symbols
- `async search_symbols(self, query: str, exchange: Optional[str] = None, industry: Optional[str] = None, to_df: bool = True, show_log: bool = False) -> Dict`: Search for symbols based on criteria
- `async get_symbol_details(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict`: Get detailed information for a specific symbol
- `async get_symbols_by_industries(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get symbols grouped by industry
- `async get_symbols_by_exchange(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get symbols grouped by exchange
- `async get_symbols_by_group(self, group: str = 'VN30', to_df: bool = True, show_log: bool = False) -> Dict`: Get symbols in a specific group like VN30, HNX30, etc.
- `async get_industries_icb(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get industry classification benchmark data
- `async get_all_future_indices(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get all future indices
- `async get_all_covered_warrant(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get all covered warrants
- `async get_all_bonds(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get all bonds
- `async get_all_government_bonds(self, to_df: bool = True, show_log: bool = False) -> Dict`: Get all government bonds

## Implementations

### VCIListingDataSource

An implementation of the `ListingDataSource` interface that retrieves data from the VCI API.

#### Methods

##### async get_all_symbols(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves a list of all available symbols from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing all symbols with their details, including stock code, company name, exchange, industry, market cap, and listing date.

**Example:**

```python
datasource = VCIListingDataSource()
all_symbols = await datasource.get_all_symbols()
```

##### async search_symbols(self, query: str, exchange: Optional[str] = None, industry: Optional[str] = None, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Searches for symbols based on provided criteria from VCI API.

**Parameters:**

- `query` (str): Search query
- `exchange` (Optional[str]): Exchange filter (HOSE, HNX, UPCOM)
- `industry` (Optional[str]): Industry filter
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing matching symbols with their details.

**Example:**

```python
datasource = VCIListingDataSource()
matching_symbols = await datasource.search_symbols("bank", exchange="HOSE")
```

##### async get_symbol_details(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves detailed information for a specific symbol from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing detailed information for the specified symbol.

**Example:**

```python
datasource = VCIListingDataSource()
symbol_details = await datasource.get_symbol_details("VCI")
```

##### async get_symbols_by_industries(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves symbols grouped by industry from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing symbols organized by their respective industries.

**Example:**

```python
datasource = VCIListingDataSource()
industry_symbols = await datasource.get_symbols_by_industries()
```

##### async get_symbols_by_exchange(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves symbols grouped by exchange from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing symbols organized by their respective exchanges.

**Example:**

```python
datasource = VCIListingDataSource()
exchange_symbols = await datasource.get_symbols_by_exchange()
```

##### async get_symbols_by_group(self, group: str = 'VN30', to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves symbols in a specific group from VCI API.

**Parameters:**

- `group` (str): Group name (default: 'VN30')
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing symbols belonging to the specified group.

**Example:**

```python
datasource = VCIListingDataSource()
vn30_symbols = await datasource.get_symbols_by_group('VN30')
```

##### async get_industries_icb(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves industry classification benchmark data from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing industry classification data according to ICB standards.

**Example:**

```python
datasource = VCIListingDataSource()
industries = await datasource.get_industries_icb()
```

##### async get_all_future_indices(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves all future indices from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing future index data.

**Example:**

```python
datasource = VCIListingDataSource()
future_indices = await datasource.get_all_future_indices()
```

##### async get_all_covered_warrant(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves all covered warrants from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing covered warrant data.

**Example:**

```python
datasource = VCIListingDataSource()
covered_warrants = await datasource.get_all_covered_warrant()
```

##### async get_all_bonds(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves all bonds from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing corporate bond data.

**Example:**

```python
datasource = VCIListingDataSource()
bonds = await datasource.get_all_bonds()
```

##### async get_all_government_bonds(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves all government bonds from VCI API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing government bond data.

**Example:**

```python
datasource = VCIListingDataSource()
government_bonds = await datasource.get_all_government_bonds()
```

### TCBSListingDataSource

An implementation of the `ListingDataSource` interface that retrieves data from the TCBS API.

#### Methods

##### async get_all_symbols(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves a list of all available symbols from TCBS API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing all symbols with their details, including stock code, company name, exchange, industry, market cap, and listing date.

**Example:**

```python
datasource = TCBSListingDataSource()
all_symbols = await datasource.get_all_symbols()
```

##### async search_symbols(self, query: str, exchange: Optional[str] = None, industry: Optional[str] = None, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Searches for symbols based on provided criteria from TCBS API.

**Parameters:**

- `query` (str): Search query
- `exchange` (Optional[str]): Exchange filter (HOSE, HNX, UPCOM)
- `industry` (Optional[str]): Industry filter
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing matching symbols with their details.

**Example:**

```python
datasource = TCBSListingDataSource()
matching_symbols = await datasource.search_symbols("bank", exchange="HOSE")
```

##### async get_symbol_details(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves detailed information for a specific symbol from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing detailed information for the specified symbol.

**Example:**

```python
datasource = TCBSListingDataSource()
symbol_details = await datasource.get_symbol_details("TCB")
```

### MSNListingDataSource

An implementation of the `ListingDataSource` interface that retrieves data from the MSN API.

#### Methods

##### async get_all_symbols(self, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves a list of all available symbols from MSN API.

**Parameters:**

- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing all symbols with their details, including stock code, company name, exchange, and other available information.

**Example:**

```python
datasource = MSNListingDataSource()
all_symbols = await datasource.get_all_symbols()
```

##### async search_symbols(self, query: str, locale: str = "en-us", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Searches for symbols based on provided criteria from MSN API.

**Parameters:**

- `query` (str): Search query
- `locale` (str): Locale for the results (e.g., "en-us")
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing matching symbols with their details.

**Example:**

```python
datasource = MSNListingDataSource()
matching_symbols = await datasource.search_symbols("MSFT", locale="en-us")
```

##### async get_symbol_details(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves detailed information for a specific symbol from MSN API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing detailed information for the specified symbol.

**Example:**

```python
datasource = MSNListingDataSource()
symbol_details = await datasource.get_symbol_details("MSFT")
```

## Factory

### DataSourceFactory

A factory class for creating data source instances.

#### Methods

##### create_listing_datasource(source: str = "vci") -> ListingDataSource

**Description:**
Creates a listing data source based on the specified source type.

**Parameters:**

- `source` (str): The source type identifier (default: "vci"). Possible values: "vci", "tcbs", "msn".

**Returns:**
An instance of a class implementing the `ListingDataSource` interface.

**Example:**

```python
factory = DataSourceFactory()
datasource = factory.create_listing_datasource("vci")
```

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module.

## Integration Notes

- VCI implementation uses the VCI-specific Listing class from vnstock
- TCBS implementation uses the TCBS-specific Listing class from vnstock (Note: Based on vnstock-data-explorer.md, TCBS might have limited listing functionality)
- MSN implementation uses the MSN-specific Listing class from vnstock
- All implementations handle DataFrame to dictionary conversion
- Asynchronous methods are used for all data retrieval operations
- Each method in the datasource directly calls the equivalent method in the vnstock Listing class
