"""
Holded API Wrapper.

A comprehensive Python wrapper for the Holded API, providing both synchronous and asynchronous clients.
"""

__version__ = "0.1.0"
__author__ = "BonifacioCalindoro"
__license__ = "MIT"

# Import main client classes for easier access
# Import API modules for direct access
from .api import accounting, crm, invoice, projects, team
from .async_client import AsyncHoldedClient
from .client import HoldedClient

# Import exceptions
from .exceptions import (
    HoldedAPIError,
    HoldedAuthError,
    HoldedConnectionError,
    HoldedError,
    HoldedNotFoundError,
    HoldedRateLimitError,
    HoldedServerError,
    HoldedTimeoutError,
    HoldedValidationError,
)

__all__ = [
    "HoldedClient",
    "AsyncHoldedClient",
    "HoldedError",
    "HoldedAPIError",
    "HoldedAuthError",
    "HoldedNotFoundError",
    "HoldedValidationError",
    "HoldedRateLimitError",
    "HoldedServerError",
    "HoldedTimeoutError",
    "HoldedConnectionError",
    "accounting",
    "crm",
    "invoice",
    "projects",
    "team",
]
