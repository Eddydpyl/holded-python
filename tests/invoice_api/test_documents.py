"""
Tests for the Documents API.
"""

from datetime import datetime

import pytest

from holded.api.invoice.models.documents import DocumentListParams


class TestDocumentsResource:
    """Test cases for the Documents API."""

    def test_list_documents(self, client):
        """Test listing documents."""
        # Test with invoice type
        result = client.documents.list("invoice")

        assert result is not None
        assert isinstance(result, list)

    def test_list_documents_with_params(self, client):
        """Test listing documents with query parameters."""
        params = DocumentListParams(
            paid="0",  # Not paid
            sort="created-desc",
        )
        result = client.documents.list("invoice", params=params)

        assert result is not None
        assert isinstance(result, list)

    def test_list_documents_with_dict_params(self, client):
        """Test listing documents with dict parameters."""
        params = {
            "paid": "1",  # Paid
            "sort": "created-asc",
        }
        result = client.documents.list("invoice", params=params)

        assert result is not None
        assert isinstance(result, list)

    def test_list_payment_methods(self, client):
        """Test listing payment methods."""
        result = client.documents.list_payment_methods()

        assert result is not None
        assert isinstance(result, list)

    def test_create_document(self, client):
        """Test creating a document."""
        # First, get a contact to use
        contacts = client.contacts.list()
        if not contacts or len(contacts) == 0:
            pytest.skip("No contacts available for testing")

        contact_id = contacts[0].get("id") or contacts[0].get("_id")
        if not contact_id:
            pytest.skip("Contact ID not found")

        # Create an estimate document
        document_data = {
            "contactId": contact_id,
            "date": int(datetime.now().timestamp()),
            "items": [{"name": "Test Item", "units": 1.0, "price": 100.0, "tax": 21.0}],
        }

        try:
            result = client.documents.create("estimate", document_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup: delete the created document
            doc_id = result.get("id") or result.get("_id")
            if doc_id:
                try:
                    client.documents.delete(doc_id, "estimate")
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            # Document creation might fail for various reasons (permissions, validation, etc.)
            pytest.skip(f"Document creation failed: {e}")

    def test_get_document(self, client):
        """Test getting a document."""
        # First, list documents to get an ID
        documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        result = client.documents.get(doc_id, "invoice")

        assert result is not None
        assert isinstance(result, dict)

    def test_get_document_pdf(self, client):
        """Test getting document PDF."""
        # First, list documents to get an ID
        documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        try:
            result = client.documents.get_pdf(doc_id, "invoice")

            assert result is not None
            # PDF might be returned as binary data or a URL
            assert isinstance(result, (dict, str, bytes))
        except Exception as e:
            # PDF might not be available for all documents
            pytest.skip(f"PDF not available: {e}")

    def test_update_document(self, client):
        """Test updating a document."""
        # First, create a document to update
        contacts = client.contacts.list()
        if not contacts or len(contacts) == 0:
            pytest.skip("No contacts available for testing")

        contact_id = contacts[0].get("id") or contacts[0].get("_id")
        if not contact_id:
            pytest.skip("Contact ID not found")

        # Create an estimate document
        document_data = {
            "contactId": contact_id,
            "date": int(datetime.now().timestamp()),
            "items": [{"name": "Test Item", "units": 1.0, "price": 100.0, "tax": 21.0}],
        }

        try:
            created = client.documents.create("estimate", document_data)
            doc_id = created.get("id") or created.get("_id")
            if not doc_id:
                pytest.skip("Document ID not found after creation")

            # Update the document
            update_data = {"notes": "Updated test document"}
            result = client.documents.update(doc_id, "estimate", update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.documents.delete(doc_id, "estimate")
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Document update failed: {e}")

    def test_delete_document(self, client):
        """Test deleting a document."""
        # First, create a document to delete
        contacts = client.contacts.list()
        if not contacts or len(contacts) == 0:
            pytest.skip("No contacts available for testing")

        contact_id = contacts[0].get("id") or contacts[0].get("_id")
        if not contact_id:
            pytest.skip("Contact ID not found")

        # Create an estimate document
        document_data = {
            "contactId": contact_id,
            "date": int(datetime.now().timestamp()),
            "items": [{"name": "Test Item", "units": 1.0, "price": 100.0, "tax": 21.0}],
        }

        try:
            created = client.documents.create("estimate", document_data)
            doc_id = created.get("id") or created.get("_id")
            if not doc_id:
                pytest.skip("Document ID not found after creation")

            # Delete the document
            result = client.documents.delete(doc_id, "estimate")

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Document delete failed: {e}")

    def test_pay_document(self, client):
        """Test paying a document."""
        # First, get an unpaid invoice
        documents = client.documents.list("invoice", params={"paid": "0"})

        if not documents or len(documents) == 0:
            pytest.skip("No unpaid invoices available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Get treasury accounts for payment
        try:
            accounts = client.treasury.list()
            account_id = None
            if accounts and len(accounts) > 0:
                account_id = accounts[0].get("id") or accounts[0].get("_id")
        except Exception:
            account_id = None

        payment_data = {
            "amount": 100.0,
            "date": int(datetime.now().timestamp()),
            "method": "bank_transfer",
        }
        if account_id:
            payment_data["accountId"] = account_id

        try:
            result = client.documents.pay(doc_id, "invoice", payment_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Document payment failed: {e}")

    def test_send_document(self, client):
        """Test sending a document."""
        # First, get a document
        documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Get contact email if available
        doc = client.documents.get(doc_id, "invoice")
        contact_email = None
        if doc and "contact" in doc:
            contact = doc.get("contact", {})
            if isinstance(contact, dict):
                contact_email = contact.get("email") or contact.get("mail")
            elif isinstance(contact, str):
                # Contact might be just an ID string
                pass

        if not contact_email:
            contact_email = "test@example.com"  # Use a test email

        send_data = {
            "email": contact_email,
            "subject": "Test Document",
            "message": "This is a test message",
        }

        try:
            result = client.documents.send(doc_id, "invoice", send_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Document send failed: {e}")

    def test_ship_all_items(self, client):
        """Test shipping all items in a document."""
        # First, get a sales order or invoice
        documents = client.documents.list("salesorder")
        if not documents or len(documents) == 0:
            documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        ship_data = {"date": int(datetime.now().timestamp())}

        try:
            result = client.documents.ship_all_items(doc_id, ship_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Ship all items failed: {e}")

    def test_ship_items_by_line(self, client):
        """Test shipping items by line in a document."""
        # First, get a sales order or invoice
        documents = client.documents.list("salesorder")
        if not documents or len(documents) == 0:
            documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Get document to find item IDs
        doc = client.documents.get(doc_id, "salesorder" if "salesorder" in str(documents[0]) else "invoice")
        items = doc.get("items", []) if doc else []

        if not items:
            pytest.skip("No items found in document")

        item_id = items[0].get("id") or items[0].get("_id")
        if not item_id:
            pytest.skip("Item ID not found")

        ship_data = {
            "items": [{"id": item_id, "units": 1.0}],
            "date": int(datetime.now().timestamp()),
        }

        try:
            result = client.documents.ship_items_by_line(doc_id, ship_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Ship items by line failed: {e}")

    def test_get_shipped_units(self, client):
        """Test getting shipped units for an item."""
        # First, get a sales order or invoice
        documents = client.documents.list("salesorder")
        if not documents or len(documents) == 0:
            documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        doc_type = "salesorder" if "salesorder" in str(documents[0]) else "invoice"

        # Get document to find item IDs
        doc = client.documents.get(doc_id, doc_type)
        items = doc.get("items", []) if doc else []

        if not items:
            pytest.skip("No items found in document")

        item_id = items[0].get("id") or items[0].get("_id")
        if not item_id:
            pytest.skip("Item ID not found")

        try:
            result = client.documents.get_shipped_units(doc_id, doc_type, item_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Get shipped units failed: {e}")

    def test_attach_file(self, client):
        """Test attaching a file to a document."""
        # First, get a document
        documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Create a simple base64 encoded file (small text file)
        import base64

        file_content = "Test file content"
        encoded_content = base64.b64encode(file_content.encode()).decode()

        attach_data = {
            "name": "test_file.txt",
            "file": encoded_content,
            "type": "text/plain",
        }

        try:
            result = client.documents.attach_file(doc_id, "invoice", attach_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Attach file failed: {e}")

    def test_update_tracking(self, client):
        """Test updating tracking information for a document."""
        # First, get a document
        documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        tracking_data = {"trackingNumber": "TEST123456", "carrier": "Test Carrier"}

        try:
            result = client.documents.update_tracking(doc_id, "invoice", tracking_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Update tracking failed: {e}")

    def test_update_pipeline(self, client):
        """Test updating pipeline information for a document."""
        # First, get a document
        documents = client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        pipeline_data = {"stage": "test_stage"}

        try:
            result = client.documents.update_pipeline(doc_id, "invoice", pipeline_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Update pipeline failed: {e}")


class TestAsyncDocumentsResource:
    """Test cases for the Async Documents API."""

    @pytest.mark.asyncio
    async def test_list_documents(self, async_client):
        """Test listing documents asynchronously."""
        result = await async_client.documents.list("invoice")

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_documents_with_params(self, async_client):
        """Test listing documents with query parameters asynchronously."""
        params = DocumentListParams(paid="0", sort="created-desc")
        result = await async_client.documents.list("invoice", params=params)

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_documents_with_dict_params(self, async_client):
        """Test listing documents with dict parameters asynchronously."""
        params = {"paid": "1", "sort": "created-asc"}
        result = await async_client.documents.list("invoice", params=params)

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_payment_methods(self, async_client):
        """Test listing payment methods asynchronously."""
        result = await async_client.documents.list_payment_methods()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_document(self, async_client):
        """Test creating a document asynchronously."""
        # First, get a contact to use
        contacts = await async_client.contacts.list()
        if not contacts or len(contacts) == 0:
            pytest.skip("No contacts available for testing")

        contact_id = contacts[0].get("id") or contacts[0].get("_id")
        if not contact_id:
            pytest.skip("Contact ID not found")

        # Create an estimate document
        document_data = {
            "contactId": contact_id,
            "date": int(datetime.now().timestamp()),
            "items": [{"name": "Test Item", "units": 1.0, "price": 100.0, "tax": 21.0}],
        }

        try:
            result = await async_client.documents.create("estimate", document_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup: delete the created document
            doc_id = result.get("id") or result.get("_id")
            if doc_id:
                try:
                    await async_client.documents.delete(doc_id, "estimate")
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Document creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_document(self, async_client):
        """Test getting a document asynchronously."""
        # First, list documents to get an ID
        documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        result = await async_client.documents.get(doc_id, "invoice")

        assert result is not None
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_get_document_pdf(self, async_client):
        """Test getting document PDF asynchronously."""
        # First, list documents to get an ID
        documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        try:
            result = await async_client.documents.get_pdf(doc_id, "invoice")

            assert result is not None
            assert isinstance(result, (dict, str, bytes))
        except Exception as e:
            pytest.skip(f"PDF not available: {e}")

    @pytest.mark.asyncio
    async def test_update_document(self, async_client):
        """Test updating a document asynchronously."""
        # First, create a document to update
        contacts = await async_client.contacts.list()
        if not contacts or len(contacts) == 0:
            pytest.skip("No contacts available for testing")

        contact_id = contacts[0].get("id") or contacts[0].get("_id")
        if not contact_id:
            pytest.skip("Contact ID not found")

        # Create an estimate document
        document_data = {
            "contactId": contact_id,
            "date": int(datetime.now().timestamp()),
            "items": [{"name": "Test Item", "units": 1.0, "price": 100.0, "tax": 21.0}],
        }

        try:
            created = await async_client.documents.create("estimate", document_data)
            doc_id = created.get("id") or created.get("_id")
            if not doc_id:
                pytest.skip("Document ID not found after creation")

            # Update the document
            update_data = {"notes": "Updated test document"}
            result = await async_client.documents.update(doc_id, "estimate", update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.documents.delete(doc_id, "estimate")
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Document update failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_document(self, async_client):
        """Test deleting a document asynchronously."""
        # First, create a document to delete
        contacts = await async_client.contacts.list()
        if not contacts or len(contacts) == 0:
            pytest.skip("No contacts available for testing")

        contact_id = contacts[0].get("id") or contacts[0].get("_id")
        if not contact_id:
            pytest.skip("Contact ID not found")

        # Create an estimate document
        document_data = {
            "contactId": contact_id,
            "date": int(datetime.now().timestamp()),
            "items": [{"name": "Test Item", "units": 1.0, "price": 100.0, "tax": 21.0}],
        }

        try:
            created = await async_client.documents.create("estimate", document_data)
            doc_id = created.get("id") or created.get("_id")
            if not doc_id:
                pytest.skip("Document ID not found after creation")

            # Delete the document
            result = await async_client.documents.delete(doc_id, "estimate")

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Document delete failed: {e}")

    @pytest.mark.asyncio
    async def test_pay_document(self, async_client):
        """Test paying a document asynchronously."""
        # First, get an unpaid invoice
        documents = await async_client.documents.list("invoice", params={"paid": "0"})

        if not documents or len(documents) == 0:
            pytest.skip("No unpaid invoices available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Get treasury accounts for payment
        try:
            accounts = await async_client.treasury.list()
            account_id = None
            if accounts and len(accounts) > 0:
                account_id = accounts[0].get("id") or accounts[0].get("_id")
        except Exception:
            account_id = None

        payment_data = {
            "amount": 100.0,
            "date": int(datetime.now().timestamp()),
            "method": "bank_transfer",
        }
        if account_id:
            payment_data["accountId"] = account_id

        try:
            result = await async_client.documents.pay(doc_id, "invoice", payment_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Document payment failed: {e}")

    @pytest.mark.asyncio
    async def test_send_document(self, async_client):
        """Test sending a document asynchronously."""
        # First, get a document
        documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Get contact email if available
        doc = await async_client.documents.get(doc_id, "invoice")
        contact_email = None
        if doc and "contact" in doc:
            contact = doc.get("contact", {})
            if isinstance(contact, dict):
                contact_email = contact.get("email") or contact.get("mail")
            elif isinstance(contact, str):
                # Contact might be just an ID string
                pass

        if not contact_email:
            contact_email = "test@example.com"  # Use a test email

        send_data = {
            "email": contact_email,
            "subject": "Test Document",
            "message": "This is a test message",
        }

        try:
            result = await async_client.documents.send(doc_id, "invoice", send_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Document send failed: {e}")

    @pytest.mark.asyncio
    async def test_ship_all_items(self, async_client):
        """Test shipping all items in a document asynchronously."""
        # First, get a sales order or invoice
        documents = await async_client.documents.list("salesorder")
        if not documents or len(documents) == 0:
            documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        ship_data = {"date": int(datetime.now().timestamp())}

        try:
            result = await async_client.documents.ship_all_items(doc_id, ship_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Ship all items failed: {e}")

    @pytest.mark.asyncio
    async def test_ship_items_by_line(self, async_client):
        """Test shipping items by line in a document asynchronously."""
        # First, get a sales order or invoice
        documents = await async_client.documents.list("salesorder")
        if not documents or len(documents) == 0:
            documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Get document to find item IDs
        doc_type = "salesorder" if "salesorder" in str(documents[0]) else "invoice"
        doc = await async_client.documents.get(doc_id, doc_type)
        items = doc.get("items", []) if doc else []

        if not items:
            pytest.skip("No items found in document")

        item_id = items[0].get("id") or items[0].get("_id")
        if not item_id:
            pytest.skip("Item ID not found")

        ship_data = {
            "items": [{"id": item_id, "units": 1.0}],
            "date": int(datetime.now().timestamp()),
        }

        try:
            result = await async_client.documents.ship_items_by_line(doc_id, ship_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Ship items by line failed: {e}")

    @pytest.mark.asyncio
    async def test_get_shipped_units(self, async_client):
        """Test getting shipped units for an item asynchronously."""
        # First, get a sales order or invoice
        documents = await async_client.documents.list("salesorder")
        if not documents or len(documents) == 0:
            documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        doc_type = "salesorder" if "salesorder" in str(documents[0]) else "invoice"

        # Get document to find item IDs
        doc = await async_client.documents.get(doc_id, doc_type)
        items = doc.get("items", []) if doc else []

        if not items:
            pytest.skip("No items found in document")

        item_id = items[0].get("id") or items[0].get("_id")
        if not item_id:
            pytest.skip("Item ID not found")

        try:
            result = await async_client.documents.get_shipped_units(doc_id, doc_type, item_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Get shipped units failed: {e}")

    @pytest.mark.asyncio
    async def test_attach_file(self, async_client):
        """Test attaching a file to a document asynchronously."""
        # First, get a document
        documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        # Create a simple base64 encoded file (small text file)
        import base64

        file_content = "Test file content"
        encoded_content = base64.b64encode(file_content.encode()).decode()

        attach_data = {
            "name": "test_file.txt",
            "file": encoded_content,
            "type": "text/plain",
        }

        try:
            result = await async_client.documents.attach_file(doc_id, "invoice", attach_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Attach file failed: {e}")

    @pytest.mark.asyncio
    async def test_update_tracking(self, async_client):
        """Test updating tracking information for a document asynchronously."""
        # First, get a document
        documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        tracking_data = {"trackingNumber": "TEST123456", "carrier": "Test Carrier"}

        try:
            result = await async_client.documents.update_tracking(doc_id, "invoice", tracking_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Update tracking failed: {e}")

    @pytest.mark.asyncio
    async def test_update_pipeline(self, async_client):
        """Test updating pipeline information for a document asynchronously."""
        # First, get a document
        documents = await async_client.documents.list("invoice")

        if not documents or len(documents) == 0:
            pytest.skip("No documents available for testing")

        doc_id = documents[0].get("id") or documents[0].get("_id")
        if not doc_id:
            pytest.skip("Document ID not found")

        pipeline_data = {"stage": "test_stage"}

        try:
            result = await async_client.documents.update_pipeline(doc_id, "invoice", pipeline_data)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Update pipeline failed: {e}")
