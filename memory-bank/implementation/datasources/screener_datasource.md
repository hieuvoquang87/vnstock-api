# Screener Data Source

## Overview

This module provides the data source layer for screening stocks based on various criteria. It defines an abstract interface for screener data sources and provides implementations that access screening functionality through the vnstock library.

## Interfaces

### ScreenerDataSource (Abstract Class)

An abstract interface that defines methods for stock screening.

#### Methods

- `async stock(self, params: Optional[Dict] = None, limit: int = 1000, lang: str = "vi", to_df: bool = True, show_log: bool = False) -> Dict`: Screen stocks based on custom criteria
- `async technical(self, params: Optional[Dict] = None, limit: int = 1000, lang: str = "vi", to_df: bool = True, show_log: bool = False) -> Dict`: Screen stocks based on technical indicators
- `async fundamental(self, params: Optional[Dict] = None, limit: int = 1000, lang: str = "vi", to_df: bool = True, show_log: bool = False) -> Dict`: Screen stocks based on fundamental indicators

## Implementations

### TCBSScreenerDataSource

An implementation of the `ScreenerDataSource` interface that retrieves data from the TCBS API.

#### Methods

##### async stock(self, params: Optional[Dict] = None, limit: int = 1000, lang: str = "vi", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Screens stocks based on custom criteria from TCBS API.

**Parameters:**

- `params` (Optional[Dict]): Dictionary of screening parameters
- `limit` (int): Maximum number of results to return
- `lang` (str): Language for results (vi or en)
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing matching stocks based on the specified criteria.

**Example:**

```python
datasource = TCBSScreenerDataSource()
params = {
    "exchangeCode": "HOSE",
    "industryCode": "I001",
    "marketCap": {"min": 1000}
}
screened_stocks = await datasource.stock(params=params)
```

##### async technical(self, params: Optional[Dict] = None, limit: int = 1000, lang: str = "vi", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Screens stocks based on technical indicators from TCBS API.

**Parameters:**

- `params` (Optional[Dict]): Dictionary of technical indicators for screening
- `limit` (int): Maximum number of results to return
- `lang` (str): Language for results (vi or en)
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing matching stocks based on technical indicators.

**Example:**

```python
datasource = TCBSScreenerDataSource()
params = {
    "priceChange1W": {"min": 5},
    "macdSignal": "bullish"
}
technical_stocks = await datasource.technical(params=params)
```

##### async fundamental(self, params: Optional[Dict] = None, limit: int = 1000, lang: str = "vi", to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Screens stocks based on fundamental indicators from TCBS API.

**Parameters:**

- `params` (Optional[Dict]): Dictionary of fundamental indicators for screening
- `limit` (int): Maximum number of results to return
- `lang` (str): Language for results (vi or en)
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing matching stocks based on fundamental indicators.

**Example:**

```python
datasource = TCBSScreenerDataSource()
params = {
    "pe": {"max": 15},
    "roe": {"min": 15}
}
fundamental_stocks = await datasource.fundamental(params=params)
```

## Factory

### DataSourceFactory

A factory class for creating data source instances.

#### Methods

##### create_screener_datasource(source: str = "tcbs") -> ScreenerDataSource

**Description:**
Creates a screener data source based on the specified source type.

**Parameters:**

- `source` (str): The source type identifier (default: "tcbs"). Currently only "tcbs" is supported.

**Returns:**
An instance of a class implementing the `ScreenerDataSource` interface.

**Example:**

```python
factory = DataSourceFactory()
datasource = factory.create_screener_datasource("tcbs")
```

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module.

## Integration Notes

- TCBS implementation uses the TCBS-specific Screener class from vnstock
- The screener functionality is currently only available through the TCBS data source
- All implementations handle DataFrame to dictionary conversion
- Asynchronous methods are used for all data retrieval operations
- Each method in the datasource directly calls the equivalent method in the vnstock Screener class
