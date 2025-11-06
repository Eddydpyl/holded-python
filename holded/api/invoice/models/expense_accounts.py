"""
Models for the Expense Accounts API.
"""

from typing import List, Optional

from pydantic import Field

from ...models import BaseModel, BaseResponse, PaginationParams


class ExpenseAccountCreate(BaseModel):
    """Model for creating an expense account."""

    name: str = Field(..., description="Expense account name")
    desc: str = Field(..., description="Expense account description")
    accountNum: int = Field(..., description="Account number")


class ExpenseAccountUpdate(BaseModel):
    """Model for updating an expense account."""

    name: Optional[str] = Field(default=None, description="Expense account name")
    desc: Optional[str] = Field(default=None, description="Expense account description")
    accountNum: Optional[int] = Field(default=None, description="Account number")


class ExpenseAccount(BaseModel):
    """Expense account model."""

    id: str = Field(..., description="Expense account ID")
    name: str = Field(..., description="Expense account name")
    desc: str = Field(..., description="Expense account description")
    accountNum: int = Field(..., description="Account number")


class ExpenseAccountListParams(PaginationParams):
    """Parameters for listing expense accounts."""

    pass


# Response models
class ExpenseAccountResponse(BaseResponse, ExpenseAccount):
    """Response model for a single expense account."""

    pass


class ExpenseAccountListResponse(BaseResponse):
    """Response model for a list of expense accounts."""

    items: List[ExpenseAccount] = Field(..., description="List of expense accounts")
    total: Optional[int] = Field(default=None, description="Total number of expense accounts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")
