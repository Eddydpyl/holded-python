"""
Async resource for interacting with the Daily Ledger API.
"""

from typing import Any, Dict, List, Optional, Union, cast

from ...base_resources import AsyncBaseResource
from ..models.daily_ledger import DailyLedgerListParams, EntryCreate, EntryResponse


class AsyncDailyLedgerResource(AsyncBaseResource):
    """Async resource for interacting with the Daily Ledger API."""

    def __init__(self, client):
        """Initialize the async daily ledger resource.

        Args:
            client: The AsyncHolded client instance.
        """
        self.client = client
        self.base_path = "accounting/dailyledger"

    async def list(
        self, params: Optional[Union[Dict[str, Any], DailyLedgerListParams]] = None
    ) -> List[Dict[str, Any]]:
        """List all daily ledger entries.
        https://developers.holded.com/reference/listdailyledger
        """
        result = await self.client.get(self.base_path, params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, entry_data: EntryCreate) -> EntryResponse:
        """Create a new daily ledger entry.
        https://developers.holded.com/reference/createentry
        """
        result = await self.client.post("accounting/entry", data=entry_data)
        return cast(EntryResponse, result)

