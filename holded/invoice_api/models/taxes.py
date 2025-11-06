"""
Models for the Taxes API.
"""
from typing import Any, Dict, List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class Tax(BaseModel):
    """Tax model."""
    
    id: Optional[str] = Field(default=None, description="Tax ID")
    name: Optional[str] = Field(default=None, description="Tax name")
    rate: Optional[float] = Field(default=None, description="Tax rate")
    type: Optional[str] = Field(default=None, description="Tax type")
    # Allow additional fields as the API structure may vary
    model_config = {"extra": "allow"}


# Response models
class TaxResponse(BaseResponse):
    """Response model for taxes."""
    
    # Taxes can be returned as a list or dict, so we'll use a flexible structure
    items: Optional[List[Tax]] = Field(default=None, description="List of taxes")
    # If it's a direct list response
    data: Optional[List[Tax]] = Field(default=None, description="Tax data")
    # Allow additional fields
    model_config = {"extra": "allow"}

