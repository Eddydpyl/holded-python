"""
Models for the Sales Channels API.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse, PaginationParams


class SalesChannelCreate(BaseModel):
    """Model for creating a sales channel."""

    name: str = Field(..., description="Sales channel name")
    desc: str = Field(..., description="Sales channel description")
    accountNum: int = Field(..., description="Account number")


class SalesChannelUpdate(BaseModel):
    """Model for updating a sales channel."""

    name: Optional[str] = Field(default=None, description="Sales channel name")
    desc: Optional[str] = Field(default=None, description="Sales channel description")
    accountNum: Optional[int] = Field(default=None, description="Account number")


class SalesChannel(SalesChannelCreate):
    """Sales channel model."""

    id: str = Field(..., description="Sales channel ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class SalesChannelListParams(PaginationParams):
    """Parameters for listing sales channels."""

    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class SalesChannelResponse(BaseResponse, SalesChannel):
    """Response model for a single sales channel."""

    pass


class SalesChannelListResponse(BaseResponse):
    """Response model for a list of sales channels."""

    items: List[SalesChannel] = Field(..., description="List of sales channels")
    total: Optional[int] = Field(default=None, description="Total number of sales channels")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")
