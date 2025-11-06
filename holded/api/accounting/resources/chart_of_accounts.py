"""
Resource for interacting with the Chart of Accounts API.
"""

from typing import Any, Dict, List, Union, cast

from ...resources import BaseResource
from ..models.chart_of_accounts import AccountCreate


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

    def create(self, data: Union[Dict[str, Any], AccountCreate]) -> Dict[str, Any]:
        """Create a new accounting account.
        https://developers.holded.com/reference/createaccount

        Args:
            data: Account data with prefix (4 digits integer) and optional name.

        Returns:
            The created account
        """
        return cast(Dict[str, Any], self.client.post("accounting/v1/account", data=data))
