"""
Tests for the Remittances API.
"""

import pytest


class TestRemittancesResource:
    """Test cases for the Remittances API."""

    def test_list_remittances(self, client):
        """Test listing remittances."""
        result = client.remittances.list()

        assert result is not None
        assert isinstance(result, list)

    def test_get_remittance(self, client):
        """Test getting a remittance."""
        # First, list remittances to get an ID
        remittances = client.remittances.list()

        if not remittances or len(remittances) == 0:
            pytest.skip("No remittances available for testing")

        remittance_id = remittances[0].get("id") or remittances[0].get("_id")
        if not remittance_id:
            pytest.skip("Remittance ID not found")

        result = client.remittances.get(remittance_id)

        assert result is not None
        assert isinstance(result, dict)


class TestAsyncRemittancesResource:
    """Test cases for the Async Remittances API."""

    @pytest.mark.asyncio
    async def test_list_remittances(self, async_client):
        """Test listing remittances asynchronously."""
        result = await async_client.remittances.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_get_remittance(self, async_client):
        """Test getting a remittance asynchronously."""
        # First, list remittances to get an ID
        remittances = await async_client.remittances.list()

        if not remittances or len(remittances) == 0:
            pytest.skip("No remittances available for testing")

        remittance_id = remittances[0].get("id") or remittances[0].get("_id")
        if not remittance_id:
            pytest.skip("Remittance ID not found")

        result = await async_client.remittances.get(remittance_id)

        assert result is not None
        assert isinstance(result, dict)
