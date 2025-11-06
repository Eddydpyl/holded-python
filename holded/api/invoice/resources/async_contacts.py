"""
Asynchronous contacts resource for the Holded API.
"""

from typing import Any, Dict, List, Optional, Union

from ...resources import AsyncBaseResource
from ..models.contacts import (
    ContactAttachmentListResponse,
    ContactAttachmentResponse,
    ContactCreate,
    ContactListParams,
    ContactListResponse,
    ContactResponse,
    ContactUpdate,
)


class AsyncContactsResource(AsyncBaseResource):
    """Resource for interacting with the Contacts API asynchronously."""

    def __init__(self, client):
        """Initialize the contacts resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/contacts"

    async def list(
        self, params: Optional[Union[Dict[str, Any], ContactListParams]] = None
    ) -> Union[List[Dict[str, Any]], ContactListResponse]:
        """List all contacts asynchronously.

        Args:
            params: Optional query parameters.
                - page: Page number.
                - limit: Number of results per page.
                - phone: Filter by phone number (exact match).
                - mobile: Filter by mobile number (exact match).
                - customId: Filter by custom ID array.

        Returns:
            A list of contacts.
        """
        return await self.client.get(self.base_path, params=params)

    async def create(self, data: Union[Dict[str, Any], ContactCreate]) -> Union[Dict[str, Any], ContactResponse]:
        """Create a new contact asynchronously.

        Args:
            data: Contact data.

        Returns:
            The created contact.
        """
        return await self.client.post(self.base_path, data=data)

    async def get(self, contact_id: str) -> Union[Dict[str, Any], ContactResponse]:
        """Get a specific contact asynchronously.

        Args:
            contact_id: The contact ID.

        Returns:
            The contact.
        """
        return await self.client.get(f"{self.base_path}/{contact_id}")

    async def update(
        self, contact_id: str, data: Union[Dict[str, Any], ContactUpdate]
    ) -> Union[Dict[str, Any], ContactResponse]:
        """Update a contact asynchronously.

        Args:
            contact_id: The contact ID.
            data: Updated contact data.

        Returns:
            The updated contact.
        """
        return await self.client.put(f"{self.base_path}/{contact_id}", data=data)

    async def delete(self, contact_id: str) -> Dict[str, Any]:
        """Delete a contact asynchronously.

        Args:
            contact_id: The contact ID.

        Returns:
            A confirmation message.
        """
        return await self.client.delete(f"{self.base_path}/{contact_id}")

    async def get_attachments(self, contact_id: str) -> Union[List[Dict[str, Any]], ContactAttachmentListResponse]:
        """Get attachments for a contact asynchronously.

        Args:
            contact_id: The contact ID.

        Returns:
            A list of attachments.
        """
        return await self.client.get(f"{self.base_path}/{contact_id}/attachments")

    async def get_attachment(
        self, contact_id: str, attachment_id: str
    ) -> Union[Dict[str, Any], ContactAttachmentResponse]:
        """Get a specific attachment for a contact asynchronously.

        Args:
            contact_id: The contact ID.
            attachment_id: The attachment ID.

        Returns:
            The attachment.
        """
        return await self.client.get(f"{self.base_path}/{contact_id}/attachments/{attachment_id}")
