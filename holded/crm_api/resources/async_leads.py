"""
Asynchronous resource for interacting with the Leads API.
"""
from typing import Any, Dict, List, cast

from ..models.leads import (
    LeadCreate,
    LeadUpdate,
    LeadNoteCreate,
    LeadNoteUpdate,
    LeadTaskCreate,
    LeadTaskUpdate,
    LeadDateUpdate,
    LeadStageUpdate,
)
from ...base_resources import AsyncBaseResource


class AsyncLeadsResource(AsyncBaseResource):
    """Resource for interacting with the Leads API asynchronously."""

    def __init__(self, client):
        """Initialize the leads resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "crm/leads"

    async def list(self) -> List[Dict[str, Any]]:
        """List all leads asynchronously.

        Returns:
            A list of leads
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: LeadCreate) -> Dict[str, Any]:
        """Create a new lead asynchronously.

        Args:
            data: Lead data

        Returns:
            The created lead
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, lead_id: str) -> Dict[str, Any]:
        """Get a specific lead asynchronously.

        Args:
            lead_id: The lead ID

        Returns:
            The lead details
        """
        result = await self.client.get(f"{self.base_path}/{lead_id}")
        return cast(Dict[str, Any], result)

    async def update(self, lead_id: str, data: LeadUpdate) -> Dict[str, Any]:
        """Update a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Updated lead data

        Returns:
            The updated lead
        """
        result = await self.client.put(f"{self.base_path}/{lead_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, lead_id: str) -> Dict[str, Any]:
        """Delete a lead asynchronously.

        Args:
            lead_id: The lead ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{lead_id}")
        return cast(Dict[str, Any], result)

    async def create_note(self, lead_id: str, data: LeadNoteCreate) -> Dict[str, Any]:
        """Create a note for a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Note data

        Returns:
            The created note
        """
        result = await self.client.post(f"{self.base_path}/{lead_id}/notes", data=data)
        return cast(Dict[str, Any], result)

    async def update_note(self, lead_id: str, data: LeadNoteUpdate) -> Dict[str, Any]:
        """Update a note for a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Updated note data

        Returns:
            The updated note
        """
        result = await self.client.put(f"{self.base_path}/{lead_id}/notes", data=data)
        return cast(Dict[str, Any], result)

    async def create_task(self, lead_id: str, data: LeadTaskCreate) -> Dict[str, Any]:
        """Create a task for a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Task data

        Returns:
            The created task
        """
        result = await self.client.post(f"{self.base_path}/{lead_id}/tasks", data=data)
        return cast(Dict[str, Any], result)

    async def update_task(self, lead_id: str, data: LeadTaskUpdate) -> Dict[str, Any]:
        """Update a task for a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Updated task data

        Returns:
            The updated task
        """
        result = await self.client.put(f"{self.base_path}/{lead_id}/tasks", data=data)
        return cast(Dict[str, Any], result)

    async def delete_task(self, lead_id: str) -> Dict[str, Any]:
        """Delete a task for a lead asynchronously.

        Args:
            lead_id: The lead ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{lead_id}/tasks")
        return cast(Dict[str, Any], result)

    async def update_date(self, lead_id: str, data: LeadDateUpdate) -> Dict[str, Any]:
        """Update the creation date of a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Date data

        Returns:
            The update response
        """
        result = await self.client.put(f"{self.base_path}/{lead_id}/dates", data=data)
        return cast(Dict[str, Any], result)

    async def update_stage(self, lead_id: str, data: LeadStageUpdate) -> Dict[str, Any]:
        """Update the stage of a lead asynchronously.

        Args:
            lead_id: The lead ID
            data: Stage data

        Returns:
            The update response
        """
        result = await self.client.put(f"{self.base_path}/{lead_id}/stages", data=data)
        return cast(Dict[str, Any], result)

