from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class FoodStatus(str, Enum):
    AVAILABLE = "available"
    MATCHED = "matched"
    ACCEPTED = "accepted"
    PICKED_UP = "picked_up"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class FoodCreate(BaseModel):
    food_name: str = Field(min_length=2, max_length=100)
    category: str = Field(min_length=2, max_length=50)
    quantity_kg: float = Field(gt=0, le=10000)
    prepared_at: datetime
    best_before: datetime
    storage_condition: str = Field(min_length=2, max_length=120)
    pickup_location: str = Field(min_length=3, max_length=200)
    notes: Optional[str] = Field(default="", max_length=500)

    @field_validator("best_before")
    @classmethod
    def expiry_after_preparation(cls, value, info):
        prepared = info.data.get("prepared_at")
        if prepared and value <= prepared:
            raise ValueError("best_before must be later than prepared_at")
        return value


class RecipientCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    recipient_type: str = Field(default="NGO", max_length=40)
    contact_person: str = Field(min_length=2, max_length=100)
    contact_phone: str = Field(min_length=5, max_length=30)
    location: str = Field(min_length=3, max_length=200)
    preferred_categories: list[str] = Field(default_factory=list)
    capacity_kg: float = Field(gt=0, le=10000)
    urgency: int = Field(default=3, ge=1, le=5)
    is_active: bool = True


class StatusUpdate(BaseModel):
    status: FoodStatus


class MatchResult(BaseModel):
    recipient_id: int
    recipient_name: str
    score: float
    reasons: list[str]
