"""Delay models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DelayResponse(BaseModel):
    """Flight delay response model."""

    id: int = Field(..., description="Flight ID")
    flight_number: str = Field(..., description="Flight number")
    airline: str = Field(..., description="Airline name")
    scheduled_time: datetime = Field(..., description="Scheduled departure time")
    actual_time: Optional[datetime] = Field(None, description="Actual departure time")
    status: str = Field(..., description="Flight status")
    delay_minutes: Optional[int] = Field(None, description="Delay in minutes")
    created_at: datetime = Field(..., description="Record creation time")

