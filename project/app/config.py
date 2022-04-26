import os
import logging
from os.path import dirname,join
from functools import lru_cache
from pydantic import BaseSettings, Field

log = logging.getLogger("uvicorn")

dotenv_path = join(os.getcwd(),".env")
#dotenv_path = dirname(__file__)

class Settings(BaseSettings):
    environment: str = Field(default="dev", env="ENVIRONMENT")
    testing: bool = Field(default=0,env="TESTING")
    class Config:
        env_file = dotenv_path
        
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()