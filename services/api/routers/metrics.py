from fastapi import APIRouter
import time, random

router = APIRouter()

@router.get("/")
def metrics():
    return [{"timestamp": int(time.time()), "value": random.randint(0, 100)} for _ in range(10)]
