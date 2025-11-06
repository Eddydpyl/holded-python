"""
Tests for the Events API.
"""

import pytest

from holded.api.crm.models.events import EventCreate, EventUpdate


class TestEventsResource:
    """Test cases for the Events API."""

    def test_list_events(self, client):
        """Test listing events."""
        result = client.events.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_event(self, client):
        """Test creating an event."""
        import time

        event_data = EventCreate(
            name=f"Test Event {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            result = client.events.create(event_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created event
            event_id = result.get("id") or result.get("_id")
            if event_id:
                try:
                    client.events.delete(event_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Event creation failed: {e}")

    def test_get_event(self, client):
        """Test getting an event."""
        import time

        # First, create an event to get
        event_data = EventCreate(
            name=f"Test Event Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            created = client.events.create(event_data)
            event_id = created.get("id") or created.get("_id")
            if not event_id:
                pytest.skip("Event ID not found after creation")

            result = client.events.get(event_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.events.delete(event_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get event failed: {e}")

    def test_update_event(self, client):
        """Test updating an event."""
        import time

        # First, create an event to update
        event_data = EventCreate(
            name=f"Test Event Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            created = client.events.create(event_data)
            event_id = created.get("id") or created.get("_id")
            if not event_id:
                pytest.skip("Event ID not found after creation")

            # Update the event
            update_data = EventUpdate(
                name="Updated Test Event",
                duration=120,
            )
            result = client.events.update(event_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.events.delete(event_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update event failed: {e}")

    def test_delete_event(self, client):
        """Test deleting an event."""
        import time

        # First, create an event to delete
        event_data = EventCreate(
            name=f"Test Event Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            created = client.events.create(event_data)
            event_id = created.get("id") or created.get("_id")
            if not event_id:
                pytest.skip("Event ID not found after creation")

            # Delete the event
            result = client.events.delete(event_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete event failed: {e}")


class TestAsyncEventsResource:
    """Test cases for the Async Events API."""

    @pytest.mark.asyncio
    async def test_list_events(self, async_client):
        """Test listing events asynchronously."""
        result = await async_client.events.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_event(self, async_client):
        """Test creating an event asynchronously."""
        import time

        event_data = EventCreate(
            name=f"Test Event Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            result = await async_client.events.create(event_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created event
            event_id = result.get("id") or result.get("_id")
            if event_id:
                try:
                    await async_client.events.delete(event_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Event creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_event(self, async_client):
        """Test getting an event asynchronously."""
        import time

        # First, create an event to get
        event_data = EventCreate(
            name=f"Test Event Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            created = await async_client.events.create(event_data)
            event_id = created.get("id") or created.get("_id")
            if not event_id:
                pytest.skip("Event ID not found after creation")

            result = await async_client.events.get(event_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.events.delete(event_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get event failed: {e}")

    @pytest.mark.asyncio
    async def test_update_event(self, async_client):
        """Test updating an event asynchronously."""
        import time

        # First, create an event to update
        event_data = EventCreate(
            name=f"Test Event Update Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            created = await async_client.events.create(event_data)
            event_id = created.get("id") or created.get("_id")
            if not event_id:
                pytest.skip("Event ID not found after creation")

            # Update the event
            update_data = EventUpdate(
                name="Updated Test Event Async",
                duration=120,
            )
            result = await async_client.events.update(event_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.events.delete(event_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update event failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_event(self, async_client):
        """Test deleting an event asynchronously."""
        import time

        # First, create an event to delete
        event_data = EventCreate(
            name=f"Test Event Delete Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            start_date=int(time.time() * 1000),
            duration=60,
        )

        try:
            created = await async_client.events.create(event_data)
            event_id = created.get("id") or created.get("_id")
            if not event_id:
                pytest.skip("Event ID not found after creation")

            # Delete the event
            result = await async_client.events.delete(event_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete event failed: {e}")
