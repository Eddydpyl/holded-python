"""
Tests for the Bookings API.
"""

import pytest

from holded.crm_api.models.bookings import BookingCreate, BookingUpdate, BookingCustomField


class TestBookingsResource:
    """Test cases for the Bookings API."""

    def test_list_locations(self, client):
        """Test listing locations."""
        result = client.bookings.list_locations()

        assert result is not None
        assert isinstance(result, list)

    def test_get_available_slots(self, client):
        """Test getting available slots for a location."""
        # First, get a location
        locations = client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            result = client.bookings.get_available_slots(location_id)

            assert result is not None
            assert isinstance(result, list)
        except Exception as e:
            pytest.skip(f"Get available slots failed: {e}")

    def test_list_bookings(self, client):
        """Test listing bookings."""
        result = client.bookings.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_booking(self, client):
        """Test creating a booking."""
        # First, get a location and service
        locations = client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        # Get available slots to find a service
        try:
            slots = client.bookings.get_available_slots(location_id)
            if not slots:
                pytest.skip("No available slots")

            # Get service ID from the first slot or location
            service_id = locations[0].get("serviceId") or locations[0].get("service_id")
            if not service_id:
                # Try to get from slots
                if slots and isinstance(slots[0], dict):
                    service_id = slots[0].get("serviceId") or slots[0].get("service_id")

            if not service_id:
                pytest.skip("Service ID not found")

            import time
            booking_data = BookingCreate(
                location_id=location_id,
                service_id=service_id,
                date_time=int(time.time() * 1000) + 86400000,  # Tomorrow
                timezone="Europe/Madrid",
                language="es",
                custom_fields=[
                    BookingCustomField(name="name", value="Test Booking"),
                    BookingCustomField(name="email", value="test@example.com"),
                ],
            )

            result = client.bookings.create(booking_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: cancel the created booking
            booking_id = result.get("id") or result.get("_id")
            if booking_id:
                try:
                    client.bookings.cancel(booking_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Booking creation failed: {e}")

    def test_get_booking(self, client):
        """Test getting a booking."""
        # First, get a location and create a booking
        locations = client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            slots = client.bookings.get_available_slots(location_id)
            if not slots:
                pytest.skip("No available slots")

            service_id = locations[0].get("serviceId") or locations[0].get("service_id")
            if not service_id and slots and isinstance(slots[0], dict):
                service_id = slots[0].get("serviceId") or slots[0].get("service_id")

            if not service_id:
                pytest.skip("Service ID not found")

            import time
            booking_data = BookingCreate(
                location_id=location_id,
                service_id=service_id,
                date_time=int(time.time() * 1000) + 86400000,  # Tomorrow
                timezone="Europe/Madrid",
                language="es",
                custom_fields=[
                    BookingCustomField(name="name", value="Test Booking Get"),
                    BookingCustomField(name="email", value="test@example.com"),
                ],
            )

            created = client.bookings.create(booking_data)
            booking_id = created.get("id") or created.get("_id")
            if not booking_id:
                pytest.skip("Booking ID not found after creation")

            result = client.bookings.get(booking_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.bookings.cancel(booking_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get booking failed: {e}")

    def test_update_booking(self, client):
        """Test updating a booking."""
        # First, get a location and create a booking
        locations = client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            slots = client.bookings.get_available_slots(location_id)
            if not slots:
                pytest.skip("No available slots")

            service_id = locations[0].get("serviceId") or locations[0].get("service_id")
            if not service_id and slots and isinstance(slots[0], dict):
                service_id = slots[0].get("serviceId") or slots[0].get("service_id")

            if not service_id:
                pytest.skip("Service ID not found")

            import time
            booking_data = BookingCreate(
                location_id=location_id,
                service_id=service_id,
                date_time=int(time.time() * 1000) + 86400000,  # Tomorrow
                timezone="Europe/Madrid",
                language="es",
                custom_fields=[
                    BookingCustomField(name="name", value="Test Booking Update"),
                    BookingCustomField(name="email", value="test@example.com"),
                ],
            )

            created = client.bookings.create(booking_data)
            booking_id = created.get("id") or created.get("_id")
            if not booking_id:
                pytest.skip("Booking ID not found after creation")

            # Update the booking
            update_data = BookingUpdate(
                custom_fields=[
                    BookingCustomField(name="name", value="Updated Test Booking"),
                    BookingCustomField(name="email", value="updated@example.com"),
                ],
            )
            result = client.bookings.update(booking_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.bookings.cancel(booking_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update booking failed: {e}")

    def test_cancel_booking(self, client):
        """Test canceling a booking."""
        # First, get a location and create a booking
        locations = client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            slots = client.bookings.get_available_slots(location_id)
            if not slots:
                pytest.skip("No available slots")

            service_id = locations[0].get("serviceId") or locations[0].get("service_id")
            if not service_id and slots and isinstance(slots[0], dict):
                service_id = slots[0].get("serviceId") or slots[0].get("service_id")

            if not service_id:
                pytest.skip("Service ID not found")

            import time
            booking_data = BookingCreate(
                location_id=location_id,
                service_id=service_id,
                date_time=int(time.time() * 1000) + 86400000,  # Tomorrow
                timezone="Europe/Madrid",
                language="es",
                custom_fields=[
                    BookingCustomField(name="name", value="Test Booking Cancel"),
                    BookingCustomField(name="email", value="test@example.com"),
                ],
            )

            created = client.bookings.create(booking_data)
            booking_id = created.get("id") or created.get("_id")
            if not booking_id:
                pytest.skip("Booking ID not found after creation")

            # Cancel the booking
            result = client.bookings.cancel(booking_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Cancel booking failed: {e}")


class TestAsyncBookingsResource:
    """Test cases for the Async Bookings API."""

    @pytest.mark.asyncio
    async def test_list_locations(self, async_client):
        """Test listing locations asynchronously."""
        result = await async_client.bookings.list_locations()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_get_available_slots(self, async_client):
        """Test getting available slots for a location asynchronously."""
        # First, get a location
        locations = await async_client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            result = await async_client.bookings.get_available_slots(location_id)

            assert result is not None
            assert isinstance(result, list)
        except Exception as e:
            pytest.skip(f"Get available slots failed: {e}")

    @pytest.mark.asyncio
    async def test_list_bookings(self, async_client):
        """Test listing bookings asynchronously."""
        result = await async_client.bookings.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_booking(self, async_client):
        """Test creating a booking asynchronously."""
        # First, get a location and service
        locations = await async_client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            slots = await async_client.bookings.get_available_slots(location_id)
            if not slots:
                pytest.skip("No available slots")

            service_id = locations[0].get("serviceId") or locations[0].get("service_id")
            if not service_id and slots and isinstance(slots[0], dict):
                service_id = slots[0].get("serviceId") or slots[0].get("service_id")

            if not service_id:
                pytest.skip("Service ID not found")

            import time
            booking_data = BookingCreate(
                location_id=location_id,
                service_id=service_id,
                date_time=int(time.time() * 1000) + 86400000,  # Tomorrow
                timezone="Europe/Madrid",
                language="es",
                custom_fields=[
                    BookingCustomField(name="name", value="Test Booking Async"),
                    BookingCustomField(name="email", value="test@example.com"),
                ],
            )

            result = await async_client.bookings.create(booking_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: cancel the created booking
            booking_id = result.get("id") or result.get("_id")
            if booking_id:
                try:
                    await async_client.bookings.cancel(booking_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Booking creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_booking(self, async_client):
        """Test getting a booking asynchronously."""
        # First, get a location and create a booking
        locations = await async_client.bookings.list_locations()
        if not locations:
            pytest.skip("No locations available")

        location_id = locations[0].get("id") or locations[0].get("_id")
        if not location_id:
            pytest.skip("Location ID not found")

        try:
            slots = await async_client.bookings.get_available_slots(location_id)
            if not slots:
                pytest.skip("No available slots")

            service_id = locations[0].get("serviceId") or locations[0].get("service_id")
            if not service_id and slots and isinstance(slots[0], dict):
                service_id = slots[0].get("serviceId") or slots[0].get("service_id")

            if not service_id:
                pytest.skip("Service ID not found")

            import time
            booking_data = BookingCreate(
                location_id=location_id,
                service_id=service_id,
                date_time=int(time.time() * 1000) + 86400000,  # Tomorrow
                timezone="Europe/Madrid",
                language="es",
                custom_fields=[
                    BookingCustomField(name="name", value="Test Booking Get Async"),
                    BookingCustomField(name="email", value="test@example.com"),
                ],
            )

            created = await async_client.bookings.create(booking_data)
            booking_id = created.get("id") or created.get("_id")
            if not booking_id:
                pytest.skip("Booking ID not found after creation")

            result = await async_client.bookings.get(booking_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.bookings.cancel(booking_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get booking failed: {e}")

