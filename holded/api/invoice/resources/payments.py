"""
Resource for interacting with the Payments API.
"""

from typing import Any, Dict, Optional, Union

from ..models.payments import PaymentCreate, PaymentListParams, PaymentListResponse, PaymentResponse, PaymentUpdate


class PaymentsResource:
    """Resource for interacting with the Payments API."""

    def __init__(self, client):
        """Initialize the payments resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/payments"

    def list(self, params: Optional[Union[Dict[str, Any], PaymentListParams]] = None) -> PaymentListResponse:
        """List all payments.

        Args:
            params: Optional query parameters (e.g., starttmp, endtmp, page, limit)

        Returns:
            A list of payments
        """
        return self.client.get(self.base_path, params=params)

    def create(self, data: Union[Dict[str, Any], PaymentCreate]) -> PaymentResponse:
        """Create a new payment.

        Args:
            data: Payment data

        Returns:
            The created payment
        """
        return self.client.post(self.base_path, data=data)

    def get(self, payment_id: str) -> PaymentResponse:
        """Get a specific payment.

        Args:
            payment_id: The payment ID

        Returns:
            The payment
        """
        return self.client.get(f"{self.base_path}/{payment_id}")

    def update(self, payment_id: str, data: Union[Dict[str, Any], PaymentUpdate]) -> PaymentResponse:
        """Update a payment.

        Args:
            payment_id: The payment ID
            data: Updated payment data

        Returns:
            The updated payment
        """
        return self.client.put(f"{self.base_path}/{payment_id}", data=data)

    def delete(self, payment_id: str) -> Dict[str, Any]:
        """Delete a payment.

        Args:
            payment_id: The payment ID

        Returns:
            A confirmation message
        """
        return self.client.delete(f"{self.base_path}/{payment_id}")
