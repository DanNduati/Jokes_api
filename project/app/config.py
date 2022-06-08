import logging
import os
from functools import lru_cache
from os.path import join

from pydantic import AnyUrl, BaseSettings, Field

log = logging.getLogger("uvicorn")

dotenv_path = join(os.getcwd(), ".env")


class Settings(BaseSettings):
    environment: str = Field(default="dev", env="ENVIRONMENT")
    testing: bool = Field(default=0, env="TESTING")
    database_url: AnyUrl = Field(..., env="DATABASE_URL")

    class Config:
        env_file = dotenv_path


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
