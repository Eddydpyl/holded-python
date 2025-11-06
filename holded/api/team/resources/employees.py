"""
Resource for interacting with the Employees API.
"""

from typing import Any, Dict, List, Optional, cast

from ...resources import BaseResource
from ..models.employees import EmployeeCreate, EmployeeUpdate


class EmployeesResource(BaseResource):
    """Resource for interacting with the Employees API."""

    def __init__(self, client):
        """Initialize the employees resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "team/employees"

    def list(self, page: Optional[int] = None) -> List[Dict[str, Any]]:
        """List all employees.

        Args:
            page: Page number for pagination (optional)

        Returns:
            A list of employees
        """
        params = {}
        if page is not None:
            params["page"] = page
        return cast(List[Dict[str, Any]], self.client.get(self.base_path, params=params))

    def create(self, data: EmployeeCreate) -> Dict[str, Any]:
        """Create a new employee.

        Args:
            data: Employee data

        Returns:
            The created employee
        """
        return cast(Dict[str, Any], self.client.post(self.base_path, data=data))

    def get(self, employee_id: str) -> Dict[str, Any]:
        """Get a specific employee.

        Args:
            employee_id: The employee ID

        Returns:
            The employee details
        """
        return cast(Dict[str, Any], self.client.get(f"{self.base_path}/{employee_id}"))

    def update(self, employee_id: str, data: EmployeeUpdate) -> Dict[str, Any]:
        """Update an employee.

        Args:
            employee_id: The employee ID
            data: Updated employee data

        Returns:
            The updated employee
        """
        return cast(
            Dict[str, Any],
            self.client.put(f"{self.base_path}/{employee_id}", data=data),
        )

    def delete(self, employee_id: str) -> Dict[str, Any]:
        """Delete an employee.

        Args:
            employee_id: The employee ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete(f"{self.base_path}/{employee_id}"))
