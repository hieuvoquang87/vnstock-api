from typing import Dict, List, Optional, Any, Union
from pydantic import BaseModel, Field

class MetadataModel(BaseModel):
    """Metadata about the response data."""
    shape: List[int] = Field(..., description="Shape of the data [rows, columns]")
    columns: List[str] = Field(..., description="Column names")
    dtypes: Dict[str, str] = Field(..., description="Data types of each column")

class ResponseModel(BaseModel):
    """Generic response model for all listing endpoints."""
    metadata: MetadataModel = Field(..., description="Metadata about the response")
    totalCount: int = Field(..., description="Total number of records")
    records: List[Dict[str, Any]] = Field(..., description="The actual data records")

class ErrorModel(BaseModel):
    """Error response model."""
    error: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")

class ApiResponse(BaseModel):
    """Standard API response model with metadata."""
    data: Union[ResponseModel, Dict[str, Any]] = Field(..., description="Response data")
    meta: Dict[str, Any] = Field(
        default_factory=lambda: {
            "version": "1.0",
        },
        description="Response metadata"
    )

class ApiErrorResponse(BaseModel):
    """Standard API error response model."""
    error: ErrorModel = Field(..., description="Error information")
    meta: Dict[str, Any] = Field(
        default_factory=lambda: {
            "version": "1.0",
        },
        description="Response metadata"
    ) 