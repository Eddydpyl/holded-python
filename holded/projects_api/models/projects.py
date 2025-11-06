"""
Models for the Projects API.
"""
from typing import Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class ProjectCreate(BaseModel):
    """Model for creating a project."""

    name: str = Field(..., description="Project name")


class ProjectUpdate(BaseModel):
    """Model for updating a project."""

    name: Optional[str] = Field(default=None, description="Project name")


class Project(BaseModel):
    """Project model."""

    id: str = Field(..., description="Project ID")
    name: Optional[str] = Field(default=None, description="Project name")


class ProjectResponse(BaseResponse):
    """Response model for a single project."""

    model_config = {"extra": "allow"}


class ProjectListResponse(BaseResponse):
    """Response model for a list of projects."""

    model_config = {"extra": "allow"}


class ProjectSummary(BaseModel):
    """Project summary model."""

    model_config = {"extra": "allow"}


class ProjectSummaryResponse(BaseResponse):
    """Response model for a project summary."""

    model_config = {"extra": "allow"}

