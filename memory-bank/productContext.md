# Product Context: vnstock-api

## Why This Project Exists

The `vnstock` Python library provides excellent functionality for accessing Vietnamese stock market data, but it has several limitations:

1. **Accessibility**: Only usable by Python developers within Python applications
2. **Integration**: Difficult to integrate with web applications, mobile apps, or other programming languages
3. **Distribution**: Requires installing and maintaining the library in each client application
4. **Usage Tracking**: No built-in way to track or limit usage

The `vnstock-api` project addresses these limitations by creating a standardized API service that:

- Makes Vietnamese stock market data accessible to any platform or language
- Provides consistent interfaces through REST and GraphQL
- Centralizes data access and caching to improve performance
- Enables usage tracking and management

## Problems It Solves

### For Developers

- **Cross-platform Access**: Access stock data from any programming language or platform
- **Simplified Integration**: Use standard HTTP requests instead of Python library integration
- **Reduced Dependency Management**: No need to manage the vnstock library and its dependencies
- **Flexible Data Queries**: Get exactly the data needed through GraphQL, reducing bandwidth usage

### For Data Providers

- **Usage Monitoring**: Track how users access and utilize the data
- **Access Control**: Implement rate limiting and user-specific permissions
- **Performance Optimization**: Reduce load on underlying data sources through caching
- **Analytics**: Gather insights on most-used data endpoints and user patterns

### For End Users

- **Faster Access**: Benefit from cached responses for commonly requested data
- **AI-Assisted Queries**: Use natural language to query market data (in later phases)
- **Consistent Experience**: Standardized data format across all platforms

## How It Should Work

1. **Client Authentication**:

   - Clients register and receive an API key
   - API key is included in each request header

2. **Request Flow**:

   - REST API: Direct endpoint calls with parameters
   - GraphQL API: Flexible queries specifying exact data needs

3. **Processing**:

   - Check cache for existing data
   - Validate request and permissions
   - Process through appropriate vnstock library functions
   - Cache results for future requests

4. **Response**:
   - Standard JSON responses with consistent structure
   - Error handling with descriptive messages
   - Rate limit and usage information in headers

## User Experience Goals

1. **Developer Experience**:

   - Simple, intuitive API endpoints
   - Comprehensive documentation
   - Predictable response formats
   - Helpful error messages
   - Easy-to-understand rate limiting

2. **Performance**:

   - Fast response times (<200ms for non-cached, <50ms for cached)
   - High availability (99.9%+ uptime)
   - Scalable to handle concurrent requests

3. **Flexibility**:
   - Support for both simple and complex data queries
   - Multiple authentication options (API key, OAuth in future)
   - Various output formats and customization options
