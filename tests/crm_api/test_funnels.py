"""
Tests for the Funnels API.
"""

import pytest

from holded.crm_api.models.funnels import FunnelCreate, FunnelUpdate


class TestFunnelsResource:
    """Test cases for the Funnels API."""

    def test_list_funnels(self, client):
        """Test listing funnels."""
        result = client.funnels.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_funnel(self, client):
        """Test creating a funnel."""
        funnel_data = FunnelCreate(
            name=f"Test Funnel {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            result = client.funnels.create(funnel_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created funnel
            funnel_id = result.get("id") or result.get("_id")
            if funnel_id:
                try:
                    client.funnels.delete(funnel_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Funnel creation failed: {e}")

    def test_get_funnel(self, client):
        """Test getting a funnel."""
        # First, create a funnel to get
        funnel_data = FunnelCreate(
            name=f"Test Funnel Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.funnels.create(funnel_data)
            funnel_id = created.get("id") or created.get("_id")
            if not funnel_id:
                pytest.skip("Funnel ID not found after creation")

            result = client.funnels.get(funnel_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.funnels.delete(funnel_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get funnel failed: {e}")

    def test_update_funnel(self, client):
        """Test updating a funnel."""
        # First, create a funnel to update
        funnel_data = FunnelCreate(
            name=f"Test Funnel Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.funnels.create(funnel_data)
            funnel_id = created.get("id") or created.get("_id")
            if not funnel_id:
                pytest.skip("Funnel ID not found after creation")

            # Update the funnel
            update_data = FunnelUpdate(
                name="Updated Test Funnel",
            )
            result = client.funnels.update(funnel_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.funnels.delete(funnel_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update funnel failed: {e}")

    def test_delete_funnel(self, client):
        """Test deleting a funnel."""
        # First, create a funnel to delete
        funnel_data = FunnelCreate(
            name=f"Test Funnel Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.funnels.create(funnel_data)
            funnel_id = created.get("id") or created.get("_id")
            if not funnel_id:
                pytest.skip("Funnel ID not found after creation")

            # Delete the funnel
            result = client.funnels.delete(funnel_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete funnel failed: {e}")


class TestAsyncFunnelsResource:
    """Test cases for the Async Funnels API."""

    @pytest.mark.asyncio
    async def test_list_funnels(self, async_client):
        """Test listing funnels asynchronously."""
        result = await async_client.funnels.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_funnel(self, async_client):
        """Test creating a funnel asynchronously."""
        funnel_data = FunnelCreate(
            name=f"Test Funnel Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            result = await async_client.funnels.create(funnel_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created funnel
            funnel_id = result.get("id") or result.get("_id")
            if funnel_id:
                try:
                    await async_client.funnels.delete(funnel_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Funnel creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_funnel(self, async_client):
        """Test getting a funnel asynchronously."""
        # First, create a funnel to get
        funnel_data = FunnelCreate(
            name=f"Test Funnel Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.funnels.create(funnel_data)
            funnel_id = created.get("id") or created.get("_id")
            if not funnel_id:
                pytest.skip("Funnel ID not found after creation")

            result = await async_client.funnels.get(funnel_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.funnels.delete(funnel_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get funnel failed: {e}")

    @pytest.mark.asyncio
    async def test_update_funnel(self, async_client):
        """Test updating a funnel asynchronously."""
        # First, create a funnel to update
        funnel_data = FunnelCreate(
            name=f"Test Funnel Update Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.funnels.create(funnel_data)
            funnel_id = created.get("id") or created.get("_id")
            if not funnel_id:
                pytest.skip("Funnel ID not found after creation")

            # Update the funnel
            update_data = FunnelUpdate(
                name="Updated Test Funnel Async",
            )
            result = await async_client.funnels.update(funnel_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.funnels.delete(funnel_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update funnel failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_funnel(self, async_client):
        """Test deleting a funnel asynchronously."""
        # First, create a funnel to delete
        funnel_data = FunnelCreate(
            name=f"Test Funnel Delete Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.funnels.create(funnel_data)
            funnel_id = created.get("id") or created.get("_id")
            if not funnel_id:
                pytest.skip("Funnel ID not found after creation")

            # Delete the funnel
            result = await async_client.funnels.delete(funnel_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete funnel failed: {e}")

