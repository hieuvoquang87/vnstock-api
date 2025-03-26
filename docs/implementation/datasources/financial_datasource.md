# Financial Data Source

## Overview

This module provides the data source layer for retrieving financial data from different sources (TCBS, VCI). It defines an abstract interface for financial data sources and provides implementations that access financial data through the vnstock library.

## Interfaces

### FinancialDataSource (Abstract Class)

An abstract interface that defines methods for retrieving financial data.

#### Methods

- `async get_balance_sheet(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict`: Get balance sheet data
- `async get_income_statement(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict`: Get income statement data
- `async get_cash_flow(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict`: Get cash flow data
- `async get_ratios(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict`: Get financial ratios data

## Implementations

### TCBSFinancialDataSource

An implementation of the `FinancialDataSource` interface that retrieves data from the TCBS API.

#### Methods

##### async get_balance_sheet(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves balance sheet data from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing balance sheet data.

**Example:**

```python
datasource = TCBSFinancialDataSource()
balance_sheet = await datasource.get_balance_sheet("FPT")
```

##### async get_income_statement(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves income statement data from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing income statement data.

**Example:**

```python
datasource = TCBSFinancialDataSource()
income_statement = await datasource.get_income_statement("FPT")
```

##### async get_cash_flow(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves cash flow data from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing cash flow data.

**Example:**

```python
datasource = TCBSFinancialDataSource()
cash_flow = await datasource.get_cash_flow("FPT")
```

##### async get_ratios(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves financial ratios data from TCBS API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing financial ratios data.

**Example:**

```python
datasource = TCBSFinancialDataSource()
ratios = await datasource.get_ratios("FPT")
```

### VCIFinancialDataSource

An implementation of the `FinancialDataSource` interface that retrieves data from the VCI API.

#### Methods

##### async get_balance_sheet(self, symbol: str, period: str = "year", lang: str = "vi", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves balance sheet data from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `lang` (str): Language (vi or en)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing balance sheet data.

**Example:**

```python
datasource = VCIFinancialDataSource()
balance_sheet = await datasource.get_balance_sheet("FPT")
```

##### async get_income_statement(self, symbol: str, period: str = "year", lang: str = "vi", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves income statement data from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `lang` (str): Language (vi or en)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing income statement data.

**Example:**

```python
datasource = VCIFinancialDataSource()
income_statement = await datasource.get_income_statement("FPT")
```

##### async get_cash_flow(self, symbol: str, period: str = "year", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves cash flow data from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing cash flow data.

**Example:**

```python
datasource = VCIFinancialDataSource()
cash_flow = await datasource.get_cash_flow("FPT")
```

##### async get_ratios(self, symbol: str, period: str = "year", lang: str = "vi", dropna: bool = True, to_df: bool = True, show_log: bool = False) -> Dict

**Description:**
Retrieves financial ratios data from VCI API.

**Parameters:**

- `symbol` (str): Stock symbol/ticker
- `period` (str): Period type (year or quarter)
- `lang` (str): Language (vi or en)
- `dropna` (bool): Drop rows with all NaN values
- `to_df` (bool): Return as DataFrame
- `show_log` (bool): Show debug logs

**Returns:**
A dictionary containing financial ratios data.

**Example:**

```python
datasource = VCIFinancialDataSource()
ratios = await datasource.get_ratios("FPT")
```

## Factory

### DataSourceFactory

A factory class for creating data source instances.

#### Methods

##### create_financial_datasource(source: str = "tcbs") -> FinancialDataSource

**Description:**
Creates a financial data source based on the specified source type.

**Parameters:**

- `source` (str): The source type identifier (default: "tcbs").

**Returns:**
An instance of a class implementing the `FinancialDataSource` interface.

**Example:**

```python
factory = DataSourceFactory()
datasource = factory.create_financial_datasource("tcbs")
```

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module.

## Integration Notes

- TCBS implementation uses the TCBS-specific Finance class from vnstock
- VCI implementation uses the common Finance class with VCI source
- Both implementations handle DataFrame to dictionary conversion
- Asynchronous methods are used for all data retrieval operations
