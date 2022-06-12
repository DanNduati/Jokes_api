# Github packages setup
[GitHub Packages](https://github.com/features/packages) is a package management service, fully integrated with GitHub. It allows you to host your software packages, publicly or privately, for use within your projects on GitHub. i'll use it to store Docker images.
Process summarized below can be found [here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

## Create a personal access token
Within the developer settings click `Personal access tokens` then click on `Generate new token`. Provide a descriptive note and select the following scopes
1. `write:packages`
2. `read:packages`
3. `delete:packages`
4. `workflow`

Copy the generated token

## Save your PAT as an environment variable 
```bash
$ export CR_PAT=YOUR_TOKEN
```
## Sign in to the Container registry service at `ghcr.io`
```bash
$ echo $CR_PAT | docker login ghcr.io -u DanNduati --password-stdin
> Login Succeeded
```
## Build and tag the image
```bash
$ docker build -f project/Dockerfile.prod -t ghcr.io/dandduati/jokes_api/jokesapi:latest ./project
```

## Push the image to the Container registry on Github Packages
```bash
$ docker push ghcr.io/dannduati/jokes_api/jokesapi:latest
The push refers to repository [ghcr.io/dannduati/jokes_api/jokesapi]
c67915f15faa: Pushed 
c7e9fccbbd11: Pushed 
d9add86eb6a0: Pushed 
dc4b8a4404da: Pushed 
546f2f05e91c: Pushed 
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
latest: digest: sha256:29e7f16b3206ffece3f97a38a8fd17241550420bfd190d16cdfeef7848a82a4f size: 3465
```
You should be able to see the package at the following URL:
