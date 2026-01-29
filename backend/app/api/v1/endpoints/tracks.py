from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.track import TrackCreate, TrackOut, TrackUpdate
from app.services.tracks import (
    create_track,
    delete_track,
    get_track,
    list_tracks,
    update_track,
)

router = APIRouter()


@router.get("/", response_model=list[TrackOut])
def read_tracks():
    return list_tracks()


@router.get("/{track_id}", response_model=TrackOut)
def read_track(track_id: str):
    track = get_track(track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.post("/", response_model=TrackOut, status_code=status.HTTP_201_CREATED)
def create_new_track(payload: TrackCreate):
    return create_track(payload)


@router.put("/{track_id}", response_model=TrackOut)
def update_existing_track(track_id: str, payload: TrackUpdate):
    track = update_track(track_id, payload)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.delete("/{track_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_track(track_id: str):
    ok = delete_track(track_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Track not found")
    return None
