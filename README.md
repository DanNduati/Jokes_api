<h1 align="center"><b>JokesAPI</b></h1>
<h2 align="center"><b>Test-Driven Development with FastAPI and Docker</b></h2>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/DanNduati/Jokes_api)
![Actions Status](https://github.com/DanNduati/Jokes_api/workflows/Build%20and%20Test/badge.svg)
## <b>Description</b>
The JokesAPI is a REST API that serves two part jokes.It supports a variety of filters that can be applied to get just the right jokes you need. It can be used without any for of API token or authentication. 

## <b>Prerequisites</b>
- [Python3](https://www.python.org/downloads/)
- [Docker and Docker compose](https://docs.docker.com/get-docker/) (optional)

## <b>Setup</b>
### <b>Docker</b>
#### Clone the repository
```bash
git clone https://github.com/DanNduati/Jokes_api.git
```

Create a `.env` file similar to [`.env.example`](./project/.env.example) inside the `project/` directory. 
Build the image and fire up the container in detached mode
```bash
$ docker compose up -d --build
```
#### Run aerich migration
```bash
$ docker compose exec web aerich upgrade
```
#### Run the tests
```bash
$ docker compose exec web python -m pytest -v
```
#### Run tests with coverage
```bash
$ docker compose exec web python -m pytest --cov="."
```
### <b> JokesBorrower</b>
Ive created a joke sourcing script as well and its usage and documentation can be found [here](https://github.com/DanNduati/Jokes_borrower)


## <b>Endpoints and Usage</b>
1. Local BaseUrl: http://0.0.0.0:6969/
2. Heroku BaseURL: https://gentle-dusk-50795.herokuapp.com/
### <b> 1. Adding/Submitting a Joke </b>
```http
POST /jokes/
```
__Sample request__
```bash
curl -X 'POST' \
  'https://gentle-dusk-50795.herokuapp.com/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "setup": "What do you call a witch at the beach?",
    "punchline": "A Sandwich.",
    "type": "Pun"
}'
```
__Sample response__
```json
{
  "id": 253,
  "setup": "What do you call a witch at the beach?",
  "punchline": "A Sandwich.",
  "type": "Pun"
}
```
### <b> 2. Getting Jokes </b>
This endpoint is the one you want to call to get joke(s). 
#### Get Joke(s)
##### Filtering Jokes
The JokesAPI has versatile filtering options. There are three different filtering methods in JokeAPI:
- Joke Type
- Search string
- Joke Count
- ID Range

All of these filtering options are enforced by the following url query parameters to the `/jokes` endpoint:
- `?type`
- `?contains`
- `?count`
- `?id_range`

__Example Usage__
#### __Joke type filter__
These are all the available joke types: ` Misc, Programming, Dark, Pun, Spooky, Christmas`. To set the category you want, you need to parse it to the query parameter `?type`:

`?type=<Joke type>`

__Sample request__
```bash
curl -X 'GET' \
  'https://gentle-dusk-50795.herokuapp.com/?type=pun' \
  -H 'accept: application/json'
```
__Sample response__
```json
[
  {
    "id": 8,
    "setup": "Thank you student loans for getting me through college.",
    "punchline": "I don't think I'll ever be able to repay you.",
    "type": "Pun"
  },
  {
    "id": 14,
    "setup": "What do you call a witch at the beach?",
    "punchline": "A Sandwich.",
    "type": "Pun"
  }
]
```
#### __Search string filter__
If a search string filter is used, only jokes that contain the specified string in either the `setup` or the `punchline` fields are returned. Parse the search string to the `?contains` query parameter as follows:

`?contains=<search string>`

__Sample request__
```bash
curl -X 'GET' \
  'https://gentle-dusk-50795.herokuapp.com/?contains=psychiatrist' \
  -H 'accept: application/json'
```
__Sample response__
```json
[
  {
    "id": 10,
    "setup": "I told my psychiatrist I got suicidal tendencies.",
    "punchline": "He said from now on I have to pay in advance.",
    "type": "Dark"
  }
]
```

#### __Joke count filter__
This filter allows you to set a certain amount of jokes to receive in a single call to the `Get Joke` endpoint.You can set it using the `?count` URL parameter. JokesAPI defaults to the maximum (10) jokes per requests `0<number<=10`

`?count=<number>`

__Sample request__
```bash
curl -X 'GET' \
  'https://gentle-dusk-50795.herokuapp.com/?count=5' \
  -H 'accept: application/json'
```
__Sample response__
```json
[
  {
    "id": 1,
    "setup": "How many programmers does it take to screw in a light bulb?",
    "punchline": "None. It's a hardware problem.",
    "type": "Programming"
  },
  {
    "id": 2,
    "setup": "Why did the web developer walk out of a resturant in disgust?",
    "punchline": "The seating was laid out in tables.",
    "type": "Programming"
  },
  {
    "id": 3,
    "setup": "Why is 6 afraid of 7 in hexadecimal Canada?",
    "punchline": "Because 7 8 9 A?",
    "type": "Programming"
  },
  {
    "id": 4,
    "setup": "Programming is like sex.",
    "punchline": "Make one mistake and you end up supporting it for the rest of your life.",
    "type": "Programming"
  },
  {
    "id": 5,
    "setup": "Hey, wanna hear a joke?",
    "punchline": "Parsing HTML with regex.",
    "type": "Programming"
  }
]
```

#### __ID Range filter__
If an ID Range filter is used, only jokes inside the specified ID range are returned. Parse the ID range string to the `?id_range` query parameter as follows:

`?id_range=number-number`

__Sample request__
```bash
curl -X 'GET' \
  'https://gentle-dusk-50795.herokuapp.com/?id_range=6-9' \
  -H 'accept: application/json'
```
__Sample response__
```json
[
  {
    "id": 6,
    "setup": "Why do programmers confuse Halloween and Christmas?",
    "punchline": "Because Oct 31 = Dec 25",
    "type": "Programming"
  },
  {
    "id": 7,
    "setup": "Why does no one like SQLrillex?",
    "punchline": "He keeps dropping the database.",
    "type": "Programming"
  },
  {
    "id": 8,
    "setup": "Thank you student loans for getting me through college.",
    "punchline": "I don't think I'll ever be able to repay you.",
    "type": "Pun"
  },
  {
    "id": 9,
    "setup": "Why is every gender equality officer female?",
    "punchline": "Because it's cheaper.",
    "type": "Misc"
  }
]
```

#### __Applying multiple filters__
You can combine multiple filters by combining the query parameters. The parameters need to be prefixed by a single question mark (?) and separate key/value pairs need to be delimited from another by an ampersand (&). Keys are separated from values with an equals sign (=).

Example: `https://gentle-dusk-50795.herokuapp.com/?count=2&joke_type=Programming&contains=program&id_range=1-5`

__Request__
```bash
curl -X 'GET' \
  'https://gentle-dusk-50795.herokuapp.com/?count=2&joke_type=Programming&contains=program&id_range=1-5' \
  -H 'accept: application/json'
```

__Sample response__
```json
[
  {
    "id": 1,
    "setup": "How many programmers does it take to screw in a light bulb?",
    "punchline": "None. It's a hardware problem.",
    "type": "Programming"
  },
  {
    "id": 4,
    "setup": "Programming is like sex.",
    "punchline": "Make one mistake and you end up supporting it for the rest of your life.",
    "type": "Programming"
  }
]
```

### <b>3. Getting a joke by id</b>
```http
GET /jokes/<id>/
```
__Sample request__
```bash
curl -X 'GET' \
  'https://gentle-dusk-50795.herokuapp.com/1' \
  -H 'accept: application/json'
```
__Sample response__
```json
{
  "id": 1,
  "setup": "How many programmers does it take to screw in a light bulb?",
  "punchline": "None. It's a hardware problem.",
  "type": "Programming"
}
```
### <b> 4. Update a Joke by id </b>
```http
PUT /jokes/<id>/
```
__Sample request__
```bash
curl -X 'PUT' \
  'https://gentle-dusk-50795.herokuapp.com/21/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "setup": "What'\''s the difference between an in-law and an outlaw?",
    "punchline": "An outlaw is wanted.",
    "type": "Misc"
}'
```
__Sample response__
```json
{
  "id": 256,
  "setup": "What's the difference between an in-law and an outlaw?",
  "punchline": "An outlaw is wanted.",
  "type": "Misc"
}
```
### <b> 5. Delete a Joke by id </b>
```http
DELETE /jokes/<id>/
```
__Sample request__
```bash
curl -X 'DELETE' \
  'https://gentle-dusk-50795.herokuapp.com/2/' \
  -H 'accept: application/json'
```
__Sample response__
```json
{
  "message": "Deleted joke with id 2"
}
```
You can also interact with the endpoints at http://0.0.0.0:6969/docs
## <b>Built with</b>
- FastAPI
- Docker 
- [Jokesborrower](https://github.com/DanNduati/Jokes_borrower)

## Todo
- [x] Implement remaining endpoints -> delete and update
- [x] Implement id range joke filtering option
- [x] Look into Uptime monitoring 
- [x] Experiment with rate limiting

## <b>License</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)