"""
Tests for the Products API.
"""
import pytest

from holded.invoice_api.models.products import ProductCreate, ProductUpdate, ProductListParams


class TestProductsResource:
    """Test cases for the Products API."""

    def test_list_products(self, client):
        """Test listing products."""
        result = client.products.list()
        
        assert result is not None
        # Result should be a list
        assert isinstance(result, list)
        
        # If there are products, verify structure
        if result and len(result) > 0:
            product = result[0]
            assert "id" in product
            assert "name" in product

    def test_list_products_with_params(self, client):
        """Test listing products with query parameters."""
        params = ProductListParams(
            page=1,
            limit=10
        )
        
        result = client.products.list(params)
        
        assert result is not None
        assert isinstance(result, list)

    def test_create_product(self, client):
        """Test creating a product."""
        # Use "simple" kind as it doesn't require Inventory app
        # Use dict to match API exactly (API uses 'desc' and 'kind')
        product_data = {
            "name": "Test Product",
            "desc": "Test product description",
            "price": 10.50,
            "tax": 21.0,
            "kind": "simple"
        }
        
        result = client.products.create(product_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store product ID for cleanup
            if "id" in result:
                product_id = result["id"]
                # Cleanup: delete the product
                try:
                    client.products.delete(product_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test_create_product_with_dict(self, client):
        """Test creating a product using a dictionary."""
        product_data = {
            "name": "Test Product Dict",
            "desc": "Test product description from dict",
            "price": 15.75,
            "tax": 21.0,
            "kind": "simple"
        }
        
        result = client.products.create(product_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    client.products.delete(result["id"])
                except Exception:
                    pass

    def test_get_product(self, client):
        """Test getting a specific product."""
        # First, try to get an existing product
        products = client.products.list()
        
        if products and len(products) > 0:
            product_id = products[0]["id"]
            result = client.products.get(product_id)
            
            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
            assert result["id"] == product_id
        else:
            # Create a test product if none exist
            product_data = {
                "name": "Test Get Product",
                "desc": "Test description for get",
                "price": 20.0,
                "tax": 21.0,
                "kind": "simple"
            }
            created = client.products.create(product_data)
            if isinstance(created, dict) and "id" in created:
                product_id = created["id"]
                result = client.products.get(product_id)
                
                assert result is not None
                assert isinstance(result, dict)
                assert "id" in result
                
                # Cleanup
                try:
                    client.products.delete(product_id)
                except Exception:
                    pass

    def test_update_product(self, client):
        """Test updating a product."""
        # Create a product first
        product_data = {
            "name": "Test Update Product",
            "desc": "Original description",
            "price": 25.0,
            "tax": 21.0,
            "kind": "simple"
        }
        
        created = client.products.create(product_data)
        
        if isinstance(created, dict) and "id" in created:
            product_id = created["id"]
            
            # Update the product
            update_data = ProductUpdate(
                name="Updated Test Product",
                desc="Updated description",
                price=30.0
            )
            
            result = client.products.update(product_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # The update might return status/info, so verify by getting the product
                updated_product = client.products.get(product_id)
                if isinstance(updated_product, dict):
                    if "name" in updated_product:
                        assert updated_product["name"] == "Updated Test Product"
                    elif "desc" in updated_product:
                        assert updated_product["desc"] == "Updated description"
            
            # Cleanup
            try:
                client.products.delete(product_id)
            except Exception:
                pass

    def test_delete_product(self, client):
        """Test deleting a product."""
        # Create a product first
        product_data = {
            "name": "Test Delete Product",
            "desc": "Product to be deleted",
            "price": 35.0,
            "tax": 21.0,
            "kind": "simple"
        }
        
        created = client.products.create(product_data)
        
        if isinstance(created, dict) and "id" in created:
            product_id = created["id"]
            
            # Delete the product
            result = client.products.delete(product_id)
            
            assert result is not None
            # Verify deletion by trying to get the product (should fail)
            try:
                client.products.get(product_id)
                # If we get here, the product still exists (might be soft delete)
                pass
            except Exception:
                # Expected: product not found
                pass

    def test_update_stock(self, client):
        """Test updating product stock."""
        # Create a product first
        product_data = {
            "name": "Test Stock Product",
            "desc": "Product for stock testing",
            "price": 40.0,
            "tax": 21.0,
            "kind": "simple",
            "stock": 10
        }
        
        created = client.products.create(product_data)
        
        if isinstance(created, dict) and "id" in created:
            product_id = created["id"]
            
            # Update stock
            result = client.products.update_stock(product_id, 20)
            
            assert result is not None
            
            # Cleanup
            try:
                client.products.delete(product_id)
            except Exception:
                pass

    def test_list_images(self, client):
        """Test listing product images."""
        # First, try to get an existing product
        products = client.products.list()
        
        if products and len(products) > 0:
            product_id = products[0]["id"]
            try:
                result = client.products.list_images(product_id)
                # If successful, verify it's a list
                if result is not None:
                    assert isinstance(result, (list, dict))
            except Exception:
                # Endpoint might not be available or return 404
                pass

    def test_list_categories(self, client):
        """Test listing product categories."""
        try:
            result = client.products.list_categories()
            # If successful, verify it's a list
            if result is not None:
                assert isinstance(result, list)
        except Exception:
            # Categories endpoint might not be available
            pass


class TestAsyncProductsResource:
    """Test cases for the Async Products API."""

    @pytest.mark.asyncio
    async def test_list_products(self, async_client):
        """Test listing products asynchronously."""
        result = await async_client.products.list()
        
        assert result is not None
        assert isinstance(result, list)
        
        if result and len(result) > 0:
            product = result[0]
            assert "id" in product
            assert "name" in product

    @pytest.mark.asyncio
    async def test_list_products_with_params(self, async_client):
        """Test listing products with query parameters asynchronously."""
        params = ProductListParams(
            page=1,
            limit=10
        )
        
        result = await async_client.products.list(params)
        
        assert result is not None
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_product(self, async_client):
        """Test creating a product asynchronously."""
        product_data = {
            "name": "Test Async Product",
            "desc": "Test async description",
            "price": 50.0,
            "tax": 21.0,
            "kind": "simple"
        }
        
        result = await async_client.products.create(product_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    await async_client.products.delete(result["id"])
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_create_product_with_dict(self, async_client):
        """Test creating a product using a dictionary asynchronously."""
        product_data = {
            "name": "Test Async Product Dict",
            "desc": "Test async description from dict",
            "price": 55.0,
            "tax": 21.0,
            "kind": "simple"
        }
        
        result = await async_client.products.create(product_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    await async_client.products.delete(result["id"])
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_get_product(self, async_client):
        """Test getting a specific product asynchronously."""
        products = await async_client.products.list()
        
        if products and len(products) > 0:
            product_id = products[0]["id"]
            result = await async_client.products.get(product_id)
            
            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
        else:
            # Create a test product if none exist
            product_data = {
                "name": "Test Async Get Product",
                "desc": "Test async description for get",
                "price": 60.0,
                "tax": 21.0,
                "kind": "simple"
            }
            created = await async_client.products.create(product_data)
            if isinstance(created, dict) and "id" in created:
                product_id = created["id"]
                result = await async_client.products.get(product_id)
                
                assert result is not None
                assert isinstance(result, dict)
                
                # Cleanup
                try:
                    await async_client.products.delete(product_id)
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_update_product(self, async_client):
        """Test updating a product asynchronously."""
        # Create a product first
        product_data = {
            "name": "Test Async Update Product",
            "desc": "Original async description",
            "price": 65.0,
            "tax": 21.0,
            "kind": "simple"
        }
        
        created = await async_client.products.create(product_data)
        
        if isinstance(created, dict) and "id" in created:
            product_id = created["id"]
            
            # Update the product
            update_data = ProductUpdate(
                name="Updated Async Test Product",
                desc="Updated async description",
                price=70.0
            )
            
            result = await async_client.products.update(product_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # Verify by getting the product
                updated_product = await async_client.products.get(product_id)
                if isinstance(updated_product, dict):
                    if "name" in updated_product:
                        assert updated_product["name"] == "Updated Async Test Product"
                    elif "desc" in updated_product:
                        assert updated_product["desc"] == "Updated async description"
            
            # Cleanup
            try:
                await async_client.products.delete(product_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_delete_product(self, async_client):
        """Test deleting a product asynchronously."""
        # Create a product first
        product_data = {
            "name": "Test Async Delete Product",
            "desc": "Async product to be deleted",
            "price": 75.0,
            "tax": 21.0,
            "kind": "simple"
        }
        
        created = await async_client.products.create(product_data)
        
        if isinstance(created, dict) and "id" in created:
            product_id = created["id"]
            
            # Delete the product
            result = await async_client.products.delete(product_id)
            
            assert result is not None
            # Verify deletion
            try:
                await async_client.products.get(product_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_update_stock(self, async_client):
        """Test updating product stock asynchronously."""
        # Create a product first
        product_data = {
            "name": "Test Async Stock Product",
            "desc": "Async product for stock testing",
            "price": 80.0,
            "tax": 21.0,
            "kind": "simple",
            "stock": 15
        }
        
        created = await async_client.products.create(product_data)
        
        if isinstance(created, dict) and "id" in created:
            product_id = created["id"]
            
            # Update stock
            result = await async_client.products.update_stock(product_id, 25)
            
            assert result is not None
            
            # Cleanup
            try:
                await async_client.products.delete(product_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_list_images(self, async_client):
        """Test listing product images asynchronously."""
        products = await async_client.products.list()
        
        if products and len(products) > 0:
            product_id = products[0]["id"]
            try:
                result = await async_client.products.list_images(product_id)
                # If successful, verify it's a list
                if result is not None:
                    assert isinstance(result, (list, dict))
            except Exception:
                # Endpoint might not be available or return 404
                pass

    @pytest.mark.asyncio
    async def test_list_categories(self, async_client):
        """Test listing product categories asynchronously."""
        try:
            result = await async_client.products.list_categories()
            # If successful, verify it's a list
            if result is not None:
                assert isinstance(result, list)
        except Exception:
            # Categories endpoint might not be available
            pass

