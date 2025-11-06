"""
Models for the Treasury API.
"""

from typing import List, Optional

from pydantic import Field

from ...base_models import BaseModel, BaseResponse


class TreasuryAccountCreate(BaseModel):
    """Model for creating a treasury account."""

    id: Optional[str] = Field(default=None, description="Account ID (optional)")
    name: str = Field(..., description="Account name")
    type: str = Field(
        ...,
        description="Account type (e.g., 'bank', 'cash', 'creditcard', 'paypal', 'other')",
    )
    balance: Optional[int] = Field(default=0, description="Initial balance")
    accountNumber: Optional[int] = Field(
        default=None, description="Account number (accounting account number)"
    )
    iban: Optional[str] = Field(default=None, description="IBAN")
    swift: Optional[str] = Field(default=None, description="SWIFT/BIC code")
    bank: Optional[str] = Field(default=None, description="Bank identifier")
    bankname: Optional[str] = Field(default=None, description="Bank name")


class TreasuryAccount(BaseModel):
    """Treasury account model."""

    id: str = Field(..., description="Account ID")
    name: str = Field(..., description="Account name")
    type: str = Field(..., description="Account type")
    balance: int = Field(..., description="Current balance")
    accountNumber: Optional[int] = Field(default=None, description="Account number")
    iban: Optional[str] = Field(default=None, description="IBAN")
    swift: Optional[str] = Field(default=None, description="SWIFT/BIC code")
    bank: Optional[str] = Field(default=None, description="Bank identifier")
    bankname: Optional[str] = Field(default=None, description="Bank name")


# Response models
class TreasuryAccountResponse(BaseResponse):
    """Response model for a single treasury account."""

    account: Optional[TreasuryAccount] = Field(
        default=None, description="Treasury account data"
    )


class TreasuryAccountListResponse(BaseResponse):
    """Response model for a list of treasury accounts."""

    items: List[TreasuryAccount] = Field(
        default_factory=list, description="List of treasury accounts"
    )
