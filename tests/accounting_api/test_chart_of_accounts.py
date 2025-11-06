"""
Tests for the Chart of Accounts API.
"""

import pytest


class TestChartOfAccountsResource:
    """Test cases for the Chart of Accounts API."""

    def test_list_accounts(self, client):
        """Test listing accounting accounts."""
        result = client.chart_of_accounts.list()

        assert result is not None
        assert isinstance(result, list)

        # If there are accounts, verify structure
        if result:
            account = result[0]
            assert isinstance(account, dict)
            # Accounts should have at least code or name
            assert "code" in account or "name" in account or "id" in account


class TestAsyncChartOfAccountsResource:
    """Test cases for the Async Chart of Accounts API."""

    @pytest.mark.asyncio
    async def test_list_accounts(self, async_client):
        """Test listing accounting accounts asynchronously."""
        result = await async_client.chart_of_accounts.list()

        assert result is not None
        assert isinstance(result, list)

        # If there are accounts, verify structure
        if result:
            account = result[0]
            assert isinstance(account, dict)
            # Accounts should have at least code or name
            assert "code" in account or "name" in account or "id" in account
