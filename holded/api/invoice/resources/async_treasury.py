"""
Asynchronous treasury resource for the Holded API.
"""

from typing import Any, Dict, List, Optional, Union

from ...resources import AsyncBaseResource
from ..models.treasury import (
    TreasuryAccount,
    TreasuryAccountCreate,
    TreasuryAccountListResponse,
    TreasuryAccountResponse,
)


class AsyncTreasuryResource(AsyncBaseResource):
    """
    Resource for interacting with the Treasury API asynchronously.
    """

    def __init__(self, client):
        """Initialize the treasury resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/treasury"

    async def list(
        self, params: Optional[Union[Dict[str, Any]]] = None
    ) -> Union[List[TreasuryAccount], TreasuryAccountListResponse, List[Dict[str, Any]]]:
        """
        List all treasury accounts asynchronously.

        Args:
            params: Optional query parameters (for pagination, etc.).

        Returns:
            A list of treasury accounts.
        """
        result = await self.client.get(self.base_path, params=params)
        return result

    async def create(
        self, data: Union[Dict[str, Any], TreasuryAccountCreate]
    ) -> Union[TreasuryAccount, TreasuryAccountResponse, Dict[str, Any]]:
        """
        Create a new treasury account asynchronously.

        Args:
            data: Treasury account data.

        Returns:
            The created treasury account.
        """
        result = await self.client.post(self.base_path, data=data)
        return result

    async def get(self, account_id: str) -> Union[TreasuryAccount, TreasuryAccountResponse, Dict[str, Any]]:
        """
        Get a specific treasury account asynchronously.

        Args:
            account_id: The treasury account ID.

        Returns:
            The treasury account.
        """
        result = await self.client.get(f"{self.base_path}/{account_id}")
        return result
