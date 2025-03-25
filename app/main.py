from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.api.rest.v1 import router as api_v1_router
from app.api.graphql.schema import schema

# Create FastAPI app
app = FastAPI(
    title="VNStock API",
    description="A REST and GraphQL API wrapper for the vnstock Python library",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define root endpoint
@app.get("/", tags=["Health"])
async def root():
    """Return API health status and information."""
    return {
        "status": "ok",
        "message": "VNStock API is running",
        "version": "0.1.0",
        "documentation": "/docs",
        "graphql": "/graphql",
    }

# Include routers
app.include_router(api_v1_router, prefix="/api/v1")

# Add GraphQL route
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 