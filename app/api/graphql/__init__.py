from fastapi import APIRouter
import strawberry
from strawberry.fastapi import GraphQLRouter
from .schema import schema

router = APIRouter()

# Create GraphQL router
graphql_app = GraphQLRouter(schema)

# Add GraphQL routes
router.include_router(graphql_app, prefix="/graphql")
