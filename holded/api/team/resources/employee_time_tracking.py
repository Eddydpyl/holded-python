"""
Resource for interacting with the Employee Time Tracking API.
"""

from typing import Any, Dict, List, Optional, cast

from ...resources import BaseResource
from ..models.employee_time_tracking import (
    EmployeeTimeTrackingCreate,
    EmployeeTimeTrackingUpdate,
)


class EmployeeTimeTrackingResource(BaseResource):
    """Resource for interacting with the Employee Time Tracking API."""

    def __init__(self, client):
        """Initialize the employee time tracking resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "team/employees"

    def list_all(self, page: Optional[int] = None) -> List[Dict[str, Any]]:
        """List all time tracking entries across all employees.

        Args:
            page: Page number for pagination (optional)

        Returns:
            A list of time tracking entries
        """
        params = {}
        if page is not None:
            params["page"] = page
        return cast(
            List[Dict[str, Any]],
            self.client.get(f"{self.base_path}/times", params=params),
        )

    def list(self, employee_id: str) -> List[Dict[str, Any]]:
        """List all time tracking entries for a specific employee.

        Args:
            employee_id: The employee ID

        Returns:
            A list of time tracking entries
        """
        return cast(
            List[Dict[str, Any]],
            self.client.get(f"{self.base_path}/{employee_id}/times"),
        )

    def create(self, employee_id: str, data: EmployeeTimeTrackingCreate) -> Dict[str, Any]:
        """Create a new time tracking entry for an employee.

        Args:
            employee_id: The employee ID
            data: Time tracking data

        Returns:
            The created time tracking entry
        """
        return cast(
            Dict[str, Any],
            self.client.post(f"{self.base_path}/{employee_id}/times", data=data),
        )

    def get(self, time_tracking_id: str) -> Dict[str, Any]:
        """Get a specific time tracking entry.

        Args:
            time_tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        return cast(
            Dict[str, Any],
            self.client.get(f"{self.base_path}/times/{time_tracking_id}"),
        )

    def update(self, time_tracking_id: str, data: EmployeeTimeTrackingUpdate) -> Dict[str, Any]:
        """Update a time tracking entry.

        Args:
            time_tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking entry
        """
        return cast(
            Dict[str, Any],
            self.client.put(f"{self.base_path}/times/{time_tracking_id}", data=data),
        )

    def delete(self, time_tracking_id: str) -> Dict[str, Any]:
        """Delete a time tracking entry.

        Args:
            time_tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        return cast(
            Dict[str, Any],
            self.client.delete(f"{self.base_path}/times/{time_tracking_id}"),
        )

    def clock_in(self, employee_id: str) -> Dict[str, Any]:
        """Clock in an employee.

        Args:
            employee_id: The employee ID

        Returns:
            The clock-in response
        """
        return cast(Dict[str, Any], self.client.post(f"{self.base_path}/{employee_id}/clock-in"))

    def clock_out(self, employee_id: str) -> Dict[str, Any]:
        """Clock out an employee.

        Args:
            employee_id: The employee ID

        Returns:
            The clock-out response
        """
        return cast(
            Dict[str, Any],
            self.client.post(f"{self.base_path}/{employee_id}/clock-out"),
        )

    def pause(self, employee_id: str) -> Dict[str, Any]:
        """Pause an employee's time tracking.

        Args:
            employee_id: The employee ID

        Returns:
            The pause response
        """
        return cast(Dict[str, Any], self.client.post(f"{self.base_path}/{employee_id}/pause"))

    def unpause(self, employee_id: str) -> Dict[str, Any]:
        """Unpause an employee's time tracking.

        Args:
            employee_id: The employee ID

        Returns:
            The unpause response
        """
        return cast(Dict[str, Any], self.client.post(f"{self.base_path}/{employee_id}/unpause"))
