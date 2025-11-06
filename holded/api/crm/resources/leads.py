"""
Resource for interacting with the Leads API.
"""

from typing import Any, Dict, List, cast

from ...resources import BaseResource
from ..models.leads import (
    LeadCreate,
    LeadDateUpdate,
    LeadNoteCreate,
    LeadNoteUpdate,
    LeadStageUpdate,
    LeadTaskCreate,
    LeadTaskUpdate,
    LeadUpdate,
)


class LeadsResource(BaseResource):
    """Resource for interacting with the Leads API."""

    def __init__(self, client):
        """Initialize the leads resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "crm/leads"

    def list(self) -> List[Dict[str, Any]]:
        """List all leads.

        Returns:
            A list of leads
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: LeadCreate) -> Dict[str, Any]:
        """Create a new lead.

        Args:
            data: Lead data

        Returns:
            The created lead
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, lead_id: str) -> Dict[str, Any]:
        """Get a specific lead.

        Args:
            lead_id: The lead ID

        Returns:
            The lead details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{lead_id}"))

    def update(self, lead_id: str, data: LeadUpdate) -> Dict[str, Any]:
        """Update a lead.

        Args:
            lead_id: The lead ID
            data: Updated lead data

        Returns:
            The updated lead
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{lead_id}", data=data))

    def delete(self, lead_id: str) -> Dict[str, Any]:
        """Delete a lead.

        Args:
            lead_id: The lead ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{lead_id}"))

    def create_note(self, lead_id: str, data: LeadNoteCreate) -> Dict[str, Any]:
        """Create a note for a lead.

        Args:
            lead_id: The lead ID
            data: Note data

        Returns:
            The created note
        """
        return cast(
            Dict[str, Any],
            self.client.post(f"{self.base_path}/{lead_id}/notes", data=data),
        )

    def update_note(self, lead_id: str, data: LeadNoteUpdate) -> Dict[str, Any]:
        """Update a note for a lead.

        Args:
            lead_id: The lead ID
            data: Updated note data

        Returns:
            The updated note
        """
        return cast(
            Dict[str, Any],
            self.client.put(f"{self.base_path}/{lead_id}/notes", data=data),
        )

    def create_task(self, lead_id: str, data: LeadTaskCreate) -> Dict[str, Any]:
        """Create a task for a lead.

        Args:
            lead_id: The lead ID
            data: Task data

        Returns:
            The created task
        """
        return cast(
            Dict[str, Any],
            self.client.post(f"{self.base_path}/{lead_id}/tasks", data=data),
        )

    def update_task(self, lead_id: str, data: LeadTaskUpdate) -> Dict[str, Any]:
        """Update a task for a lead.

        Args:
            lead_id: The lead ID
            data: Updated task data

        Returns:
            The updated task
        """
        return cast(
            Dict[str, Any],
            self.client.put(f"{self.base_path}/{lead_id}/tasks", data=data),
        )

    def delete_task(self, lead_id: str) -> Dict[str, Any]:
        """Delete a task for a lead.

        Args:
            lead_id: The lead ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{lead_id}/tasks"))

    def update_date(self, lead_id: str, data: LeadDateUpdate) -> Dict[str, Any]:
        """Update the creation date of a lead.

        Args:
            lead_id: The lead ID
            data: Date data

        Returns:
            The update response
        """
        return cast(
            Dict[str, Any],
            self.client.put(f"{self.base_path}/{lead_id}/dates", data=data),
        )

    def update_stage(self, lead_id: str, data: LeadStageUpdate) -> Dict[str, Any]:
        """Update the stage of a lead.

        Args:
            lead_id: The lead ID
            data: Stage data

        Returns:
            The update response
        """
        return cast(
            Dict[str, Any],
            self.client.put(f"{self.base_path}/{lead_id}/stages", data=data),
        )
