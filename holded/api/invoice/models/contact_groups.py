"""
Models for the Contact Groups API.
"""

from typing import Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse


class ContactGroupCreate(BaseModel):
    """Model for creating a contact group."""

    name: str = Field(..., description="Contact group name")
    desc: Optional[str] = Field(default=None, description="Contact group description")
    color: Optional[str] = Field(default=None, description="Contact group color")


class ContactGroupUpdate(BaseModel):
    """Model for updating a contact group."""

    name: Optional[str] = Field(default=None, description="Contact group name")
    desc: Optional[str] = Field(default=None, description="Contact group description")
    color: Optional[str] = Field(default=None, description="Contact group color")


class ContactGroup(BaseModel):
    """Contact group model."""

    id: str = Field(..., description="Contact group ID")
    name: str = Field(..., description="Contact group name")
    desc: Optional[str] = Field(default=None, description="Contact group description")
    color: Optional[str] = Field(default=None, description="Contact group color")
    # Allow additional fields
    model_config = {"extra": "allow"}


# Response models
class ContactGroupResponse(BaseResponse):
    """Response model for a single contact group."""

    # Contact group can be returned directly or wrapped
    id: Optional[str] = Field(default=None, description="Contact group ID")
    name: Optional[str] = Field(default=None, description="Contact group name")
    desc: Optional[str] = Field(default=None, description="Contact group description")
    color: Optional[str] = Field(default=None, description="Contact group color")
    # Allow additional fields
    model_config = {"extra": "allow"}


class ContactGroupListResponse(BaseResponse):
    """Response model for a list of contact groups."""

    items: Optional[list[ContactGroup]] = Field(default=None, description="List of contact groups")
    # Allow additional fields
    model_config = {"extra": "allow"}
