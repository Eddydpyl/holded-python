"""
Models for the Leads API.
"""
from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class LeadCreate(BaseModel):
    """Model for creating a lead."""

    funnel_id: str = Field(..., alias="funnelId", description="Funnel ID")
    contact_id: Optional[str] = Field(default=None, alias="contactId", description="Contact ID")
    contact_name: Optional[str] = Field(default=None, alias="contactName", description="Contact name")
    name: str = Field(..., description="Lead name")
    value: Optional[int] = Field(default=None, description="Lead value")
    potential: Optional[int] = Field(default=None, description="Lead potential")
    due_date: Optional[int] = Field(default=None, alias="dueDate", description="Due date (timestamp)")
    stage_id: Optional[str] = Field(default=None, alias="stageId", description="Stage ID or name")


class LeadUpdate(BaseModel):
    """Model for updating a lead."""

    contact_id: Optional[str] = Field(default=None, alias="contactId", description="Contact ID")
    contact_name: Optional[str] = Field(default=None, alias="contactName", description="Contact name")
    name: Optional[str] = Field(default=None, description="Lead name")
    value: Optional[int] = Field(default=None, description="Lead value")
    potential: Optional[int] = Field(default=None, description="Lead potential")
    due_date: Optional[int] = Field(default=None, alias="dueDate", description="Due date (timestamp)")
    stage_id: Optional[str] = Field(default=None, alias="stageId", description="Stage ID or name")


class LeadNoteCreate(BaseModel):
    """Model for creating a lead note."""

    note: str = Field(..., description="Note text")


class LeadNoteUpdate(BaseModel):
    """Model for updating a lead note."""

    note: str = Field(..., description="Note text")


class LeadTaskCreate(BaseModel):
    """Model for creating a lead task."""

    task: str = Field(..., description="Task text")
    done: Optional[bool] = Field(default=False, description="Whether the task is done")


class LeadTaskUpdate(BaseModel):
    """Model for updating a lead task."""

    task: Optional[str] = Field(default=None, description="Task text")
    done: Optional[bool] = Field(default=None, description="Whether the task is done")


class LeadDateUpdate(BaseModel):
    """Model for updating a lead creation date."""

    date: int = Field(..., description="Creation date (timestamp)")


class LeadStageUpdate(BaseModel):
    """Model for updating a lead stage."""

    stage_id: str = Field(..., alias="stageId", description="Stage ID or name")


class Lead(BaseModel):
    """Lead model."""

    id: str = Field(..., description="Lead ID")
    funnel_id: Optional[str] = Field(default=None, alias="funnelId", description="Funnel ID")
    contact_id: Optional[str] = Field(default=None, alias="contactId", description="Contact ID")
    name: Optional[str] = Field(default=None, description="Lead name")
    value: Optional[int] = Field(default=None, description="Lead value")
    potential: Optional[int] = Field(default=None, description="Lead potential")
    due_date: Optional[int] = Field(default=None, alias="dueDate", description="Due date (timestamp)")
    stage_id: Optional[str] = Field(default=None, alias="stageId", description="Stage ID")


class LeadResponse(BaseResponse):
    """Response model for a single lead."""

    model_config = {"extra": "allow"}


class LeadListResponse(BaseResponse):
    """Response model for a list of leads."""

    model_config = {"extra": "allow"}

