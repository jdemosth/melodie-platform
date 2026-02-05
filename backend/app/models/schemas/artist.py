from __future__ import annotations
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class ArtistCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)


class ArtistOut(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime
