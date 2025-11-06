"""
Asynchronous resource for interacting with the Projects API.
"""

from typing import Any, Dict, List, cast

from ...resources import AsyncBaseResource
from ..models.projects import ProjectCreate, ProjectUpdate


class AsyncProjectsResource(AsyncBaseResource):
    """Resource for interacting with the Projects API asynchronously."""

    def __init__(self, client):
        """Initialize the projects resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "projects/projects"

    async def list(self) -> List[Dict[str, Any]]:
        """List all projects asynchronously.

        Returns:
            A list of projects
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: ProjectCreate) -> Dict[str, Any]:
        """Create a new project asynchronously.

        Args:
            data: Project data

        Returns:
            The created project
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, project_id: str) -> Dict[str, Any]:
        """Get a specific project asynchronously.

        Args:
            project_id: The project ID

        Returns:
            The project details
        """
        result = await self.client.get(f"{self.base_path}/{project_id}")
        return cast(Dict[str, Any], result)

    async def update(self, project_id: str, data: ProjectUpdate) -> Dict[str, Any]:
        """Update a project asynchronously.

        Args:
            project_id: The project ID
            data: Updated project data

        Returns:
            The updated project
        """
        result = await self.client.put(f"{self.base_path}/{project_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, project_id: str) -> Dict[str, Any]:
        """Delete a project asynchronously.

        Args:
            project_id: The project ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{project_id}")
        return cast(Dict[str, Any], result)

    async def get_summary(self, project_id: str) -> Dict[str, Any]:
        """Get a project summary asynchronously.

        Args:
            project_id: The project ID

        Returns:
            The project summary
        """
        result = await self.client.get(f"{self.base_path}/{project_id}/summary")
        return cast(Dict[str, Any], result)
