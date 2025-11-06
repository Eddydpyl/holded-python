"""
Models for the Funnels API.
"""

from typing import Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse


class FunnelCreate(BaseModel):
    """Model for creating a funnel."""

    name: str = Field(..., description="Funnel name")


class FunnelUpdate(BaseModel):
    """Model for updating a funnel."""

    name: Optional[str] = Field(default=None, description="Funnel name")


class Funnel(BaseModel):
    """Funnel model."""

    id: str = Field(..., description="Funnel ID")
    name: str = Field(..., description="Funnel name")


class FunnelResponse(BaseResponse):
    """Response model for a single funnel."""

    model_config = {"extra": "allow"}


class FunnelListResponse(BaseResponse):
    """Response model for a list of funnels."""

    model_config = {"extra": "allow"}
