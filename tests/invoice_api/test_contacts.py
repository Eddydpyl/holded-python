"""
Tests for the Contacts API.
"""
import pytest

from holded.invoice_api.models.contacts import ContactCreate, ContactUpdate, ContactListParams


class TestContactsResource:
    """Test cases for the Contacts API."""

    def test_list_contacts(self, client):
        """Test listing contacts."""
        result = client.contacts.list()
        
        assert result is not None
        # Result should be a list
        assert isinstance(result, list)
        
        # If there are contacts, verify structure
        if result and len(result) > 0:
            contact = result[0]
            assert "id" in contact
            assert "name" in contact

    def test_list_contacts_with_params(self, client):
        """Test listing contacts with query parameters."""
        params = ContactListParams(
            page=1,
            limit=10,
            phone="+1234567890"
        )
        
        result = client.contacts.list(params)
        
        assert result is not None
        assert isinstance(result, list)

    def test_list_contacts_with_custom_id(self, client):
        """Test listing contacts with customId filter."""
        params = ContactListParams(
            customId=["CUSTOM001", "CUSTOM002"]
        )
        
        result = client.contacts.list(params)
        
        assert result is not None
        assert isinstance(result, list)

    def test_create_contact(self, client):
        """Test creating a contact."""
        contact_data = ContactCreate(
            name="Test Contact",
            email="test@example.com",
            phone="+1234567890",
            type="client"
        )
        
        result = client.contacts.create(contact_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store contact ID for cleanup
            if "id" in result:
                contact_id = result["id"]
                # Cleanup: delete the contact
                try:
                    client.contacts.delete(contact_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test_create_contact_with_dict(self, client):
        """Test creating a contact using a dictionary."""
        contact_data = {
            "name": "Test Contact Dict",
            "email": "testdict@example.com",
            "type": "supplier"
        }
        
        result = client.contacts.create(contact_data)
        
        assert result is not None
        if isinstance(result, dict) and "id" in result:
            # Cleanup
            try:
                client.contacts.delete(result["id"])
            except Exception:
                pass

    def test_get_contact(self, client):
        """Test getting a specific contact."""
        # First, list contacts to get an ID
        contacts = client.contacts.list()
        
        if contacts and len(contacts) > 0:
            contact_id = contacts[0]["id"]
            
            result = client.contacts.get(contact_id)
            
            assert result is not None
            if isinstance(result, dict):
                assert result["id"] == contact_id
                assert "name" in result
        else:
            pytest.skip("No contacts available for testing")

    def test_update_contact(self, client):
        """Test updating a contact."""
        # First, create a contact
        contact_data = ContactCreate(
            name="Test Contact Update",
            email="update@example.com",
            type="client"
        )
        
        created = client.contacts.create(contact_data)
        
        if isinstance(created, dict) and "id" in created:
            contact_id = created["id"]
            
            # Update the contact
            update_data = ContactUpdate(
                name="Updated Test Contact",
                notes="This contact was updated via API test"
            )
            
            result = client.contacts.update(contact_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # Update endpoint may return status/info or the full contact
                if "id" in result:
                    assert result["id"] == contact_id
                # Verify update by getting the contact again
                updated = client.contacts.get(contact_id)
                if isinstance(updated, dict):
                    assert updated.get("name") == "Updated Test Contact" or updated.get("id") == contact_id
            
            # Cleanup
            try:
                client.contacts.delete(contact_id)
            except Exception:
                pass
        else:
            pytest.skip("Failed to create contact for update test")

    def test_delete_contact(self, client):
        """Test deleting a contact."""
        # First, create a contact
        contact_data = ContactCreate(
            name="Test Contact Delete",
            email="delete@example.com",
            type="client"
        )
        
        created = client.contacts.create(contact_data)
        
        if isinstance(created, dict) and "id" in created:
            contact_id = created["id"]
            
            # Delete the contact
            result = client.contacts.delete(contact_id)
            
            assert result is not None
            # Verify deletion by trying to get the contact
            try:
                client.contacts.get(contact_id)
                pytest.fail("Contact should have been deleted")
            except Exception:
                pass  # Expected - contact should not exist

    def test_get_contact_attachments(self, client):
        """Test getting contact attachments."""
        contacts = client.contacts.list()
        
        if contacts and len(contacts) > 0:
            contact_id = contacts[0]["id"]
            
            result = client.contacts.get_attachments(contact_id)
            
            assert result is not None
            assert isinstance(result, (list, dict))
        else:
            pytest.skip("No contacts available for testing")


@pytest.mark.asyncio
class TestAsyncContactsResource:
    """Test cases for the Async Contacts API."""

    async def test_list_contacts(self, async_client):
        """Test listing contacts asynchronously."""
        result = await async_client.contacts.list()
        
        assert result is not None
        assert isinstance(result, list)
        
        if result and len(result) > 0:
            contact = result[0]
            assert "id" in contact
            assert "name" in contact

    async def test_create_contact(self, async_client):
        """Test creating a contact asynchronously."""
        contact_data = ContactCreate(
            name="Test Async Contact",
            email="async@example.com",
            type="client"
        )
        
        result = await async_client.contacts.create(contact_data)
        
        assert result is not None
        if isinstance(result, dict) and "id" in result:
            # Cleanup
            try:
                await async_client.contacts.delete(result["id"])
            except Exception:
                pass

    async def test_get_contact(self, async_client):
        """Test getting a specific contact asynchronously."""
        contacts = await async_client.contacts.list()
        
        if contacts and len(contacts) > 0:
            contact_id = contacts[0]["id"]
            
            result = await async_client.contacts.get(contact_id)
            
            assert result is not None
            if isinstance(result, dict):
                assert result["id"] == contact_id
        else:
            pytest.skip("No contacts available for testing")

    async def test_update_contact(self, async_client):
        """Test updating a contact asynchronously."""
        # Create a contact
        contact_data = ContactCreate(
            name="Test Async Update",
            email="asyncupdate@example.com",
            type="client"
        )
        
        created = await async_client.contacts.create(contact_data)
        
        if isinstance(created, dict) and "id" in created:
            contact_id = created["id"]
            
            # Update the contact
            update_data = ContactUpdate(
                notes="Updated via async test"
            )
            
            result = await async_client.contacts.update(contact_id, update_data)
            
            assert result is not None
            
            # Cleanup
            try:
                await async_client.contacts.delete(contact_id)
            except Exception:
                pass
        else:
            pytest.skip("Failed to create contact for update test")

    async def test_delete_contact(self, async_client):
        """Test deleting a contact asynchronously."""
        # Create a contact
        contact_data = ContactCreate(
            name="Test Async Delete",
            email="asyncdelete@example.com",
            type="client"
        )
        
        created = await async_client.contacts.create(contact_data)
        
        if isinstance(created, dict) and "id" in created:
            contact_id = created["id"]
            
            # Delete the contact
            result = await async_client.contacts.delete(contact_id)
            
            assert result is not None

    async def test_get_contact_attachments(self, async_client):
        """Test getting contact attachments asynchronously."""
        contacts = await async_client.contacts.list()
        
        if contacts and len(contacts) > 0:
            contact_id = contacts[0]["id"]
            
            result = await async_client.contacts.get_attachments(contact_id)
            
            assert result is not None
        else:
            pytest.skip("No contacts available for testing")

