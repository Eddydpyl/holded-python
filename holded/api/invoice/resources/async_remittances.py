"""
Asynchronous resource for interacting with the Remittances API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource


class AsyncRemittancesResource(AsyncBaseResource):
    """Resource for interacting with the Remittances API asynchronously."""

    def __init__(self, client):
        """Initialize the remittances resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/remittances"

    async def list(self) -> List[Dict[str, Any]]:
        """List all remittances asynchronously.

        Returns:
            A list of remittances
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def get(self, remittance_id: str) -> Dict[str, Any]:
        """Get a specific remittance asynchronously.

        Args:
            remittance_id: The remittance ID

        Returns:
            The remittance details
        """
        result = await self.client.get(f"{self.base_path}/{remittance_id}")
        return cast(Dict[str, Any], result)
