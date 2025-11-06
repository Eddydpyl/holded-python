"""
Data models for the Holded CRM API.
"""

from .bookings import (
    Booking,
    BookingCreate,
    BookingListResponse,
    BookingResponse,
    BookingUpdate,
    Location,
    LocationListResponse,
    LocationResponse,
    Slot,
    SlotListResponse,
)
from .events import (
    Event,
    EventCreate,
    EventListResponse,
    EventResponse,
    EventUpdate,
)
from .funnels import (
    Funnel,
    FunnelCreate,
    FunnelListResponse,
    FunnelResponse,
    FunnelUpdate,
)
from .leads import (
    Lead,
    LeadCreate,
    LeadDateUpdate,
    LeadListResponse,
    LeadNoteCreate,
    LeadNoteUpdate,
    LeadResponse,
    LeadStageUpdate,
    LeadTaskCreate,
    LeadTaskUpdate,
    LeadUpdate,
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
    "LocationResponse",
    "LocationListResponse",
    "SlotListResponse",
    "BookingResponse",
    "BookingListResponse",
]
