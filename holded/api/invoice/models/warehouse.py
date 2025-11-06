"""
Models for the Warehouse API.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse, PaginationParams


class WarehouseAddress(BaseModel):
    """Warehouse address model."""

    address: Optional[str] = Field(default=None, description="Street address")
    city: Optional[str] = Field(default=None, description="City")
    postalCode: Optional[str] = Field(default=None, description="Postal code")
    province: Optional[str] = Field(default=None, description="Province or state")
    country: Optional[str] = Field(default=None, description="Country")
    countryCode: Optional[str] = Field(default=None, description="Country code")


class WarehouseCreate(BaseModel):
    """Model for creating a warehouse."""

    name: str = Field(..., description="Warehouse name")
    email: Optional[str] = Field(default=None, description="Warehouse email")
    phone: Optional[str] = Field(default=None, description="Warehouse phone")
    mobile: Optional[str] = Field(default=None, description="Warehouse mobile")
    address: Optional[WarehouseAddress] = Field(default=None, description="Warehouse address")
    default: Optional[bool] = Field(default=None, description="Whether this is the default warehouse")


class WarehouseUpdate(BaseModel):
    """Model for updating a warehouse."""

    name: Optional[str] = Field(default=None, description="Warehouse name")
    email: Optional[str] = Field(default=None, description="Warehouse email")
    phone: Optional[str] = Field(default=None, description="Warehouse phone")
    mobile: Optional[str] = Field(default=None, description="Warehouse mobile")
    address: Optional[WarehouseAddress] = Field(default=None, description="Warehouse address")
    default: Optional[bool] = Field(default=None, description="Whether this is the default warehouse")


class Warehouse(WarehouseCreate):
    """Warehouse model."""

    id: str = Field(..., description="Warehouse ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class WarehouseListParams(PaginationParams):
    """Parameters for listing warehouses."""

    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class WarehouseResponse(BaseResponse, Warehouse):
    """Response model for a single warehouse."""

    pass


class WarehouseListResponse(BaseResponse):
    """Response model for a list of warehouses."""

    items: List[Warehouse] = Field(..., description="List of warehouses")
    total: Optional[int] = Field(default=None, description="Total number of warehouses")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")
