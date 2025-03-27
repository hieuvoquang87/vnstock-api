# Quote Data Source

## Overview

This module provides the data source layer for retrieving quote (price) data from different sources (VCI, TCBS, MSN). It defines an abstract interface for quote data sources and provides implementations that access quote data through the vnstock library.

## Interfaces

### QuoteDataSource (Abstract Class)

An abstract interface that defines methods for retrieving quote data.

#### Methods

- `async get_history(self, symbol: str, start_date: Optional[str] = None, end_date: Optional[str] = None, resolution: str = "1D", type: str = "stock", to_df: bool = True, show_log: bool = False) -> Dict`: Get historical price data
- `async get_intraday(self, symbol: str, page_size: int = 500, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict`: Get intraday price data
- `async get_price_depth(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict`: Get market depth data

## Implementations

### VCIQuoteDataSource

An implementation of the `QuoteDataSource` interface that retrieves data from the VCI API.

#### Methods

##### async get_history(self, symbol: str, start_date: Optional[str] = None, end_date: Optional[str] = None, resolution: str = "1D", type: str = "stock", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves historical price data from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `start_date` (Optional[str]): Start date in format YYYY-MM-DD
- `end_date` (Optional[str]): End date in format YYYY-MM-DD
- `resolution` (str): Time resolution (e.g., "1D" for daily, "1W" for weekly)
- `type` (str): Type of instrument (default: "stock")
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing historical price data including open, high, low, close, and volume.

**Example:**

```python
datasource = VCIQuoteDataSource()
history = await datasource.get_history("FPT", start_date="2023-01-01", end_date="2023-12-31")
```

##### async get_intraday(self, symbol: str, page_size: int = 500, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves intraday price data from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `page_size` (int): Number of records per page
- `page` (int): Page number
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing intraday price data.

**Example:**

```python
datasource = VCIQuoteDataSource()
intraday = await datasource.get_intraday("FPT")
```

##### async get_price_depth(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves market depth data (order book) from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing market depth data including bid and ask levels.

**Example:**

```python
datasource = VCIQuoteDataSource()
price_depth = await datasource.get_price_depth("FPT")
```

### TCBSQuoteDataSource

An implementation of the `QuoteDataSource` interface that retrieves data from the TCBS API.

#### Methods

##### async get_history(self, symbol: str, start_date: Optional[str] = None, end_date: Optional[str] = None, resolution: str = "1D", type: str = "stock", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves historical price data from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `start_date` (Optional[str]): Start date in format YYYY-MM-DD
- `end_date` (Optional[str]): End date in format YYYY-MM-DD
- `resolution` (str): Time resolution (e.g., "1D" for daily, "1W" for weekly)
- `type` (str): Type of instrument (default: "stock")
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing historical price data including open, high, low, close, and volume.

**Example:**

```python
datasource = TCBSQuoteDataSource()
history = await datasource.get_history("TCB", start_date="2023-01-01", end_date="2023-12-31")
```

##### async get_intraday(self, symbol: str, page_size: int = 500, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves intraday price data from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `page_size` (int): Number of records per page
- `page` (int): Page number
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing intraday price data.

**Example:**

```python
datasource = TCBSQuoteDataSource()
intraday = await datasource.get_intraday("TCB")
```

##### async get_price_depth(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves market depth data (order book) from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing market depth data including bid and ask levels.

**Example:**

```python
datasource = TCBSQuoteDataSource()
price_depth = await datasource.get_price_depth("TCB")
```

### MSNQuoteDataSource

An implementation of the `QuoteDataSource` interface that retrieves data from the MSN API.

#### Methods

##### async get_history(self, symbol: str, start_date: Optional[str] = None, end_date: Optional[str] = None, resolution: str = "1D", type: str = "stock", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves historical price data from MSN API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `start_date` (Optional[str]): Start date in format YYYY-MM-DD
- `end_date` (Optional[str]): End date in format YYYY-MM-DD
- `resolution` (str): Time resolution (e.g., "1D" for daily, "1W" for weekly)
- `type` (str): Type of instrument (default: "stock")
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing historical price data including open, high, low, close, and volume.

**Example:**

```python
datasource = MSNQuoteDataSource()
history = await datasource.get_history("MSFT", start_date="2023-01-01", end_date="2023-12-31")
```

##### async get_intraday(self, symbol: str, page_size: int = 500, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves intraday price data from MSN API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `page_size` (int): Number of records per page
- `page` (int): Page number
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing intraday price data.

**Example:**

```python
datasource = MSNQuoteDataSource()
intraday = await datasource.get_intraday("MSFT")
```

##### async get_price_depth(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves market depth data (order book) from MSN API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing market depth data including bid and ask levels.

**Example:**

```python
datasource = MSNQuoteDataSource()
price_depth = await datasource.get_price_depth("MSFT")
```

## Factory

### DataSourceFactory

A factory class for creating data source instances.

#### Methods

##### create_quote_datasource(source: str = "vci") -> QuoteDataSource

**Description:**
Creates a quote data source based on the specified source type.

**Parameters:**

- `source` (str): The source type identifier (default: "vci"). Possible values: "vci", "tcbs", "msn".

**Returns:**
An instance of a class implementing the `QuoteDataSource` interface.

**Example:**

```python
factory = DataSourceFactory()
datasource = factory.create_quote_datasource("vci")
```

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module.

## Integration Notes

- VCI implementation uses the VCI-specific Quote class from vnstock
- TCBS implementation uses the TCBS-specific Quote class from vnstock
- MSN implementation uses the MSN-specific Quote class from vnstock
- All implementations handle DataFrame to dictionary conversion
- Asynchronous methods are used for all data retrieval operations
- Each method in the datasource directly calls the equivalent method in the vnstock Quote class
