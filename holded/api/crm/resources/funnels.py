"""
Resource for interacting with the Funnels API.
"""

from typing import Any, Dict, List, cast

from ...resources import BaseResource
from ..models.funnels import FunnelCreate, FunnelUpdate


class FunnelsResource(BaseResource):
    """Resource for interacting with the Funnels API."""

    def __init__(self, client):
        """Initialize the funnels resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "crm/funnels"

    def list(self) -> List[Dict[str, Any]]:
        """List all funnels.

        Returns:
            A list of funnels
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: FunnelCreate) -> Dict[str, Any]:
        """Create a new funnel.

        Args:
            data: Funnel data

        Returns:
            The created funnel
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, funnel_id: str) -> Dict[str, Any]:
        """Get a specific funnel.

        Args:
            funnel_id: The funnel ID

        Returns:
            The funnel details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{funnel_id}"))

    def update(self, funnel_id: str, data: FunnelUpdate) -> Dict[str, Any]:
        """Update a funnel.

        Args:
            funnel_id: The funnel ID
            data: Updated funnel data

        Returns:
            The updated funnel
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{funnel_id}", data=data))

    def delete(self, funnel_id: str) -> Dict[str, Any]:
        """Delete a funnel.

        Args:
            funnel_id: The funnel ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{funnel_id}"))
