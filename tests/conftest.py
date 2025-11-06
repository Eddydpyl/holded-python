"""
Pytest configuration and fixtures for Holded API tests.
"""

import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def api_key() -> str:
    """
    Get the Holded API key from environment variable.

    Returns:
        The API key string.

    Raises:
        ValueError: If HOLDED_API_KEY is not set in environment.
    """
    api_key = os.getenv("HOLDED_API_KEY")
    if not api_key:
        raise ValueError(
            "HOLDED_API_KEY environment variable is not set. "
            "Please create a .env file with HOLDED_API_KEY=your_api_key"
        )
    return api_key


@pytest.fixture(scope="function")
def client(api_key: str) -> HoldedClient:
    """
    Create a Holded client instance for testing.

    Args:
        api_key: The API key to use.

    Yields:
        A HoldedClient instance.
    """
    client = HoldedClient(api_key=api_key)
    yield client
    client.close()


@pytest_asyncio.fixture(scope="function")
async def async_client(api_key: str) -> AsyncHoldedClient:
    """
    Create an async Holded client instance for testing.

    Args:
        api_key: The API key to use.

    Yields:
        An AsyncHoldedClient instance.
    """
    client = AsyncHoldedClient(api_key=api_key)
    yield client
    await client.close()
