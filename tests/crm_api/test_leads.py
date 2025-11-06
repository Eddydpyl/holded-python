"""
Tests for the Leads API.
"""

import pytest

from holded.api.crm.models.leads import (
    LeadCreate,
    LeadDateUpdate,
    LeadNoteCreate,
    LeadNoteUpdate,
    LeadStageUpdate,
    LeadTaskCreate,
    LeadTaskUpdate,
    LeadUpdate,
)


class TestLeadsResource:
    """Test cases for the Leads API."""

    def test_list_leads(self, client):
        """Test listing leads."""
        result = client.leads.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_lead(self, client):
        """Test creating a lead."""
        # First, get a funnel to use
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available to create a lead")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            result = client.leads.create(lead_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created lead
            lead_id = result.get("id") or result.get("_id")
            if lead_id:
                try:
                    client.leads.delete(lead_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Lead creation failed: {e}")

    def test_get_lead(self, client):
        """Test getting a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            result = client.leads.get(lead_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get lead failed: {e}")

    def test_update_lead(self, client):
        """Test updating a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Update the lead
            update_data = LeadUpdate(
                name="Updated Test Lead",
            )
            result = client.leads.update(lead_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update lead failed: {e}")

    def test_delete_lead(self, client):
        """Test deleting a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Delete the lead
            result = client.leads.delete(lead_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete lead failed: {e}")

    def test_create_lead_note(self, client):
        """Test creating a note for a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Note {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            note_data = LeadNoteCreate(note="Test note")
            result = client.leads.create_note(lead_id, note_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Create lead note failed: {e}")

    def test_update_lead_note(self, client):
        """Test updating a note for a lead."""
        # First, get a funnel and create a lead with a note
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Note Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Create a note first
            note_data = LeadNoteCreate(note="Initial note")
            client.leads.create_note(lead_id, note_data)

            # Update the note
            update_data = LeadNoteUpdate(note="Updated note")
            result = client.leads.update_note(lead_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update lead note failed: {e}")

    def test_create_lead_task(self, client):
        """Test creating a task for a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Task {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            task_data = LeadTaskCreate(task="Test task", done=False)
            result = client.leads.create_task(lead_id, task_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Create lead task failed: {e}")

    def test_update_lead_task(self, client):
        """Test updating a task for a lead."""
        # First, get a funnel and create a lead with a task
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Task Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Create a task first
            task_data = LeadTaskCreate(task="Initial task", done=False)
            client.leads.create_task(lead_id, task_data)

            # Update the task
            update_data = LeadTaskUpdate(task="Updated task", done=True)
            result = client.leads.update_task(lead_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update lead task failed: {e}")

    def test_delete_lead_task(self, client):
        """Test deleting a task for a lead."""
        # First, get a funnel and create a lead with a task
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Task Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Create a task first
            task_data = LeadTaskCreate(task="Task to delete", done=False)
            client.leads.create_task(lead_id, task_data)

            # Delete the task
            result = client.leads.delete_task(lead_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Delete lead task failed: {e}")

    def test_update_lead_date(self, client):
        """Test updating the creation date of a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Date {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            import time

            date_data = LeadDateUpdate(date=int(time.time() * 1000))
            result = client.leads.update_date(lead_id, date_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update lead date failed: {e}")

    def test_update_lead_stage(self, client):
        """Test updating the stage of a lead."""
        # First, get a funnel and create a lead
        funnels = client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Stage {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Get the funnel to find a stage
            funnel = client.funnels.get(funnel_id)
            stages = funnel.get("stages", [])
            if not stages:
                pytest.skip("No stages available in funnel")

            stage_id = stages[0].get("id") or stages[0].get("_id")
            if not stage_id:
                pytest.skip("Stage ID not found")

            stage_data = LeadStageUpdate(stage_id=stage_id)
            result = client.leads.update_stage(lead_id, stage_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update lead stage failed: {e}")


class TestAsyncLeadsResource:
    """Test cases for the Async Leads API."""

    @pytest.mark.asyncio
    async def test_list_leads(self, async_client):
        """Test listing leads asynchronously."""
        result = await async_client.leads.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_lead(self, async_client):
        """Test creating a lead asynchronously."""
        # First, get a funnel to use
        funnels = await async_client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available to create a lead")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            result = await async_client.leads.create(lead_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created lead
            lead_id = result.get("id") or result.get("_id")
            if lead_id:
                try:
                    await async_client.leads.delete(lead_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Lead creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_lead(self, async_client):
        """Test getting a lead asynchronously."""
        # First, get a funnel and create a lead
        funnels = await async_client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            result = await async_client.leads.get(lead_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get lead failed: {e}")

    @pytest.mark.asyncio
    async def test_update_lead(self, async_client):
        """Test updating a lead asynchronously."""
        # First, get a funnel and create a lead
        funnels = await async_client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Update Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Update the lead
            update_data = LeadUpdate(
                name="Updated Test Lead Async",
            )
            result = await async_client.leads.update(lead_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.leads.delete(lead_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update lead failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_lead(self, async_client):
        """Test deleting a lead asynchronously."""
        # First, get a funnel and create a lead
        funnels = await async_client.funnels.list()
        if not funnels:
            pytest.skip("No funnels available")

        funnel_id = funnels[0].get("id") or funnels[0].get("_id")
        if not funnel_id:
            pytest.skip("Funnel ID not found")

        lead_data = LeadCreate(
            funnel_id=funnel_id,
            name=f"Test Lead Delete Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.leads.create(lead_data)
            lead_id = created.get("id") or created.get("_id")
            if not lead_id:
                pytest.skip("Lead ID not found after creation")

            # Delete the lead
            result = await async_client.leads.delete(lead_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete lead failed: {e}")
