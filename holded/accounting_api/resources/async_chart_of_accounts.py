"""
Async resource for interacting with the Chart of Accounts API.
"""

from typing import Any, Dict, List, cast

from ...base_resources import AsyncBaseResource


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

