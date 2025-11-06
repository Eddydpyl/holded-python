"""
Resource for interacting with the Tasks API.
"""
from typing import Any, Dict, List, cast

from ..models.tasks import TaskCreate
from ...base_resources import BaseResource


class TasksResource(BaseResource):
    """Resource for interacting with the Tasks API."""

    def __init__(self, client):
        """Initialize the tasks resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "projects/tasks"

    def list(self) -> List[Dict[str, Any]]:
        """List all tasks.

        Returns:
            A list of tasks
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: TaskCreate) -> Dict[str, Any]:
        """Create a new task.

        Args:
            data: Task data

        Returns:
            The created task
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, task_id: str) -> Dict[str, Any]:
        """Get a specific task.

        Args:
            task_id: The task ID

        Returns:
            The task details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{task_id}"))

    def delete(self, task_id: str) -> Dict[str, Any]:
        """Delete a task.

        Args:
            task_id: The task ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{task_id}"))

