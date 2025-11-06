"""
Asynchronous resource for interacting with the Bookings API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource
from ..models.bookings import BookingCreate, BookingUpdate


class AsyncBookingsResource(AsyncBaseResource):
    """Resource for interacting with the Bookings API asynchronously."""

    def __init__(self, client):
        """Initialize the bookings resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "crm/bookings"

    async def list_locations(self) -> List[Dict[str, Any]]:
        """List all locations asynchronously.

        Returns:
            A list of locations
        """
        result = await self.client.get(f"{self.base_path}/locations")
        return cast(List[Dict[str, Any]], result)

    async def get_available_slots(self, location_id: str) -> List[Dict[str, Any]]:
        """Get available slots for a location asynchronously.

        Args:
            location_id: The location ID

        Returns:
            A list of available slots
        """
        result = await self.client.get(f"{self.base_path}/locations/{location_id}/slots")
        return cast(List[Dict[str, Any]], result)

    async def list(self) -> List[Dict[str, Any]]:
        """List all bookings asynchronously.

        Returns:
            A list of bookings
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: BookingCreate) -> Dict[str, Any]:
        """Create a new booking asynchronously.

        Args:
            data: Booking data

        Returns:
            The created booking
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, booking_id: str) -> Dict[str, Any]:
        """Get a specific booking asynchronously.

        Args:
            booking_id: The booking ID

        Returns:
            The booking details
        """
        result = await self.client.get(f"{self.base_path}/{booking_id}")
        return cast(Dict[str, Any], result)

    async def update(self, booking_id: str, data: BookingUpdate) -> Dict[str, Any]:
        """Update a booking asynchronously.

        Args:
            booking_id: The booking ID
            data: Updated booking data

        Returns:
            The updated booking
        """
        result = await self.client.put(f"{self.base_path}/{booking_id}", data=data)
        return cast(Dict[str, Any], result)

    async def cancel(self, booking_id: str) -> Dict[str, Any]:
        """Cancel a booking asynchronously.

        Args:
            booking_id: The booking ID

        Returns:
            The cancellation response
        """
        result = await self.client.delete(f"{self.base_path}/{booking_id}")
        return cast(Dict[str, Any], result)
