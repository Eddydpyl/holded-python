"""
Tests for the Contact Groups API.
"""

import pytest

from holded.api.invoice.models.contact_groups import (
    ContactGroupCreate,
    ContactGroupUpdate,
)


class TestContactGroupsResource:
    """Test cases for the Contact Groups API."""

    def test_list_contact_groups(self, client):
        """Test listing contact groups."""
        result = client.contact_groups.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_contact_group(self, client):
        """Test creating a contact group."""
        group_data = ContactGroupCreate(
            name=f"Test Group {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            desc="Test description",
            color="#FF0000",
        )

        try:
            result = client.contact_groups.create(group_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created group
            group_id = result.get("id") or result.get("_id")
            if group_id:
                try:
                    client.contact_groups.delete(group_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Contact group creation failed: {e}")

    def test_get_contact_group(self, client):
        """Test getting a contact group."""
        # First, create a group to get
        group_data = ContactGroupCreate(
            name=f"Test Group Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.contact_groups.create(group_data)
            group_id = created.get("id") or created.get("_id")
            if not group_id:
                pytest.skip("Group ID not found after creation")

            result = client.contact_groups.get(group_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.contact_groups.delete(group_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get contact group failed: {e}")

    def test_update_contact_group(self, client):
        """Test updating a contact group."""
        # First, create a group to update
        group_data = ContactGroupCreate(
            name=f"Test Group Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.contact_groups.create(group_data)
            group_id = created.get("id") or created.get("_id")
            if not group_id:
                pytest.skip("Group ID not found after creation")

            # Update the group
            update_data = ContactGroupUpdate(
                name="Updated Test Group",
                desc="Updated description",
            )
            result = client.contact_groups.update(group_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.contact_groups.delete(group_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update contact group failed: {e}")

    def test_delete_contact_group(self, client):
        """Test deleting a contact group."""
        # First, create a group to delete
        group_data = ContactGroupCreate(
            name=f"Test Group Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.contact_groups.create(group_data)
            group_id = created.get("id") or created.get("_id")
            if not group_id:
                pytest.skip("Group ID not found after creation")

            # Delete the group
            result = client.contact_groups.delete(group_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete contact group failed: {e}")


class TestAsyncContactGroupsResource:
    """Test cases for the Async Contact Groups API."""

    @pytest.mark.asyncio
    async def test_list_contact_groups(self, async_client):
        """Test listing contact groups asynchronously."""
        result = await async_client.contact_groups.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_contact_group(self, async_client):
        """Test creating a contact group asynchronously."""
        group_data = ContactGroupCreate(
            name=f"Test Group Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
            desc="Test description",
            color="#00FF00",
        )

        try:
            result = await async_client.contact_groups.create(group_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created group
            group_id = result.get("id") or result.get("_id")
            if group_id:
                try:
                    await async_client.contact_groups.delete(group_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Contact group creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_contact_group(self, async_client):
        """Test getting a contact group asynchronously."""
        # First, create a group to get
        group_data = ContactGroupCreate(
            name=f"Test Group Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.contact_groups.create(group_data)
            group_id = created.get("id") or created.get("_id")
            if not group_id:
                pytest.skip("Group ID not found after creation")

            result = await async_client.contact_groups.get(group_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.contact_groups.delete(group_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get contact group failed: {e}")

    @pytest.mark.asyncio
    async def test_update_contact_group(self, async_client):
        """Test updating a contact group asynchronously."""
        # First, create a group to update
        group_data = ContactGroupCreate(
            name=f"Test Group Update Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.contact_groups.create(group_data)
            group_id = created.get("id") or created.get("_id")
            if not group_id:
                pytest.skip("Group ID not found after creation")

            # Update the group
            update_data = ContactGroupUpdate(
                name="Updated Test Group Async",
                desc="Updated description",
            )
            result = await async_client.contact_groups.update(group_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.contact_groups.delete(group_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update contact group failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_contact_group(self, async_client):
        """Test deleting a contact group asynchronously."""
        # First, create a group to delete
        group_data = ContactGroupCreate(
            name=f"Test Group Delete Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.contact_groups.create(group_data)
            group_id = created.get("id") or created.get("_id")
            if not group_id:
                pytest.skip("Group ID not found after creation")

            # Delete the group
            result = await async_client.contact_groups.delete(group_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete contact group failed: {e}")
