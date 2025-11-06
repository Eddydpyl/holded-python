"""
Models for the Tasks API.
"""
from typing import Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class TaskCreate(BaseModel):
    """Model for creating a task."""

    name: str = Field(..., description="Task name")
    project_id: Optional[str] = Field(default=None, alias="projectId", description="Project ID")
    desc: Optional[str] = Field(default=None, description="Task description")
    done: Optional[bool] = Field(default=False, description="Whether the task is done")


class TaskUpdate(BaseModel):
    """Model for updating a task."""

    name: Optional[str] = Field(default=None, description="Task name")
    project_id: Optional[str] = Field(default=None, alias="projectId", description="Project ID")
    desc: Optional[str] = Field(default=None, description="Task description")
    done: Optional[bool] = Field(default=None, description="Whether the task is done")


class Task(BaseModel):
    """Task model."""

    id: str = Field(..., description="Task ID")
    name: Optional[str] = Field(default=None, description="Task name")
    project_id: Optional[str] = Field(default=None, alias="projectId", description="Project ID")
    desc: Optional[str] = Field(default=None, description="Task description")
    done: Optional[bool] = Field(default=None, description="Whether the task is done")


class TaskResponse(BaseResponse):
    """Response model for a single task."""

    model_config = {"extra": "allow"}


class TaskListResponse(BaseResponse):
    """Response model for a list of tasks."""

    model_config = {"extra": "allow"}

