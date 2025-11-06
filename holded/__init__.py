"""
Holded API Wrapper.

A comprehensive Python wrapper for the Holded API, providing both synchronous and asynchronous clients.
"""

__version__ = "0.1.0"
__author__ = "BonifacioCalindoro"
__license__ = "MIT"

# Import main client classes for easier access
from .client import HoldedClient
from .async_client import AsyncHoldedClient

# Import exceptions
from .exceptions import (
    HoldedError,
    HoldedAPIError,
    HoldedAuthError,
    HoldedNotFoundError,
    HoldedValidationError,
    HoldedRateLimitError,
    HoldedServerError,
    HoldedTimeoutError,
    HoldedConnectionError,
)

# Import API modules for direct access
from . import accounting_api
from . import crm_api
from . import invoice_api
from . import projects_api
from . import team_api

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
    "accounting_api",
    "crm_api",
    "invoice_api",
    "projects_api",
    "team_api",
]
