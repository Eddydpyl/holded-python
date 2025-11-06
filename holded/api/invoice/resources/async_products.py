"""
Asynchronous products resource for the Holded API.
"""

from typing import Any, Dict, List, Optional, Union, cast

from ...resources import AsyncBaseResource
from ..models.products import ProductCreate, ProductListParams, ProductUpdate


class AsyncProductsResource(AsyncBaseResource):
    """
    Resource for interacting with the Products API asynchronously.
    """

    def __init__(self, client):
        """Initialize the products resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/products"

    async def list(self, params: Optional[Union[Dict[str, Any], ProductListParams]] = None) -> List[Dict[str, Any]]:
        """
        List all products asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of products.
        """
        result = await self.client.get(self.base_path, params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Union[Dict[str, Any], ProductCreate]) -> Dict[str, Any]:
        """
        Create a new product asynchronously.

        Args:
            data: Product data.

        Returns:
            The created product.
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, product_id: str) -> Dict[str, Any]:
        """
        Get a specific product asynchronously.

        Args:
            product_id: The product ID.

        Returns:
            The product.
        """
        result = await self.client.get(f"{self.base_path}/{product_id}")
        return cast(Dict[str, Any], result)

    async def update(self, product_id: str, data: Union[Dict[str, Any], ProductUpdate]) -> Dict[str, Any]:
        """
        Update a product asynchronously.

        Args:
            product_id: The product ID.
            data: Updated product data.

        Returns:
            The updated product.
        """
        result = await self.client.put(f"{self.base_path}/{product_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, product_id: str) -> Dict[str, Any]:
        """
        Delete a product asynchronously.

        Args:
            product_id: The product ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/{product_id}")
        return cast(Dict[str, Any], result)

    async def get_main_image(self, product_id: str) -> bytes:
        """
        Get the main image for a product asynchronously.

        Args:
            product_id: The product ID.

        Returns:
            The image bytes.
        """
        result = await self.client.get(f"{self.base_path}/{product_id}/image")
        return result

    async def list_images(self, product_id: str) -> List[Dict[str, Any]]:
        """
        List all images for a product asynchronously.

        Args:
            product_id: The product ID.

        Returns:
            A list of product images.
        """
        result = await self.client.get(f"{self.base_path}/{product_id}/images")
        return cast(List[Dict[str, Any]], result)

    async def get_secondary_image(self, product_id: str, image_filename: str) -> bytes:
        """
        Get a secondary image for a product asynchronously.

        Args:
            product_id: The product ID.
            image_filename: The image filename.

        Returns:
            The image bytes.
        """
        result = await self.client.get(f"{self.base_path}/{product_id}/image/{image_filename}")
        return result

    async def update_stock(self, product_id: str, stock: int) -> Dict[str, Any]:
        """
        Update product stock asynchronously.

        Args:
            product_id: The product ID.
            stock: The new stock quantity.

        Returns:
            The updated product stock information.
        """
        result = await self.client.put(f"{self.base_path}/{product_id}/stock", data={"stock": stock})
        return cast(Dict[str, Any], result)

    async def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all product categories asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of product categories.
        """
        result = await self.client.get(f"{self.base_path}/categories", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product category asynchronously.

        Args:
            data: Category data.

        Returns:
            The created category.
        """
        result = await self.client.post(f"{self.base_path}/categories", data=data)
        return cast(Dict[str, Any], result)

    async def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a product category asynchronously.

        Args:
            category_id: The category ID.
            data: Updated category data.

        Returns:
            The updated category.
        """
        result = await self.client.put(f"{self.base_path}/categories/{category_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a product category asynchronously.

        Args:
            category_id: The category ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/categories/{category_id}")
        return cast(Dict[str, Any], result)
