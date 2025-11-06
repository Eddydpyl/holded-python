"""
Models for the Employee Time Tracking API.
"""
from typing import Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class EmployeeTimeTrackingCreate(BaseModel):
    """Model for creating an employee time tracking entry."""

    start_tmp: str = Field(..., alias="startTmp", description="Start timestamp (ISO 8601 format)")
    end_tmp: str = Field(..., alias="endTmp", description="End timestamp (ISO 8601 format)")


class EmployeeTimeTrackingUpdate(BaseModel):
    """Model for updating an employee time tracking entry."""

    start_tmp: Optional[str] = Field(default=None, alias="startTmp", description="Start timestamp (ISO 8601 format)")
    end_tmp: Optional[str] = Field(default=None, alias="endTmp", description="End timestamp (ISO 8601 format)")


class EmployeeTimeTracking(BaseModel):
    """Employee time tracking model."""

    id: str = Field(..., description="Time tracking ID")
    employee_id: Optional[str] = Field(default=None, alias="employeeId", description="Employee ID")
    start_tmp: Optional[str] = Field(default=None, alias="startTmp", description="Start timestamp")
    end_tmp: Optional[str] = Field(default=None, alias="endTmp", description="End timestamp")


class EmployeeTimeTrackingResponse(BaseResponse):
    """Response model for a single employee time tracking entry."""

    model_config = {"extra": "allow"}


class EmployeeTimeTrackingListResponse(BaseResponse):
    """Response model for a list of employee time tracking entries."""

    model_config = {"extra": "allow"}

