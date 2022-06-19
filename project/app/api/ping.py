from datetime import datetime

from app.config import Settings, get_settings
from fastapi import APIRouter, Depends

router = APIRouter(tags=["Ping"])


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
        "timestamp": datetime.strftime(datetime.utcnow(), "%s"),
    }
