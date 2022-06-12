<h1 align="center"><b>JokesAPI<b></h1>
<h2 align="center"><b>Test-Driven Development with FastAPI and Docker</b></h2>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/DanNduati/Jokes_api)

## <b>Description</b>
The JokesAPI is a test-driven development project. This is me learning how to develop and test an asynchronous API built with FastAPI, Postgres, pytest and Docker.

## <b>Prerequisites</b>
- [Python3](https://www.python.org/downloads/)
- [Docker and Docker compose](https://docs.docker.com/get-docker/) (optional)

## <b>Setup</b>
### <b>Docker</b>
#### Build image and run container
Build the image and fire up the container in detached mode
```bash
$ docker compose up -d --build
```
#### Check logs for the `web` service
```bash
$ docker compose logs web
```
#### Run aerich migration
```bash
$ docker compose exec web aerich upgrade
```

#### Run the tests
```bash
$ docker compose exec web python -m pytest -v
```
#### Test it out with curl or [HTTPie](https://httpie.org/):
```bash
$ http --format-options json.sort_keys:false --pretty=all get http://0.0.0.0:6969/jokes/
HTTP/1.1 200 OK
content-length: 692
content-type: application/json
date: Sun, 12 Jun 2022 07:32:53 GMT
server: uvicorn

[
    {
        "id": 1,
        "setup": "why was the pig covered in ink?",
        "punchline": "Because he lived in a pen",
        "type": "pun"
    },
    {
        "id": 2,
        "setup": "What is the difference between acne and a catholic priest?",
        "punchline": "Acne usually comes on a boys face after he turns 12.",
        "type": "dark"
    },
    {
        "id": 3,
        "setup": "What's the difference between an in-law and an outlaw?",
        "punchline": "An outlaw is wanted.",
        "type": "Misc"
    },
    {
        "id": 4,
        "setup": "Why are cats so good at video games?",
        "punchline": "they have nine lives.",
        "type": "misc"
    },
    {
        "id": 5,
        "setup": "what is the least spoken language in the world?",
        "punchline": "Sign Language",
        "type": "dark"
    },
    {
        "id": 6,
        "setup": "Why are cats so good at video games?",
        "punchline": "they have nine lives.",
        "type": "misc"
    }
]
```
You can also interact with the endpoints at http://0.0.0.0:6969/docs
## <b>Built with</b>
- Python 3.7
- FastAPI
- Docker
- Pipenv
- Black
- Isort

## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)