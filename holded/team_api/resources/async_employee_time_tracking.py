"""
Asynchronous resource for interacting with the Employee Time Tracking API.
"""
from typing import Any, Dict, List, Optional, cast

from ..models.employee_time_tracking import EmployeeTimeTrackingCreate, EmployeeTimeTrackingUpdate
from ...base_resources import AsyncBaseResource


class AsyncEmployeeTimeTrackingResource(AsyncBaseResource):
    """Resource for interacting with the Employee Time Tracking API asynchronously."""

    def __init__(self, client):
        """Initialize the employee time tracking resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "team/employees"

    async def list_all(self, page: Optional[int] = None) -> List[Dict[str, Any]]:
        """List all time tracking entries across all employees asynchronously.

        Args:
            page: Page number for pagination (optional)

        Returns:
            A list of time tracking entries
        """
        params = {}
        if page is not None:
            params["page"] = page
        result = await self.client.get(f"{self.base_path}/times", params=params)
        return cast(List[Dict[str, Any]], result)

    async def list(self, employee_id: str) -> List[Dict[str, Any]]:
        """List all time tracking entries for a specific employee asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            A list of time tracking entries
        """
        result = await self.client.get(f"{self.base_path}/{employee_id}/times")
        return cast(List[Dict[str, Any]], result)

    async def create(self, employee_id: str, data: EmployeeTimeTrackingCreate) -> Dict[str, Any]:
        """Create a new time tracking entry for an employee asynchronously.

        Args:
            employee_id: The employee ID
            data: Time tracking data

        Returns:
            The created time tracking entry
        """
        result = await self.client.post(f"{self.base_path}/{employee_id}/times", data=data)
        return cast(Dict[str, Any], result)

    async def get(self, time_tracking_id: str) -> Dict[str, Any]:
        """Get a specific time tracking entry asynchronously.

        Args:
            time_tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        result = await self.client.get(f"{self.base_path}/times/{time_tracking_id}")
        return cast(Dict[str, Any], result)

    async def update(self, time_tracking_id: str, data: EmployeeTimeTrackingUpdate) -> Dict[str, Any]:
        """Update a time tracking entry asynchronously.

        Args:
            time_tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking entry
        """
        result = await self.client.put(f"{self.base_path}/times/{time_tracking_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete(self, time_tracking_id: str) -> Dict[str, Any]:
        """Delete a time tracking entry asynchronously.

        Args:
            time_tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        result = await self.client.delete(f"{self.base_path}/times/{time_tracking_id}")
        return cast(Dict[str, Any], result)

    async def clock_in(self, employee_id: str) -> Dict[str, Any]:
        """Clock in an employee asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            The clock-in response
        """
        result = await self.client.post(f"{self.base_path}/{employee_id}/clock-in")
        return cast(Dict[str, Any], result)

    async def clock_out(self, employee_id: str) -> Dict[str, Any]:
        """Clock out an employee asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            The clock-out response
        """
        result = await self.client.post(f"{self.base_path}/{employee_id}/clock-out")
        return cast(Dict[str, Any], result)

    async def pause(self, employee_id: str) -> Dict[str, Any]:
        """Pause an employee's time tracking asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            The pause response
        """
        result = await self.client.post(f"{self.base_path}/{employee_id}/pause")
        return cast(Dict[str, Any], result)

    async def unpause(self, employee_id: str) -> Dict[str, Any]:
        """Unpause an employee's time tracking asynchronously.

        Args:
            employee_id: The employee ID

        Returns:
            The unpause response
        """
        result = await self.client.post(f"{self.base_path}/{employee_id}/unpause")
        return cast(Dict[str, Any], result)

