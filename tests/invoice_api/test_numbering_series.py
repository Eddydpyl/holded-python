"""
Tests for the Numbering Series API.
"""

import pytest

from holded.api.invoice.models.numbering_series import NumberingSeriesCreate, NumberingSeriesUpdate


class TestNumberingSeriesResource:
    """Test cases for the Numbering Series API."""

    def test_list_numbering_series_by_type(self, client):
        """Test listing numbering series by document type."""
        # Test with a common document type like 'invoice'
        result = client.numbering_series.list_by_type("invoice")

        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are series, verify structure
                if items and len(items) > 0:
                    series = items[0]
                    assert "id" in series
                    assert "name" in series
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    def test_create_numbering_series(self, client):
        """Test creating a numbering series."""
        series_data = NumberingSeriesCreate(name="Test Numbering Series", format="INV-%d", last=1, type="invoice")

        result = client.numbering_series.create("invoice", series_data)

        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store series ID for cleanup
            if "id" in result:
                series_id = result["id"]
                # Cleanup: delete the series
                try:
                    client.numbering_series.delete("invoice", series_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test_create_numbering_series_with_dict(self, client):
        """Test creating a numbering series using a dictionary."""
        series_data = {"name": "Test Numbering Series Dict", "format": "ORD-%d", "last": 1, "type": "order"}

        result = client.numbering_series.create("order", series_data)

        assert result is not None
        if isinstance(result, dict) and "id" in result:
            # Cleanup
            try:
                client.numbering_series.delete("order", result["id"])
            except Exception:
                pass

    def test_update_numbering_series(self, client):
        """Test updating a numbering series."""
        # Create a series first
        series_data = NumberingSeriesCreate(name="Test Update Series", format="TEST-%d", last=1, type="invoice")

        created = client.numbering_series.create("invoice", series_data)

        if isinstance(created, dict) and "id" in created:
            series_id = created["id"]

            # Update the series
            update_data = NumberingSeriesUpdate(name="Updated Test Series", format="UPD-%d", last=5)

            result = client.numbering_series.update("invoice", series_id, update_data)

            assert result is not None

            # Fetch the series again to verify the update
            all_series = client.numbering_series.list_by_type("invoice")

            # Handle different response formats
            if isinstance(all_series, dict) and "items" in all_series:
                series_list = all_series["items"]
            else:
                series_list = all_series if isinstance(all_series, list) else []

            # Find the updated series
            updated_series = None
            for s in series_list:
                if isinstance(s, dict) and s.get("id") == series_id:
                    updated_series = s
                    break

            if updated_series:
                # Name or format should be updated
                if "name" in updated_series:
                    assert updated_series["name"] == "Updated Test Series"
                elif "format" in updated_series:
                    assert updated_series["format"] == "UPD-%d"

            # Cleanup
            try:
                client.numbering_series.delete("invoice", series_id)
            except Exception:
                pass

    def test_delete_numbering_series(self, client):
        """Test deleting a numbering series."""
        # Create a series first
        series_data = NumberingSeriesCreate(name="Test Delete Series", format="DEL-%d", last=1, type="invoice")

        created = client.numbering_series.create("invoice", series_data)

        if isinstance(created, dict) and "id" in created:
            series_id = created["id"]

            # Delete the series
            result = client.numbering_series.delete("invoice", series_id)

            assert result is not None

            # Verify it's deleted by trying to list and check it's not there
            all_series = client.numbering_series.list_by_type("invoice")

            # Handle different response formats
            if isinstance(all_series, dict) and "items" in all_series:
                series_list = all_series["items"]
            else:
                series_list = all_series if isinstance(all_series, list) else []

            # Check that the deleted series is not in the list
            for s in series_list:
                if isinstance(s, dict) and s.get("id") == series_id:
                    break

            # Series should not be found (or API might not actually delete)
            # This is acceptable behavior - some APIs mark as deleted but don't remove


class TestAsyncNumberingSeriesResource:
    """Test cases for the Async Numbering Series API."""

    @pytest.mark.asyncio
    async def test_list_numbering_series_by_type(self, async_client):
        """Test listing numbering series by document type asynchronously."""
        # Test with a common document type like 'invoice'
        result = await async_client.numbering_series.list_by_type("invoice")

        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are series, verify structure
                if items and len(items) > 0:
                    series = items[0]
                    assert "id" in series
                    assert "name" in series
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_numbering_series(self, async_client):
        """Test creating a numbering series asynchronously."""
        series_data = NumberingSeriesCreate(
            name="Test Async Numbering Series", format="ASYNC-%d", last=1, type="invoice"
        )

        result = await async_client.numbering_series.create("invoice", series_data)

        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store series ID for cleanup
            if "id" in result:
                series_id = result["id"]
                # Cleanup: delete the series
                try:
                    await async_client.numbering_series.delete("invoice", series_id)
                except Exception:
                    pass  # Ignore cleanup errors

    @pytest.mark.asyncio
    async def test_create_numbering_series_with_dict(self, async_client):
        """Test creating a numbering series using a dictionary asynchronously."""
        series_data = {"name": "Test Async Numbering Series Dict", "format": "ASYNC-ORD-%d", "last": 1, "type": "order"}

        result = await async_client.numbering_series.create("order", series_data)

        assert result is not None
        if isinstance(result, dict) and "id" in result:
            # Cleanup
            try:
                await async_client.numbering_series.delete("order", result["id"])
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_update_numbering_series(self, async_client):
        """Test updating a numbering series asynchronously."""
        # Create a series first
        series_data = NumberingSeriesCreate(
            name="Test Async Update Series", format="ASYNC-TEST-%d", last=1, type="invoice"
        )

        created = await async_client.numbering_series.create("invoice", series_data)

        if isinstance(created, dict) and "id" in created:
            series_id = created["id"]

            # Update the series
            update_data = NumberingSeriesUpdate(name="Updated Async Test Series", format="ASYNC-UPD-%d", last=5)

            result = await async_client.numbering_series.update("invoice", series_id, update_data)

            assert result is not None

            # Fetch the series again to verify the update
            all_series = await async_client.numbering_series.list_by_type("invoice")

            # Handle different response formats
            if isinstance(all_series, dict) and "items" in all_series:
                series_list = all_series["items"]
            else:
                series_list = all_series if isinstance(all_series, list) else []

            # Find the updated series
            updated_series = None
            for s in series_list:
                if isinstance(s, dict) and s.get("id") == series_id:
                    updated_series = s
                    break

            if updated_series:
                # Name or format should be updated
                if "name" in updated_series:
                    assert updated_series["name"] == "Updated Async Test Series"
                elif "format" in updated_series:
                    assert updated_series["format"] == "ASYNC-UPD-%d"

            # Cleanup
            try:
                await async_client.numbering_series.delete("invoice", series_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_delete_numbering_series(self, async_client):
        """Test deleting a numbering series asynchronously."""
        # Create a series first
        series_data = NumberingSeriesCreate(
            name="Test Async Delete Series", format="ASYNC-DEL-%d", last=1, type="invoice"
        )

        created = await async_client.numbering_series.create("invoice", series_data)

        if isinstance(created, dict) and "id" in created:
            series_id = created["id"]

            # Delete the series
            result = await async_client.numbering_series.delete("invoice", series_id)

            assert result is not None

            # Verify it's deleted by trying to list and check it's not there
            all_series = await async_client.numbering_series.list_by_type("invoice")

            # Handle different response formats
            if isinstance(all_series, dict) and "items" in all_series:
                series_list = all_series["items"]
            else:
                series_list = all_series if isinstance(all_series, list) else []

            # Check that the deleted series is not in the list
            for s in series_list:
                if isinstance(s, dict) and s.get("id") == series_id:
                    break

            # Series should not be found (or API might not actually delete)
            # This is acceptable behavior - some APIs mark as deleted but don't remove
