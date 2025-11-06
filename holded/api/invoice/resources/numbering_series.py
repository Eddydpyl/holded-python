"""
Resource for interacting with the Numbering Series API.
"""

from typing import Any, Dict, Union

from ..models.numbering_series import (
    NumberingSeriesCreate,
    NumberingSeriesListResponse,
    NumberingSeriesResponse,
    NumberingSeriesUpdate,
)


class NumberingSeriesResource:
    """Resource for interacting with the Numbering Series API."""

    def __init__(self, client):
        """Initialize the numbering series resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/numberingseries"

    def list_by_type(self, doc_type: str) -> NumberingSeriesListResponse:
        """Get numbering series by document type.

        Args:
            doc_type: The document type (invoice, order, etc.)

        Returns:
            A list of numbering series for the specified document type
        """
        return self.client.get(f"{self.base_path}/{doc_type}")

    def create(self, doc_type: str, data: Union[Dict[str, Any], NumberingSeriesCreate]) -> NumberingSeriesResponse:
        """Create a new numbering series.

        Args:
            doc_type: The document type (invoice, order, etc.)
            data: Numbering series data

        Returns:
            The created numbering series
        """
        return self.client.post(f"{self.base_path}/{doc_type}", data=data)

    def update(
        self, doc_type: str, series_id: str, data: Union[Dict[str, Any], NumberingSeriesUpdate]
    ) -> NumberingSeriesResponse:
        """Update a numbering series.

        Args:
            doc_type: The document type (invoice, order, etc.)
            series_id: The numbering series ID
            data: Updated numbering series data

        Returns:
            The updated numbering series
        """
        return self.client.put(f"{self.base_path}/{doc_type}/{series_id}", data=data)

    def delete(self, doc_type: str, series_id: str) -> Dict[str, Any]:
        """Delete a numbering series.

        Args:
            doc_type: The document type (invoice, order, etc.)
            series_id: The numbering series ID

        Returns:
            A confirmation message
        """
        return self.client.delete(f"{self.base_path}/{doc_type}/{series_id}")
