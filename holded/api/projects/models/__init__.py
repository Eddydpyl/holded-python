"""
Data models for the Holded Projects API.
"""

from .projects import (
    Project,
    ProjectCreate,
    ProjectListResponse,
    ProjectResponse,
    ProjectSummary,
    ProjectSummaryResponse,
    ProjectUpdate,
)
from .tasks import (
    Task,
    TaskCreate,
    TaskListResponse,
    TaskResponse,
    TaskUpdate,
)
from .time_tracking import (
    TimeTracking,
    TimeTrackingCreate,
    TimeTrackingListResponse,
    TimeTrackingResponse,
    TimeTrackingUpdate,
)

__all__ = [
    # Projects
    "Project",
    "ProjectCreate",
    "ProjectUpdate",
    "ProjectResponse",
    "ProjectListResponse",
    "ProjectSummary",
    "ProjectSummaryResponse",
    # Tasks
    "Task",
    "TaskCreate",
    "TaskUpdate",
    "TaskResponse",
    "TaskListResponse",
    # Time Tracking
    "TimeTracking",
    "TimeTrackingCreate",
    "TimeTrackingUpdate",
    "TimeTrackingResponse",
    "TimeTrackingListResponse",
]
