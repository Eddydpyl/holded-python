"""
Models for the Numbering Series API.
"""
from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class NumberingSeriesCreate(BaseModel):
    """Model for creating a numbering series."""
    
    name: str = Field(..., description="Numbering series name")
    format: str = Field(..., description="Format string for the numbering")
    last: int = Field(..., description="Last number used in the series")
    type: str = Field(..., description="Document type (invoice, order, etc.)")


class NumberingSeriesUpdate(BaseModel):
    """Model for updating a numbering series."""
    
    name: Optional[str] = Field(default=None, description="Numbering series name")
    format: Optional[str] = Field(default=None, description="Format string for the numbering")
    last: Optional[int] = Field(default=None, description="Last number used in the series")


class NumberingSeries(BaseModel):
    """Numbering series model."""
    
    id: str = Field(..., description="Numbering series ID")
    name: str = Field(..., description="Numbering series name")
    format: str = Field(..., description="Format string for the numbering")
    last: int = Field(..., description="Last number used in the series")
    type: Optional[str] = Field(default=None, description="Document type")


# Response models
class NumberingSeriesResponse(BaseResponse, NumberingSeries):
    """Response model for a single numbering series."""
    pass


class NumberingSeriesListResponse(BaseResponse):
    """Response model for a list of numbering series."""
    
    items: List[NumberingSeries] = Field(..., description="List of numbering series")
    total: Optional[int] = Field(default=None, description="Total number of numbering series") 