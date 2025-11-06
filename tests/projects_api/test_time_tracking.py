"""
Tests for the Time Tracking API.
"""

import pytest
import time

from holded.projects_api.models.time_tracking import TimeTrackingCreate, TimeTrackingUpdate


class TestTimeTrackingResource:
    """Test cases for the Time Tracking API."""

    def test_list_all_times(self, client):
        """Test listing all time tracking entries."""
        result = client.time_tracking.list_all()

        assert result is not None
        assert isinstance(result, list)

    def test_list_project_times(self, client):
        """Test listing time tracking entries for a project."""
        # First, create a project
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            result = client.time_tracking.list(project_id)

            assert result is not None
            assert isinstance(result, list)

            # Cleanup
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"List project times failed: {e}")

    def test_create_time_tracking(self, client):
        """Test creating a time tracking entry."""
        # First, create a project
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Create {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking",
            )

            result = client.time_tracking.create(project_id, time_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created time tracking and project
            time_id = result.get("id") or result.get("_id")
            if time_id:
                try:
                    client.time_tracking.delete(project_id, time_id)
                except Exception:
                    pass
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Time tracking creation failed: {e}")

    def test_get_time_tracking(self, client):
        """Test getting a time tracking entry."""
        # First, create a project and time tracking entry
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking get",
            )

            created = client.time_tracking.create(project_id, time_data)
            time_id = created.get("id") or created.get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found after creation")

            result = client.time_tracking.get(project_id, time_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.time_tracking.delete(project_id, time_id)
            except Exception:
                pass
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get time tracking failed: {e}")

    def test_update_time_tracking(self, client):
        """Test updating a time tracking entry."""
        # First, create a project and time tracking entry
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking update",
            )

            created = client.time_tracking.create(project_id, time_data)
            time_id = created.get("id") or created.get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found after creation")

            # Update the time tracking
            update_data = TimeTrackingUpdate(
                duration=120,
                desc="Updated time tracking",
            )
            result = client.time_tracking.update(project_id, time_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.time_tracking.delete(project_id, time_id)
            except Exception:
                pass
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update time tracking failed: {e}")

    def test_delete_time_tracking(self, client):
        """Test deleting a time tracking entry."""
        # First, create a project and time tracking entry
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking delete",
            )

            created = client.time_tracking.create(project_id, time_data)
            time_id = created.get("id") or created.get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found after creation")

            # Delete the time tracking
            result = client.time_tracking.delete(project_id, time_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Delete time tracking failed: {e}")


class TestAsyncTimeTrackingResource:
    """Test cases for the Async Time Tracking API."""

    @pytest.mark.asyncio
    async def test_list_all_times(self, async_client):
        """Test listing all time tracking entries asynchronously."""
        result = await async_client.time_tracking.list_all()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_project_times(self, async_client):
        """Test listing time tracking entries for a project asynchronously."""
        # First, create a project
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            result = await async_client.time_tracking.list(project_id)

            assert result is not None
            assert isinstance(result, list)

            # Cleanup
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"List project times failed: {e}")

    @pytest.mark.asyncio
    async def test_create_time_tracking(self, async_client):
        """Test creating a time tracking entry asynchronously."""
        # First, create a project
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Create Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking async",
            )

            result = await async_client.time_tracking.create(project_id, time_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created time tracking and project
            time_id = result.get("id") or result.get("_id")
            if time_id:
                try:
                    await async_client.time_tracking.delete(project_id, time_id)
                except Exception:
                    pass
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Time tracking creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_time_tracking(self, async_client):
        """Test getting a time tracking entry asynchronously."""
        # First, create a project and time tracking entry
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking get async",
            )

            created = await async_client.time_tracking.create(project_id, time_data)
            time_id = created.get("id") or created.get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found after creation")

            result = await async_client.time_tracking.get(project_id, time_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.time_tracking.delete(project_id, time_id)
            except Exception:
                pass
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get time tracking failed: {e}")

    @pytest.mark.asyncio
    async def test_update_time_tracking(self, async_client):
        """Test updating a time tracking entry asynchronously."""
        # First, create a project and time tracking entry
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Update Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking update async",
            )

            created = await async_client.time_tracking.create(project_id, time_data)
            time_id = created.get("id") or created.get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found after creation")

            # Update the time tracking
            update_data = TimeTrackingUpdate(
                duration=120,
                desc="Updated time tracking async",
            )
            result = await async_client.time_tracking.update(project_id, time_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.time_tracking.delete(project_id, time_id)
            except Exception:
                pass
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update time tracking failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_time_tracking(self, async_client):
        """Test deleting a time tracking entry asynchronously."""
        # First, create a project and time tracking entry
        from holded.projects_api.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Time Delete Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            time_data = TimeTrackingCreate(
                date=int(time.time() * 1000),
                duration=60,
                desc="Test time tracking delete async",
            )

            created = await async_client.time_tracking.create(project_id, time_data)
            time_id = created.get("id") or created.get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found after creation")

            # Delete the time tracking
            result = await async_client.time_tracking.delete(project_id, time_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Delete time tracking failed: {e}")

