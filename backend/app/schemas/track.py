from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl


class TrackCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    artist: str | None = Field(default=None, max_length=200)
    price_usd: float = Field(ge=0, default=0.0)
    preview_url: HttpUrl | None = None
    download_url: HttpUrl | None = None


class TrackOut(TrackCreate):
    id: str
    created_at: datetime

