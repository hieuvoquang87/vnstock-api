# Project Brief: vnstock-api

## Project Definition

Create a production-ready API wrapper for the `vnstock` Python library that exposes both REST and GraphQL interfaces, providing Vietnamese stock market data to clients through standardized APIs.

## Core Requirements

1. **API Functionality**

   - Expose all `vnstock` library functions through REST endpoints
   - Provide GraphQL interface for flexible data querying
   - Ensure 1:1 feature parity with the original library
   - Expose OpenAPI documentation UI and GraphQL Explorer for users

2. **Authentication & Security**

   - Implement API key authentication system
   - Track usage per user
   - Apply rate limiting and throttling
   - Secure all endpoints

3. **Performance**

   - Implement caching using external Redis service for frequently accessed data
   - Store historical data in Supabase/PostgreSQL to reduce third-party API calls
   - Optimize for response time and throughput

4. **Documentation**

   - Provide comprehensive OpenAPI documentation
   - Include GraphQL Explorer interface
   - Include usage examples
   - Document all endpoints and parameters
   - Maintain implementation documentation that mirrors application structure
   - Each implementation file must have a corresponding documentation file
   - Document all functions with descriptions, parameters, and examples

5. **Quality Assurance**

   - Maintain >85% code coverage
   - Implement CI/CD pipeline for automated testing
   - Follow best practices for code quality and security

6. **AI Integration**

   - Add MCP server for LLM model interaction with the API
   - Enable natural language queries to extract market data

7. **Deployment**

   - Optimize for serverless deployment (AWS Lambda or similar)
   - Use external managed services for storage and caching
   - Create infrastructure as code for deployment

8. **Technical Requirements**
   - Use Python 3.12 for all development
   - Implement proper folder structure following layered architecture
   - Follow consistent file naming and module organization
   - Structure documentation to mirror code organization

## Project Goals

1. **Phase 1 (MVP):** Create REST API with core vnstock functionality and >85% test coverage
2. **Phase 2:** Add GraphQL API with complete feature parity to REST API
3. **Phase 3:** Integrate external Redis service and Supabase for data persistence
4. **Phase 4:** Add AI capabilities through MCP server integration
5. **Phase 5:** Implement user management, API key system, and usage tracking

## Documentation Structure

The project will maintain comprehensive documentation that mirrors the application structure:

1. **Implementation Documentation**

   - Mirror the `app` directory structure in `docs/implementation`
   - Each implementation file (.py) has a corresponding documentation file (.md)
   - Document all functions, parameters, return types, and examples
   - Keep documentation updated as code changes

2. **API Documentation**

   - OpenAPI documentation with Swagger UI and ReDoc
   - GraphQL Explorer for interactive queries
   - Usage examples for common scenarios

3. **User and Developer Guides**
   - Getting started guides
   - Advanced usage examples
   - Integration instructions

## Success Criteria

1. All endpoints match `vnstock` library functionality
2. API response time under 200ms for non-cached requests, under 50ms for cached requests
3. Documentation covers all endpoints and use cases
4. Code coverage exceeds 85%
5. API key management system allows for user tracking and throttling
6. System can scale to handle 100+ requests per second
7. Successful deployment to serverless environment
8. OpenAPI documentation and GraphQL Explorer accessible to users
9. Complete implementation documentation for all code modules
