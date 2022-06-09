<h1 align="center"><b>Test-Driven Development with FastAPI and Docker</b></h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/DanNduati/FastAPI-tdd)

## <b>Description</b>
This is a test-driven development approach to creating APIs with the FastAPI web framework.

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

## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)