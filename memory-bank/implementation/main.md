# main

## Overview

This module serves as the entry point for the VNStock API application. It sets up the FastAPI application with middleware, documentation URLs, and the root endpoint for health checking.

## Functions

### root()

**Description:**
An asynchronous function that returns the API health status and basic information.

**Parameters:**
None

**Returns:**
A dictionary containing:

- `message`: A welcome message
- `documentation`: URL path to the API documentation

**Example:**

```python
# Direct API call
response = await root()
print(response["message"])  # Outputs: "Welcome to VNStock API"

# HTTP request
# GET /
# Response: {"message": "Welcome to VNStock API", "documentation": "/docs"}
```

**Notes:**
This endpoint is used for health checks and provides basic information about the API.

## Variables

### app

**Description:**
The main FastAPI application instance with configured title, description, version, and documentation URLs.

**Type:**
`fastapi.FastAPI`

## Usage Notes

- The app includes CORS middleware configured to allow all origins (should be restricted in production)
- The API documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc)
- For local development, the application can be run directly using `uvicorn app.main:app --reload`
- For production deployment, the application can be run using any ASGI server (e.g., Uvicorn, Hypercorn) or containerized using Docker
