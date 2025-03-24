# Unified GraphQL API Structure

This document outlines the proposed GraphQL API structure for vnstock-api, designed to complement the REST API while providing the flexibility and efficiency benefits of GraphQL.

## API Design Principles

1. **Type-based schema**: Schema organized around core types (Company, Financial, Market, etc.)
2. **Field-level resolution**: Clients can request exactly what they need
3. **Consistent naming**: Fields follow predictable naming patterns
4. **Source-agnostic**: Client can use data without knowing the underlying source
5. **Multi-source capability**: Can combine or select specific data sources
6. **Proper character handling**: Vietnamese characters are properly encoded

## GraphQL Endpoint

```
/api/graphql
```

## Schema Types

### Common Types

```graphql
enum DataSource {
  AUTO
  TCBS
  VCI
  MSN
}

enum Period {
  YEARLY
  QUARTERLY
}

enum Resolution {
  MIN_1
  MIN_5
  MIN_15
  MIN_30
  HOUR_1
  DAY_1
  WEEK_1
  MONTH_1
}

enum SortOrder {
  ASC
  DESC
}

input PaginationInput {
  page: Int = 0
  limit: Int = 20
}

input DateRangeInput {
  from: String!
  to: String
}

input SourceInput {
  source: DataSource = AUTO
  combine: Boolean = false
  sources: [DataSource!]
}

type Pagination {
  page: Int!
  limit: Int!
  total: Int!
  pages: Int!
}

type Meta {
  timestamp: String!
  source: String
  pagination: Pagination
  version: String!
}
```

### Company Types

```graphql
type Company {
  symbol: String!
  name: String!
  exchange: String!
  industry: String!
  companyType: String
  foreignPercent: Float
  outstandingShares: Float
  establishedYear: Int
  employees: Int
  website: String

  # Relationships
  profile: CompanyProfile
  officers: [CompanyOfficer!]
  shareholders: [Shareholder!]
  insiderTrading: [InsiderTrade!]
  subsidiaries: [Subsidiary!]
  events: [CompanyEvent!]
  news: [News!]
  dividends: [Dividend!]
  financials: Financials
}

type CompanyProfile {
  description: String
  history: String
  businessModel: String
  products: [String!]
  address: String
  phoneNumber: String
  email: String
  taxCode: String
}

type CompanyOfficer {
  name: String!
  position: String!
  appointmentDate: String
  biography: String
  shareOwnership: Float
}

type Shareholder {
  name: String!
  ownership: Float!
  shares: Float
  shareChangePercent: Float
  lastUpdate: String
}

type InsiderTrade {
  officer: CompanyOfficer
  tradeDate: String!
  type: String!
  volume: Float!
  price: Float
  totalValue: Float
  sharesAfter: Float
  ownershipAfter: Float
}

type Subsidiary {
  name: String!
  ownership: Float!
  businessType: String
}

type CompanyEvent {
  date: String!
  title: String!
  description: String
  eventType: String!
  url: String
}

type News {
  date: String!
  title: String!
  content: String
  source: String!
  url: String
}

type Dividend {
  exDate: String!
  recordDate: String
  paymentDate: String
  value: Float!
  yield: Float
  eventType: String!
}
```

### Financial Types

```graphql
type Financials {
  incomeStatement(
    period: Period = YEARLY
    all: Boolean = false
  ): [IncomeStatement!]
  balanceSheet(period: Period = YEARLY, all: Boolean = false): [BalanceSheet!]
  cashFlow(period: Period = YEARLY, all: Boolean = false): [CashFlow!]
  ratios(period: Period = YEARLY, all: Boolean = false): [FinancialRatio!]
}

type IncomeStatement {
  period: String!
  fiscalYear: Int!
  quarter: Int
  revenue: Float
  costOfGoodsSold: Float
  grossProfit: Float
  operatingExpenses: Float
  operatingIncome: Float
  pretaxIncome: Float
  netIncome: Float
  eps: Float
  dilutedEps: Float
  # Additional fields as needed
}

type BalanceSheet {
  period: String!
  fiscalYear: Int!
  quarter: Int
  totalAssets: Float
  currentAssets: Float
  cash: Float
  shortTermInvestments: Float
  receivables: Float
  inventory: Float
  totalLiabilities: Float
  currentLiabilities: Float
  longTermDebt: Float
  shareholdersEquity: Float
  # Additional fields as needed
}

type CashFlow {
  period: String!
  fiscalYear: Int!
  quarter: Int
  operatingCashFlow: Float
  investingCashFlow: Float
  financingCashFlow: Float
  netCashFlow: Float
  freeCashFlow: Float
  # Additional fields as needed
}

type FinancialRatio {
  period: String!
  fiscalYear: Int!
  quarter: Int
  peRatio: Float
  pbRatio: Float
  roa: Float
  roe: Float
  debtToEquity: Float
  currentRatio: Float
  quickRatio: Float
  grossMargin: Float
  operatingMargin: Float
  netMargin: Float
  # Additional fields as needed
}
```

### Market Types

```graphql
type MarketData {
  prices(
    symbol: String!
    dateRange: DateRangeInput!
    resolution: Resolution = DAY_1
  ): [PriceData!]
  intraday(symbol: String!): [IntradayData!]
  quotes(symbols: [String!]!): [Quote!]
  overview: MarketOverview
}

type PriceData {
  date: String!
  open: Float!
  high: Float!
  low: Float!
  close: Float!
  volume: Float!
  value: Float
}

type IntradayData {
  time: String!
  price: Float!
  volume: Float!
  side: String
}

type Quote {
  symbol: String!
  price: Float!
  change: Float!
  percentChange: Float!
  open: Float
  high: Float
  low: Float
  volume: Float
  value: Float
  marketCap: Float
}

type MarketOverview {
  indices: [IndexData!]
  topGainers: [Quote!]
  topLosers: [Quote!]
  topVolume: [Quote!]
  foreignTrades: [ForeignTrade!]
}

type IndexData {
  code: String!
  name: String!
  value: Float!
  change: Float!
  percentChange: Float!
  volume: Float
  value: Float
}

type ForeignTrade {
  symbol: String!
  buyVolume: Float!
  sellVolume: Float!
  netVolume: Float!
  buyValue: Float
  sellValue: Float
  netValue: Float
}
```

### Industry Types

```graphql
type Industry {
  id: ID!
  name: String!
  companies: [Company!]
  averageRatios: FinancialRatio
}
```

### Screener Types

```graphql
input FilterInput {
  field: String!
  operator: String!
  value: String!
}

input SortInput {
  field: String!
  order: SortOrder = DESC
}

type ScreenerResult {
  companies: [Company!]
  meta: Meta!
}
```

## Queries

```graphql
type Query {
  # Company Queries
  company(symbol: String!, sourceInput: SourceInput): Company
  companies(
    symbols: [String!]!
    sourceInput: SourceInput
    pagination: PaginationInput
  ): [Company!]!

  # Financial Queries
  financials(symbol: String!, sourceInput: SourceInput): Financials

  # Market Queries
  marketData: MarketData
  prices(
    symbol: String!
    dateRange: DateRangeInput!
    resolution: Resolution = DAY_1
    sourceInput: SourceInput
  ): [PriceData!]
  quotes(symbols: [String!]!, sourceInput: SourceInput): [Quote!]
  marketOverview(sourceInput: SourceInput): MarketOverview

  # Industry Queries
  industries(sourceInput: SourceInput): [Industry!]!
  industry(id: ID!, sourceInput: SourceInput): Industry

  # Screener Queries
  screenStocks(
    filters: [FilterInput!]!
    sort: SortInput
    pagination: PaginationInput
    sourceInput: SourceInput
  ): ScreenerResult
}
```

## Example Queries

### Get Company with Financial Ratios

```graphql
query {
  company(symbol: "VNM") {
    name
    exchange
    industry
    foreignPercent
    profile {
      description
      businessModel
    }
    financials {
      ratios(period: YEARLY) {
        period
        peRatio
        pbRatio
        roe
        roa
      }
    }
  }
}
```

### Get Historical Prices and Company News

```graphql
query {
  prices(
    symbol: "FPT"
    dateRange: { from: "2023-01-01", to: "2023-12-31" }
    resolution: DAY_1
  ) {
    date
    close
    volume
  }

  company(symbol: "FPT") {
    news(pagination: { limit: 5 }) {
      date
      title
      source
    }
  }
}
```

### Screen for Stocks with Multiple Criteria

```graphql
query {
  screenStocks(
    filters: [
      { field: "pe", operator: "<=", value: "15" }
      { field: "market_cap", operator: ">", value: "1000000000000" }
      { field: "roe", operator: ">=", value: "15" }
    ]
    sort: { field: "market_cap", order: DESC }
    pagination: { limit: 10 }
  ) {
    companies {
      symbol
      name
      financials {
        ratios(period: YEARLY) {
          peRatio
          roe
        }
      }
    }
    meta {
      pagination {
        total
      }
    }
  }
}
```

## Implementation Notes

1. The GraphQL API will use the same datasource abstraction as the REST API
2. Field resolvers can be implemented to fetch only required data
3. Vietnamese character handling will be consistent with the REST API
4. Error handling should use GraphQL's error specification
5. Authentication and rate limiting should be applied
6. Complexity analysis should be implemented to prevent excessive queries
7. Dataloaders should be used to avoid N+1 query problems

## Next Steps

1. Review this GraphQL schema
2. Finalize type definitions
3. Implement core resolvers
4. Integrate with datasource abstraction layer
5. Develop GraphQL playground interface
