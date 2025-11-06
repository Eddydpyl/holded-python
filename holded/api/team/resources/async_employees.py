"""
Asynchronous resource for interacting with the Employees API.
"""

from typing import Any, Dict, List, Optional, cast

from ...resources import AsyncBaseResource
from ..models.employees import EmployeeCreate, EmployeeUpdate


class AsyncEmployeesResource(AsyncBaseResource):
    """Resource for interacting with the Employees API asynchronously."""

    def __init__(self, client):
        """Initialize the employees resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "team/employees"

    async def list(self, page: Optional[int] = None) -> List[Dict[str, Any]]:
        """List all employees asynchronously.

        Args:
            page: Page number for pagination (optional)

        Returns:
            A list of employees
        """
        params = {}
        if page is not None:
            params["page"] = page
        result = await self.client.get(self.base_path, params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: EmployeeCreate) -> Dict[str, Any]:
        """Create a new employee asynchronously.

        Args:
            data: Employee data

        Returns:
            The created employee
        """
        result = await self.client.post(self.base_path, data=data)
        return cast(Dict[str, Any], result)

    async def get(self, employee_id: str) -> Dict[str, Any]:
        """Get a specific employee asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            The employee details
        """
        result = await self.client.get(f"{self.base_path}/{employee_id}")
        return cast(Dict[str, Any], result)

    async def update(self, employee_id: str, data: EmployeeUpdate) -> Dict[str, Any]:
        """Update an employee asynchronously.

        Args:
            employee_id: The employee ID
            data: Updated employee data

        Returns:
            The updated employee
        """
        result = await self.client.put(f"{self.base_path}/{employee_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, employee_id: str) -> Dict[str, Any]:
        """Delete an employee asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/{employee_id}")
        return cast(Dict[str, Any], result)
