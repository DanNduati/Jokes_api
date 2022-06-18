from typing import List, Optional, Union

from app.models.models import Joke_pydantic, Jokes
from app.models.schemas import JokeCreate
from fastapi import APIRouter, HTTPException, Query, status
from tortoise.expressions import Q

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.post("/", response_model=Joke_pydantic, status_code=status.HTTP_201_CREATED)
async def add_joke(joke: JokeCreate):
    """
    Add/create a joke
    """
    # jk = Jokes(setup=joke.setup, punchline=joke.punchline, type=joke.type)
    # await jk.save()
    joke_obj = await Jokes.create(**joke.dict())
    return await Joke_pydantic.from_tortoise_orm(joke_obj)


@router.get("/", response_model=List[Joke_pydantic])
async def get_jokes(
    count: Optional[int] = Query(default=5, gt=0, le=10),
    type: Union[List[str], None] = Query(
        default=["Pun", "Programming", "Dark", "Misc", "Spooky", "Christmas"]
    ),
    contains: Optional[str] = "",
):
    """
    Get jokes
    """
    print(type)
    return await Joke_pydantic.from_queryset(
        Jokes.filter(type__in=type)
        .filter(Q(setup__icontains=contains) | Q(punchline__icontains=contains))
        .limit(limit=count)
        .all()
    )


@router.get("/{joke_id}", response_model=Joke_pydantic)
async def get_joke(joke_id: int):
    """
    Get joke by id
    """
    joke_obj = await Jokes.filter(id=joke_id).count()
    if not joke_obj:
        print("Joke does not exist!!")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"joke with id {joke_id} was not found",
        )
    return await Joke_pydantic.from_queryset_single(Jokes.get(id=joke_id))
