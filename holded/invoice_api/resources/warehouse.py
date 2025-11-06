"""
Resource for interacting with the Warehouse API.
"""
from typing import Any, Dict, Optional, Union

from ..models.warehouse import (
    WarehouseCreate, WarehouseUpdate, WarehouseListParams,
    WarehouseResponse, WarehouseListResponse
)


class WarehouseResource:
    """Resource for interacting with the Warehouse API."""

    def __init__(self, client):
        """Initialize the warehouse resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/warehouses"

    def list(self, params: Optional[Union[Dict[str, Any], WarehouseListParams]] = None) -> WarehouseListResponse:
        """List all warehouses.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of warehouses
        """
        return self.client.get(self.base_path, params=params)

    def create(self, data: Union[Dict[str, Any], WarehouseCreate]) -> WarehouseResponse:
        """Create a new warehouse.

        Args:
            data: Warehouse data

        Returns:
            The created warehouse
        """
        return self.client.post(self.base_path, data=data)

    def get(self, warehouse_id: str) -> WarehouseResponse:
        """Get a specific warehouse.

        Args:
            warehouse_id: The warehouse ID

        Returns:
            The warehouse
        """
        return self.client.get(f"{self.base_path}/{warehouse_id}")

    def update(self, warehouse_id: str, data: Union[Dict[str, Any], WarehouseUpdate]) -> WarehouseResponse:
        """Update a warehouse.

        Args:
            warehouse_id: The warehouse ID
            data: Updated warehouse data

        Returns:
            The updated warehouse
        """
        return self.client.put(f"{self.base_path}/{warehouse_id}", data=data)

    def delete(self, warehouse_id: str) -> Dict[str, Any]:
        """Delete a warehouse.

        Args:
            warehouse_id: The warehouse ID

        Returns:
            A confirmation message
        """
        return self.client.delete(f"{self.base_path}/{warehouse_id}")

    def list_stock(self, warehouse_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """List products stock for a specific warehouse.

        Args:
            warehouse_id: The warehouse ID
            params: Optional query parameters

        Returns:
            Stock information for products in the warehouse
        """
        return self.client.get(f"{self.base_path}/{warehouse_id}/stock", params=params)
