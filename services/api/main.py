from fastapi import FastAPI
from routers.events import router as events_router
from routers.metrics import router as metrics_router

app = FastAPI(title="NionPulse API")
app.include_router(events_router, prefix="/events")
app.include_router(metrics_router, prefix="/metrics")
