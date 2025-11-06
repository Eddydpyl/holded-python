"""
Models for the Bookings API.
"""
from typing import Any, Dict, List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class BookingCustomField(BaseModel):
    """Model for a booking custom field."""

    name: str = Field(..., description="Custom field name")
    value: Any = Field(..., description="Custom field value")


class BookingCreate(BaseModel):
    """Model for creating a booking."""

    location_id: str = Field(..., alias="locationId", description="Location ID")
    service_id: str = Field(..., alias="serviceId", description="Service ID")
    date_time: int = Field(..., alias="dateTime", description="Booking date and time (timestamp)")
    timezone: str = Field(..., description="Timezone (e.g., 'Europe/Madrid')")
    language: str = Field(..., description="Language code (e.g., 'es', 'en')")
    custom_fields: List[BookingCustomField] = Field(..., alias="customFields", description="Custom fields")


class BookingUpdate(BaseModel):
    """Model for updating a booking."""

    location_id: Optional[str] = Field(default=None, alias="locationId", description="Location ID")
    service_id: Optional[str] = Field(default=None, alias="serviceId", description="Service ID")
    date_time: Optional[int] = Field(default=None, alias="dateTime", description="Booking date and time (timestamp)")
    timezone: Optional[str] = Field(default=None, description="Timezone (e.g., 'Europe/Madrid')")
    language: Optional[str] = Field(default=None, description="Language code (e.g., 'es', 'en')")
    custom_fields: Optional[List[BookingCustomField]] = Field(default=None, alias="customFields", description="Custom fields")


class Location(BaseModel):
    """Location model."""

    id: str = Field(..., description="Location ID")
    name: Optional[str] = Field(default=None, description="Location name")


class LocationResponse(BaseResponse):
    """Response model for a single location."""

    model_config = {"extra": "allow"}


class LocationListResponse(BaseResponse):
    """Response model for a list of locations."""

    model_config = {"extra": "allow"}


class Slot(BaseModel):
    """Available slot model."""

    start: int = Field(..., description="Slot start time (timestamp)")
    end: int = Field(..., description="Slot end time (timestamp)")


class SlotListResponse(BaseResponse):
    """Response model for a list of available slots."""

    model_config = {"extra": "allow"}


class Booking(BaseModel):
    """Booking model."""

    id: str = Field(..., description="Booking ID")
    location_id: Optional[str] = Field(default=None, alias="locationId", description="Location ID")
    service_id: Optional[str] = Field(default=None, alias="serviceId", description="Service ID")
    date_time: Optional[int] = Field(default=None, alias="dateTime", description="Booking date and time (timestamp)")
    timezone: Optional[str] = Field(default=None, description="Timezone")
    language: Optional[str] = Field(default=None, description="Language code")
    custom_fields: Optional[List[Dict[str, Any]]] = Field(default=None, alias="customFields", description="Custom fields")


class BookingResponse(BaseResponse):
    """Response model for a single booking."""

    model_config = {"extra": "allow"}


class BookingListResponse(BaseResponse):
    """Response model for a list of bookings."""

    model_config = {"extra": "allow"}

