"""
Asynchronous resource for interacting with the Payments API.
"""

from typing import Any, Dict, Optional, Union

from ..models.payments import PaymentCreate, PaymentListParams, PaymentListResponse, PaymentResponse, PaymentUpdate


class AsyncPaymentsResource:
    """Resource for interacting with the Payments API asynchronously."""

    def __init__(self, client):
        """Initialize the payments resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "invoicing/payments"

    async def list(self, params: Optional[Union[Dict[str, Any], PaymentListParams]] = None) -> PaymentListResponse:
        """List all payments asynchronously.

        Args:
            params: Optional query parameters (e.g., starttmp, endtmp, page, limit)

        Returns:
            A list of payments
        """
        return await self.client.get(self.base_path, params=params)

    async def create(self, data: Union[Dict[str, Any], PaymentCreate]) -> PaymentResponse:
        """Create a new payment asynchronously.

        Args:
            data: Payment data

        Returns:
            The created payment
        """
        return await self.client.post(self.base_path, data=data)

    async def get(self, payment_id: str) -> PaymentResponse:
        """Get a specific payment asynchronously.

        Args:
            payment_id: The payment ID

        Returns:
            The payment
        """
        return await self.client.get(f"{self.base_path}/{payment_id}")

    async def update(self, payment_id: str, data: Union[Dict[str, Any], PaymentUpdate]) -> PaymentResponse:
        """Update a payment asynchronously.

        Args:
            payment_id: The payment ID
            data: Updated payment data

        Returns:
            The updated payment
        """
        return await self.client.put(f"{self.base_path}/{payment_id}", data=data)

    async def delete(self, payment_id: str) -> Dict[str, Any]:
        """Delete a payment asynchronously.

        Args:
            payment_id: The payment ID

        Returns:
            A confirmation message
        """
        return await self.client.delete(f"{self.base_path}/{payment_id}")
