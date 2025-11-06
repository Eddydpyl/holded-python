"""
Resource for interacting with the Contact Groups API.
"""
from typing import Any, Dict, List, Optional, cast

from ..models.contact_groups import (
    ContactGroupCreate,
    ContactGroupUpdate,
    ContactGroupResponse,
    ContactGroupListResponse,
)
from ...base_resources import BaseResource


class ContactGroupsResource(BaseResource):
    """Resource for interacting with the Contact Groups API."""

    def __init__(self, client):
        """Initialize the contact groups resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/contacts/groups"

    def list(self) -> List[Dict[str, Any]]:
        """List all contact groups.

        Returns:
            A list of contact groups
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: ContactGroupCreate) -> Dict[str, Any]:
        """Create a new contact group.

        Args:
            data: Contact group data

        Returns:
            The created contact group
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, group_id: str) -> Dict[str, Any]:
        """Get a specific contact group.

        Args:
            group_id: The contact group ID

        Returns:
            The contact group details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{group_id}"))

    def update(self, group_id: str, data: ContactGroupUpdate) -> Dict[str, Any]:
        """Update a contact group.

        Args:
            group_id: The contact group ID
            data: Updated contact group data

        Returns:
            The updated contact group
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{group_id}", data=data))

    def delete(self, group_id: str) -> Dict[str, Any]:
        """Delete a contact group.

        Args:
            group_id: The contact group ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{group_id}"))

