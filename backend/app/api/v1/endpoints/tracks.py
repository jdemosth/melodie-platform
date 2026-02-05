#from fastapi import APIRouter, status
#from app.schemas.track import TrackCreate, TrackOut
#from app.services.track_service import list_tracks, create_track

#router = APIRouter()

#@router.get("/", response_model=list[TrackOut])
#d#ef read_tracks():
   # return list_tracks()

#@router.post("/", response_model=TrackOut, status_code=status.HTTP_201_CREATED)
#def create_new_track(payload: TrackCreate):
    #return create_track(payload)



from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException
from supabase import Client

from app.core.supabase_client import get_supabase
from app.models.schemas.track import TrackCreate, TrackOut
from app.services.track_service import create_track

router = APIRouter()


@router.post("/", response_model=TrackOut)
def post_track(payload: TrackCreate, db: Client = Depends(get_supabase)):
    try:
        return create_track(db, payload)
    except ValueError as e:
        # for "Artist not found"
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
