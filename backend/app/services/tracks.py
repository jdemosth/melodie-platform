from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from uuid import uuid4

from app.schemas.track import TrackCreate, TrackOut, TrackUpdate

# In-memory DB (temporary)
_TRACKS: Dict[str, TrackOut] = {}


def list_tracks() -> List[TrackOut]:
    # newest first
    return sorted(_TRACKS.values(), key=lambda t: t.created_at, reverse=True)


def get_track(track_id: str) -> TrackOut | None:
    return _TRACKS.get(track_id)


def create_track(payload: TrackCreate) -> TrackOut:
    track_id = str(uuid4())
    track = TrackOut(
        id=track_id,
        created_at=datetime.utcnow(),
        **payload.model_dump(),
    )
    _TRACKS[track_id] = track
    return track


def update_track(track_id: str, payload: TrackUpdate) -> TrackOut | None:
    existing = _TRACKS.get(track_id)
    if not existing:
        return None

    data = existing.model_dump()
    updates = payload.model_dump(exclude_unset=True)

    data.update(updates)
    updated = TrackOut(**data)
    _TRACKS[track_id] = updated
    return updated


def delete_track(track_id: str) -> bool:
    return _TRACKS.pop(track_id, None) is not None
