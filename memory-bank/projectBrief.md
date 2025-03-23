# Project Brief: vnstock-api

## Project Definition

Create a production-ready API wrapper for the `vnstock` Python library that exposes both REST and GraphQL interfaces, providing Vietnamese stock market data to clients through standardized APIs.

## Core Requirements

1. **API Functionality**

   - Expose all `vnstock` library functions through REST endpoints
   - Provide GraphQL interface for flexible data querying
   - Ensure 1:1 feature parity with the original library

2. **Authentication & Security**

   - Implement API key authentication system
   - Track usage per user
   - Apply rate limiting and throttling
   - Secure all endpoints

3. **Performance**

   - Implement caching using Redis for frequently accessed data
   - Store historical data in Supabase/PostgreSQL to reduce third-party API calls
   - Optimize for response time and throughput

4. **Documentation**

   - Provide comprehensive OpenAPI documentation
   - Include usage examples
   - Document all endpoints and parameters

5. **Quality Assurance**

   - Maintain >85% code coverage
   - Implement CI/CD pipeline for automated testing
   - Follow best practices for code quality and security

6. **AI Integration**
   - Add MCP server for LLM model interaction with the API
   - Enable natural language queries to extract market data

## Project Goals

1. **Phase 1 (MVP):** Create REST API with core vnstock functionality and >85% test coverage
2. **Phase 2:** Add GraphQL API with complete feature parity to REST API
3. **Phase 3:** Integrate Redis caching and Supabase for data persistence
4. **Phase 4:** Add AI capabilities through MCP server integration
5. **Phase 5:** Implement user management, API key system, and usage tracking

## Success Criteria

1. All endpoints match `vnstock` library functionality
2. API response time under 200ms for non-cached requests, under 50ms for cached requests
3. Documentation covers all endpoints and use cases
4. Code coverage exceeds 85%
5. API key management system allows for user tracking and throttling
6. System can scale to handle 100+ requests per second
