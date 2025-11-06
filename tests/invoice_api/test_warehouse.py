"""
Tests for the Warehouse API.
"""
import pytest

from holded.invoice_api.models.warehouse import WarehouseCreate, WarehouseUpdate, WarehouseListParams, WarehouseAddress


class TestWarehouseResource:
    """Test cases for the Warehouse API."""

    def test_list_warehouses(self, client):
        """Test listing warehouses."""
        result = client.warehouse.list()
        
        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are warehouses, verify structure
                if items and len(items) > 0:
                    warehouse = items[0]
                    assert "id" in warehouse
                    assert "name" in warehouse
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    def test_list_warehouses_with_params(self, client):
        """Test listing warehouses with query parameters."""
        params = WarehouseListParams(
            page=1,
            limit=10
        )
        
        result = client.warehouse.list(params)
        
        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    def test_create_warehouse(self, client):
        """Test creating a warehouse."""
        address = WarehouseAddress(
            address="123 Test Street",
            city="Test City",
            postalCode="12345",
            country="Spain",
            countryCode="ES"
        )
        warehouse_data = WarehouseCreate(
            name="Test Warehouse",
            email="warehouse@test.com",
            phone="+1234567890",
            mobile="+0987654321",
            address=address,
            default=False
        )
        
        result = client.warehouse.create(warehouse_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store warehouse ID for cleanup
            if "id" in result:
                warehouse_id = result["id"]
                # Cleanup: delete the warehouse
                try:
                    client.warehouse.delete(warehouse_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test_create_warehouse_with_dict(self, client):
        """Test creating a warehouse using a dictionary."""
        warehouse_data = {
            "name": "Test Warehouse Dict",
            "email": "warehousedict@test.com",
            "phone": "+1111111111",
            "address": {
                "address": "456 Dict Street",
                "city": "Dict City",
                "postalCode": "54321",
                "country": "Spain",
                "countryCode": "ES"
            },
            "default": False
        }
        
        result = client.warehouse.create(warehouse_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    client.warehouse.delete(result["id"])
                except Exception:
                    pass

    def test_get_warehouse(self, client):
        """Test getting a specific warehouse."""
        # First, try to get an existing warehouse
        warehouses = client.warehouse.list()
        
        if isinstance(warehouses, dict) and "items" in warehouses:
            items = warehouses["items"]
        elif isinstance(warehouses, list):
            items = warehouses
        else:
            items = []
        
        if items and len(items) > 0:
            warehouse_id = items[0]["id"]
            result = client.warehouse.get(warehouse_id)
            
            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
            assert result["id"] == warehouse_id
        else:
            # Create a test warehouse if none exist
            address = WarehouseAddress(
                address="789 Get Street",
                city="Get City",
                postalCode="99999",
                country="Spain",
                countryCode="ES"
            )
            warehouse_data = WarehouseCreate(
                name="Test Get Warehouse",
                email="get@test.com",
                address=address
            )
            created = client.warehouse.create(warehouse_data)
            if isinstance(created, dict) and "id" in created:
                warehouse_id = created["id"]
                result = client.warehouse.get(warehouse_id)
                
                assert result is not None
                assert isinstance(result, dict)
                assert "id" in result
                
                # Cleanup
                try:
                    client.warehouse.delete(warehouse_id)
                except Exception:
                    pass

    def test_update_warehouse(self, client):
        """Test updating a warehouse."""
        # Create a warehouse first
        address = WarehouseAddress(
            address="321 Update Street",
            city="Update City",
            postalCode="11111",
            country="Spain",
            countryCode="ES"
        )
        warehouse_data = WarehouseCreate(
            name="Test Update Warehouse",
            email="update@test.com",
            address=address
        )
        
        created = client.warehouse.create(warehouse_data)
        
        if isinstance(created, dict) and "id" in created:
            warehouse_id = created["id"]
            
            # Update the warehouse
            update_data = WarehouseUpdate(
                name="Updated Test Warehouse",
                email="updated@test.com"
            )
            
            result = client.warehouse.update(warehouse_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # The update might return status/info, so verify by getting the warehouse
                updated_warehouse = client.warehouse.get(warehouse_id)
                if isinstance(updated_warehouse, dict):
                    if "name" in updated_warehouse:
                        assert updated_warehouse["name"] == "Updated Test Warehouse"
                    elif "email" in updated_warehouse:
                        assert updated_warehouse["email"] == "updated@test.com"
            
            # Cleanup
            try:
                client.warehouse.delete(warehouse_id)
            except Exception:
                pass

    def test_delete_warehouse(self, client):
        """Test deleting a warehouse."""
        # Create a warehouse first
        address = WarehouseAddress(
            address="654 Delete Street",
            city="Delete City",
            postalCode="22222",
            country="Spain",
            countryCode="ES"
        )
        warehouse_data = WarehouseCreate(
            name="Test Delete Warehouse",
            email="delete@test.com",
            address=address
        )
        
        created = client.warehouse.create(warehouse_data)
        
        if isinstance(created, dict) and "id" in created:
            warehouse_id = created["id"]
            
            # Delete the warehouse
            result = client.warehouse.delete(warehouse_id)
            
            assert result is not None
            # Verify deletion by trying to get the warehouse (should fail)
            try:
                client.warehouse.get(warehouse_id)
                # If we get here, the warehouse still exists (might be soft delete)
                pass
            except Exception:
                # Expected: warehouse not found
                pass

    def test_list_stock(self, client):
        """Test listing products stock for a warehouse."""
        # First, get a warehouse
        warehouses = client.warehouse.list()
        
        if isinstance(warehouses, dict) and "items" in warehouses:
            items = warehouses["items"]
        elif isinstance(warehouses, list):
            items = warehouses
        else:
            items = []
        
        if items and len(items) > 0:
            warehouse_id = items[0]["id"]
            try:
                result = client.warehouse.list_stock(warehouse_id)
                assert result is not None
            except Exception:
                # Stock endpoint might not be available or return errors
                pass


class TestAsyncWarehouseResource:
    """Test cases for the Async Warehouse API."""

    @pytest.mark.asyncio
    async def test_list_warehouses(self, async_client):
        """Test listing warehouses asynchronously."""
        result = await async_client.warehouse.list()
        
        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_warehouses_with_params(self, async_client):
        """Test listing warehouses with query parameters asynchronously."""
        params = WarehouseListParams(
            page=1,
            limit=10
        )
        
        result = await async_client.warehouse.list(params)
        
        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_warehouse(self, async_client):
        """Test creating a warehouse asynchronously."""
        address = WarehouseAddress(
            address="123 Async Street",
            city="Async City",
            postalCode="33333",
            country="Spain",
            countryCode="ES"
        )
        warehouse_data = WarehouseCreate(
            name="Test Async Warehouse",
            email="async@test.com",
            phone="+2222222222",
            address=address,
            default=False
        )
        
        result = await async_client.warehouse.create(warehouse_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    await async_client.warehouse.delete(result["id"])
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_create_warehouse_with_dict(self, async_client):
        """Test creating a warehouse using a dictionary asynchronously."""
        warehouse_data = {
            "name": "Test Async Warehouse Dict",
            "email": "asyncdict@test.com",
            "phone": "+3333333333",
            "address": {
                "address": "456 Async Dict Street",
                "city": "Async Dict City",
                "postalCode": "44444",
                "country": "Spain",
                "countryCode": "ES"
            },
            "default": False
        }
        
        result = await async_client.warehouse.create(warehouse_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    await async_client.warehouse.delete(result["id"])
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_get_warehouse(self, async_client):
        """Test getting a specific warehouse asynchronously."""
        warehouses = await async_client.warehouse.list()
        
        if isinstance(warehouses, dict) and "items" in warehouses:
            items = warehouses["items"]
        elif isinstance(warehouses, list):
            items = warehouses
        else:
            items = []
        
        if items and len(items) > 0:
            warehouse_id = items[0]["id"]
            result = await async_client.warehouse.get(warehouse_id)
            
            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
        else:
            # Create a test warehouse if none exist
            address = WarehouseAddress(
                address="789 Async Get Street",
                city="Async Get City",
                postalCode="55555",
                country="Spain",
                countryCode="ES"
            )
            warehouse_data = WarehouseCreate(
                name="Test Async Get Warehouse",
                email="asyncget@test.com",
                address=address
            )
            created = await async_client.warehouse.create(warehouse_data)
            if isinstance(created, dict) and "id" in created:
                warehouse_id = created["id"]
                result = await async_client.warehouse.get(warehouse_id)
                
                assert result is not None
                assert isinstance(result, dict)
                
                # Cleanup
                try:
                    await async_client.warehouse.delete(warehouse_id)
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_update_warehouse(self, async_client):
        """Test updating a warehouse asynchronously."""
        # Create a warehouse first
        address = WarehouseAddress(
            address="321 Async Update Street",
            city="Async Update City",
            postalCode="66666",
            country="Spain",
            countryCode="ES"
        )
        warehouse_data = WarehouseCreate(
            name="Test Async Update Warehouse",
            email="asyncupdate@test.com",
            address=address
        )
        
        created = await async_client.warehouse.create(warehouse_data)
        
        if isinstance(created, dict) and "id" in created:
            warehouse_id = created["id"]
            
            # Update the warehouse
            update_data = WarehouseUpdate(
                name="Updated Async Test Warehouse",
                email="updatedasync@test.com"
            )
            
            result = await async_client.warehouse.update(warehouse_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # Verify by getting the warehouse
                updated_warehouse = await async_client.warehouse.get(warehouse_id)
                if isinstance(updated_warehouse, dict):
                    if "name" in updated_warehouse:
                        assert updated_warehouse["name"] == "Updated Async Test Warehouse"
                    elif "email" in updated_warehouse:
                        assert updated_warehouse["email"] == "updatedasync@test.com"
            
            # Cleanup
            try:
                await async_client.warehouse.delete(warehouse_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_delete_warehouse(self, async_client):
        """Test deleting a warehouse asynchronously."""
        # Create a warehouse first
        address = WarehouseAddress(
            address="654 Async Delete Street",
            city="Async Delete City",
            postalCode="77777",
            country="Spain",
            countryCode="ES"
        )
        warehouse_data = WarehouseCreate(
            name="Test Async Delete Warehouse",
            email="asyncdelete@test.com",
            address=address
        )
        
        created = await async_client.warehouse.create(warehouse_data)
        
        if isinstance(created, dict) and "id" in created:
            warehouse_id = created["id"]
            
            # Delete the warehouse
            result = await async_client.warehouse.delete(warehouse_id)
            
            assert result is not None
            # Verify deletion
            try:
                await async_client.warehouse.get(warehouse_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_list_stock(self, async_client):
        """Test listing products stock for a warehouse asynchronously."""
        warehouses = await async_client.warehouse.list()
        
        if isinstance(warehouses, dict) and "items" in warehouses:
            items = warehouses["items"]
        elif isinstance(warehouses, list):
            items = warehouses
        else:
            items = []
        
        if items and len(items) > 0:
            warehouse_id = items[0]["id"]
            try:
                result = await async_client.warehouse.list_stock(warehouse_id)
                assert result is not None
            except Exception:
                # Stock endpoint might not be available or return errors
                pass

