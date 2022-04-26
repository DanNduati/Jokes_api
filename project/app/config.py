import os
import logging
from os.path import join
from pydantic import BaseSettings, Field,AnyUrl

log = logging.getLogger("uvicorn")

dotenv_path = join(os.getcwd(),".env")

class Settings(BaseSettings):
    environment: str = Field(default="dev", env="ENVIRONMENT")
    testing: bool = Field(default=0,env="TESTING")
    database_url:AnyUrl = Field(...,env="DATABASE_URL")
    class Config:
        env_file = dotenv_path

settings = Settings()