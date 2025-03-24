# Unified REST API Structure

This document outlines the proposed unified REST API structure for vnstock-api, designed to integrate multiple data sources while providing a consistent interface to clients.

## API Design Principles

1. **Resource-oriented**: APIs are organized around resources (stocks, markets, etc.)
2. **Consistent naming**: Endpoints follow predictable patterns
3. **Standardized responses**: All responses use the same format
4. **Source-agnostic**: Client can use data without knowing the underlying source
5. **Multi-source capability**: Can combine or select specific data sources
6. **Proper character handling**: Vietnamese characters are properly encoded

## Base URL

```
/api/v1
```

## Common Query Parameters

All endpoints support these common query parameters:

| Parameter | Description                | Default | Example        |
| --------- | -------------------------- | ------- | -------------- |
| `source`  | Data source to use         | `auto`  | `source=tcbs`  |
| `combine` | Combine multiple sources   | `false` | `combine=true` |
| `format`  | Response format            | `json`  | `format=csv`   |
| `lang`    | Response language          | `en`    | `lang=vi`      |
| `page`    | Page number for pagination | `0`     | `page=2`       |
| `limit`   | Items per page             | `20`    | `limit=50`     |

## Resource Structure

### 1. Companies

#### 1.1 Company Information

```
GET /api/v1/companies/{symbol}
```

Fetches comprehensive company information.

**Example:** `/api/v1/companies/VNM`

#### 1.2 Company Profile

```
GET /api/v1/companies/{symbol}/profile
```

Fetches detailed company profile.

**Example:** `/api/v1/companies/VNM/profile`

#### 1.3 Company Officers

```
GET /api/v1/companies/{symbol}/officers
```

Fetches company management information.

**Example:** `/api/v1/companies/VNM/officers`

#### 1.4 Shareholders

```
GET /api/v1/companies/{symbol}/shareholders
```

Fetches major shareholders information.

**Example:** `/api/v1/companies/VNM/shareholders`

#### 1.5 Insider Trading

```
GET /api/v1/companies/{symbol}/insider-trading
```

Fetches insider trading information.

**Example:** `/api/v1/companies/VNM/insider-trading`

#### 1.6 Subsidiaries

```
GET /api/v1/companies/{symbol}/subsidiaries
```

Fetches company subsidiaries.

**Example:** `/api/v1/companies/VNM/subsidiaries`

#### 1.7 Company Events

```
GET /api/v1/companies/{symbol}/events
```

Fetches company events.

**Example:** `/api/v1/companies/VNM/events`

#### 1.8 Company News

```
GET /api/v1/companies/{symbol}/news
```

Fetches company news.

**Example:** `/api/v1/companies/VNM/news`

#### 1.9 Dividends

```
GET /api/v1/companies/{symbol}/dividends
```

Fetches dividend history.

**Example:** `/api/v1/companies/VNM/dividends`

### 2. Financials

#### 2.1 Income Statement

```
GET /api/v1/financials/{symbol}/income
```

Fetches income statement.

**Parameters:**

- `period`: `yearly` or `quarterly` (default: `yearly`)
- `all`: Include all available periods (default: `false`)

**Example:** `/api/v1/financials/VNM/income?period=quarterly&all=true`

#### 2.2 Balance Sheet

```
GET /api/v1/financials/{symbol}/balance
```

Fetches balance sheet.

**Parameters:**

- `period`: `yearly` or `quarterly` (default: `yearly`)
- `all`: Include all available periods (default: `false`)

**Example:** `/api/v1/financials/VNM/balance?period=yearly&all=true`

#### 2.3 Cash Flow

```
GET /api/v1/financials/{symbol}/cashflow
```

Fetches cash flow statement.

**Parameters:**

- `period`: `yearly` or `quarterly` (default: `yearly`)
- `all`: Include all available periods (default: `false`)

**Example:** `/api/v1/financials/VNM/cashflow?period=yearly&all=true`

#### 2.4 Financial Ratios

```
GET /api/v1/financials/{symbol}/ratios
```

Fetches financial ratios.

**Parameters:**

- `period`: `yearly` or `quarterly` (default: `yearly`)
- `all`: Include all available periods (default: `false`)

**Example:** `/api/v1/financials/VNM/ratios?period=yearly&all=true`

### 3. Market Data

#### 3.1 Historical Prices

```
GET /api/v1/market/prices/{symbol}
```

Fetches historical price data.

**Parameters:**

- `from`: Start date (format: YYYY-MM-DD)
- `to`: End date (format: YYYY-MM-DD)
- `resolution`: Time interval (`1m`, `5m`, `15m`, `30m`, `1h`, `1d`, `1w`, `1M`)

**Example:** `/api/v1/market/prices/VNM?from=2023-01-01&to=2023-12-31&resolution=1d`

#### 3.2 Intraday Data

```
GET /api/v1/market/intraday/{symbol}
```

Fetches intraday trading data.

**Example:** `/api/v1/market/intraday/VNM`

#### 3.3 Current Prices

```
GET /api/v1/market/quotes
```

Fetches current price quotes for multiple symbols.

**Parameters:**

- `symbols`: Comma-separated list of stock symbols

**Example:** `/api/v1/market/quotes?symbols=VNM,FPT,HPG`

#### 3.4 Market Overview

```
GET /api/v1/market/overview
```

Fetches market overview data including indices, top gainers, losers, etc.

**Example:** `/api/v1/market/overview`

### 4. Screener

#### 4.1 Stock Screening

```
POST /api/v1/screener/stocks
```

Screens stocks based on specified criteria.

**Request Body:**

```json
{
  "filters": [
    {
      "field": "pe",
      "operator": "<=",
      "value": 15
    },
    {
      "field": "market_cap",
      "operator": ">",
      "value": 1000000000000
    }
  ],
  "sort": {
    "field": "market_cap",
    "order": "desc"
  },
  "limit": 20
}
```

### 5. Industries

#### 5.1 List Industries

```
GET /api/v1/industries
```

Lists all industries.

**Example:** `/api/v1/industries`

#### 5.2 Industry Companies

```
GET /api/v1/industries/{industry_id}/companies
```

Lists companies in a specific industry.

**Example:** `/api/v1/industries/7/companies`

## Standardized Response Format

All API responses follow this structure:

```json
{
  "data": {
    // Main response data
  },
  "meta": {
    "timestamp": "2023-03-01T12:34:56Z",
    "source": "tcbs",
    "pagination": {
      "page": 0,
      "limit": 20,
      "total": 100,
      "pages": 5
    },
    "version": "0.1.0"
  }
}
```

## Error Response Format

Error responses follow this structure:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": {
      // Additional error information
    }
  }
}
```

## Multiple Data Sources

The API supports specifying and combining multiple data sources:

### Specific Source Selection

```
GET /api/v1/companies/VNM?source=tcbs
```

### Multiple Source Priority

```
GET /api/v1/companies/VNM?source=tcbs,vps,ssi
```

(Tries each source in order until successful)

### Data Combination

```
GET /api/v1/companies/VNM?combine=true&sources=tcbs,vps
```

(Combines data from multiple sources)

## Implementation Notes

1. All endpoints should implement proper Vietnamese character handling
2. Caching should be implemented based on data update frequency
3. Rate limiting should be applied to prevent abuse
4. Authentication will be required for certain endpoints
5. Datasources are abstracted through adapter pattern in the backend
6. Response transformation ensures consistent format regardless of source
7. Error handling should include source-specific error codes when relevant

## Next Steps

1. Review this API structure
2. Prioritize endpoints for implementation
3. Implement core adapter pattern for datasources
4. Develop standardized response transformation
5. Begin implementation of highest priority endpoints
