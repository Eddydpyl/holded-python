"""
Asynchronous resource for interacting with the Funnels API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource
from ..models.funnels import FunnelCreate, FunnelUpdate


class AsyncFunnelsResource(AsyncBaseResource):
    """Resource for interacting with the Funnels API asynchronously."""

    def __init__(self, client):
        """Initialize the funnels resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "crm/funnels"

    async def list(self) -> List[Dict[str, Any]]:
        """List all funnels asynchronously.

        Returns:
            A list of funnels
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: FunnelCreate) -> Dict[str, Any]:
        """Create a new funnel asynchronously.

        Args:
            data: Funnel data

        Returns:
            The created funnel
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, funnel_id: str) -> Dict[str, Any]:
        """Get a specific funnel asynchronously.

        Args:
            funnel_id: The funnel ID

        Returns:
            The funnel details
        """
        result = await self.client.get(f"{self.base_path}/{funnel_id}")
        return cast(Dict[str, Any], result)

    async def update(self, funnel_id: str, data: FunnelUpdate) -> Dict[str, Any]:
        """Update a funnel asynchronously.

        Args:
            funnel_id: The funnel ID
            data: Updated funnel data

        Returns:
            The updated funnel
        """
        result = await self.client.put(f"{self.base_path}/{funnel_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, funnel_id: str) -> Dict[str, Any]:
        """Delete a funnel asynchronously.

        Args:
            funnel_id: The funnel ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{funnel_id}")
        return cast(Dict[str, Any], result)
