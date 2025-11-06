"""
Resource for interacting with the Daily Ledger API.
"""

from typing import Any, Dict, List, Optional, Union, cast

from ...resources import BaseResource
from ..models.daily_ledger import DailyLedgerListParams, EntryCreate


class DailyLedgerResource(BaseResource):
    """Resource for interacting with the Daily Ledger API."""

    def __init__(self, client):
        """Initialize the daily ledger resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "accounting/dailyledger"

    def list(self, params: Optional[Union[Dict[str, Any], DailyLedgerListParams]] = None) -> List[Dict[str, Any]]:
        """List all daily ledger entries.

        Args:
            params: Optional query parameters (page, starttmp, endtmp)

        Returns:
            A list of entries
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path, params=params))

    def create(self, data: Union[Dict[str, Any], EntryCreate]) -> Dict[str, Any]:
        """Create a new daily ledger entry.

        Args:
            data: Entry data with at least 2 lines

        Returns:
            The created entry
        """
        return cast(Dict[str, Any], self.client.post("accounting/entry", data=data))
