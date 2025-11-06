"""
Asynchronous resource for interacting with the Events API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource
from ..models.events import EventCreate, EventUpdate


class AsyncEventsResource(AsyncBaseResource):
    """Resource for interacting with the Events API asynchronously."""

    def __init__(self, client):
        """Initialize the events resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "crm/events"

    async def list(self) -> List[Dict[str, Any]]:
        """List all events asynchronously.

        Returns:
            A list of events
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: EventCreate) -> Dict[str, Any]:
        """Create a new event asynchronously.

        Args:
            data: Event data

        Returns:
            The created event
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, event_id: str) -> Dict[str, Any]:
        """Get a specific event asynchronously.

        Args:
            event_id: The event ID

        Returns:
            The event details
        """
        result = await self.client.get(f"{self.base_path}/{event_id}")
        return cast(Dict[str, Any], result)

    async def update(self, event_id: str, data: EventUpdate) -> Dict[str, Any]:
        """Update an event asynchronously.

        Args:
            event_id: The event ID
            data: Updated event data

        Returns:
            The updated event
        """
        result = await self.client.put(f"{self.base_path}/{event_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, event_id: str) -> Dict[str, Any]:
        """Delete an event asynchronously.

        Args:
            event_id: The event ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{event_id}")
        return cast(Dict[str, Any], result)
