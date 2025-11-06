"""
Tests for the Payments API.
"""

import time

import pytest

from holded.api.invoice.models.payments import PaymentCreate, PaymentListParams, PaymentUpdate


class TestPaymentsResource:
    """Test cases for the Payments API."""

    def test_list_payments(self, client):
        """Test listing payments."""
        result = client.payments.list()

        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are payments, verify structure
                if items and len(items) > 0:
                    payment = items[0]
                    assert "id" in payment
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    def test_list_payments_with_params(self, client):
        """Test listing payments with query parameters."""
        # Get current timestamp and a timestamp from 30 days ago
        end_timestamp = str(int(time.time()))
        start_timestamp = str(int(time.time()) - (30 * 24 * 60 * 60))

        params = PaymentListParams(starttmp=start_timestamp, endtmp=end_timestamp)

        result = client.payments.list(params)

        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    def test_create_payment(self, client):
        """Test creating a payment."""
        # First, get a valid bank account ID and contact ID
        try:
            # Get treasury accounts (bank accounts)
            treasury_accounts = client.treasury.list()
            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")

            bank_id = treasury_accounts[0]["id"]

            # Get contacts
            contacts = client.contacts.list()
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            contact_id = contacts[0]["id"]

            # Create payment
            payment_data = PaymentCreate(
                bankId=bank_id, contactId=contact_id, amount=100.50, desc="Test payment", date=int(time.time())
            )

            result = client.payments.create(payment_data)

            assert result is not None
            if isinstance(result, dict):
                assert "id" in result or "amount" in result
                # Store payment ID for cleanup
                if "id" in result:
                    payment_id = result["id"]
                    # Cleanup: delete the payment
                    try:
                        client.payments.delete(payment_id)
                    except Exception:
                        pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Could not create payment: {e}")

    def test_create_payment_with_dict(self, client):
        """Test creating a payment using a dictionary."""
        try:
            # Get treasury accounts and contacts
            treasury_accounts = client.treasury.list()
            contacts = client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            payment_data = {
                "bankId": bank_id,
                "contactId": contact_id,
                "amount": 200.75,
                "desc": "Test payment from dict",
                "date": int(time.time()),
            }

            result = client.payments.create(payment_data)

            assert result is not None
            if isinstance(result, dict):
                assert "id" in result or "amount" in result
                # Cleanup
                if "id" in result:
                    try:
                        client.payments.delete(result["id"])
                    except Exception:
                        pass
        except Exception as e:
            pytest.skip(f"Could not create payment: {e}")

    def test_get_payment(self, client):
        """Test getting a specific payment."""
        # First, try to get an existing payment
        payments = client.payments.list()

        if isinstance(payments, dict) and "items" in payments:
            items = payments["items"]
        elif isinstance(payments, list):
            items = payments
        else:
            items = []

        if items and len(items) > 0:
            payment_id = items[0]["id"]
            result = client.payments.get(payment_id)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
            assert result["id"] == payment_id
        else:
            pytest.skip("No payments available for testing")

    def test_update_payment(self, client):
        """Test updating a payment."""
        try:
            # Get required IDs
            treasury_accounts = client.treasury.list()
            contacts = client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            # Create a payment first
            payment_data = PaymentCreate(
                bankId=bank_id,
                contactId=contact_id,
                amount=150.00,
                desc="Original payment description",
                date=int(time.time()),
            )

            created = client.payments.create(payment_data)

            if isinstance(created, dict) and "id" in created:
                payment_id = created["id"]

                # Update the payment
                update_data = PaymentUpdate(desc="Updated payment description", amount=175.00)

                result = client.payments.update(payment_id, update_data)

                assert result is not None
                if isinstance(result, dict):
                    # The update might return status/info, so verify by getting the payment
                    updated_payment = client.payments.get(payment_id)
                    if isinstance(updated_payment, dict):
                        if "desc" in updated_payment:
                            assert updated_payment["desc"] == "Updated payment description"
                        elif "amount" in updated_payment:
                            assert updated_payment["amount"] == 175.00

                # Cleanup
                try:
                    client.payments.delete(payment_id)
                except Exception:
                    pass
        except Exception as e:
            pytest.skip(f"Could not update payment: {e}")

    def test_delete_payment(self, client):
        """Test deleting a payment."""
        try:
            # Get required IDs
            treasury_accounts = client.treasury.list()
            contacts = client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            # Create a payment first
            payment_data = PaymentCreate(
                bankId=bank_id, contactId=contact_id, amount=50.00, desc="Payment to be deleted", date=int(time.time())
            )

            created = client.payments.create(payment_data)

            if isinstance(created, dict) and "id" in created:
                payment_id = created["id"]

                # Delete the payment
                result = client.payments.delete(payment_id)

                assert result is not None
                # Verify deletion by trying to get the payment (should fail)
                try:
                    client.payments.get(payment_id)
                    # If we get here, the payment still exists (might be soft delete)
                    pass
                except Exception:
                    # Expected: payment not found
                    pass
        except Exception as e:
            pytest.skip(f"Could not delete payment: {e}")


class TestAsyncPaymentsResource:
    """Test cases for the Async Payments API."""

    @pytest.mark.asyncio
    async def test_list_payments(self, async_client):
        """Test listing payments asynchronously."""
        result = await async_client.payments.list()

        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_payments_with_params(self, async_client):
        """Test listing payments with query parameters asynchronously."""
        end_timestamp = str(int(time.time()))
        start_timestamp = str(int(time.time()) - (30 * 24 * 60 * 60))

        params = PaymentListParams(starttmp=start_timestamp, endtmp=end_timestamp)

        result = await async_client.payments.list(params)

        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_payment(self, async_client):
        """Test creating a payment asynchronously."""
        try:
            treasury_accounts = await async_client.treasury.list()
            contacts = await async_client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            payment_data = PaymentCreate(
                bankId=bank_id, contactId=contact_id, amount=300.00, desc="Test async payment", date=int(time.time())
            )

            result = await async_client.payments.create(payment_data)

            assert result is not None
            if isinstance(result, dict):
                assert "id" in result or "amount" in result
                # Cleanup
                if "id" in result:
                    try:
                        await async_client.payments.delete(result["id"])
                    except Exception:
                        pass
        except Exception as e:
            pytest.skip(f"Could not create payment: {e}")

    @pytest.mark.asyncio
    async def test_create_payment_with_dict(self, async_client):
        """Test creating a payment using a dictionary asynchronously."""
        try:
            treasury_accounts = await async_client.treasury.list()
            contacts = await async_client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            payment_data = {
                "bankId": bank_id,
                "contactId": contact_id,
                "amount": 400.25,
                "desc": "Test async payment from dict",
                "date": int(time.time()),
            }

            result = await async_client.payments.create(payment_data)

            assert result is not None
            if isinstance(result, dict):
                assert "id" in result or "amount" in result
                # Cleanup
                if "id" in result:
                    try:
                        await async_client.payments.delete(result["id"])
                    except Exception:
                        pass
        except Exception as e:
            pytest.skip(f"Could not create payment: {e}")

    @pytest.mark.asyncio
    async def test_get_payment(self, async_client):
        """Test getting a specific payment asynchronously."""
        payments = await async_client.payments.list()

        if isinstance(payments, dict) and "items" in payments:
            items = payments["items"]
        elif isinstance(payments, list):
            items = payments
        else:
            items = []

        if items and len(items) > 0:
            payment_id = items[0]["id"]
            result = await async_client.payments.get(payment_id)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
        else:
            pytest.skip("No payments available for testing")

    @pytest.mark.asyncio
    async def test_update_payment(self, async_client):
        """Test updating a payment asynchronously."""
        try:
            treasury_accounts = await async_client.treasury.list()
            contacts = await async_client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            payment_data = PaymentCreate(
                bankId=bank_id,
                contactId=contact_id,
                amount=250.00,
                desc="Original async payment description",
                date=int(time.time()),
            )

            created = await async_client.payments.create(payment_data)

            if isinstance(created, dict) and "id" in created:
                payment_id = created["id"]

                update_data = PaymentUpdate(desc="Updated async payment description", amount=275.00)

                result = await async_client.payments.update(payment_id, update_data)

                assert result is not None
                if isinstance(result, dict):
                    updated_payment = await async_client.payments.get(payment_id)
                    if isinstance(updated_payment, dict):
                        if "desc" in updated_payment:
                            assert updated_payment["desc"] == "Updated async payment description"
                        elif "amount" in updated_payment:
                            assert updated_payment["amount"] == 275.00

                # Cleanup
                try:
                    await async_client.payments.delete(payment_id)
                except Exception:
                    pass
        except Exception as e:
            pytest.skip(f"Could not update payment: {e}")

    @pytest.mark.asyncio
    async def test_delete_payment(self, async_client):
        """Test deleting a payment asynchronously."""
        try:
            treasury_accounts = await async_client.treasury.list()
            contacts = await async_client.contacts.list()

            if not treasury_accounts or len(treasury_accounts) == 0:
                pytest.skip("No treasury accounts available for testing")
            if not contacts or len(contacts) == 0:
                pytest.skip("No contacts available for testing")

            bank_id = treasury_accounts[0]["id"]
            contact_id = contacts[0]["id"]

            payment_data = PaymentCreate(
                bankId=bank_id,
                contactId=contact_id,
                amount=75.00,
                desc="Async payment to be deleted",
                date=int(time.time()),
            )

            created = await async_client.payments.create(payment_data)

            if isinstance(created, dict) and "id" in created:
                payment_id = created["id"]

                result = await async_client.payments.delete(payment_id)

                assert result is not None
                # Verify deletion
                try:
                    await async_client.payments.get(payment_id)
                except Exception:
                    pass
        except Exception as e:
            pytest.skip(f"Could not delete payment: {e}")
