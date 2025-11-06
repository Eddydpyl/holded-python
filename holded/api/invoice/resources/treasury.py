"""
Treasury resource for the Holded API.
"""

from typing import Any, Dict, List, Optional, Union

from ...resources import BaseResource
from ..models.treasury import (
    TreasuryAccount,
    TreasuryAccountCreate,
    TreasuryAccountListResponse,
    TreasuryAccountResponse,
)


class TreasuryResource(BaseResource):
    """
    Resource for interacting with the Treasury API.
    """

    def __init__(self, client):
        """Initialize the treasury resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/treasury"

    def list(
        self, params: Optional[Union[Dict[str, Any]]] = None
    ) -> Union[List[TreasuryAccount], TreasuryAccountListResponse, List[Dict[str, Any]]]:
        """
        List all treasury accounts.

        Args:
            params: Optional query parameters (for pagination, etc.).

        Returns:
            A list of treasury accounts.
        """
        result = self.client.get(self.base_path, params=params)
        return result

    def create(
        self, data: Union[Dict[str, Any], TreasuryAccountCreate]
    ) -> Union[TreasuryAccount, TreasuryAccountResponse, Dict[str, Any]]:
        """
        Create a new treasury account.

        Args:
            data: Treasury account data.

        Returns:
            The created treasury account.
        """
        result = self.client.post(self.base_path, data=data)
        return result

    def get(self, account_id: str) -> Union[TreasuryAccount, TreasuryAccountResponse, Dict[str, Any]]:
        """
        Get a specific treasury account.

        Args:
            account_id: The treasury account ID.

        Returns:
            The treasury account.
        """
        result = self.client.get(f"{self.base_path}/{account_id}")
        return result
