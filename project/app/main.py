from fastapi import FastAPI, Depends
from app.config import get_settings, Settings,settingz
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app=app,
    db_url=settingz.database_url,
    modules={"models":["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/ping")
async def pong(settings:Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment":settings.environment,
        "testing":settings.testing
    }