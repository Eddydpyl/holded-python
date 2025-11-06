"""
Resource for interacting with the Remittances API.
"""
from typing import Any, Dict, List, cast

from ...base_resources import BaseResource


class RemittancesResource(BaseResource):
    """Resource for interacting with the Remittances API."""

    def __init__(self, client):
        """Initialize the remittances resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/remittances"

    def list(self) -> List[Dict[str, Any]]:
        """List all remittances.

        Returns:
            A list of remittances
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def get(self, remittance_id: str) -> Dict[str, Any]:
        """Get a specific remittance.

        Args:
            remittance_id: The remittance ID

        Returns:
            The remittance details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{remittance_id}")) 