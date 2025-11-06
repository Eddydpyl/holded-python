"""
Models for the Daily Ledger API.
"""

from typing import List, Optional

from pydantic import Field, model_validator

from ...models import BaseModel, BaseResponse, PaginationParams


class EntryLine(BaseModel):
    """Model for an entry line in the daily ledger."""

    account: str = Field(..., description="Account code (must match existing accounting account)")
    debit: Optional[float] = Field(default=None, description="Debit amount (can be 0 or empty)")
    credit: Optional[float] = Field(default=None, description="Credit amount (can be 0 or empty)")

    @model_validator(mode="after")
    def validate_debit_credit(self):
        """Validate that debit and credit are not both set."""
        if self.debit and self.credit:
            raise ValueError("Entry lines cannot have both debit and credit values")
        return self


class EntryCreate(BaseModel):
    """Model for creating a daily ledger entry."""

    lines: List[EntryLine] = Field(..., min_length=2, description="At least 2 entry lines required")
    desc: Optional[str] = Field(default=None, description="Entry description")
    date: Optional[int] = Field(default=None, description="Entry date as Unix timestamp")

    @model_validator(mode="after")
    def validate_balanced(self):
        """Validate that debit and credit totals match."""
        if len(self.lines) < 2:
            raise ValueError("At least 2 entry lines are required")

        total_debit = sum(line.debit or 0 for line in self.lines)
        total_credit = sum(line.credit or 0 for line in self.lines)

        if abs(total_debit - total_credit) > 0.01:  # Allow small floating point differences
            raise ValueError("Debit and credit totals must match")

        return self


class EntryLineResponse(BaseModel):
    """Response model for an entry line."""

    account: str = Field(..., description="Account code")
    debit: Optional[float] = Field(default=None, description="Debit amount")
    credit: Optional[float] = Field(default=None, description="Credit amount")


class Entry(BaseModel):
    """Model for a daily ledger entry."""

    id: str = Field(..., description="Entry ID")
    lines: List[EntryLineResponse] = Field(..., description="Entry lines")
    desc: Optional[str] = Field(default=None, description="Entry description")
    date: Optional[int] = Field(default=None, description="Entry date as Unix timestamp")
    created: Optional[int] = Field(default=None, description="Creation timestamp")
    modified: Optional[int] = Field(default=None, description="Last modification timestamp")


class DailyLedgerListParams(PaginationParams):
    """Parameters for listing daily ledger entries."""

    starttmp: Optional[str] = Field(default=None, description="Starting timestamp")
    endtmp: Optional[str] = Field(default=None, description="Ending timestamp")


class EntryResponse(BaseResponse):
    """Response model for a single entry."""

    id: Optional[str] = Field(default=None, description="Entry ID")
    status: Optional[str] = Field(default=None, description="Entry status")


class EntryListResponse(BaseResponse):
    """Response model for a list of entries."""

    items: List[Entry] = Field(default_factory=list, description="List of entries")
    total: Optional[int] = Field(default=None, description="Total number of entries")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")
