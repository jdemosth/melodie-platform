from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException
from supabase import Client

from app.core.supabase_client import get_supabase
from app.models.schemas.artist import ArtistCreate, ArtistOut
from app.services.artist_service import create_artist

router = APIRouter()


@router.post("/", response_model=ArtistOut)
def post_artist(payload: ArtistCreate, db: Client = Depends(get_supabase)):
    try:
        return create_artist(db, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))