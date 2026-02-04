from fastapi import APIRouter, status
from app.schemas.track import TrackCreate, TrackOut
from app.services.track_service import list_tracks, create_track

router = APIRouter()

@router.get("/", response_model=list[TrackOut])
def read_tracks():
    return list_tracks()

@router.post("/", response_model=TrackOut, status_code=status.HTTP_201_CREATED)
def create_new_track(payload: TrackCreate):
    return create_track(payload)
