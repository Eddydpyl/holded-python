"""
Resource for interacting with the Projects API.
"""

from typing import Any, Dict, List, cast

from ...resources import BaseResource
from ..models.projects import ProjectCreate, ProjectUpdate


class ProjectsResource(BaseResource):
    """Resource for interacting with the Projects API."""

    def __init__(self, client):
        """Initialize the projects resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "projects/projects"

    def list(self) -> List[Dict[str, Any]]:
        """List all projects.

        Returns:
            A list of projects
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: ProjectCreate) -> Dict[str, Any]:
        """Create a new project.

        Args:
            data: Project data

        Returns:
            The created project
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, project_id: str) -> Dict[str, Any]:
        """Get a specific project.

        Args:
            project_id: The project ID

        Returns:
            The project details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{project_id}"))

    def update(self, project_id: str, data: ProjectUpdate) -> Dict[str, Any]:
        """Update a project.

        Args:
            project_id: The project ID
            data: Updated project data

        Returns:
            The updated project
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{project_id}", data=data))

    def delete(self, project_id: str) -> Dict[str, Any]:
        """Delete a project.

        Args:
            project_id: The project ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{project_id}"))

    def get_summary(self, project_id: str) -> Dict[str, Any]:
        """Get a project summary.

        Args:
            project_id: The project ID

        Returns:
            The project summary
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{project_id}/summary"))
