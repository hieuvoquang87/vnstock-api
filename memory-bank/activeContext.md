# Active Context: vnstock-api

## Current Work Focus

The project is currently in the planning phase, focused on establishing the foundational documentation and project structure before beginning implementation. The main focus areas are:

1. **Project Setup**

   - Establishing project documentation
   - Creating the Memory Bank structure
   - Setting up the basic repository structure
   - Defining detailed file and folder organization
   - Creating implementation documentation structure

2. **Initial Planning**

   - Defining the API wrapper scope based on vnstock library capabilities
   - Planning the architecture and component design
   - Establishing development phases and milestones
   - Designing for serverless deployment
   - Designing documentation strategy

3. **Requirements Analysis**
   - Understanding the vnstock library functionality
   - Identifying key API endpoints to implement
   - Defining authentication and security requirements
   - Planning for external managed services integration
   - Determining implementation documentation templates

## Recent Changes

- Created project README.md with comprehensive overview
- Established Memory Bank structure with core documentation files
- Defined the multi-phase development approach
- Outlined system architecture and component relationships
- Added detailed file and folder structure
- Updated to require Python 3.12
- Changed deployment strategy to serverless
- Added requirements for OpenAPI UI and GraphQL Explorer
- Created docs/implementation folder structure mirroring app structure
- Added documentation approach requiring corresponding .md files for each implementation file
- Implemented mock data for GraphQL endpoints while REST API is being finalized

## Next Steps

### Immediate (Phase 1 MVP Preparation)

1. **Project Structure Setup**

   - Initialize Poetry project with pyproject.toml (Python 3.12)
   - Set up Makefile with common commands
   - Create basic directory structure following the defined file organization
   - Set up serverless.yml configuration
   - Create documentation template for implementation files

2. **Environment Configuration**

   - Set up development environment
   - Configure linting and code formatting
   - Create sample environment variables file
   - Set up local development with Docker
   - Create documentation structure and initial templates

3. **Initial Code Implementation**
   - Create FastAPI application skeleton
   - Configure OpenAPI documentation UI
   - Implement basic health check endpoint
   - Set up testing framework
   - Configure serverless handler (Mangum)
   - Create corresponding documentation files for initial implementation

### Short-term (Phase 1 MVP Implementation)

1. **Core API Development**

   - Create vnstock adapter module
   - Implement first REST endpoints
   - Set up OpenAPI documentation with interactive examples
   - Ensure compatibility with serverless deployment
   - Document all implemented functions and endpoints

2. **Testing Strategy**

   - Develop unit tests for adapters and services
   - Implement integration tests for API endpoints
   - Configure test coverage reporting
   - Add serverless-specific tests
   - Document testing approach and patterns

3. **CI/CD Pipeline**
   - Set up GitHub Actions workflow
   - Configure automated testing
   - Set up code quality checks
   - Add serverless deployment pipeline
   - Add documentation validation checks

### Medium-term (Phase 2-3 Planning)

1. **GraphQL Implementation Planning**

   - Research GraphQL schema design for vnstock
   - Plan resolver implementation
   - Design type system
   - Plan GraphQL Explorer integration
   - Create documentation templates for GraphQL components

2. **External Services Integration**
   - Design Redis Cloud integration
   - Plan Supabase integration
   - Define infrastructure as code
   - Design cache invalidation strategy
   - Document integration patterns and configurations

## Active Decisions and Considerations

1. **API Design Decisions**

   - How closely should REST endpoints mirror vnstock function names vs. being more RESTful?
   - How to structure the OpenAPI documentation for best user experience?
   - What authentication mechanism should be used for the MVP?
   - How to handle rate limiting in the initial implementation?
   - What documentation template should be used for implementation files?
   - **GraphQL Implementation**: Using mock data for GraphQL endpoints initially while focusing on REST API development. Will revisit and integrate with real data sources after the REST API is finalized.

2. **Technical Considerations**

   - How to optimize serverless cold start times with Python 3.12?
   - Should we use async or sync functions for the adapters?
   - How to handle long-running operations in a serverless environment?
   - What error handling strategy should be used?
   - How to structure the project for optimal serverless deployment?
   - How to ensure documentation stays synchronized with code?

3. **Open Questions**
   - What is the expected load and traffic pattern?
   - Are there any specific performance benchmarks to target?
   - How frequently does the vnstock library update, and how to handle versioning?
   - What are the cost implications of the serverless approach?
   - Should documentation generation be automated or manual?

## Current Development Phase

The project is currently in **Phase 0: Planning and Setup** before beginning the implementation of Phase 1 (MVP). The focus is on establishing a solid foundation and clear direction for the project, with particular attention to serverless architecture, managed services integration, and comprehensive documentation practices.
