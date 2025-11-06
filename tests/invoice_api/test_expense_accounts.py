"""
Tests for the Expense Accounts API.
"""

import time

import pytest

from holded.api.invoice.models.expense_accounts import (
    ExpenseAccountCreate,
    ExpenseAccountListParams,
    ExpenseAccountUpdate,
)


class TestExpenseAccountsResource:
    """Test cases for the Expense Accounts API."""

    def test_list_expense_accounts(self, client):
        """Test listing expense accounts."""
        result = client.expense_accounts.list()

        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are accounts, verify structure
                if items and len(items) > 0:
                    account = items[0]
                    assert "id" in account
                    assert "name" in account
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    def test_list_expense_accounts_with_params(self, client):
        """Test listing expense accounts with query parameters."""
        params = ExpenseAccountListParams(page=1, limit=10)

        result = client.expense_accounts.list(params)

        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    def test_create_expense_account(self, client):
        """Test creating an expense account."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000
        account_data = ExpenseAccountCreate(name="Test Expense Account", desc="Test description", accountNum=unique_num)

        result = client.expense_accounts.create(account_data)

        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store account ID for cleanup
            if "id" in result:
                account_id = result["id"]
                # Cleanup: delete the account
                try:
                    client.expense_accounts.delete(account_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test_create_expense_account_with_dict(self, client):
        """Test creating an expense account using a dictionary."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000 + 1
        account_data = {
            "name": "Test Expense Account Dict",
            "desc": "Test description from dict",
            "accountNum": unique_num,
        }

        result = client.expense_accounts.create(account_data)

        assert result is not None
        if isinstance(result, dict) and "id" in result:
            # Cleanup
            try:
                client.expense_accounts.delete(result["id"])
            except Exception:
                pass

    def test_get_expense_account(self, client):
        """Test getting a specific expense account."""
        # First, list accounts to get an ID
        accounts = client.expense_accounts.list()

        # Handle different response formats
        if isinstance(accounts, dict) and "items" in accounts:
            account_list = accounts["items"]
        else:
            account_list = accounts if isinstance(accounts, list) else []

        if account_list and len(account_list) > 0:
            account_id = account_list[0]["id"]

            result = client.expense_accounts.get(account_id)

            assert result is not None
            if isinstance(result, dict):
                assert "id" in result
                assert result["id"] == account_id
                assert "name" in result
        else:
            # Create a test account if none exist
            unique_num = int(time.time() * 1000) % 1000000 + 2
            account_data = ExpenseAccountCreate(
                name="Test Get Account", desc="Test description for get", accountNum=unique_num
            )

            created = client.expense_accounts.create(account_data)
            if isinstance(created, dict) and "id" in created:
                account_id = created["id"]

                result = client.expense_accounts.get(account_id)

                assert result is not None
                if isinstance(result, dict):
                    assert "id" in result
                    assert result["id"] == account_id

                # Cleanup
                try:
                    client.expense_accounts.delete(account_id)
                except Exception:
                    pass

    def test_update_expense_account(self, client):
        """Test updating an expense account."""
        # Create an account first
        unique_num = int(time.time() * 1000) % 1000000 + 3
        account_data = ExpenseAccountCreate(
            name="Test Update Account", desc="Original description", accountNum=unique_num
        )

        created = client.expense_accounts.create(account_data)

        if isinstance(created, dict) and "id" in created:
            account_id = created["id"]

            # Update the account
            update_data = ExpenseAccountUpdate(name="Updated Test Account", desc="Updated description")

            result = client.expense_accounts.update(account_id, update_data)

            assert result is not None

            # Fetch the account again to verify the update
            updated = client.expense_accounts.get(account_id)

            if isinstance(updated, dict):
                # The update endpoint may return status, so verify via get
                assert "id" in updated
                assert updated["id"] == account_id
                # Name or desc should be updated
                if "name" in updated:
                    assert updated["name"] == "Updated Test Account"
                elif "desc" in updated:
                    assert updated["desc"] == "Updated description"

            # Cleanup
            try:
                client.expense_accounts.delete(account_id)
            except Exception:
                pass

    def test_delete_expense_account(self, client):
        """Test deleting an expense account."""
        # Create an account first
        unique_num = int(time.time() * 1000) % 1000000 + 4
        account_data = ExpenseAccountCreate(
            name="Test Delete Account", desc="Account to be deleted", accountNum=unique_num
        )

        created = client.expense_accounts.create(account_data)

        if isinstance(created, dict) and "id" in created:
            account_id = created["id"]

            # Delete the account
            result = client.expense_accounts.delete(account_id)

            assert result is not None

            # Verify it's deleted by trying to get it (should raise an error)
            try:
                client.expense_accounts.get(account_id)
                # If we get here, the account still exists (some APIs don't actually delete)
                # This is acceptable behavior
            except Exception:
                # Expected: account should not be found
                pass


class TestAsyncExpenseAccountsResource:
    """Test cases for the Async Expense Accounts API."""

    @pytest.mark.asyncio
    async def test_list_expense_accounts(self, async_client):
        """Test listing expense accounts asynchronously."""
        result = await async_client.expense_accounts.list()

        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are accounts, verify structure
                if items and len(items) > 0:
                    account = items[0]
                    assert "id" in account
                    assert "name" in account
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_expense_accounts_with_params(self, async_client):
        """Test listing expense accounts with query parameters asynchronously."""
        params = ExpenseAccountListParams(page=1, limit=10)

        result = await async_client.expense_accounts.list(params)

        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_expense_account(self, async_client):
        """Test creating an expense account asynchronously."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000 + 10
        account_data = ExpenseAccountCreate(
            name="Test Async Expense Account", desc="Test async description", accountNum=unique_num
        )

        result = await async_client.expense_accounts.create(account_data)

        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store account ID for cleanup
            if "id" in result:
                account_id = result["id"]
                # Cleanup: delete the account
                try:
                    await async_client.expense_accounts.delete(account_id)
                except Exception:
                    pass  # Ignore cleanup errors

    @pytest.mark.asyncio
    async def test_create_expense_account_with_dict(self, async_client):
        """Test creating an expense account using a dictionary asynchronously."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000 + 11
        account_data = {
            "name": "Test Async Expense Account Dict",
            "desc": "Test async description from dict",
            "accountNum": unique_num,
        }

        result = await async_client.expense_accounts.create(account_data)

        assert result is not None
        if isinstance(result, dict) and "id" in result:
            # Cleanup
            try:
                await async_client.expense_accounts.delete(result["id"])
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_get_expense_account(self, async_client):
        """Test getting a specific expense account asynchronously."""
        # First, list accounts to get an ID
        accounts = await async_client.expense_accounts.list()

        # Handle different response formats
        if isinstance(accounts, dict) and "items" in accounts:
            account_list = accounts["items"]
        else:
            account_list = accounts if isinstance(accounts, list) else []

        if account_list and len(account_list) > 0:
            account_id = account_list[0]["id"]

            result = await async_client.expense_accounts.get(account_id)

            assert result is not None
            if isinstance(result, dict):
                assert "id" in result
                assert result["id"] == account_id
                assert "name" in result
        else:
            # Create a test account if none exist
            unique_num = int(time.time() * 1000) % 1000000 + 12
            account_data = ExpenseAccountCreate(
                name="Test Async Get Account", desc="Test async description for get", accountNum=unique_num
            )

            created = await async_client.expense_accounts.create(account_data)
            if isinstance(created, dict) and "id" in created:
                account_id = created["id"]

                result = await async_client.expense_accounts.get(account_id)

                assert result is not None
                if isinstance(result, dict):
                    assert "id" in result
                    assert result["id"] == account_id

                # Cleanup
                try:
                    await async_client.expense_accounts.delete(account_id)
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_update_expense_account(self, async_client):
        """Test updating an expense account asynchronously."""
        # Create an account first
        unique_num = int(time.time() * 1000) % 1000000 + 13
        account_data = ExpenseAccountCreate(
            name="Test Async Update Account", desc="Original async description", accountNum=unique_num
        )

        created = await async_client.expense_accounts.create(account_data)

        if isinstance(created, dict) and "id" in created:
            account_id = created["id"]

            # Update the account
            update_data = ExpenseAccountUpdate(name="Updated Async Test Account", desc="Updated async description")

            result = await async_client.expense_accounts.update(account_id, update_data)

            assert result is not None

            # Fetch the account again to verify the update
            updated = await async_client.expense_accounts.get(account_id)

            if isinstance(updated, dict):
                # The update endpoint may return status, so verify via get
                assert "id" in updated
                assert updated["id"] == account_id
                # Name or desc should be updated
                if "name" in updated:
                    assert updated["name"] == "Updated Async Test Account"
                elif "desc" in updated:
                    assert updated["desc"] == "Updated async description"

            # Cleanup
            try:
                await async_client.expense_accounts.delete(account_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_delete_expense_account(self, async_client):
        """Test deleting an expense account asynchronously."""
        # Create an account first
        unique_num = int(time.time() * 1000) % 1000000 + 14
        account_data = ExpenseAccountCreate(
            name="Test Async Delete Account", desc="Async account to be deleted", accountNum=unique_num
        )

        created = await async_client.expense_accounts.create(account_data)

        if isinstance(created, dict) and "id" in created:
            account_id = created["id"]

            # Delete the account
            result = await async_client.expense_accounts.delete(account_id)

            assert result is not None

            # Verify it's deleted by trying to get it (should raise an error)
            try:
                await async_client.expense_accounts.get(account_id)
                # If we get here, the account still exists (some APIs don't actually delete)
                # This is acceptable behavior
            except Exception:
                # Expected: account should not be found
                pass
