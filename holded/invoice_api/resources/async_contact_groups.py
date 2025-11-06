"""
Asynchronous resource for interacting with the Contact Groups API.
"""
from typing import Any, Dict, List, Optional, cast

from ..models.contact_groups import (
    ContactGroupCreate,
    ContactGroupUpdate,
    ContactGroupResponse,
    ContactGroupListResponse,
)
from ...base_resources import AsyncBaseResource


class AsyncContactGroupsResource(AsyncBaseResource):
    """Resource for interacting with the Contact Groups API asynchronously."""

    def __init__(self, client):
        """Initialize the contact groups resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/contacts/groups"

    async def list(self) -> List[Dict[str, Any]]:
        """List all contact groups asynchronously.

        Returns:
            A list of contact groups
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: ContactGroupCreate) -> Dict[str, Any]:
        """Create a new contact group asynchronously.

        Args:
            data: Contact group data

        Returns:
            The created contact group
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, group_id: str) -> Dict[str, Any]:
        """Get a specific contact group asynchronously.

        Args:
            group_id: The contact group ID

        Returns:
            The contact group details
        """
        result = await self.client.get(f"{self.base_path}/{group_id}")
        return cast(Dict[str, Any], result)

    async def update(self, group_id: str, data: ContactGroupUpdate) -> Dict[str, Any]:
        """Update a contact group asynchronously.

        Args:
            group_id: The contact group ID
            data: Updated contact group data

        Returns:
            The updated contact group
        """
        result = await self.client.put(f"{self.base_path}/{group_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, group_id: str) -> Dict[str, Any]:
        """Delete a contact group asynchronously.

        Args:
            group_id: The contact group ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{group_id}")
        return cast(Dict[str, Any], result)

