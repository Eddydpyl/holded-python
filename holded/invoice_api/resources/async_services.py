"""
Asynchronous resource for interacting with the Services API.
"""
from typing import Any, Dict, List, cast

from ..models.services import ServiceCreate, ServiceUpdate
from ...base_resources import AsyncBaseResource


class AsyncServicesResource(AsyncBaseResource):
    """Resource for interacting with the Services API asynchronously."""

    def __init__(self, client):
        """Initialize the services resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/services"

    async def list(self) -> List[Dict[str, Any]]:
        """List all services asynchronously.

        Returns:
            A list of services
        """
        result = await self.client.get(self.base_path)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: ServiceCreate) -> Dict[str, Any]:
        """Create a new service asynchronously.

        Args:
            data: Service data

        Returns:
            The created service
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, service_id: str) -> Dict[str, Any]:
        """Get a specific service asynchronously.

        Args:
            service_id: The service ID

        Returns:
            The service details
        """
        result = await self.client.get(f"{self.base_path}/{service_id}")
        return cast(Dict[str, Any], result)

    async def update(self, service_id: str, data: ServiceUpdate) -> Dict[str, Any]:
        """Update a service asynchronously.

        Args:
            service_id: The service ID
            data: Updated service data

        Returns:
            The updated service
        """
        result = await self.client.put(f"{self.base_path}/{service_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, service_id: str) -> Dict[str, Any]:
        """Delete a service asynchronously.

        Args:
            service_id: The service ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{service_id}")
        return cast(Dict[str, Any], result)

