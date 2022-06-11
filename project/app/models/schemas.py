from pydantic import BaseModel


class JokeCreate(BaseModel):
    setup: str
    punchline: str
    type: str


class JokesResponse(JokeCreate):
    id: int
