# Heroku deployement
## Create a new app:
```bash
$ heroku create
Creating app... done, ⬢ gentle-dusk-50795
https://gentle-dusk-50795.herokuapp.com/ | https://git.heroku.com/gentle-dusk-50795.git
```

## Log in to the [Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime)
```bash
$ heroku container:login
```

## Provision a new Postgres database with the hobby-dev plan:
```bash
$ heroku addons:create heroku-postgresql:hobby-dev --app gentle-dusk-50795
 ›   Warning: heroku update available from 7.60.1 to 7.60.2.
Creating heroku-postgresql:hobby-dev on ⬢ gentle-dusk-50795... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-regular-08685 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation
```
## Build the production image and tag it with the following format:
```
registry.heroku.com/<app>/<process-type>
```
Replace `<app>` with the name of the Heroku app you have just created and <process-type> with `web` since this will be the [web dyno](https://www.heroku.com/dynos). something like: 

```bash
$ docker build -f project/Dockerfile.prod -t registry.heroku.com/gentle-dusk-50795/web ./project
```
To test locally :
```bash
$ docker run --name fastapi-tdd -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db -p 5003:8765 registry.heroku.com/gentle-dusk-50795/web:latest

[2022-06-12 08:30:31 +0000] [9] [INFO] Starting gunicorn 20.1.0
[2022-06-12 08:30:31 +0000] [9] [INFO] Listening at: http://0.0.0.0:8765 (9)
[2022-06-12 08:30:31 +0000] [9] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2022-06-12 08:30:31 +0000] [12] [INFO] Booting worker with pid: 12
[2022-06-12 08:30:31 +0000] [12] [INFO] Started server process [12]
[2022-06-12 08:30:31 +0000] [12] [INFO] Waiting for application startup.
[2022-06-12 08:30:31 +0000] [12] [INFO] Application startup complete.
```

Navigate to http://localhost:5003/ping/ you should see:
```json
{
  "ping": "pong",
  "environment": "prod",
  "testing": false
}
```

Bring down the container once done:
```bash
$ docker rm fastapi-tdd -f
```
## Push the image to the registry:

```bash
$ docker push registry.heroku.com/gentle-dusk-50795/web:latest
The push refers to repository [registry.heroku.com/gentle-dusk-50795/web]
35055b754b3b: Pushed 
49b480dda23e: Pushed 
0742a72a35f8: Pushed 
d1ad0ae124c1: Pushed 
167f0d653e76: Pushed 
90d6439d0967: Pushed 
a892e33c79a9: Pushed 
f997de4a3ef4: Pushed 
a4246c0f58f4: Pushed 
208f17034f75: Pushed 
fa8a2adf7020: Pushed 
1286c8c60b62: Pushed 
3c97f5d9ffd6: Pushed 
832439eadb07: Pushed 
0ad3ddf4a4ce: Pushed 
latest: digest: sha256:fde81df16ef47107fe249882736cadde25fe49feee9d878bf6391d7ae39fcfd8 size: 3464
```

## Release the image:
```bash
$ heroku container:release web --app gentle-dusk-50795
Releasing images web to gentle-dusk-50795... done
```
This will run the container. You should be able to view the app at https://gentle-dusk-50795.herokuapp.com/ping/.

## Apply the migrations
```bash
$ heroku run aerich upgrade --app gentle-dusk-50795
 ›   Warning: heroku update available from 7.60.1 to 7.60.2.
Running aerich upgrade on ⬢ gentle-dusk-50795... up, run.4149 (Free)
Success upgrade 0_20220426205932_init.sql
```

## Test remote heroku endpoints
Try adding a new joke
```bash
$ http --json POST https://gentle-dusk-50795.herokuapp.com/jokes/ \
> setup="What do you call a cheap circumcision?" \
> punchline="A rip off" \
> type="pun"
HTTP/1.1 201 Created
Connection: keep-alive
Content-Length: 94
Content-Type: application/json
Date: Sun, 12 Jun 2022 09:02:48 GMT
Server: uvicorn
Via: 1.1 vegur

{
    "id": 1,
    "setup": "What do you call a cheap circumcision?",
    "punchline": "A rip off",
    "type": "pun"
}
```