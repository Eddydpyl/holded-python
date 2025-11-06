"""
Models for the Time Tracking API.
"""

from typing import Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse


class TimeTrackingCreate(BaseModel):
    """Model for creating a time tracking entry."""

    date: int = Field(..., description="Date (timestamp)")
    duration: int = Field(..., description="Duration in minutes")
    desc: Optional[str] = Field(default=None, description="Description")
    task_id: Optional[str] = Field(default=None, alias="taskId", description="Task ID")
    user_id: Optional[str] = Field(default=None, alias="userId", description="User ID")


class TimeTrackingUpdate(BaseModel):
    """Model for updating a time tracking entry."""

    date: Optional[int] = Field(default=None, description="Date (timestamp)")
    duration: Optional[int] = Field(default=None, description="Duration in minutes")
    desc: Optional[str] = Field(default=None, description="Description")
    task_id: Optional[str] = Field(default=None, alias="taskId", description="Task ID")
    user_id: Optional[str] = Field(default=None, alias="userId", description="User ID")


class TimeTracking(BaseModel):
    """Time tracking model."""

    id: str = Field(..., description="Time tracking ID")
    date: Optional[int] = Field(default=None, description="Date (timestamp)")
    duration: Optional[int] = Field(default=None, description="Duration in minutes")
    desc: Optional[str] = Field(default=None, description="Description")
    task_id: Optional[str] = Field(default=None, alias="taskId", description="Task ID")
    project_id: Optional[str] = Field(default=None, alias="projectId", description="Project ID")
    user_id: Optional[str] = Field(default=None, alias="userId", description="User ID")


class TimeTrackingResponse(BaseResponse):
    """Response model for a single time tracking entry."""

    model_config = {"extra": "allow"}


class TimeTrackingListResponse(BaseResponse):
    """Response model for a list of time tracking entries."""

    model_config = {"extra": "allow"}
