"""
Models for the Events API.
"""
from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class EventCreate(BaseModel):
    """Model for creating an event."""

    name: str = Field(..., description="Event name")
    contact_id: Optional[str] = Field(default=None, alias="contactId", description="Contact ID")
    contact_name: Optional[str] = Field(default=None, alias="contactName", description="Contact name")
    kind: Optional[str] = Field(default=None, description="Event kind")
    desc: Optional[str] = Field(default=None, description="Event description")
    start_date: Optional[int] = Field(default=None, alias="startDate", description="Start date (timestamp)")
    duration: Optional[int] = Field(default=None, description="Duration in minutes")
    status: Optional[int] = Field(default=None, description="Event status")
    tags: Optional[List[str]] = Field(default=None, description="Event tags")
    location_desc: Optional[str] = Field(default=None, alias="locationDesc", description="Location description")
    lead_id: Optional[str] = Field(default=None, alias="leadId", description="Lead ID")
    funnel_id: Optional[str] = Field(default=None, alias="funnelId", description="Funnel ID")
    user_id: Optional[str] = Field(default=None, alias="userId", description="User ID")


class EventUpdate(BaseModel):
    """Model for updating an event."""

    name: Optional[str] = Field(default=None, description="Event name")
    contact_id: Optional[str] = Field(default=None, alias="contactId", description="Contact ID")
    contact_name: Optional[str] = Field(default=None, alias="contactName", description="Contact name")
    kind: Optional[str] = Field(default=None, description="Event kind")
    desc: Optional[str] = Field(default=None, description="Event description")
    start_date: Optional[int] = Field(default=None, alias="startDate", description="Start date (timestamp)")
    duration: Optional[int] = Field(default=None, description="Duration in minutes")
    status: Optional[int] = Field(default=None, description="Event status")
    tags: Optional[List[str]] = Field(default=None, description="Event tags")
    location_desc: Optional[str] = Field(default=None, alias="locationDesc", description="Location description")
    lead_id: Optional[str] = Field(default=None, alias="leadId", description="Lead ID")
    funnel_id: Optional[str] = Field(default=None, alias="funnelId", description="Funnel ID")
    user_id: Optional[str] = Field(default=None, alias="userId", description="User ID")


class Event(BaseModel):
    """Event model."""

    id: str = Field(..., description="Event ID")
    name: Optional[str] = Field(default=None, description="Event name")
    contact_id: Optional[str] = Field(default=None, alias="contactId", description="Contact ID")
    kind: Optional[str] = Field(default=None, description="Event kind")
    desc: Optional[str] = Field(default=None, description="Event description")
    start_date: Optional[int] = Field(default=None, alias="startDate", description="Start date (timestamp)")
    duration: Optional[int] = Field(default=None, description="Duration in minutes")
    status: Optional[int] = Field(default=None, description="Event status")
    tags: Optional[List[str]] = Field(default=None, description="Event tags")
    location_desc: Optional[str] = Field(default=None, alias="locationDesc", description="Location description")
    lead_id: Optional[str] = Field(default=None, alias="leadId", description="Lead ID")
    funnel_id: Optional[str] = Field(default=None, alias="funnelId", description="Funnel ID")
    user_id: Optional[str] = Field(default=None, alias="userId", description="User ID")


class EventResponse(BaseResponse):
    """Response model for a single event."""

    model_config = {"extra": "allow"}


class EventListResponse(BaseResponse):
    """Response model for a list of events."""

    model_config = {"extra": "allow"}

