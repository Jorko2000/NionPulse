from pydantic import BaseModel

class EventCreate(BaseModel):
    type: str
    payload: dict
