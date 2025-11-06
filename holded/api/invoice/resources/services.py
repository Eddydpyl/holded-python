"""
Resource for interacting with the Services API.
"""

from typing import Any, Dict, List, cast

from ...resources import BaseResource
from ..models.services import ServiceCreate, ServiceUpdate


class ServicesResource(BaseResource):
    """Resource for interacting with the Services API."""

    def __init__(self, client):
        """Initialize the services resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/services"

    def list(self) -> List[Dict[str, Any]]:
        """List all services.

        Returns:
            A list of services
        """
        return cast(List[Dict[str, Any]], self.client.get(self.base_path))

    def create(self, data: ServiceCreate) -> Dict[str, Any]:
        """Create a new service.

        Args:
            data: Service data

        Returns:
            The created service
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, service_id: str) -> Dict[str, Any]:
        """Get a specific service.

        Args:
            service_id: The service ID

        Returns:
            The service details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{service_id}"))

    def update(self, service_id: str, data: ServiceUpdate) -> Dict[str, Any]:
        """Update a service.

        Args:
            service_id: The service ID
            data: Updated service data

        Returns:
            The updated service
        """
        return cast(Dict[str, Any], self.client.put(f"{self.base_path}/{service_id}", data=data))

    def delete(self, service_id: str) -> Dict[str, Any]:
        """Delete a service.

        Args:
            service_id: The service ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{service_id}"))
