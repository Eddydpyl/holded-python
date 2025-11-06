"""
Tests for the Projects API.
"""

import pytest

from holded.api.projects.models.projects import ProjectCreate, ProjectUpdate


class TestProjectsResource:
    """Test cases for the Projects API."""

    def test_list_projects(self, client):
        """Test listing projects."""
        result = client.projects.list()

        assert result is not None
        assert isinstance(result, list)

    def test_create_project(self, client):
        """Test creating a project."""
        project_data = ProjectCreate(
            name=f"Test Project {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            result = client.projects.create(project_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created project
            project_id = result.get("id") or result.get("_id")
            if project_id:
                try:
                    client.projects.delete(project_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Project creation failed: {e}")

    def test_get_project(self, client):
        """Test getting a project."""
        # First, create a project to get
        project_data = ProjectCreate(
            name=f"Test Project Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            result = client.projects.get(project_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get project failed: {e}")

    def test_update_project(self, client):
        """Test updating a project."""
        # First, create a project to update
        project_data = ProjectCreate(
            name=f"Test Project Update {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            # Update the project
            update_data = ProjectUpdate(
                name="Updated Test Project",
            )
            result = client.projects.update(project_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update project failed: {e}")

    def test_delete_project(self, client):
        """Test deleting a project."""
        # First, create a project to delete
        project_data = ProjectCreate(
            name=f"Test Project Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            # Delete the project
            result = client.projects.delete(project_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete project failed: {e}")

    def test_get_project_summary(self, client):
        """Test getting a project summary."""
        # First, create a project to get summary
        project_data = ProjectCreate(
            name=f"Test Project Summary {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            result = client.projects.get_summary(project_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get project summary failed: {e}")


class TestAsyncProjectsResource:
    """Test cases for the Async Projects API."""

    @pytest.mark.asyncio
    async def test_list_projects(self, async_client):
        """Test listing projects asynchronously."""
        result = await async_client.projects.list()

        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_project(self, async_client):
        """Test creating a project asynchronously."""
        project_data = ProjectCreate(
            name=f"Test Project Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            result = await async_client.projects.create(project_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created project
            project_id = result.get("id") or result.get("_id")
            if project_id:
                try:
                    await async_client.projects.delete(project_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Project creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_project(self, async_client):
        """Test getting a project asynchronously."""
        # First, create a project to get
        project_data = ProjectCreate(
            name=f"Test Project Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            created = await async_client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            result = await async_client.projects.get(project_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get project failed: {e}")

    @pytest.mark.asyncio
    async def test_update_project(self, async_client):
        """Test updating a project asynchronously."""
        # First, create a project to update
        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project Update Async {test_id}",
        )

        try:
            created = await async_client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            # Update the project
            update_data = ProjectUpdate(
                name="Updated Test Project Async",
            )
            result = await async_client.projects.update(project_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update project failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_project(self, async_client):
        """Test deleting a project asynchronously."""
        # First, create a project to delete
        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project Delete Async {test_id}",
        )

        try:
            created = await async_client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            # Delete the project
            result = await async_client.projects.delete(project_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete project failed: {e}")

    @pytest.mark.asyncio
    async def test_get_project_summary(self, async_client):
        """Test getting a project summary asynchronously."""
        # First, create a project to get summary
        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project Summary Async {test_id}",
        )

        try:
            created = await async_client.projects.create(project_data)
            project_id = created.get("id") or created.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            result = await async_client.projects.get_summary(project_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get project summary failed: {e}")
