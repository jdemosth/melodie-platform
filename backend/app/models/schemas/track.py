from __future__ import annotations
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class TrackCreate(BaseModel):
    artist_id: UUID
    title: str = Field(min_length=1, max_length=200)
    price_cents: int = Field(ge=0)
    file_path: str = Field(min_length=1, max_length=500)


class TrackOut(BaseModel):
    id: UUID
    artist_id: UUID
    title: str
    price_cents: int
    file_path: str
    created_at: datetime
