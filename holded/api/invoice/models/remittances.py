"""
Models for the Remittances API.
"""

from typing import Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse


class Remittance(BaseModel):
    """Remittance model."""

    id: Optional[str] = Field(default=None, description="Remittance ID")
    # Allow additional fields as the API structure may vary
    model_config = {"extra": "allow"}


# Response models
class RemittanceResponse(BaseResponse):
    """Response model for a single remittance."""

    # Allow flexible structure
    model_config = {"extra": "allow"}


class RemittanceListResponse(BaseResponse):
    """Response model for a list of remittances."""

    # Allow flexible structure - API may return list directly or wrapped
    model_config = {"extra": "allow"}
