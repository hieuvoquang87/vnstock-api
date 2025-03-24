from typing import Any, Dict, Generic, Optional, TypeVar
from pydantic import BaseModel, Field
from datetime import datetime

# Generic type for response data
T = TypeVar('T')


class ResponseMetadata(BaseModel):
    """Metadata included in all API responses"""
    timestamp: datetime = Field(default_factory=datetime.now, description="Response timestamp")
    version: str = Field("1.0", description="API version")


class ErrorDetails(BaseModel):
    """Error details for error responses"""
    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


class APIResponse(BaseModel, Generic[T]):
    """Standard API response format"""
    data: Optional[T] = Field(None, description="Response data")
    meta: ResponseMetadata = Field(default_factory=ResponseMetadata, description="Response metadata")


class ErrorResponse(BaseModel):
    """Standard error response format"""
    error: ErrorDetails = Field(..., description="Error information")
    meta: ResponseMetadata = Field(default_factory=ResponseMetadata, description="Response metadata")


def create_api_response(data: Any) -> Dict[str, Any]:
    """Create a standardized API response with the provided data"""
    return APIResponse(data=data).dict()


def create_error_response(code: str, message: str, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a standardized error response"""
    error = ErrorDetails(code=code, message=message, details=details)
    return ErrorResponse(error=error).dict() 