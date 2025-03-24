# Datasource Abstraction Layer

This document outlines the datasource abstraction layer that enables the vnstock-api to work with multiple data providers while presenting a unified API to clients.

## Architecture Overview

The datasource abstraction layer sits between the API controllers and the external data sources. It provides a consistent interface for accessing data, regardless of the underlying provider.

```
┌─────────────┐     ┌─────────────┐     ┌──────────────────┐     ┌─────────────┐
│  API Layer  │────►│  Services   │────►│ Datasource Layer │────►│ Data Sources│
│ REST/GraphQL│     │             │     │                  │     │             │
└─────────────┘     └─────────────┘     └──────────────────┘     └─────────────┘
                                                  │
                                                  ▼
                          ┌─────────────────────────────────────────┐
                          │                                         │
                    ┌─────┴─────┐                            ┌──────┴─────┐
                    │ Adapters  │                            │  Factories │
                    └───────────┘                            └────────────┘
```

## Key Components

### 1. DataSource Interface

Each datasource type implements a common interface that defines standard methods for retrieving data:

```python
class DataSource(ABC):
    """Abstract base class for all data sources."""

    @abstractmethod
    async def get_company_info(self, symbol: str) -> Dict:
        """Get company information."""
        pass

    @abstractmethod
    async def get_historical_prices(self, symbol: str, from_date: str, to_date: str, resolution: str) -> List[Dict]:
        """Get historical price data."""
        pass

    # ... Other method definitions
```

### 2. Concrete Implementations

Each data provider has its own implementation:

```python
class TcbsDataSource(DataSource):
    """TCBS implementation of the DataSource interface."""

    async def get_company_info(self, symbol: str) -> Dict:
        """Get company information from TCBS."""
        # Implementation specific to TCBS

    # ... Other method implementations

class VpsDataSource(DataSource):
    """VPS implementation of the DataSource interface."""

    async def get_company_info(self, symbol: str) -> Dict:
        """Get company information from VPS."""
        # Implementation specific to VPS

    # ... Other method implementations
```

### 3. DataSource Factory

The factory creates the appropriate datasource based on configuration:

```python
class DataSourceFactory:
    """Factory for creating data sources."""

    @staticmethod
    def create(source: str = "auto") -> DataSource:
        """Create a data source instance."""
        if source == "tcbs":
            return TcbsDataSource()
        elif source == "vps":
            return VpsDataSource()
        elif source == "ssi":
            return SsiDataSource()
        # ... other data sources
        else:
            return AutoDataSource()  # Automatically selects best source
```

### 4. Composite DataSource

For combining data from multiple sources:

```python
class CompositeDataSource(DataSource):
    """Combines data from multiple sources."""

    def __init__(self, sources: List[DataSource]):
        self.sources = sources

    async def get_company_info(self, symbol: str) -> Dict:
        """Get and combine company information from multiple sources."""
        results = {}
        for source in self.sources:
            try:
                data = await source.get_company_info(symbol)
                results = self._merge_data(results, data)
            except Exception as e:
                logger.warning(f"Failed to get data from source: {e}")
        return results

    # ... Other method implementations
```

### 5. Fallback DataSource

For trying multiple sources in order until successful:

```python
class FallbackDataSource(DataSource):
    """Tries multiple sources in order until one succeeds."""

    def __init__(self, sources: List[DataSource]):
        self.sources = sources

    async def get_company_info(self, symbol: str) -> Dict:
        """Get company information, trying each source in order."""
        for source in self.sources:
            try:
                return await source.get_company_info(symbol)
            except Exception as e:
                logger.warning(f"Source failed: {e}")
        raise Exception("All data sources failed")

    # ... Other method implementations
```

## Implementation Pattern

### 1. Service Layer

The service layer utilizes the datasource abstraction:

```python
class CompanyService:
    """Service for company-related operations."""

    def __init__(self, data_source_factory=DataSourceFactory()):
        self.data_source_factory = data_source_factory

    async def get_company_info(self, symbol: str, source="auto", combine=False, sources=None):
        """Get company information."""
        if combine and sources:
            # Create a composite datasource
            data_sources = [self.data_source_factory.create(s) for s in sources]
            data_source = CompositeDataSource(data_sources)
        elif sources and len(sources) > 1:
            # Create a fallback datasource
            data_sources = [self.data_source_factory.create(s) for s in sources]
            data_source = FallbackDataSource(data_sources)
        else:
            # Create a single datasource
            data_source = self.data_source_factory.create(source)

        # Get the data
        data = await data_source.get_company_info(symbol)

        # Transform to standard format
        return self._transform_company_info(data)

    def _transform_company_info(self, data: Dict) -> Dict:
        """Transform data to standard format."""
        # Transformation logic to standardize fields
```

### 2. Controller Layer (REST)

The REST controller uses the service:

```python
@router.get("/companies/{symbol}")
async def get_company(
    symbol: str,
    source: str = "auto",
    combine: bool = False,
    sources: Optional[str] = None
):
    """Get company information."""
    source_list = sources.split(",") if sources else None

    # Use the service
    company_service = CompanyService()
    data = await company_service.get_company_info(
        symbol=symbol,
        source=source,
        combine=combine,
        sources=source_list
    )

    # Create the response
    return create_api_response(data)
```

### 3. Resolver Layer (GraphQL)

The GraphQL resolver uses the same service:

```python
async def resolve_company(_, info, symbol, source_input=None):
    """Resolve company query."""
    source = "auto"
    combine = False
    sources = None

    if source_input:
        source = source_input.get("source", "auto")
        combine = source_input.get("combine", False)
        sources = source_input.get("sources")

    # Use the service
    company_service = CompanyService()
    return await company_service.get_company_info(
        symbol=symbol,
        source=source,
        combine=combine,
        sources=sources
    )
```

## Caching Strategy

The datasource layer implements caching to improve performance and reduce load on external APIs:

```python
class CachedDataSource(DataSource):
    """Adds caching to a data source."""

    def __init__(self, data_source: DataSource, cache_service: CacheService, ttl=3600):
        self.data_source = data_source
        self.cache_service = cache_service
        self.ttl = ttl

    async def get_company_info(self, symbol: str) -> Dict:
        """Get company information with caching."""
        cache_key = f"company_info:{symbol}"
        cached_data = await self.cache_service.get(cache_key)

        if cached_data:
            return cached_data

        data = await self.data_source.get_company_info(symbol)
        await self.cache_service.set(cache_key, data, ttl=self.ttl)
        return data

    # ... Other method implementations
```

## Error Handling

The datasource layer implements standardized error handling:

```python
class DataSourceError(Exception):
    """Base class for all data source errors."""

    def __init__(self, message, code, source=None, details=None):
        self.message = message
        self.code = code
        self.source = source
        self.details = details
        super().__init__(message)

class SymbolNotFoundError(DataSourceError):
    """Raised when a symbol is not found."""

    def __init__(self, symbol, source=None):
        super().__init__(
            message=f"Symbol '{symbol}' not found",
            code="SYMBOL_NOT_FOUND",
            source=source,
            details={"symbol": symbol}
        )

# Usage in datasource implementation
async def get_company_info(self, symbol: str) -> Dict:
    """Get company information."""
    try:
        # Try to get data from external API
    except ExternalApiError as e:
        if e.status_code == 404:
            raise SymbolNotFoundError(symbol, source="tcbs")
        raise DataSourceError(
            message=f"Failed to get company info: {str(e)}",
            code="EXTERNAL_API_ERROR",
            source="tcbs",
            details={"status_code": e.status_code}
        )
```

## Configuration

Datasource configuration is managed via environment variables or configuration files:

```python
class DataSourceConfig:
    """Configuration for data sources."""

    def __init__(self):
        self.tcbs_api_key = os.getenv("TCBS_API_KEY")
        self.tcbs_base_url = os.getenv("TCBS_BASE_URL", "https://apipubaws.tcbs.com.vn/")
        self.vps_api_key = os.getenv("VPS_API_KEY")
        self.vps_base_url = os.getenv("VPS_BASE_URL")
        # ... other configuration
```

## Vietnamese Character Handling

All datasources implement consistent handling of Vietnamese characters:

```python
def _process_response(self, response_data: Dict) -> Dict:
    """Process response to handle Vietnamese characters."""
    # Convert the response to JSON with proper Vietnamese character handling
    json_str = json.dumps(response_data, ensure_ascii=False)
    return json.loads(json_str)
```

## Next Steps

1. Implement the base DataSource interface
2. Create concrete implementations for each data provider
3. Implement the factory and composite patterns
4. Add caching to improve performance
5. Implement comprehensive error handling
6. Develop unit tests for each datasource implementation
