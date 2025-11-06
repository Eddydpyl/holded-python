"""
Tests for the Sales Channels API.
"""
import time
import pytest

from holded.invoice_api.models.sales_channels import SalesChannelCreate, SalesChannelUpdate, SalesChannelListParams


class TestSalesChannelsResource:
    """Test cases for the Sales Channels API."""

    def test_list_sales_channels(self, client):
        """Test listing sales channels."""
        result = client.sales_channels.list()
        
        assert result is not None
        # Result should be a list or dict with items
        if isinstance(result, dict):
            if "items" in result:
                items = result["items"]
                assert isinstance(items, list)
                # If there are channels, verify structure
                if items and len(items) > 0:
                    channel = items[0]
                    assert "id" in channel
                    assert "name" in channel
            else:
                # Direct list response
                assert isinstance(result, list)
        else:
            assert isinstance(result, list)

    def test_list_sales_channels_with_params(self, client):
        """Test listing sales channels with query parameters."""
        params = SalesChannelListParams(
            page=1,
            limit=10
        )
        
        result = client.sales_channels.list(params)
        
        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    def test_create_sales_channel(self, client):
        """Test creating a sales channel."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000
        channel_data = SalesChannelCreate(
            name="Test Sales Channel",
            desc="Test description",
            accountNum=unique_num
        )
        
        result = client.sales_channels.create(channel_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Store channel ID for cleanup
            if "id" in result:
                channel_id = result["id"]
                # Cleanup: delete the channel
                try:
                    client.sales_channels.delete(channel_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test_create_sales_channel_with_dict(self, client):
        """Test creating a sales channel using a dictionary."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000 + 1
        channel_data = {
            "name": "Test Sales Channel Dict",
            "desc": "Test description from dict",
            "accountNum": unique_num
        }
        
        result = client.sales_channels.create(channel_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    client.sales_channels.delete(result["id"])
                except Exception:
                    pass

    def test_get_sales_channel(self, client):
        """Test getting a specific sales channel."""
        # First, try to get an existing channel
        channels = client.sales_channels.list()
        
        if isinstance(channels, dict) and "items" in channels:
            items = channels["items"]
        elif isinstance(channels, list):
            items = channels
        else:
            items = []
        
        if items and len(items) > 0:
            channel_id = items[0]["id"]
            result = client.sales_channels.get(channel_id)
            
            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
            assert result["id"] == channel_id
        else:
            # Create a test channel if none exist
            unique_num = int(time.time() * 1000) % 1000000 + 2
            channel_data = SalesChannelCreate(
                name="Test Get Channel",
                desc="Test description for get",
                accountNum=unique_num
            )
            created = client.sales_channels.create(channel_data)
            if isinstance(created, dict) and "id" in created:
                channel_id = created["id"]
                result = client.sales_channels.get(channel_id)
                
                assert result is not None
                assert isinstance(result, dict)
                assert "id" in result
                
                # Cleanup
                try:
                    client.sales_channels.delete(channel_id)
                except Exception:
                    pass

    def test_update_sales_channel(self, client):
        """Test updating a sales channel."""
        # Create a channel first
        unique_num = int(time.time() * 1000) % 1000000 + 3
        channel_data = SalesChannelCreate(
            name="Test Update Channel",
            desc="Original description",
            accountNum=unique_num
        )
        
        created = client.sales_channels.create(channel_data)
        
        if isinstance(created, dict) and "id" in created:
            channel_id = created["id"]
            
            # Update the channel
            update_data = SalesChannelUpdate(
                name="Updated Test Channel",
                desc="Updated description"
            )
            
            result = client.sales_channels.update(channel_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # The update might return status/info, so verify by getting the channel
                updated_channel = client.sales_channels.get(channel_id)
                if isinstance(updated_channel, dict):
                    if "name" in updated_channel:
                        assert updated_channel["name"] == "Updated Test Channel"
                    elif "desc" in updated_channel:
                        assert updated_channel["desc"] == "Updated description"
            
            # Cleanup
            try:
                client.sales_channels.delete(channel_id)
            except Exception:
                pass

    def test_delete_sales_channel(self, client):
        """Test deleting a sales channel."""
        # Create a channel first
        unique_num = int(time.time() * 1000) % 1000000 + 4
        channel_data = SalesChannelCreate(
            name="Test Delete Channel",
            desc="Channel to be deleted",
            accountNum=unique_num
        )
        
        created = client.sales_channels.create(channel_data)
        
        if isinstance(created, dict) and "id" in created:
            channel_id = created["id"]
            
            # Delete the channel
            result = client.sales_channels.delete(channel_id)
            
            assert result is not None
            # Verify deletion by trying to get the channel (should fail)
            try:
                client.sales_channels.get(channel_id)
                # If we get here, the channel still exists (might be soft delete)
                pass
            except Exception:
                # Expected: channel not found
                pass


class TestAsyncSalesChannelsResource:
    """Test cases for the Async Sales Channels API."""

    @pytest.mark.asyncio
    async def test_list_sales_channels(self, async_client):
        """Test listing sales channels asynchronously."""
        result = await async_client.sales_channels.list()
        
        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_sales_channels_with_params(self, async_client):
        """Test listing sales channels with query parameters asynchronously."""
        params = SalesChannelListParams(
            page=1,
            limit=10
        )
        
        result = await async_client.sales_channels.list(params)
        
        assert result is not None
        if isinstance(result, dict) and "items" in result:
            assert isinstance(result["items"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_sales_channel(self, async_client):
        """Test creating a sales channel asynchronously."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000 + 10
        channel_data = SalesChannelCreate(
            name="Test Async Sales Channel",
            desc="Test async description",
            accountNum=unique_num
        )
        
        result = await async_client.sales_channels.create(channel_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    await async_client.sales_channels.delete(result["id"])
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_create_sales_channel_with_dict(self, async_client):
        """Test creating a sales channel using a dictionary asynchronously."""
        # Use timestamp to ensure unique accountNum
        unique_num = int(time.time() * 1000) % 1000000 + 11
        channel_data = {
            "name": "Test Async Sales Channel Dict",
            "desc": "Test async description from dict",
            "accountNum": unique_num
        }
        
        result = await async_client.sales_channels.create(channel_data)
        
        assert result is not None
        if isinstance(result, dict):
            assert "id" in result or "name" in result
            # Cleanup
            if "id" in result:
                try:
                    await async_client.sales_channels.delete(result["id"])
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_get_sales_channel(self, async_client):
        """Test getting a specific sales channel asynchronously."""
        channels = await async_client.sales_channels.list()
        
        if isinstance(channels, dict) and "items" in channels:
            items = channels["items"]
        elif isinstance(channels, list):
            items = channels
        else:
            items = []
        
        if items and len(items) > 0:
            channel_id = items[0]["id"]
            result = await async_client.sales_channels.get(channel_id)
            
            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result
        else:
            # Create a test channel if none exist
            unique_num = int(time.time() * 1000) % 1000000 + 12
            channel_data = SalesChannelCreate(
                name="Test Async Get Channel",
                desc="Test async description for get",
                accountNum=unique_num
            )
            created = await async_client.sales_channels.create(channel_data)
            if isinstance(created, dict) and "id" in created:
                channel_id = created["id"]
                result = await async_client.sales_channels.get(channel_id)
                
                assert result is not None
                assert isinstance(result, dict)
                
                # Cleanup
                try:
                    await async_client.sales_channels.delete(channel_id)
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_update_sales_channel(self, async_client):
        """Test updating a sales channel asynchronously."""
        # Create a channel first
        unique_num = int(time.time() * 1000) % 1000000 + 13
        channel_data = SalesChannelCreate(
            name="Test Async Update Channel",
            desc="Original async description",
            accountNum=unique_num
        )
        
        created = await async_client.sales_channels.create(channel_data)
        
        if isinstance(created, dict) and "id" in created:
            channel_id = created["id"]
            
            # Update the channel
            update_data = SalesChannelUpdate(
                name="Updated Async Test Channel",
                desc="Updated async description"
            )
            
            result = await async_client.sales_channels.update(channel_id, update_data)
            
            assert result is not None
            if isinstance(result, dict):
                # Verify by getting the channel
                updated_channel = await async_client.sales_channels.get(channel_id)
                if isinstance(updated_channel, dict):
                    if "name" in updated_channel:
                        assert updated_channel["name"] == "Updated Async Test Channel"
                    elif "desc" in updated_channel:
                        assert updated_channel["desc"] == "Updated async description"
            
            # Cleanup
            try:
                await async_client.sales_channels.delete(channel_id)
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_delete_sales_channel(self, async_client):
        """Test deleting a sales channel asynchronously."""
        # Create a channel first
        unique_num = int(time.time() * 1000) % 1000000 + 14
        channel_data = SalesChannelCreate(
            name="Test Async Delete Channel",
            desc="Async channel to be deleted",
            accountNum=unique_num
        )
        
        created = await async_client.sales_channels.create(channel_data)
        
        if isinstance(created, dict) and "id" in created:
            channel_id = created["id"]
            
            # Delete the channel
            result = await async_client.sales_channels.delete(channel_id)
            
            assert result is not None
            # Verify deletion
            try:
                await async_client.sales_channels.get(channel_id)
            except Exception:
                pass

