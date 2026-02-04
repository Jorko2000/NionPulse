from fastapi import APIRouter, Depends
from schemas.events import EventCreate
from services.publisher import publish_event

router = APIRouter()

@router.post("/")
def create_event(event: EventCreate):
    publish_event(event.dict())
    return {"status": "queued"}
