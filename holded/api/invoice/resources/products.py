"""
Products resource for the Holded API.
"""

from typing import Any, Dict, List, Optional, Union

from ...resources import BaseResource
from ..models.products import ProductCreate, ProductListParams, ProductUpdate


class ProductsResource(BaseResource):
    """
    Resource for interacting with the Products API.
    """

    def __init__(self, client):
        """Initialize the products resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/products"

    def list(self, params: Optional[Union[Dict[str, Any], ProductListParams]] = None) -> List[Dict[str, Any]]:
        """
        List all products.

        Args:
            params: Optional query parameters.

        Returns:
            A list of products.
        """
        result = self.client.get(self.base_path, params=params)
        return result

    def create(self, data: Union[Dict[str, Any], ProductCreate]) -> Dict[str, Any]:
        """
        Create a new product.

        Args:
            data: Product data.

        Returns:
            The created product.
        """
        result = self.client.post(self.base_path, data=data)
        return result

    def get(self, product_id: str) -> Dict[str, Any]:
        """
        Get a specific product.

        Args:
            product_id: The product ID.

        Returns:
            The product.
        """
        result = self.client.get(f"{self.base_path}/{product_id}")
        return result

    def update(self, product_id: str, data: Union[Dict[str, Any], ProductUpdate]) -> Dict[str, Any]:
        """
        Update a product.

        Args:
            product_id: The product ID.
            data: Updated product data.

        Returns:
            The updated product.
        """
        result = self.client.put(f"{self.base_path}/{product_id}", data=data)
        return result

    def delete(self, product_id: str) -> Dict[str, Any]:
        """
        Delete a product.

        Args:
            product_id: The product ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"{self.base_path}/{product_id}")
        return result

    def get_main_image(self, product_id: str) -> bytes:
        """
        Get the main image for a product.

        Args:
            product_id: The product ID.

        Returns:
            The image bytes.
        """
        result = self.client.get(f"{self.base_path}/{product_id}/image")
        return result

    def list_images(self, product_id: str) -> List[Dict[str, Any]]:
        """
        List all images for a product.

        Args:
            product_id: The product ID.

        Returns:
            A list of product images.
        """
        result = self.client.get(f"{self.base_path}/{product_id}/images")
        return result

    def get_secondary_image(self, product_id: str, image_filename: str) -> bytes:
        """
        Get a secondary image for a product.

        Args:
            product_id: The product ID.
            image_filename: The image filename.

        Returns:
            The image bytes.
        """
        result = self.client.get(f"{self.base_path}/{product_id}/image/{image_filename}")
        return result

    def update_stock(self, product_id: str, stock: int) -> Dict[str, Any]:
        """
        Update product stock.

        Args:
            product_id: The product ID.
            stock: The new stock quantity.

        Returns:
            The updated product stock information.
        """
        result = self.client.put(f"{self.base_path}/{product_id}/stock", data={"stock": stock})
        return result

    def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all product categories.

        Args:
            params: Optional query parameters.

        Returns:
            A list of product categories.
        """
        result = self.client.get(f"{self.base_path}/categories", params=params)
        return result

    def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product category.

        Args:
            data: Category data.

        Returns:
            The created category.
        """
        result = self.client.post(f"{self.base_path}/categories", data=data)
        return result

    def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a product category.

        Args:
            category_id: The category ID.
            data: Updated category data.

        Returns:
            The updated category.
        """
        result = self.client.put(f"{self.base_path}/categories/{category_id}", data=data)
        return result

    def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a product category.

        Args:
            category_id: The category ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"{self.base_path}/categories/{category_id}")
        return result
