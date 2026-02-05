from __future__ import annotations



from __future__ import annotations
from supabase import Client
from app.models.schemas.track import TrackCreate, TrackOut

from typing import List
from fastapi import HTTPException


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



def _artist_exists(db: Client, artist_id: str) -> bool:
    res = (
        db.table("artists")
        .select("id")
        .eq("id", artist_id)
        .limit(1)
        .execute()
    )
    return bool(res.data)


def create_track(db: Client, payload: TrackCreate) -> TrackOut:
    if not _artist_exists(db, str(payload.artist_id)):
        raise ValueError("Artist not found")

    data = (
        db.table("tracks")
        .insert(
            {
                "artist_id": str(payload.artist_id),
                "title": payload.title,
                "price_cents": payload.price_cents,
                "file_path": payload.file_path,
            }
        )
        .execute()
    )

    row = data.data[0]
    return TrackOut(**row)


