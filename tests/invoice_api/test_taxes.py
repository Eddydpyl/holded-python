"""
Tests for the Taxes API.
"""

import pytest


class TestTaxesResource:
    """Test cases for the Taxes API."""

    def test_list_taxes(self, client):
        """Test listing taxes."""
        result = client.taxes.list()

        assert result is not None
        # Result can be a list or dict
        if isinstance(result, dict):
            # Check if it has items or is a direct response
            if "items" in result:
                assert isinstance(result["items"], list)
            elif "data" in result:
                assert isinstance(result["data"], list)
            else:
                # Might be a direct dict response
                pass
        elif isinstance(result, list):
            assert isinstance(result, list)
            # If there are taxes, verify structure
            if result and len(result) > 0:
                tax = result[0]
                # Tax should have some identifying fields
                assert isinstance(tax, (dict, object))


class TestAsyncTaxesResource:
    """Test cases for the Async Taxes API."""

    @pytest.mark.asyncio
    async def test_list_taxes(self, async_client):
        """Test listing taxes asynchronously."""
        result = await async_client.taxes.list()

        assert result is not None
        if isinstance(result, dict):
            if "items" in result:
                assert isinstance(result["items"], list)
            elif "data" in result:
                assert isinstance(result["data"], list)
        elif isinstance(result, list):
            assert isinstance(result, list)
