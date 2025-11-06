"""
Models for the Chart of Accounts API.
"""

from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class Account(BaseModel):
    """Model for an accounting account."""

    id: Optional[str] = Field(default=None, description="Account ID")
    code: Optional[str] = Field(default=None, description="Account code")
    name: Optional[str] = Field(default=None, description="Account name")
    type: Optional[str] = Field(default=None, description="Account type")
    parent: Optional[str] = Field(default=None, description="Parent account code")
    level: Optional[int] = Field(default=None, description="Account level in hierarchy")
    balance: Optional[float] = Field(default=None, description="Account balance")


class AccountListResponse(BaseResponse):
    """Response model for a list of accounts."""

    items: List[Account] = Field(default_factory=list, description="List of accounts")
    total: Optional[int] = Field(default=None, description="Total number of accounts")

