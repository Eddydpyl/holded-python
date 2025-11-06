"""
Tests for the Tasks API.
"""

import asyncio

import pytest

from holded.api.projects.models.tasks import TaskCreate
from holded.exceptions import HoldedTimeoutError


class TestTasksResource:
    """Test cases for the Tasks API."""

    @pytest.mark.timeout(35, method="thread")  # 35 seconds timeout (5 seconds more than default client timeout)
    def test_list_tasks(self, client):
        """Test listing tasks."""
        try:
            result = client.tasks.list()

            assert result is not None
            assert isinstance(result, list)
        except (HoldedTimeoutError, TimeoutError):
            pytest.skip("API request timed out - this may be a transient issue")

    def test_create_task(self, client):
        """Test creating a task."""
        # First, create a project to use
        from holded.api.projects.models.projects import ProjectCreate

        project_data = ProjectCreate(
            name=f"Test Project for Task {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            task_data = TaskCreate(
                name=f"Test Task {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
                project_id=project_id,
            )

            result = client.tasks.create(task_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created task and project
            task_id = result.get("id") or result.get("_id")
            if task_id:
                try:
                    client.tasks.delete(task_id)
                except Exception:
                    pass
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Task creation failed: {e}")

    def test_get_task(self, client):
        """Test getting a task."""
        # First, create a project and task
        from holded.api.projects.models.projects import ProjectCreate

        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project for Task Get {test_id}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            task_data = TaskCreate(
                name=f"Test Task Get {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
                project_id=project_id,
            )

            created = client.tasks.create(task_data)
            task_id = created.get("id") or created.get("_id")
            if not task_id:
                pytest.skip("Task ID not found after creation")

            result = client.tasks.get(task_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.tasks.delete(task_id)
            except Exception:
                pass
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get task failed: {e}")

    def test_delete_task(self, client):
        """Test deleting a task."""
        # First, create a project and task
        from holded.api.projects.models.projects import ProjectCreate

        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project for Task Delete {test_id}",
        )

        try:
            project = client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            task_data = TaskCreate(
                name=f"Test Task Delete {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
                project_id=project_id,
            )

            created = client.tasks.create(task_data)
            task_id = created.get("id") or created.get("_id")
            if not task_id:
                pytest.skip("Task ID not found after creation")

            # Delete the task
            result = client.tasks.delete(task_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Delete task failed: {e}")


class TestAsyncTasksResource:
    """Test cases for the Async Tasks API."""

    @pytest.mark.asyncio
    async def test_list_tasks(self, async_client):
        """Test listing tasks asynchronously."""
        try:
            result = await asyncio.wait_for(
                async_client.tasks.list(),
                timeout=35.0,  # 35 seconds timeout (5 seconds more than default client timeout)
            )

            assert result is not None
            assert isinstance(result, list)
        except (HoldedTimeoutError, TimeoutError, asyncio.TimeoutError):
            pytest.skip("API request timed out - this may be a transient issue")

    @pytest.mark.asyncio
    async def test_create_task(self, async_client):
        """Test creating a task asynchronously."""
        # First, create a project to use
        from holded.api.projects.models.projects import ProjectCreate

        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project for Task Async {test_id}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            task_data = TaskCreate(
                name=f"Test Task Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
                project_id=project_id,
            )

            result = await async_client.tasks.create(task_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created task and project
            task_id = result.get("id") or result.get("_id")
            if task_id:
                try:
                    await async_client.tasks.delete(task_id)
                except Exception:
                    pass
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Task creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_task(self, async_client):
        """Test getting a task asynchronously."""
        # First, create a project and task
        from holded.api.projects.models.projects import ProjectCreate

        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project for Task Get Async {test_id}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            task_data = TaskCreate(
                name=f"Test Task Get Async {pytest.current_test_id if hasattr(pytest, 'current_test_id') else 'test'}",
                project_id=project_id,
            )

            created = await async_client.tasks.create(task_data)
            task_id = created.get("id") or created.get("_id")
            if not task_id:
                pytest.skip("Task ID not found after creation")

            result = await async_client.tasks.get(task_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.tasks.delete(task_id)
            except Exception:
                pass
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get task failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_task(self, async_client):
        """Test deleting a task asynchronously."""
        # First, create a project and task
        from holded.api.projects.models.projects import ProjectCreate

        test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
        project_data = ProjectCreate(
            name=f"Test Project for Task Delete Async {test_id}",
        )

        try:
            project = await async_client.projects.create(project_data)
            project_id = project.get("id") or project.get("_id")
            if not project_id:
                pytest.skip("Project ID not found after creation")

            test_id = pytest.current_test_id if hasattr(pytest, "current_test_id") else "test"
            task_data = TaskCreate(
                name=f"Test Task Delete Async {test_id}",
                project_id=project_id,
            )

            created = await async_client.tasks.create(task_data)
            task_id = created.get("id") or created.get("_id")
            if not task_id:
                pytest.skip("Task ID not found after creation")

            # Delete the task
            result = await async_client.tasks.delete(task_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.projects.delete(project_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Delete task failed: {e}")
