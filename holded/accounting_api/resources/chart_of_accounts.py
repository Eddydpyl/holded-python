"""
Resource for interacting with the Chart of Accounts API.
"""

from typing import Any, Dict, List, Optional, cast

from ...base_resources import BaseResource


class ChartOfAccountsResource(BaseResource):
    """Resource for interacting with the Chart of Accounts API."""

    def __init__(self, client):
        """Initialize the chart of accounts resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "accounting/chartofaccounts"

    def list(self) -> List[Dict[str, Any]]:
        """List all accounting accounts.

        Returns:
            A list of accounts
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

