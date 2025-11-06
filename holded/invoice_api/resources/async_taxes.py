"""
Asynchronous resource for interacting with the Taxes API.
"""
from typing import Any, Dict, Optional

from ..models.taxes import TaxResponse


class AsyncTaxesResource:
    """Resource for interacting with the Taxes API asynchronously."""

    def __init__(self, client):
        """Initialize the taxes resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/taxes"

    async def list(self) -> TaxResponse:
        """Get all taxes information for the account asynchronously.

        Returns:
            Taxes information
        """
        return await self.client.get(self.base_path)

