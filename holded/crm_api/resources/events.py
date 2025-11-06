"""
Resource for interacting with the Events API.
"""
from typing import Any, Dict, List, cast

from ..models.events import EventCreate, EventUpdate
from ...base_resources import BaseResource


class EventsResource(BaseResource):
    """Resource for interacting with the Events API."""

    def __init__(self, client):
        """Initialize the events resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "crm/events"

    def list(self) -> List[Dict[str, Any]]:
        """List all events.

        Returns:
            A list of events
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: EventCreate) -> Dict[str, Any]:
        """Create a new event.

        Args:
            data: Event data

        Returns:
            The created event
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, event_id: str) -> Dict[str, Any]:
        """Get a specific event.

        Args:
            event_id: The event ID

        Returns:
            The event details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{event_id}"))

    def update(self, event_id: str, data: EventUpdate) -> Dict[str, Any]:
        """Update an event.

        Args:
            event_id: The event ID
            data: Updated event data

        Returns:
            The updated event
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{event_id}", data=data))

    def delete(self, event_id: str) -> Dict[str, Any]:
        """Delete an event.

        Args:
            event_id: The event ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{event_id}"))

