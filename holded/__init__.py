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

# Import invoice API resources for direct access if needed
from .invoice_api.resources.contacts import ContactsResource
from .invoice_api.resources.documents import DocumentsResource
from .invoice_api.resources.products import ProductsResource
from .invoice_api.resources.treasury import TreasuryResource
from .invoice_api.resources.warehouse import WarehouseResource
from .invoice_api.resources.sales_channels import SalesChannelsResource
from .invoice_api.resources.numbering_series import NumberingSeriesResource
from .invoice_api.resources.expense_accounts import ExpenseAccountsResource
from .invoice_api.resources.remittances import RemittancesResource
from .invoice_api.resources.payments import PaymentsResource
from .invoice_api.resources.taxes import TaxesResource
from .invoice_api.resources.contact_groups import ContactGroupsResource
from .invoice_api.resources.services import ServicesResource

# Import async invoice API resources
from .invoice_api.resources.async_contacts import AsyncContactsResource
from .invoice_api.resources.async_documents import AsyncDocumentsResource
from .invoice_api.resources.async_products import AsyncProductsResource
from .invoice_api.resources.async_treasury import AsyncTreasuryResource
from .invoice_api.resources.async_warehouse import AsyncWarehouseResource
from .invoice_api.resources.async_sales_channels import AsyncSalesChannelsResource
from .invoice_api.resources.async_numbering_series import AsyncNumberingSeriesResource
from .invoice_api.resources.async_expense_accounts import AsyncExpenseAccountsResource
from .invoice_api.resources.async_remittances import AsyncRemittancesResource
from .invoice_api.resources.async_payments import AsyncPaymentsResource
from .invoice_api.resources.async_taxes import AsyncTaxesResource
from .invoice_api.resources.async_contact_groups import AsyncContactGroupsResource
from .invoice_api.resources.async_services import AsyncServicesResource

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
]