from __future__ import annotations

from typing import List
from fastapi import HTTPException

from app.core.supabase_client import get_supabase
from app.schemas.track import TrackCreate, TrackOut


TABLE = "tracks"


def list_tracks() -> List[TrackOut]:
    supabase = get_supabase()

    response = (
        supabase.table(TABLE)
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    # response.data is typically a list of dict rows
    if response.data is None:
        return []

    return [TrackOut.model_validate(row) for row in response.data]


def create_track(payload: TrackCreate) -> TrackOut:
    supabase = get_supabase()

    response = (
        supabase.table(TABLE)
        .insert(payload.model_dump(mode="json"))
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=500, detail="Insert failed")

    # Supabase returns inserted rows
    return TrackOut.model_validate(response.data[0])

