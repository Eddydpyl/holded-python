"""
Tests for the Treasury API.
"""

import pytest

from holded.api.invoice.models.treasury import TreasuryAccountCreate


class TestTreasuryResource:
    """Test cases for the Treasury API."""

    def test_list_treasury_accounts(self, client):
        """Test listing treasury accounts."""
        result = client.treasury.list()

        assert result is not None
        # Result should be a list
        assert isinstance(result, list)

        # If there are accounts, verify structure
        if result and len(result) > 0:
            account = result[0]
            assert "id" in account
            assert "name" in account
            assert "type" in account
            assert "balance" in account

    def test_create_treasury_account(self, client):
        """Test creating a treasury account."""
        # Use a valid IBAN format or omit it
        account_data = TreasuryAccountCreate(
            name="Test Treasury Account",
            type="bank",
            balance=0,
            # Using a valid Spanish IBAN format (24 characters)
            iban="ES9121000418450200051332",
            swift="TESTESMM",
            bank="test_bank",
            bankname="Test Bank",
        )

        result = client.treasury.create(account_data)

        assert result is not None
        # Verify the account was created
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store account ID for cleanup if needed
            if "id" in result:
                result["id"]
                # Cleanup: delete the account if possible
                # Note: Treasury API doesn't have delete, so we'll just verify creation

    def test_get_treasury_account(self, client):
        """Test getting a specific treasury account."""
        # First, list accounts to get an ID
        accounts = client.treasury.list()

        if accounts and len(accounts) > 0:
            account_id = accounts[0]["id"]

            result = client.treasury.get(account_id)

            assert result is not None
            if isinstance(result, dict):
                assert result["id"] == account_id
                assert "name" in result
                assert "type" in result
                assert "balance" in result
        else:
            pytest.skip("No treasury accounts available for testing")

    def test_create_treasury_account_with_dict(self, client):
        """Test creating a treasury account using a dictionary."""
        account_data = {
            "name": "Test Treasury Account Dict",
            "type": "cash",
            "balance": 1000,
        }

        result = client.treasury.create(account_data)

        assert result is not None


@pytest.mark.asyncio
class TestAsyncTreasuryResource:
    """Test cases for the Async Treasury API."""

    async def test_list_treasury_accounts(self, async_client):
        """Test listing treasury accounts asynchronously."""
        result = await async_client.treasury.list()

        assert result is not None
        assert isinstance(result, list)

        if result and len(result) > 0:
            account = result[0]
            assert "id" in account
            assert "name" in account

    async def test_create_treasury_account(self, async_client):
        """Test creating a treasury account asynchronously."""
        # Create account without IBAN to avoid validation issues
        account_data = TreasuryAccountCreate(
            name="Test Async Treasury Account",
            type="cash",
            balance=0,
        )

        result = await async_client.treasury.create(account_data)

        assert result is not None

    async def test_get_treasury_account(self, async_client):
        """Test getting a specific treasury account asynchronously."""
        accounts = await async_client.treasury.list()

        if accounts and len(accounts) > 0:
            account_id = accounts[0]["id"]

            result = await async_client.treasury.get(account_id)

            assert result is not None
            if isinstance(result, dict):
                assert result["id"] == account_id
        else:
            pytest.skip("No treasury accounts available for testing")
