"""
Models for the Employees API.
"""
from typing import Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class EmployeeCreate(BaseModel):
    """Model for creating an employee."""

    name: str = Field(..., description="Employee first name")
    last_name: str = Field(..., alias="lastName", description="Employee last name")
    email: str = Field(..., description="Employee email")
    send_invite: Optional[bool] = Field(default=None, alias="sendInvite", description="Whether to send an invite email")


class EmployeeUpdate(BaseModel):
    """Model for updating an employee."""

    name: Optional[str] = Field(default=None, description="Employee first name")
    last_name: Optional[str] = Field(default=None, alias="lastName", description="Employee last name")
    email: Optional[str] = Field(default=None, description="Employee email")
    send_invite: Optional[bool] = Field(default=None, alias="sendInvite", description="Whether to send an invite email")


class Employee(BaseModel):
    """Employee model."""

    id: str = Field(..., description="Employee ID")
    name: Optional[str] = Field(default=None, description="Employee first name")
    last_name: Optional[str] = Field(default=None, alias="lastName", description="Employee last name")
    email: Optional[str] = Field(default=None, description="Employee email")


class EmployeeResponse(BaseResponse):
    """Response model for a single employee."""

    model_config = {"extra": "allow"}


class EmployeeListResponse(BaseResponse):
    """Response model for a list of employees."""

    model_config = {"extra": "allow"}

