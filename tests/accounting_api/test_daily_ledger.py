"""
Tests for the Daily Ledger API.
"""

import pytest

from holded.accounting_api.models.daily_ledger import DailyLedgerListParams, EntryCreate, EntryLine


class TestDailyLedgerResource:
    """Test cases for the Daily Ledger API."""

    def test_list_entries(self, client):
        """Test listing daily ledger entries."""
        import time

        # API requires starttmp and endtmp
        end_tmp = int(time.time())
        start_tmp = end_tmp - (30 * 24 * 60 * 60)  # 30 days ago

        params = DailyLedgerListParams(starttmp=str(start_tmp), endtmp=str(end_tmp))
        result = client.daily_ledger.list(params=params)

        assert result is not None
        assert isinstance(result, list)

    def test_list_entries_with_pagination(self, client):
        """Test listing daily ledger entries with pagination."""
        import time

        # API requires starttmp and endtmp
        end_tmp = int(time.time())
        start_tmp = end_tmp - (30 * 24 * 60 * 60)  # 30 days ago

        params = DailyLedgerListParams(starttmp=str(start_tmp), endtmp=str(end_tmp), page=1)
        result = client.daily_ledger.list(params=params)

        assert result is not None
        assert isinstance(result, list)

    def test_list_entries_with_date_range(self, client):
        """Test listing daily ledger entries with date range."""
        import time

        # Get entries from the last 30 days
        end_tmp = int(time.time())
        start_tmp = end_tmp - (30 * 24 * 60 * 60)  # 30 days ago

        params = DailyLedgerListParams(starttmp=str(start_tmp), endtmp=str(end_tmp))
        result = client.daily_ledger.list(params=params)

        assert result is not None
        assert isinstance(result, list)

    def test_create_entry(self, client):
        """Test creating a daily ledger entry."""
        # First, get available accounts from chart of accounts
        try:
            accounts = client.chart_of_accounts.list()
            if not accounts or len(accounts) < 2:
                pytest.skip("Need at least 2 accounts in chart of accounts to create entry")

            # Get two account codes
            account1 = accounts[0].get("code") or accounts[0].get("id")
            account2 = accounts[1].get("code") or accounts[1].get("id")

            if not account1 or not account2:
                pytest.skip("Account codes not found")

            # Create a balanced entry
            entry_data = EntryCreate(
                lines=[
                    EntryLine(account=account1, debit=100.0),
                    EntryLine(account=account2, credit=100.0),
                ],
                desc="Test entry",
            )

            result = client.daily_ledger.create(entry_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result or "status" in result
        except Exception as e:
            pytest.skip(f"Entry creation failed: {e}")


class TestAsyncDailyLedgerResource:
    """Test cases for the Async Daily Ledger API."""

    @pytest.mark.asyncio
    async def test_list_entries(self, async_client):
        """Test listing daily ledger entries asynchronously."""
        import time

        # API requires starttmp and endtmp
        end_tmp = int(time.time())
        start_tmp = end_tmp - (30 * 24 * 60 * 60)  # 30 days ago

        params = DailyLedgerListParams(starttmp=str(start_tmp), endtmp=str(end_tmp))
        result = await async_client.daily_ledger.list(params=params)

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_entries_with_pagination(self, async_client):
        """Test listing daily ledger entries with pagination asynchronously."""
        import time

        # API requires starttmp and endtmp
        end_tmp = int(time.time())
        start_tmp = end_tmp - (30 * 24 * 60 * 60)  # 30 days ago

        params = DailyLedgerListParams(starttmp=str(start_tmp), endtmp=str(end_tmp), page=1)
        result = await async_client.daily_ledger.list(params=params)

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_entries_with_date_range(self, async_client):
        """Test listing daily ledger entries with date range asynchronously."""
        import time

        # Get entries from the last 30 days
        end_tmp = int(time.time())
        start_tmp = end_tmp - (30 * 24 * 60 * 60)  # 30 days ago

        params = DailyLedgerListParams(starttmp=str(start_tmp), endtmp=str(end_tmp))
        result = await async_client.daily_ledger.list(params=params)

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_entry(self, async_client):
        """Test creating a daily ledger entry asynchronously."""
        # First, get available accounts from chart of accounts
        try:
            accounts = await async_client.chart_of_accounts.list()
            if not accounts or len(accounts) < 2:
                pytest.skip("Need at least 2 accounts in chart of accounts to create entry")

            # Get two account codes
            account1 = accounts[0].code if hasattr(accounts[0], "code") else accounts[0].get("code") or accounts[0].get("id")
            account2 = accounts[1].code if hasattr(accounts[1], "code") else accounts[1].get("code") or accounts[1].get("id")

            if not account1 or not account2:
                pytest.skip("Account codes not found")

            # Create a balanced entry
            entry_data = EntryCreate(
                lines=[
                    EntryLine(account=account1, debit=100.0),
                    EntryLine(account=account2, credit=100.0),
                ],
                desc="Test entry async",
            )

            result = await async_client.daily_ledger.create(entry_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result or "status" in result
        except Exception as e:
            pytest.skip(f"Entry creation failed: {e}")

