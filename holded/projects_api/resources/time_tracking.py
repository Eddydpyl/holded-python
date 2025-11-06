"""
Resource for interacting with the Time Tracking API.
"""
from typing import Any, Dict, List, cast

from ..models.time_tracking import TimeTrackingCreate, TimeTrackingUpdate
from ...base_resources import BaseResource


class TimeTrackingResource(BaseResource):
    """Resource for interacting with the Time Tracking API."""

    def __init__(self, client):
        """Initialize the time tracking resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "projects/projects"

    def list_all(self) -> List[Dict[str, Any]]:
        """List all time tracking entries across all projects.

        Returns:
            A list of time tracking entries
        """
        return cast(List[Dict[str, Any]], self.client.get(f"{self.base_path}/times"))

    def list(self, project_id: str) -> List[Dict[str, Any]]:
        """List all time tracking entries for a project.

        Args:
            project_id: The project ID

        Returns:
            A list of time tracking entries
        """
        return cast(List[Dict[str, Any]], self.client.get(f"{self.base_path}/{project_id}/times"))

    def create(self, project_id: str, data: TimeTrackingCreate) -> Dict[str, Any]:
        """Create a new time tracking entry.

        Args:
            project_id: The project ID
            data: Time tracking data

        Returns:
            The created time tracking entry
        """
        return cast(Dict[str, Any], self.client.post(f"{self.base_path}/{project_id}/times", data=data))

    def get(self, project_id: str, time_tracking_id: str) -> Dict[str, Any]:
        """Get a specific time tracking entry.

        Args:
            project_id: The project ID
            time_tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{project_id}/times/{time_tracking_id}"))

    def update(self, project_id: str, time_tracking_id: str, data: TimeTrackingUpdate) -> Dict[str, Any]:
        """Update a time tracking entry.

        Args:
            project_id: The project ID
            time_tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking entry
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{project_id}/times/{time_tracking_id}", data=data))

    def delete(self, project_id: str, time_tracking_id: str) -> Dict[str, Any]:
        """Delete a time tracking entry.

        Args:
            project_id: The project ID
            time_tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{project_id}/times/{time_tracking_id}"))

