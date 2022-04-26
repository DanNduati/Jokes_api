<h1 align="center"><b>Test-Driven Development with FastAPI and Docker</b></h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/DanNduati/FastAPI-tdd)

## <b>Description</b>
This is a test-driven development approach to creating APIs with the FastAPI web framework.

## <b>Prerequisites</b>
- [Python3](https://www.python.org/downloads/)
- [Docker and Docker compose](https://docs.docker.com/get-docker/) (optional)

## <b>Setup</b>
### <b> 1. Local Setup</b>
#### clone the repository and navigate to the project directory
```bash
git clone git@github.com:DanNduati/FastAPI-tdd.git
cd project/
```
#### Create a python virtual environment activate it
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Install Project dependencies
```bash
pip install -r requirements.txt
```
#### Install Project dependencies
```bash
pip install -r requirements.txt
```
Create a `.env` file similar to [`.env.example`](./project/.env.example).

### Run uvicorn server
```bash
uvicorn app.main:app --reload
```

### <b> 2. Docker</b>

#### Build image and run container
Build the image and fire up the container in detached mode
```bash
docker compose --env-file ./project/.env up -d --build
```
#### Check logs for the `web` service
```bash
docker compose logs web
```
#### Access db directly via psql
```bash
docker compose exec web-db psql -U postgres
```
Then you can connect to the database:
```bash
postgres=# \c web_dev
# show jokes table definition
postgres=# \d jokes
#quit
postgres=# \q
```
View more psql commands in [me cheatsheet](https://github.com/DanNduati/cheatsheets/blob/main/Postgres.md)
## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)