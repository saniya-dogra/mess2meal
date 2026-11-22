from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator


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

    @model_validator(mode="after")
    def validate_times(self):
        if self.prepared_at.tzinfo is None or self.best_before.tzinfo is None:
            raise ValueError("prepared_at and best_before must include a timezone")
        if self.best_before <= self.prepared_at:
            raise ValueError("best_before must be later than prepared_at")
        return self


class RecipientCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    recipient_type: str = Field(default="NGO", max_length=40)
    contact_person: str = Field(min_length=2, max_length=100)
    contact_phone: str = Field(min_length=5, max_length=30)
    location: str = Field(min_length=3, max_length=200)
    preferred_categories: list[str] = Field(default_factory=list)
    capacity_kg: float = Field(gt=0, le=10000)
    urgency: int = Field(default=3, ge=1, le=5)
    distance_km: float = Field(default=0, ge=0, le=10000)
    is_active: bool = True


class StatusUpdate(BaseModel):
    status: FoodStatus
    note: str = Field(default="", max_length=300)


class MatchResult(BaseModel):
    recipient_id: int
    recipient_name: str
    score: float
    reasons: list[str]
