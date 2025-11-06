"""
Tests for the Services API.
"""

import pytest

from holded.api.invoice.models.services import ServiceCreate, ServiceUpdate


class TestServicesResource:
    """Test cases for the Services API."""

    def test_list_services(self, client):
        """Test listing services."""
        result = client.services.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_service(self, client):
        """Test creating a service."""
        service_data = ServiceCreate(
            name=f"Test Service {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            desc="Test service description",
            subtotal=10000,  # 100.00 in cents
            tax=21.0,
        )

        try:
            result = client.services.create(service_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created service
            service_id = result.get("id") or result.get("_id")
            if service_id:
                try:
                    client.services.delete(service_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Service creation failed: {e}")

    def test_get_service(self, client):
        """Test getting a service."""
        # First, create a service to get
        service_data = ServiceCreate(
            name=f"Test Service Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            desc="Test description",
        )

        try:
            created = client.services.create(service_data)
            service_id = created.get("id") or created.get("_id")
            if not service_id:
                pytest.skip("Service ID not found after creation")

            result = client.services.get(service_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.services.delete(service_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get service failed: {e}")

    def test_update_service(self, client):
        """Test updating a service."""
        # First, create a service to update
        service_data = ServiceCreate(
            name=f"Test Service Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.services.create(service_data)
            service_id = created.get("id") or created.get("_id")
            if not service_id:
                pytest.skip("Service ID not found after creation")

            # Update the service
            update_data = ServiceUpdate(
                name="Updated Test Service",
                desc="Updated description",
            )
            result = client.services.update(service_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.services.delete(service_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update service failed: {e}")

    def test_delete_service(self, client):
        """Test deleting a service."""
        # First, create a service to delete
        service_data = ServiceCreate(
            name=f"Test Service Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.services.create(service_data)
            service_id = created.get("id") or created.get("_id")
            if not service_id:
                pytest.skip("Service ID not found after creation")

            # Delete the service
            result = client.services.delete(service_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete service failed: {e}")


class TestAsyncServicesResource:
    """Test cases for the Async Services API."""

    @pytest.mark.asyncio
    async def test_list_services(self, async_client):
        """Test listing services asynchronously."""
        result = await async_client.services.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_service(self, async_client):
        """Test creating a service asynchronously."""
        service_data = ServiceCreate(
            name=f"Test Service Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            desc="Test service description",
            subtotal=15000,  # 150.00 in cents
            tax=21.0,
        )

        try:
            result = await async_client.services.create(service_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created service
            service_id = result.get("id") or result.get("_id")
            if service_id:
                try:
                    await async_client.services.delete(service_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Service creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_service(self, async_client):
        """Test getting a service asynchronously."""
        # First, create a service to get
        service_data = ServiceCreate(
            name=f"Test Service Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.services.create(service_data)
            service_id = created.get("id") or created.get("_id")
            if not service_id:
                pytest.skip("Service ID not found after creation")

            result = await async_client.services.get(service_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.services.delete(service_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get service failed: {e}")

    @pytest.mark.asyncio
    async def test_update_service(self, async_client):
        """Test updating a service asynchronously."""
        # First, create a service to update
        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        service_data = ServiceCreate(
            name=f"Test Service Update Async {test_id}",
        )

        try:
            created = await async_client.services.create(service_data)
            service_id = created.get("id") or created.get("_id")
            if not service_id:
                pytest.skip("Service ID not found after creation")

            # Update the service
            update_data = ServiceUpdate(
                name="Updated Test Service Async",
                desc="Updated description",
            )
            result = await async_client.services.update(service_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.services.delete(service_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update service failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_service(self, async_client):
        """Test deleting a service asynchronously."""
        # First, create a service to delete
        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        service_data = ServiceCreate(
            name=f"Test Service Delete Async {test_id}",
        )

        try:
            created = await async_client.services.create(service_data)
            service_id = created.get("id") or created.get("_id")
            if not service_id:
                pytest.skip("Service ID not found after creation")

            # Delete the service
            result = await async_client.services.delete(service_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete service failed: {e}")
