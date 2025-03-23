import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

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
    }

# Handler for serverless deployment
handler = Mangum(app)

# Include routers
# Example: app.include_router(stocks_router, prefix="/api/v1/stocks", tags=["Stocks"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 