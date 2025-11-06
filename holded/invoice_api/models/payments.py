"""
Models for the Payments API.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse, PaginationParams


class PaymentCreate(BaseModel):
    """Model for creating a payment."""
    
    bankId: str = Field(..., description="Bank account ID")
    contactId: str = Field(..., description="Contact ID")
    amount: float = Field(..., description="Payment amount")
    desc: str = Field(..., description="Payment description")
    date: int = Field(..., description="Payment date as timestamp")


class PaymentUpdate(BaseModel):
    """Model for updating a payment."""
    
    bankId: Optional[str] = Field(default=None, description="Bank account ID")
    contactId: Optional[str] = Field(default=None, description="Contact ID")
    amount: Optional[float] = Field(default=None, description="Payment amount")
    desc: Optional[str] = Field(default=None, description="Payment description")
    date: Optional[int] = Field(default=None, description="Payment date as timestamp")


class Payment(PaymentCreate):
    """Payment model."""
    
    id: str = Field(..., description="Payment ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class PaymentListParams(PaginationParams):
    """Parameters for listing payments."""
    
    starttmp: Optional[str] = Field(default=None, description="Starting timestamp")
    endtmp: Optional[str] = Field(default=None, description="Ending timestamp")


# Response models
class PaymentResponse(BaseResponse, Payment):
    """Response model for a single payment."""
    pass


class PaymentListResponse(BaseResponse):
    """Response model for a list of payments."""
    
    items: List[Payment] = Field(..., description="List of payments")
    total: Optional[int] = Field(default=None, description="Total number of payments")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")

