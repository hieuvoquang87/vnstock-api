# Trading Data Source

## Overview

This module provides the data source layer for retrieving real-time trading data from different sources (VCI, TCBS). It defines an abstract interface for trading data sources and provides implementations that access trading data through the vnstock library.

## Interfaces

### TradingDataSource (Abstract Class)

An abstract interface that defines methods for retrieving trading data.

#### Methods

- `async get_price_board(self, symbols_list: List[str], to_df: bool = True, show_log: bool = False) -> Dict`: Get price board data for multiple symbols
- `async get_order_book(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict`: Get order book data for a specific symbol
- `async get_trading_history(self, symbol: str, page_size: int = 50, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict`: Get recent trading history for a specific symbol
- `async get_market_overview(self, exchange: str = "all", to_df: bool = True, show_log: bool = False) -> Dict`: Get market overview data

## Implementations

### VCITradingDataSource

An implementation of the `TradingDataSource` interface that retrieves data from the VCI API.

#### Methods

##### async get_price_board(self, symbols_list: List[str], to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves price board data for multiple symbols from VCI API.

**Parameters:**

- `symbols_list` (List[str]): List of stock symbols/tickers
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing price board data for the specified symbols.

**Example:**

```python
datasource = VCITradingDataSource()
price_board = await datasource.get_price_board(["FPT", "VNM", "VHM"])
```

##### async get_order_book(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves order book data for a specific symbol from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing order book data for the specified symbol.

**Example:**

```python
datasource = VCITradingDataSource()
order_book = await datasource.get_order_book("FPT")
```

##### async get_trading_history(self, symbol: str, page_size: int = 50, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves recent trading history for a specific symbol from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `page_size` (int): Number of records per page
- `page` (int): Page number
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing recent trading history for the specified symbol.

**Example:**

```python
datasource = VCITradingDataSource()
trading_history = await datasource.get_trading_history("FPT")
```

##### async get_market_overview(self, exchange: str = "all", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves market overview data from VCI API.

**Parameters:**

- `exchange` (str): Exchange filter (all, HOSE, HNX, UPCOM)
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing market overview data.

**Example:**

```python
datasource = VCITradingDataSource()
market_overview = await datasource.get_market_overview(exchange="HOSE")
```

### TCBSTradingDataSource

An implementation of the `TradingDataSource` interface that retrieves data from the TCBS API.

#### Methods

##### async get_price_board(self, symbols_list: List[str], to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves price board data for multiple symbols from TCBS API.

**Parameters:**

- `symbols_list` (List[str]): List of stock symbols/tickers
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing price board data for the specified symbols.

**Example:**

```python
datasource = TCBSTradingDataSource()
price_board = await datasource.get_price_board(["TCB", "VPB", "MBB"])
```

##### async get_order_book(self, symbol: str, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves order book data for a specific symbol from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing order book data for the specified symbol.

**Example:**

```python
datasource = TCBSTradingDataSource()
order_book = await datasource.get_order_book("TCB")
```

##### async get_trading_history(self, symbol: str, page_size: int = 50, page: int = 0, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves recent trading history for a specific symbol from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `page_size` (int): Number of records per page
- `page` (int): Page number
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing recent trading history for the specified symbol.

**Example:**

```python
datasource = TCBSTradingDataSource()
trading_history = await datasource.get_trading_history("TCB")
```

##### async get_market_overview(self, exchange: str = "all", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves market overview data from TCBS API.

**Parameters:**

- `exchange` (str): Exchange filter (all, HOSE, HNX, UPCOM)
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing market overview data.

**Example:**

```python
datasource = TCBSTradingDataSource()
market_overview = await datasource.get_market_overview(exchange="HOSE")
```

## Factory

### DataSourceFactory

A factory class for creating data source instances.

#### Methods

##### create_trading_datasource(source: str = "vci") -> TradingDataSource

**Description:**
Creates a trading data source based on the specified source type.

**Parameters:**

- `source` (str): The source type identifier (default: "vci"). Possible values: "vci", "tcbs".

**Returns:**
An instance of a class implementing the `TradingDataSource` interface.

**Example:**

```python
factory = DataSourceFactory()
datasource = factory.create_trading_datasource("vci")
```

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module.

## Integration Notes

- VCI implementation uses the VCI-specific Trading class from vnstock
- TCBS implementation uses the TCBS-specific Trading class from vnstock
- All implementations handle DataFrame to dictionary conversion
- Asynchronous methods are used for all data retrieval operations
- Each method in the datasource directly calls the equivalent method in the vnstock Trading class
