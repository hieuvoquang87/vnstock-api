from fastapi import APIRouter, Request, Depends
from graphql import graphql_sync
from .schema import schema
import json
import asyncio
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.post("/")
async def graphql_handler(request: Request):
    # Parse the request body
    body = await request.json()
    query = body.get("query")
    variables = body.get("variables")
    operation_name = body.get("operationName")
    
    # Execute the GraphQL query
    result = graphql_sync(
        schema=schema,
        source=query,
        variable_values=variables,
        operation_name=operation_name,
    )
    
    # Return the result
    response = {"data": result.data}
    if result.errors:
        response["errors"] = [
            {
                "message": str(error),
                "path": error.path if hasattr(error, "path") else None,
                "locations": [
                    {"line": loc.line, "column": loc.column}
                    for loc in error.locations
                ] if hasattr(error, "locations") else None
            }
            for error in result.errors
        ]
    
    return response

# Also provide a GraphQL playground
@router.get("/")
async def graphql_playground():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset=utf-8/>
        <meta name="viewport" content="user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, minimal-ui">
        <title>VNStock API - GraphQL Playground</title>
        <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css" />
        <link rel="shortcut icon" href="//cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png" />
        <script src="//cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
    </head>
    <body>
        <div id="root">
            <style>
                body {
                    background-color: rgb(23, 42, 58);
                    font-family: Open Sans, sans-serif;
                    height: 90vh;
                }
                #root {
                    height: 100%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .loading {
                    font-size: 32px;
                    font-weight: 200;
                    color: rgba(255, 255, 255, .6);
                    margin-left: 20px;
                }
                img {
                    width: 78px;
                    height: 78px;
                }
                .title {
                    font-weight: 400;
                }
            </style>
            <img src='//cdn.jsdelivr.net/npm/graphql-playground-react/build/logo.png' alt=''>
            <div class="loading"> Loading
                <span class="title">VNStock API - GraphQL Playground</span>
            </div>
        </div>
        <script>window.addEventListener('load', function (event) {
                GraphQLPlayground.init(document.getElementById('root'), {
                    endpoint: '/graphql'
                })
            })</script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
