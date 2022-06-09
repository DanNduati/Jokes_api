from pydantic import BaseModel


class JokeSchema(BaseModel):
    setup: str
    punchline: str
    type: str
