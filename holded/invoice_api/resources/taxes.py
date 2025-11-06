"""
Resource for interacting with the Taxes API.
"""
from typing import Any, Dict, Optional

from ..models.taxes import TaxResponse


class TaxesResource:
    """Resource for interacting with the Taxes API."""

    def __init__(self, client):
        """Initialize the taxes resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/taxes"

    def list(self) -> TaxResponse:
        """Get all taxes information for the account.

        Returns:
            Taxes information
        """
        return self.client.get(self.base_path)

