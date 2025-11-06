"""
Asynchronous resource for interacting with the Time Tracking API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource
from ..models.time_tracking import TimeTrackingCreate, TimeTrackingUpdate


class AsyncTimeTrackingResource(AsyncBaseResource):
    """Resource for interacting with the Time Tracking API asynchronously."""

    def __init__(self, client):
        """Initialize the time tracking resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "projects/projects"

    async def list_all(self) -> List[Dict[str, Any]]:
        """List all time tracking entries across all projects asynchronously.

        Returns:
            A list of time tracking entries
        """
        result = await self.client.get(f"{self.base_path}/times")
        return cast(List[Dict[str, Any]], result)

    async def list(self, project_id: str) -> List[Dict[str, Any]]:
        """List all time tracking entries for a project asynchronously.

        Args:
            project_id: The project ID

        Returns:
            A list of time tracking entries
        """
        result = await self.client.get(f"{self.base_path}/{project_id}/times")
        return cast(List[Dict[str, Any]], result)

    async def create(self, project_id: str, data: TimeTrackingCreate) -> Dict[str, Any]:
        """Create a new time tracking entry asynchronously.

        Args:
            project_id: The project ID
            data: Time tracking data

        Returns:
            The created time tracking entry
        """
        result = await self.client.post(f"{self.base_path}/{project_id}/times", data=data)
        return cast(Dict[str, Any], result)

    async def get(self, project_id: str, time_tracking_id: str) -> Dict[str, Any]:
        """Get a specific time tracking entry asynchronously.

        Args:
            project_id: The project ID
            time_tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        result = await self.client.get(f"{self.base_path}/{project_id}/times/{time_tracking_id}")
        return cast(Dict[str, Any], result)

    async def update(self, project_id: str, time_tracking_id: str, data: TimeTrackingUpdate) -> Dict[str, Any]:
        """Update a time tracking entry asynchronously.

        Args:
            project_id: The project ID
            time_tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking entry
        """
        result = await self.client.put(f"{self.base_path}/{project_id}/times/{time_tracking_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, project_id: str, time_tracking_id: str) -> Dict[str, Any]:
        """Delete a time tracking entry asynchronously.

        Args:
            project_id: The project ID
            time_tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{project_id}/times/{time_tracking_id}")
        return cast(Dict[str, Any], result)
