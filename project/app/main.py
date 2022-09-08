import logging

from app.api import jokes, ping
from app.db import init_db
from fastapi import FastAPI

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI(
        title="JokesAPI",
        description=("The JokesAPI is a REST API that serves two part jokes."),
        version="0.0.1",
        docs_url="/",
        contact={
            "name": "Nduati Daniel",
            "url": "https://danielchege.me",
        },
        license_info={
            "name": "MIT",
            "url": "https://github.com/DanNduati/Jokes_api/blob/main/LICENSE",
        },
    )
    application.include_router(ping.router)
    application.include_router(jokes.router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
