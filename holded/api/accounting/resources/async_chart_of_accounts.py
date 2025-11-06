"""
Async resource for interacting with the Chart of Accounts API.
"""

from typing import Any, Dict, List, Union, cast

from ...resources import AsyncBaseResource
from ..models.chart_of_accounts import AccountCreate


class AsyncChartOfAccountsResource(AsyncBaseResource):
    """Async resource for interacting with the Chart of Accounts API."""

    def __init__(self, client):
        """Initialize the async chart of accounts resource.

        Args:
            client: The AsyncHolded client instance.
        """
        self.client = client
        self.base_path = "accounting/chartofaccounts"

    async def list(self) -> List[Dict[str, Any]]:
        """List all accounting accounts.
        https://developers.holded.com/reference/listaccounts
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Union[Dict[str, Any], AccountCreate]) -> Dict[str, Any]:
        """Create a new accounting account.
        https://developers.holded.com/reference/createaccount

        Args:
            data: Account data with prefix (4 digits integer) and optional name.

        Returns:
            The created account
        """
        result = await self.client.post("accounting/v1/account", data=data)
        return cast(Dict[str, Any], result)
