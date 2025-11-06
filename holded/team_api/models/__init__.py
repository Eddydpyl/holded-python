"""
Data models for the Holded Team API.
"""

from .employees import (
    Employee,
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
    EmployeeListResponse,
)
from .employee_time_tracking import (
    EmployeeTimeTracking,
    EmployeeTimeTrackingCreate,
    EmployeeTimeTrackingUpdate,
    EmployeeTimeTrackingResponse,
    EmployeeTimeTrackingListResponse,
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

