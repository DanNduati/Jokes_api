from typing import List, Optional, Union

from app.models.models import Joke_pydantic, Jokes
from app.models.schemas import DeleteResponse, JokeCreate
from fastapi import APIRouter, HTTPException, Path, Query, status
from tortoise.expressions import Q

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.post("/", response_model=Joke_pydantic, status_code=status.HTTP_201_CREATED)
async def add_joke(joke: JokeCreate):
    """_Add a joke_

    Args:
        joke (JokeCreate): _valid joke json object_

    Returns:
        _Joke_: _Joke added_
    """
    joke_obj = await Jokes.create(**joke.dict())
    return await Joke_pydantic.from_tortoise_orm(joke_obj)


@router.get("/", response_model=List[Joke_pydantic])
async def get_jokes(
    count: Optional[int] = Query(
        default=10,
        gt=0,
        le=10,
        title="Jokes count",
        description="The number of jokes you want returned 0<count<=10",
    ),
    joke_type: Union[List[str], None] = Query(
        default=["Pun", "Programming", "Dark", "Misc", "Spooky", "Christmas"],
        title="Joke type string",
        description="Joke type from the 6 joke types ",
        max_length=15,
    ),
    contains: Optional[str] = Query(
        default="",
        title="Joke search string",
        description="Search for a joke that contains this search string",
        max_length=50,
    ),
    id_range: Optional[str] = Query(
        default="1-999",  # ToDo: Think of a better way to do this
        title="Jokes id range",
        description="Get jokes that are within the specified range of IDs",
        regex=r"\d+\-\d+",  # valid range should be of the form: "A decimal digit followed by the character - followed by a decimal digit"
    ),
):
    """_Get Jokes_

    Args:
        count (Optional[int], optional): _Number of jokes to return_. Defaults to 10.
        joke_type (Union[List[str], None], optional): _Joke type you want_. Defaults to Query( default=["Pun", "Programming", "Dark", "Misc", "Spooky", "Christmas"], title="Joke type string", description="Joke type from the 6 joke types ", max_length=15, ).
        contains (Optional[str], optional): _Search string_. Defaults to "".
        id_range (Optional[str],optional) : _Id Range of the jokes_ default to "".
    Returns:
        _list_: _List of Jokes_
    """
    return await Joke_pydantic.from_queryset(
        Jokes.filter(type__in=[x.capitalize() for x in joke_type])
        .filter(id__range=[int(id_) for id_ in id_range.split("-")])
        .filter(Q(setup__icontains=contains) | Q(punchline__icontains=contains))
        .limit(limit=count)
        .all()
    )


@router.get("/{joke_id}/", response_model=Joke_pydantic)
async def get_joke(joke_id: int = Path(..., title="The ID of the joke to get", gt=0)):
    """_Get a joke by id_

    Args:
        joke_id (int): _The ID of the joke to get_.

    Returns:
        _Joke_: _Joke_
    """
    joke_obj = await Jokes.filter(id=joke_id).count()
    if not joke_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"joke with id {joke_id} was not found",
        )
    return await Joke_pydantic.from_queryset_single(Jokes.get(id=joke_id))


@router.put("/{joke_id}/", response_model=Joke_pydantic)
async def update_joke(
    joke: JokeCreate,
    joke_id: int = Path(..., title="The ID of the joke to update", gt=0),
):
    """_Update a Joke_

    Args:
        joke (JokeCreate): _valid joke json object_
        joke_id (int): _The ID of the joke to update_.

    Returns:
        _Joke_: _Updated Joke_
    """
    joke_obj = await Jokes.filter(id=joke_id).all()
    if not joke_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"joke with id {joke_id} was not found",
        )
    updated_joke = await Jokes.filter(id=joke_id).update(**joke.dict())
    return await Joke_pydantic.from_queryset_single(Jokes.get(id=joke_id))


@router.delete("/{joke_id}/", response_model=DeleteResponse)
async def delete_joke(
    joke_id: int = Path(..., title="The ID of the joke to delete", gt=0)
):
    """_Delete a joke_

    Args:
        joke_id (int): _he ID of the joke to delete_.

    Returns:
        _str_: _Message with deleted joke id_
    """
    joke_obj = await Jokes.filter(id=joke_id).delete()
    if not joke_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"joke with id {joke_id} was not found",
        )

    return DeleteResponse(message=f"Deleted joke with id {joke_id}")
