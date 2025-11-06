"""
Data models for the Holded CRM API.
"""

from .funnels import (
    Funnel,
    FunnelCreate,
    FunnelUpdate,
    FunnelResponse,
    FunnelListResponse,
)
from .leads import (
    Lead,
    LeadCreate,
    LeadUpdate,
    LeadNoteCreate,
    LeadNoteUpdate,
    LeadTaskCreate,
    LeadTaskUpdate,
    LeadDateUpdate,
    LeadStageUpdate,
    LeadResponse,
    LeadListResponse,
)
from .events import (
    Event,
    EventCreate,
    EventUpdate,
    EventResponse,
    EventListResponse,
)
from .bookings import (
    Location,
    Slot,
    Booking,
    BookingCreate,
    BookingUpdate,
    BookingCustomField,
    LocationResponse,
    LocationListResponse,
    SlotListResponse,
    BookingResponse,
    BookingListResponse,
)

__all__ = [
    # Funnels
    "Funnel",
    "FunnelCreate",
    "FunnelUpdate",
    "FunnelResponse",
    "FunnelListResponse",
    # Leads
    "Lead",
    "LeadCreate",
    "LeadUpdate",
    "LeadNoteCreate",
    "LeadNoteUpdate",
    "LeadTaskCreate",
    "LeadTaskUpdate",
    "LeadDateUpdate",
    "LeadStageUpdate",
    "LeadResponse",
    "LeadListResponse",
    # Events
    "Event",
    "EventCreate",
    "EventUpdate",
    "EventResponse",
    "EventListResponse",
    # Bookings
    "Location",
    "Slot",
    "Booking",
    "BookingCreate",
    "BookingUpdate",
    "BookingCustomField",
    "LocationResponse",
    "LocationListResponse",
    "SlotListResponse",
    "BookingResponse",
    "BookingListResponse",
]

