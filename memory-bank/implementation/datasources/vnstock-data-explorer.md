# VNStock Data Explorer Module Documentation

## Overview

The `data_explorer` module provides a comprehensive framework for exploring and retrieving financial data from various sources. It implements a component-based architecture that allows for seamless switching between different data providers.

## Config Class

Configuration settings for the data explorer module.

```python
class Config:
    DEFAULT_SOURCE = "VCI"
    DEFAULT_TIMEOUT = 30  # seconds
    DEFAULT_RETRIES = 3
    CACHE_SIZE = 128
    LOG_LEVEL = logging.INFO

    @classmethod
    def setup(cls, **kwargs)
```

### Methods

**`setup(cls, **kwargs)`\*\*

- **Description**: Updates configuration settings dynamically.
- **Parameters**:
  - `**kwargs`: Configuration parameters to update with their new values.
- **Returns**: None
- **Usage**: This method allows for runtime modification of configuration parameters like timeout, retries, and cache size.

## BaseComponent Class

Abstract base class for all components in the data explorer module.

```python
class BaseComponent:
    SUPPORTED_SOURCES = []

    def __init__(self, symbol: Optional[str] = None, source: str = Config.DEFAULT_SOURCE)
```

### Methods

**`__init__(self, symbol: Optional[str] = None, source: str = Config.DEFAULT_SOURCE)`**

- **Description**: Initializes the component with a symbol and data source.
- **Parameters**:
  - `symbol`: Optional symbol identifier for the financial instrument.
  - `source`: Data source to use (defaults to Config.DEFAULT_SOURCE).
- **Returns**: None
- **Usage**: Creates a base component with specified symbol and data source.

**`_validate_source(self)`**

- **Description**: Validates that the selected source is supported.
- **Parameters**: None
- **Returns**: None
- **Usage**: Internal method that ensures the data source is in the SUPPORTED_SOURCES list.

**`_load_data_source(self)`**

- **Description**: Abstract method to load the appropriate data source.
- **Parameters**: None
- **Returns**: Object representing the data source
- **Usage**: Must be implemented by subclasses to load the specific data source implementation.

## StockComponents Class

Main entry point for accessing stock data from different sources. Manages multiple sub-components.

```python
class StockComponents(BaseComponent):
    SUPPORTED_SOURCES = ["VCI", "TCBS", "MSN"]

    def __init__(self, symbol: str, source: str = Config.DEFAULT_SOURCE, show_log: bool = True)
```

### Methods

**`__init__(self, symbol: str, source: str = Config.DEFAULT_SOURCE, show_log: bool = True)`**

- **Description**: Initializes the component with stock symbol and data source.
- **Parameters**:
  - `symbol`: Stock symbol to retrieve data for.
  - `source`: Data source to use (defaults to Config.DEFAULT_SOURCE).
  - `show_log`: Whether to show logs during operations.
- **Returns**: None
- **Usage**: Creates a stock components manager that provides access to various sub-components.

**`_initialize_components(self)`**

- **Description**: Initializes sub-components (company, finance, listing, etc.).
- **Parameters**: None
- **Returns**: None
- **Usage**: Internal method that sets up the appropriate sub-components based on the selected data source.

**`_load_data_source(self)`**

- **Description**: Returns self as this component manages multiple data sources.
- **Parameters**: None
- **Returns**: self
- **Usage**: This class doesn't load a single data source but rather initializes multiple components.

**`update_symbol(self, symbol: str)`**

- **Description**: Updates the current symbol and reinitializes components.
- **Parameters**:
  - `symbol`: New stock symbol to use.
- **Returns**: None
- **Usage**: Changes the current stock symbol and refreshes all sub-components to use the new symbol.

## Quote Class

Provides access to price quote data for financial instruments.

```python
class Quote(BaseComponent):
    SUPPORTED_SOURCES = ["VCI", "TCBS", "MSN"]

    def __init__(self, symbol: str, source: str = Config.DEFAULT_SOURCE)
```

### Methods

**`__init__(self, symbol: str, source: str = Config.DEFAULT_SOURCE)`**

- **Description**: Initializes the component with symbol and data source.
- **Parameters**:
  - `symbol`: Financial instrument symbol to retrieve quotes for.
  - `source`: Data source to use (defaults to Config.DEFAULT_SOURCE).
- **Returns**: None
- **Usage**: Creates a quote component to retrieve price data for the specified symbol.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific quote data source
- **Usage**: Internal method that dynamically loads the quote implementation for the selected source.

**`_update_data_source(self, symbol: Optional[str] = None)`**

- **Description**: Updates the data source with a new symbol.
- **Parameters**:
  - `symbol`: Optional new symbol to use.
- **Returns**: None
- **Usage**: Internal method to update the symbol and reload the data source if needed.

**`history(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves historical price data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters like start_date, end_date, resolution.
- **Returns**: DataFrame containing historical price data
- **Usage**: Gets historical price data for the specified time period and resolution.

**`intraday(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves intraday price data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing intraday price data
- **Usage**: Gets price data for the current trading day at specific intervals.

**`price_depth(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves market depth data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing market depth data
- **Usage**: Gets bid/ask data showing the order book depth for a symbol.

## Listing Class

Provides access to listings of financial instruments.

```python
class Listing(BaseComponent):
    SUPPORTED_SOURCES = ["VCI", "MSN"]

    def __init__(self, source: str = Config.DEFAULT_SOURCE)
```

### Methods

**`__init__(self, source: str = Config.DEFAULT_SOURCE)`**

- **Description**: Initializes the component with data source.
- **Parameters**:
  - `source`: Data source to use (defaults to Config.DEFAULT_SOURCE).
- **Returns**: None
- **Usage**: Creates a listing component to retrieve lists of financial instruments.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific listing data source
- **Usage**: Internal method that dynamically loads the listing implementation for the selected source.

**`all_symbols(self, **kwargs)`\*\*

- **Description**: Retrieves all available symbols.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing all available symbols
- **Usage**: Gets a comprehensive list of all tradable symbols from the selected source.

**`symbols_by_industries(self, **kwargs)`\*\*

- **Description**: Retrieves symbols grouped by industry.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing symbols organized by industry
- **Usage**: Gets symbols categorized by their respective industries.

**`symbols_by_exchange(self, **kwargs)`\*\*

- **Description**: Retrieves symbols grouped by exchange.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing symbols organized by exchange
- **Usage**: Gets symbols categorized by the exchange they are listed on.

**`symbols_by_group(self, group='VN30', **kwargs)`\*\*

- **Description**: Retrieves symbols in a specific group.
- **Parameters**:
  - `group`: Group name (default: 'VN30')
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing symbols in the specified group
- **Usage**: Gets symbols that belong to specific indices or groups like VN30, HNX30, etc.

**`industries_icb(self, **kwargs)`\*\*

- **Description**: Retrieves industry classification benchmark data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing industry classification data
- **Usage**: Gets information about industry classifications according to ICB standards.

**`all_future_indices(self, **kwargs)`\*\*

- **Description**: Retrieves all future indices.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing future index data
- **Usage**: Gets a list of all available future contracts on indices.

**`all_covered_warrant(self, **kwargs)`\*\*

- **Description**: Retrieves all covered warrants.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing covered warrant data
- **Usage**: Gets a list of all available covered warrants.

**`all_bonds(self, **kwargs)`\*\*

- **Description**: Retrieves all bonds.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing bond data
- **Usage**: Gets a list of all available corporate bonds.

**`all_government_bonds(self, **kwargs)`\*\*

- **Description**: Retrieves all government bonds.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing government bond data
- **Usage**: Gets a list of all available government bonds.

## Trading Class

Provides access to trading-related data.

```python
class Trading(BaseComponent):
    SUPPORTED_SOURCES = ["VCI", "TCBS"]

    def __init__(self, symbol: Optional[str] = 'VN30F1M', source: str = Config.DEFAULT_SOURCE)
```

### Methods

**`__init__(self, symbol: Optional[str] = 'VN30F1M', source: str = Config.DEFAULT_SOURCE)`**

- **Description**: Initializes the component with symbol and data source.
- **Parameters**:
  - `symbol`: Optional symbol, defaults to 'VN30F1M' (futures contract).
  - `source`: Data source to use (defaults to Config.DEFAULT_SOURCE).
- **Returns**: None
- **Usage**: Creates a trading component to access real-time trading data.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific trading data source
- **Usage**: Internal method that dynamically loads the trading implementation for the selected source.

**`_update_data_source(self, symbol: Optional[str] = None)`**

- **Description**: Updates the data source with a new symbol.
- **Parameters**:
  - `symbol`: Optional new symbol to use.
- **Returns**: None
- **Usage**: Internal method to update the symbol and reload the data source if needed.

**`price_board(self, symbols_list: list, **kwargs)`\*\*

- **Description**: Retrieves price board data for multiple symbols.
- **Parameters**:
  - `symbols_list`: List of symbols to retrieve data for.
  - `**kwargs`: Additional parameters for filtering data.
- **Returns**: DataFrame containing price board data
- **Usage**: Gets current price information for multiple symbols simultaneously.

## Company Class

Provides access to company information.

```python
class Company(BaseComponent):
    SUPPORTED_SOURCES = ["TCBS", "VCI"]

    def __init__(self, symbol: Optional[str] = 'ACB', source: str = "TCBS")
```

### Methods

**`__init__(self, symbol: Optional[str] = 'ACB', source: str = "TCBS")`**

- **Description**: Initializes the component with symbol and data source.
- **Parameters**:
  - `symbol`: Optional symbol, defaults to 'ACB'.
  - `source`: Data source to use (defaults to "TCBS").
- **Returns**: None
- **Usage**: Creates a company component to access company information.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific company data source
- **Usage**: Internal method that dynamically loads the company information implementation for the selected source.

**`_update_data_source(self, symbol: Optional[str] = None)`**

- **Description**: Updates the data source with a new symbol.
- **Parameters**:
  - `symbol`: Optional new symbol to use.
- **Returns**: None
- **Usage**: Internal method to update the symbol and reload the data source if needed.

**`overview(self, **kwargs)`\*\*

- **Description**: Retrieves company overview data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing company overview
- **Usage**: Gets general information about the company like sector, industry, description.

**`profile(self, **kwargs)`\*\*

- **Description**: Retrieves company profile data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing company profile details
- **Usage**: Gets detailed profile information about the company.

**`shareholders(self, **kwargs)`\*\*

- **Description**: Retrieves shareholder data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing shareholder information
- **Usage**: Gets information about major shareholders of the company.

**`insider_deals(self, **kwargs)`\*\*

- **Description**: Retrieves insider transaction data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing insider transaction details
- **Usage**: Gets information about trading activities by company insiders.

**`subsidiaries(self, **kwargs)`\*\*

- **Description**: Retrieves subsidiary company data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing subsidiary information
- **Usage**: Gets information about companies owned or controlled by this company.

**`officers(self, **kwargs)`\*\*

- **Description**: Retrieves company officer data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing officer information
- **Usage**: Gets information about key officers and executives of the company.

**`events(self, **kwargs)`\*\*

- **Description**: Retrieves company events data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing event information
- **Usage**: Gets information about important company events like earnings releases, shareholder meetings.

**`news(self, **kwargs)`\*\*

- **Description**: Retrieves company news data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing news articles
- **Usage**: Gets recent news articles about the company.

**`dividends(self, **kwargs)`\*\*

- **Description**: Retrieves dividend history data.
- **Parameters**:
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing dividend history
- **Usage**: Gets historical dividend payment information for the company.

## Finance Class

Provides access to financial statement data.

```python
class Finance(BaseComponent):
    SUPPORTED_SOURCES = ["TCBS", "VCI"]
    SUPPORTED_PERIODS = ["quarter", "annual"]

    def __init__(
        self,
        symbol: str,
        period: str = 'quarter',
        source: str = 'TCBS',
        get_all: bool = True
    )
```

### Methods

**`__init__(self, symbol: str, period: str = 'quarter', source: str = 'TCBS', get_all: bool = True)`**

- **Description**: Initializes the component with symbol, period, source, and retrieval option.
- **Parameters**:
  - `symbol`: Company symbol.
  - `period`: Reporting period (default: 'quarter'). Can be 'quarter' or 'annual'.
  - `source`: Data source to use (defaults to 'TCBS').
  - `get_all`: Whether to retrieve all data (default: True).
- **Returns**: None
- **Usage**: Creates a finance component to access financial statement data.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific finance data source
- **Usage**: Internal method that dynamically loads the financial data implementation for the selected source.

**`_update_data_source(self, symbol: Optional[str] = None)`**

- **Description**: Updates the data source with a new symbol.
- **Parameters**:
  - `symbol`: Optional new symbol to use.
- **Returns**: None
- **Usage**: Internal method to update the symbol and reload the data source if needed.

**`_process_kwargs(self, kwargs: Dict[str, Any])`**

- **Description**: Processes and filters keyword arguments based on the source.
- **Parameters**:
  - `kwargs`: Keyword arguments to process.
- **Returns**: Dict of processed keyword arguments
- **Usage**: Internal method to handle source-specific parameter limitations and requirements.

**`\_get_financial_data(self, data_type: str, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Generic method to retrieve financial data by type.
- **Parameters**:
  - `data_type`: Type of financial data to retrieve (e.g., 'balance_sheet', 'income_statement').
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing requested financial data
- **Usage**: Internal method used by specific financial data retrieval methods.

**`balance_sheet(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves balance sheet data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing balance sheet data
- **Usage**: Gets balance sheet data for the specified period (quarter or annual).

**`income_statement(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves income statement data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing income statement data
- **Usage**: Gets income statement data for the specified period (quarter or annual).

**`cash_flow(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves cash flow statement data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing cash flow statement data
- **Usage**: Gets cash flow statement data for the specified period (quarter or annual).

**`ratio(self, symbol: Optional[str] = None, **kwargs)`\*\*

- **Description**: Retrieves financial ratio data.
- **Parameters**:
  - `symbol`: Optional symbol override.
  - `**kwargs`: Additional parameters for filtering or formatting.
- **Returns**: DataFrame containing financial ratio data
- **Usage**: Gets financial ratios like P/E, ROE, ROA for the specified period.

## Screener Class

Provides stock screening functionality.

```python
class Screener(BaseComponent):
    SUPPORTED_SOURCES = ["TCBS"]

    def __init__(self, source: str = "TCBS")
```

### Methods

**`__init__(self, source: str = "TCBS")`**

- **Description**: Initializes the component with data source.
- **Parameters**:
  - `source`: Data source to use (defaults to "TCBS").
- **Returns**: None
- **Usage**: Creates a screener component to screen stocks based on criteria.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific screener data source
- **Usage**: Internal method that dynamically loads the screener implementation for the selected source.

**`stock(self, **kwargs)`\*\*

- **Description**: Screens stocks based on provided parameters.
- **Parameters**:
  - `**kwargs`: Parameters including 'params' (criteria for screening), 'limit' (result limit), 'lang' (language).
- **Returns**: DataFrame containing stocks matching criteria
- **Usage**: Filters stocks based on criteria like exchange, industry, financial metrics, etc.

## Fund Class

Provides access to fund data.

```python
class Fund(BaseComponent):
    SUPPORTED_SOURCES = ["FMARKET"]

    def __init__(self, source: str = "FMARKET", random_agent: bool = False)
```

### Methods

**`__init__(self, source: str = "FMARKET", random_agent: bool = False)`**

- **Description**: Initializes the component with data source and agent option.
- **Parameters**:
  - `source`: Data source to use (defaults to "FMARKET").
  - `random_agent`: Whether to use random user agent (default: False) to avoid rate limiting.
- **Returns**: None
- **Usage**: Creates a fund component to access fund data.

**`_load_data_source(self)`**

- **Description**: Loads the appropriate data source module.
- **Parameters**: None
- **Returns**: Object representing the specific fund data source
- **Usage**: Internal method that dynamically loads the fund data implementation for the selected source.

## MSNComponents Class

Provides access to MSN-specific data components, particularly for forex markets.

```python
class MSNComponents:
    def __init__(self, symbol: Optional[str]='EURUSD', source: str = "MSN")
```

### Methods

**`__init__(self, symbol: Optional[str]='EURUSD', source: str = "MSN")`**

- **Description**: Initializes the component with symbol and data source.
- **Parameters**:
  - `symbol`: Optional forex pair symbol (default: 'EURUSD').
  - `source`: Data source (default: "MSN").
- **Returns**: None
- **Usage**: Creates an MSN components manager focused on forex data.

**`_initialize_components(self)`**

- **Description**: Initializes sub-components (quote, listing).
- **Parameters**: None
- **Returns**: None
- **Usage**: Internal method that sets up the relevant components for MSN data.

**`update_symbol(self, symbol: str)`**

- **Description**: Updates the current symbol and reinitializes components.
- **Parameters**:
  - `symbol`: New symbol to use.
- **Returns**: None
- **Usage**: Changes the current symbol and refreshes all sub-components to use the new symbol.

## Usage Examples

### Basic Stock Data Retrieval

```python
from vnstock.common.data.data_explorer import StockComponents

# Initialize with a stock symbol and data source
stock_data = StockComponents(symbol="VNM", source="TCBS")

# Get company overview
overview = stock_data.company.overview()

# Get historical prices
history = stock_data.quote.history(start_date="2023-01-01", end_date="2023-12-31")

# Get financial statements
balance_sheet = stock_data.finance.balance_sheet()
income_stmt = stock_data.finance.income_statement()
```

### Listing All Symbols

```python
from vnstock.common.data.data_explorer import Listing

# Initialize listing component
listing = Listing(source="VCI")

# Get all symbols
all_symbols = listing.all_symbols()

# Get VN30 symbols
vn30_symbols = listing.symbols_by_group(group="VN30")
```

### Stock Screening

```python
from vnstock.common.data.data_explorer import Screener

# Initialize screener
screener = Screener(source="TCBS")

# Screen stocks with parameters
params = {
    "exchangeCode": "HOSE",
    "industryCode": "I001",
    "marketCap": {"min": 1000}
}
screened_stocks = screener.stock(params=params)
```
