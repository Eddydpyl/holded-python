"""
Models for the Services API.
"""
from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class ServiceCreate(BaseModel):
    """Model for creating a service."""

    name: str = Field(..., description="Service name")
    desc: Optional[str] = Field(default=None, description="Service description")
    tags: Optional[List[str]] = Field(default=None, description="Service tags")
    tax: Optional[float] = Field(default=None, description="Tax rate")
    subtotal: Optional[int] = Field(default=None, description="Subtotal amount")
    salesChannelId: Optional[str] = Field(default=None, description="Sales channel ID")
    cost: Optional[float] = Field(default=None, description="Service cost")


class ServiceUpdate(BaseModel):
    """Model for updating a service."""

    name: Optional[str] = Field(default=None, description="Service name")
    desc: Optional[str] = Field(default=None, description="Service description")
    tags: Optional[List[str]] = Field(default=None, description="Service tags")
    tax: Optional[float] = Field(default=None, description="Tax rate")
    subtotal: Optional[int] = Field(default=None, description="Subtotal amount")
    salesChannelId: Optional[str] = Field(default=None, description="Sales channel ID")
    cost: Optional[float] = Field(default=None, description="Service cost")


class Service(BaseModel):
    """Service model."""

    id: str = Field(..., description="Service ID")
    name: str = Field(..., description="Service name")
    desc: Optional[str] = Field(default=None, description="Service description")
    tags: Optional[List[str]] = Field(default=None, description="Service tags")
    tax: Optional[float] = Field(default=None, description="Tax rate")
    subtotal: Optional[int] = Field(default=None, description="Subtotal amount")
    salesChannelId: Optional[str] = Field(default=None, description="Sales channel ID")
    cost: Optional[float] = Field(default=None, description="Service cost")
    # Allow additional fields
    model_config = {"extra": "allow"}


# Response models
class ServiceResponse(BaseResponse):
    """Response model for a single service."""

    # Service can be returned directly or wrapped
    id: Optional[str] = Field(default=None, description="Service ID")
    name: Optional[str] = Field(default=None, description="Service name")
    desc: Optional[str] = Field(default=None, description="Service description")
    tags: Optional[List[str]] = Field(default=None, description="Service tags")
    tax: Optional[float] = Field(default=None, description="Tax rate")
    subtotal: Optional[int] = Field(default=None, description="Subtotal amount")
    salesChannelId: Optional[str] = Field(default=None, description="Sales channel ID")
    cost: Optional[float] = Field(default=None, description="Service cost")
    # Allow additional fields
    model_config = {"extra": "allow"}


class ServiceListResponse(BaseResponse):
    """Response model for a list of services."""

    items: Optional[List[Service]] = Field(default=None, description="List of services")
    # Allow additional fields
    model_config = {"extra": "allow"}

