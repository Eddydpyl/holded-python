"""
Asynchronous resource for interacting with the Warehouse API.
"""
from typing import Any, Dict, Optional, Union

from ..models.warehouse import (
    WarehouseCreate, WarehouseUpdate, WarehouseListParams,
    WarehouseResponse, WarehouseListResponse
)


class AsyncWarehouseResource:
    """Resource for interacting with the Warehouse API asynchronously."""

    def __init__(self, client):
        """Initialize the warehouse resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/warehouses"

    async def list(self, params: Optional[Union[Dict[str, Any], WarehouseListParams]] = None) -> WarehouseListResponse:
        """List all warehouses asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of warehouses
        """
        return await self.client.get(self.base_path, params=params)

    async def create(self, data: Union[Dict[str, Any], WarehouseCreate]) -> WarehouseResponse:
        """Create a new warehouse asynchronously.

        Args:
            data: Warehouse data

        Returns:
            The created warehouse
        """
        return await self.client.post(self.base_path, data=data)

    async def get(self, warehouse_id: str) -> WarehouseResponse:
        """Get a specific warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID

        Returns:
            The warehouse
        """
        return await self.client.get(f"{self.base_path}/{warehouse_id}")

    async def update(self, warehouse_id: str, data: Union[Dict[str, Any], WarehouseUpdate]) -> WarehouseResponse:
        """Update a warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID
            data: Updated warehouse data

        Returns:
            The updated warehouse
        """
        return await self.client.put(f"{self.base_path}/{warehouse_id}", data=data)

    async def delete(self, warehouse_id: str) -> Dict[str, Any]:
        """Delete a warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID

        Returns:
            A confirmation message
        """
        return await self.client.delete(f"{self.base_path}/{warehouse_id}")

    async def list_stock(self, warehouse_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List products stock for a specific warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID
            params: Optional query parameters

        Returns:
            Stock information for products in the warehouse
        """
        return await self.client.get(f"{self.base_path}/{warehouse_id}/stock", params=params)
