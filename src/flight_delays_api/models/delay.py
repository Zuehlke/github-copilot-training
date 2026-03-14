"""Pydantic models for delay endpoints."""

from datetime import datetime

from pydantic import BaseModel


class Delay(BaseModel):
    """Represents a flight delay record loaded from the sample dataset."""

    id: int
    flight_number: str
    airline: str
    scheduled_time: datetime
    actual_time: datetime | None
    status: str
    delay_minutes: int | None
    created_at: datetime

