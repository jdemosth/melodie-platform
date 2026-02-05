from __future__ import annotations
from supabase import Client
from app.models.schemas.artist import ArtistCreate, ArtistOut


def create_artist(db: Client, payload: ArtistCreate) -> ArtistOut:
    data = (
        db.table("artists")
        .insert({"name": payload.name})
        .execute()
    )

    row = data.data[0]
    return ArtistOut(**row)
