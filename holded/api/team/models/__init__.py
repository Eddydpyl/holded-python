"""
Data models for the Holded Team API.
"""

from .employee_time_tracking import (
    EmployeeTimeTracking,
    EmployeeTimeTrackingCreate,
    EmployeeTimeTrackingListResponse,
    EmployeeTimeTrackingResponse,
    EmployeeTimeTrackingUpdate,
)
from .employees import (
    Employee,
    EmployeeCreate,
    EmployeeListResponse,
    EmployeeResponse,
    EmployeeUpdate,
)

__all__ = [
    # Employees
    "Employee",
    "EmployeeCreate",
    "EmployeeUpdate",
    "EmployeeResponse",
    "EmployeeListResponse",
    # Employee Time Tracking
    "EmployeeTimeTracking",
    "EmployeeTimeTrackingCreate",
    "EmployeeTimeTrackingUpdate",
    "EmployeeTimeTrackingResponse",
    "EmployeeTimeTrackingListResponse",
]
