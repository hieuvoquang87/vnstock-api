# main

## Overview

This module serves as the entry point for the VNStock API application. It sets up the FastAPI application with middleware, documentation URLs, and the root endpoint for health checking. It also includes the Mangum handler for serverless deployment.

## Functions

### root()

**Description:**
An asynchronous function that returns the API health status and basic information.

**Parameters:**
None

**Returns:**
A dictionary containing:

- `status`: Current API status ("ok")
- `message`: A message indicating the API is running
- `version`: Current API version
- `documentation`: URL path to the API documentation

**Example:**

```python
# Direct API call
response = await root()
print(response["status"])  # Outputs: "ok"

# HTTP request
# GET /
# Response: {"status": "ok", "message": "VNStock API is running", "version": "0.1.0", "documentation": "/docs"}
```

**Notes:**
This endpoint is used for health checks and provides basic information about the API.

## Variables

### app

**Description:**
The main FastAPI application instance with configured title, description, version, and documentation URLs.

**Type:**
`fastapi.FastAPI`

### handler

**Description:**
Mangum handler for AWS Lambda integration, used when deploying the API as a serverless function.

**Type:**
`mangum.Mangum`

## Usage Notes

- The app includes CORS middleware configured to allow all origins (should be restricted in production)
- The API documentation is available at `/docs` (Swagger UI) and `/redoc` (ReDoc)
- For local development, the application can be run directly using `uvicorn app.main:app --reload`
- For serverless deployment, the `handler` object is the entry point for the Lambda function
