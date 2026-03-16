"""Delay response models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DelayResponse(BaseModel):
    """Flight delay response model."""

    id: int = Field(..., description="Flight record ID")
    flight_number: str = Field(..., description="Flight number")
    airline: str = Field(..., description="Airline code")
    scheduled_time: datetime = Field(..., description="Scheduled departure time")
    actual_time: Optional[datetime] = Field(
        ..., description="Actual departure time"
    )
    status: str = Field(..., description="Flight status")
    delay_minutes: Optional[int] = Field(
        ..., description="Delay in minutes"
    )
    created_at: datetime = Field(..., description="Record creation timestamp")

