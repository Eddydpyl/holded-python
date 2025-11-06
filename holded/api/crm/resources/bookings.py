"""
Resource for interacting with the Bookings API.
"""

from typing import Any, Dict, List, cast

from ...resources import BaseResource
from ..models.bookings import BookingCreate, BookingUpdate


class BookingsResource(BaseResource):
    """Resource for interacting with the Bookings API."""

    def __init__(self, client):
        """Initialize the bookings resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "crm/bookings"

    def list_locations(self) -> List[Dict[str, Any]]:
        """List all locations.

        Returns:
            A list of locations
        """
        return cast(List[Dict[str, Any]], self.client.get(f"{self.base_path}/locations"))

    def get_available_slots(self, location_id: str) -> List[Dict[str, Any]]:
        """Get available slots for a location.

        Args:
            location_id: The location ID

        Returns:
            A list of available slots
        """
        return cast(
            List[Dict[str, Any]],
            self.client.get(f"{self.base_path}/locations/{location_id}/slots"),
        )

    def list(self) -> List[Dict[str, Any]]:
        """List all bookings.

        Returns:
            A list of bookings
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: BookingCreate) -> Dict[str, Any]:
        """Create a new booking.

        Args:
            data: Booking data

        Returns:
            The created booking
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, booking_id: str) -> Dict[str, Any]:
        """Get a specific booking.

        Args:
            booking_id: The booking ID

        Returns:
            The booking details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{booking_id}"))

    def update(self, booking_id: str, data: BookingUpdate) -> Dict[str, Any]:
        """Update a booking.

        Args:
            booking_id: The booking ID
            data: Updated booking data

        Returns:
            The updated booking
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{booking_id}", data=data))

    def cancel(self, booking_id: str) -> Dict[str, Any]:
        """Cancel a booking.

        Args:
            booking_id: The booking ID

        Returns:
            The cancellation response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{booking_id}"))
