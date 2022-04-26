<h1 align="center"><b>Test-Driven Development with FastAPI and Docker</b></h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/DanNduati)

## <b>Description</b>
This is 

## <b>Prerequisites</b>
- [Python3](https://www.python.org/downloads/)
- [Docker and Docker compose](https://docs.docker.com/get-docker/) (optional)

## <b>Setup</b>
### <b> 1. Local Setup</b>
#### clone the repository and navigate to the project directory
```bash
git clone git@github.com:DanNduati/.git
cd /
```
#### Create a python virtual environment activate it
```bash
cd project/
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
#### 1. Build the image
```bash
docker-compose build
```

#### 2. Start the container
Once the build is done, fire up the container
```bash
ocker compose --env-file ./project/.env up
```

## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)