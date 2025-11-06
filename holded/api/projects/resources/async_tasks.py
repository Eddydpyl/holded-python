"""
Asynchronous resource for interacting with the Tasks API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource
from ..models.tasks import TaskCreate


class AsyncTasksResource(AsyncBaseResource):
    """Resource for interacting with the Tasks API asynchronously."""

    def __init__(self, client):
        """Initialize the tasks resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "projects/tasks"

    async def list(self) -> List[Dict[str, Any]]:
        """List all tasks asynchronously.

        Returns:
            A list of tasks
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: TaskCreate) -> Dict[str, Any]:
        """Create a new task asynchronously.

        Args:
            data: Task data

        Returns:
            The created task
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, task_id: str) -> Dict[str, Any]:
        """Get a specific task asynchronously.

        Args:
            task_id: The task ID

        Returns:
            The task details
        """
        result = await self.client.get(f"{self.base_path}/{task_id}")
        return cast(Dict[str, Any], result)

    async def delete(self, task_id: str) -> Dict[str, Any]:
        """Delete a task asynchronously.

        Args:
            task_id: The task ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{task_id}")
        return cast(Dict[str, Any], result)
