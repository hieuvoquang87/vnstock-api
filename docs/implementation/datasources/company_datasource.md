# Company Data Source

## Overview

This module provides the data source layer for retrieving company-related information. It defines an abstract interface for company data sources and provides an implementation that accesses VNStock data for Vietnamese companies.

## Interfaces

### CompanyDataSource (Abstract Class)

An abstract interface that defines methods for retrieving company data.

#### Methods

- `async get_company_info(self, symbol: str) -> Dict`: Get comprehensive company information
- `async get_company_profile(self, symbol: str) -> Dict`: Get company profile information
- `async get_company_officers(self, symbol: str) -> List[Dict]`: Get company officers information
- `async get_shareholders(self, symbol: str) -> List[Dict]`: Get major shareholders information
- `async get_insider_trading(self, symbol: str) -> List[Dict]`: Get insider trading information
- `async get_subsidiaries(self, symbol: str) -> List[Dict]`: Get company subsidiaries information
- `async get_company_events(self, symbol: str) -> List[Dict]`: Get company events
- `async get_company_news(self, symbol: str) -> List[Dict]`: Get company news
- `async get_dividends(self, symbol: str) -> List[Dict]`: Get dividend history

## Implementations

### VnstockCompanyDataSource

An implementation of the `CompanyDataSource` interface that retrieves data from the VNStock library.

#### Methods

##### async get_company_info(self, symbol: str) -> Dict

**Description:**
Retrieves comprehensive company information by aggregating data from multiple sources.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A dictionary containing comprehensive company information including profile, officers, shareholders, etc.

**Example:**

```python
datasource = VnstockCompanyDataSource()
company_info = await datasource.get_company_info("VNM")
```

##### async get_company_profile(self, symbol: str) -> Dict

**Description:**
Retrieves the company profile information.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A dictionary containing company profile data such as company name, exchange, industry, etc.

**Example:**

```python
datasource = VnstockCompanyDataSource()
profile = await datasource.get_company_profile("VNM")
```

##### async get_company_officers(self, symbol: str) -> List[Dict]

**Description:**
Retrieves information about company officers.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about a company officer including name, position, and ownership percentage.

**Example:**

```python
datasource = VnstockCompanyDataSource()
officers = await datasource.get_company_officers("VNM")
```

##### async get_shareholders(self, symbol: str) -> List[Dict]

**Description:**
Retrieves information about major shareholders.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about a major shareholder including name and ownership percentage.

**Example:**

```python
datasource = VnstockCompanyDataSource()
shareholders = await datasource.get_shareholders("VNM")
```

##### async get_insider_trading(self, symbol: str) -> List[Dict]

**Description:**
Retrieves insider trading information.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about an insider transaction including transaction date, person/entity, dealing method, and quantity.

**Example:**

```python
datasource = VnstockCompanyDataSource()
insider_transactions = await datasource.get_insider_trading("VNM")
```

##### async get_subsidiaries(self, symbol: str) -> List[Dict]

**Description:**
Retrieves information about company subsidiaries.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about a subsidiary including name and ownership percentage.

**Example:**

```python
datasource = VnstockCompanyDataSource()
subsidiaries = await datasource.get_subsidiaries("VNM")
```

##### async get_company_events(self, symbol: str) -> List[Dict]

**Description:**
Retrieves company events.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about a company event including event name, date, and description.

**Example:**

```python
datasource = VnstockCompanyDataSource()
events = await datasource.get_company_events("VNM")
```

##### async get_company_news(self, symbol: str) -> List[Dict]

**Description:**
Retrieves company news.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about a news item including title, published date, and source.

**Example:**

```python
datasource = VnstockCompanyDataSource()
news = await datasource.get_company_news("VNM")
```

##### async get_dividends(self, symbol: str) -> List[Dict]

**Description:**
Retrieves dividend history.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.

**Returns:**
A list of dictionaries, each containing information about a dividend payment including ex-date, dividend type, and amount.

**Example:**

```python
datasource = VnstockCompanyDataSource()
dividends = await datasource.get_dividends("VNM")
```

## Factory

### DataSourceFactory

A factory class for creating data source instances.

#### Methods

##### create_company_datasource(source: str = "vnstock") -> CompanyDataSource

**Description:**
Creates a company data source based on the specified source type.

**Parameters:**

- `source` (str): The source type identifier (default: "vnstock").

**Returns:**
An instance of a class implementing the `CompanyDataSource` interface.

**Example:**

```python
factory = DataSourceFactory()
datasource = factory.create_company_datasource("vnstock")
```

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module.

## Integration Notes

- Currently using placeholder data in the VNStock implementation
- Will be replaced with actual VNStock library integration
- Data format is consistent with the TCBS data structure
- Asynchronous methods are used for all data retrieval operations
