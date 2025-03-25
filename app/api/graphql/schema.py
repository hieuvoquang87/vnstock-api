from graphql import (
    GraphQLSchema, 
    GraphQLObjectType, 
    GraphQLString, 
    GraphQLList, 
    GraphQLNonNull, 
    GraphQLEnumType, 
    GraphQLArgument,
    GraphQLField
)
import json
from app.services.company_service import CompanyService
from app.datasources.base import SOURCE_TCBS, SOURCE_VCI, SOURCE_ALL
import asyncio

# Create a function that wraps our async resolvers to make them compatible with GraphQL's execution model
def wrap_async_resolver(resolver):
    def wrapped(obj, info, **kwargs):
        # Create a new event loop for this resolver
        loop = asyncio.new_event_loop()
        try:
            # Run the async resolver in the new loop
            return loop.run_until_complete(resolver(obj, info, **kwargs))
        finally:
            # Close the loop when done
            loop.close()
    return wrapped

# Define the resolver functions
async def resolve_company_info(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_company_info(symbol, source)
    return json.dumps(result)

async def resolve_company_profile(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_company_profile(symbol, source)
    return json.dumps(result)

async def resolve_company_officers(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_company_officers(symbol, source)
    return json.dumps(result)

async def resolve_shareholders(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_shareholders(symbol, source)
    return json.dumps(result)

async def resolve_insider_trading(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_insider_trading(symbol, source)
    return json.dumps(result)

async def resolve_subsidiaries(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_subsidiaries(symbol, source)
    return json.dumps(result)

async def resolve_company_events(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_company_events(symbol, source)
    return json.dumps(result)

async def resolve_company_news(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_company_news(symbol, source)
    return json.dumps(result)

async def resolve_dividends(root, info, symbol, source=SOURCE_ALL):
    service = CompanyService()
    result = await service.get_dividends(symbol, source)
    return json.dumps(result)

# Define an enum for data sources
data_source_enum = GraphQLEnumType(
    'DataSource',
    {
        'TCBS': SOURCE_TCBS,
        'VCI': SOURCE_VCI,
        'ALL': SOURCE_ALL
    },
    description='Data source for stock information'
)

# Now define the query fields using GraphQLField
query_fields = {
    'companyInfo': GraphQLField(
        GraphQLString,  # We'll return JSON string for simplicity
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_company_info)
    ),
    'companyProfile': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_company_profile)
    ),
    'companyOfficers': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_company_officers)
    ),
    'shareholders': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_shareholders)
    ),
    'insiderTrading': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_insider_trading)
    ),
    'subsidiaries': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_subsidiaries)
    ),
    'companyEvents': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_company_events)
    ),
    'companyNews': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_company_news)
    ),
    'dividends': GraphQLField(
        GraphQLString,
        args={
            'symbol': GraphQLArgument(GraphQLNonNull(GraphQLString)),
            'source': GraphQLArgument(data_source_enum, default_value=SOURCE_ALL)
        },
        resolve=wrap_async_resolver(resolve_dividends)
    )
}

# Define Query type
query_type = GraphQLObjectType(
    'Query', 
    lambda: query_fields
)

# Create schema
schema = GraphQLSchema(query=query_type) 