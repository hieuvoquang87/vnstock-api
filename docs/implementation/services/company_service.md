# Company Service

## Overview

This module provides service-level operations for retrieving and processing company-related data from various data sources. It encapsulates business logic related to Vietnamese companies' information, including company profiles, officers, shareholders, insider trading, subsidiaries, events, news, and dividends.

## Functions

### **init**(self, data_source_factory=DataSourceFactory())

**Description:**
Initializes the CompanyService with a data source factory.

**Parameters:**

- `data_source_factory` (DataSourceFactory, optional): Factory for creating data sources. Defaults to a new instance of DataSourceFactory.

**Returns:**
None.

### async get_company_info(self, symbol: str, source: str = "vnstock") -> Dict

**Description:**
Retrieves comprehensive company information for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A dictionary containing comprehensive company information.

**Example:**

```python
company_service = CompanyService()
company_info = await company_service.get_company_info("VNM")
```

### async get_company_profile(self, symbol: str, source: str = "vnstock") -> Dict

**Description:**
Retrieves the company profile information for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A dictionary containing company profile data.

**Example:**

```python
company_service = CompanyService()
profile = await company_service.get_company_profile("VNM")
```

### async get_company_officers(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves information about company officers for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about a company officer.

**Example:**

```python
company_service = CompanyService()
officers = await company_service.get_company_officers("VNM")
```

### async get_shareholders(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves information about major shareholders for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about a major shareholder.

**Example:**

```python
company_service = CompanyService()
shareholders = await company_service.get_shareholders("VNM")
```

### async get_insider_trading(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves insider trading information for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about an insider transaction.

**Example:**

```python
company_service = CompanyService()
insider_transactions = await company_service.get_insider_trading("VNM")
```

### async get_subsidiaries(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves information about company subsidiaries for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about a subsidiary.

**Example:**

```python
company_service = CompanyService()
subsidiaries = await company_service.get_subsidiaries("VNM")
```

### async get_company_events(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves company events for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about a company event.

**Example:**

```python
company_service = CompanyService()
events = await company_service.get_company_events("VNM")
```

### async get_company_news(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves company news for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about a news item.

**Example:**

```python
company_service = CompanyService()
news = await company_service.get_company_news("VNM")
```

### async get_dividends(self, symbol: str, source: str = "vnstock") -> List[Dict]

**Description:**
Retrieves dividend history for a given stock symbol.

**Parameters:**

- `symbol` (str): Stock symbol/ticker for the company.
- `source` (str, optional): Data source identifier. Defaults to "vnstock".

**Returns:**
A list of dictionaries, each containing information about a dividend payment.

**Example:**

```python
company_service = CompanyService()
dividends = await company_service.get_dividends("VNM")
```

## Private Methods

The service includes several private transformation methods that standardize the data format returned by the data sources:

- `_transform_company_info(self, data: Dict) -> Dict`
- `_transform_company_profile(self, data: Dict) -> Dict`
- `_transform_company_officers(self, data: List[Dict]) -> List[Dict]`
- `_transform_shareholders(self, data: List[Dict]) -> List[Dict]`
- `_transform_insider_trading(self, data: List[Dict]) -> List[Dict]`
- `_transform_subsidiaries(self, data: List[Dict]) -> List[Dict]`
- `_transform_company_events(self, data: List[Dict]) -> List[Dict]`
- `_transform_company_news(self, data: List[Dict]) -> List[Dict]`
- `_transform_dividends(self, data: List[Dict]) -> List[Dict]`

These methods ensure that the data returned by the service adheres to the standardized format expected by the API endpoints, regardless of the source.

## Error Handling

All methods include try-except blocks to catch and log exceptions. Errors are logged using the Python logging module and re-raised to be handled by the caller.

## Integration with Data Sources

The service uses the `DataSourceFactory` to create data source instances based on the requested source (e.g., "vnstock"). This abstraction allows for easy switching between different data providers while maintaining a consistent interface.
