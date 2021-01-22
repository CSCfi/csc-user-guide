# Keeping docker images small

It is important to keep docker image small. The smaller the image is, the faster it will be pulled, speeding up deployments, both in production and development environments. In addition, bigger images get deleted from the nodes cache sooner. The maximum size for an image stored in Rahti's internal regiatry is 5GB. Images over 1GB are already considered very big images.

## Be mindfull about what is added to the image

The first way to keep an image small is to by simply not adding unnecessary files. When developing is common to install full sources of libraries or other dependencies, for example the Linux kernel headers. These sources are not anymore necessatry in production deployments.

## Reduce the number of layers

For every `Dockerfile` instruction (`RUN`, `COPY`, `CMD`, `EXPOSE`, ...), a new layer is added to the docker image. Each layer is stored as the difference from the previous one. This means that if some data is added in one layer, but removed in the next, the image will still contain said data. In order to see how much data each layer adds to the image, you may use:

`docker history image_name`

There are 3 approaches to reduce the number of layers:

* Combine layers in the `Dockerfile`. Sometimes there are several `RUN` instructions one after the other. They can be easily convined by using `&&`:

```
RUN apt update

RUN apt install git
```

will become:

```
RUN apt update && \
    apt install git
```

* Use multi stage builds (This feature was introduced in docker v17.05). The idea behind multi stage builds is to have several `FROM` commands in the same `Dockerfile`, each `FROM` starts a new stage in the build and does not carry the files from the previous stage, but allows copying files from the previous stages. The pattern used here is, to build the application in the first stage, and then in the second stage copy only the compiled application, leaving behind the sources and other compilation subproducts that we do not need to run the application. For example:

```
FROM golang:1.7.3
WORKDIR /go/src/github.com/alexellis/href-counter/
RUN go get -d -v golang.org/x/net/html
COPY app.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/alexellis/href-counter/app .
CMD ["./app"]
```

The example was taken from the [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) article in docker's documentation.

* Use [docker squash](https://github.com/jwilder/docker-squash). Docker squash is a user made tool to combine all layers that adds files into a single one:

```
docker save b7ec51bbc38f | sudo docker-squash -t squash -verbose | docker load
```

For more information, please check the documentation in the repository.

## Use a small base image

The most common image to use as a base in the `FROM` is Alpine Linux.

> Alpine Linux is a security-oriented, lightweight Linux distribution based on **musl libc** and **busybox**.

Currently the base image for Alpine (`docker.io/alpine`) is only 5.61 MB. For comparison, the sizes of ubuntu's and cento's base images are 
72.9 MB and 209 MB respectevely. The biggest drawback that Alpine has versus other base images is that some applications are not compatible with [musl libc](https://en.wikipedia.org/wiki/Musl) and require `glibc`.

## Keep data out of the image

Images should only contain the application's runtime. This means that the data needed to run the applicatiuon should not be added to the image. This way not only the image is smaller, but we avoid rebuilding i when the data changes. The data can de stored in a external volume (PVC) that will be attached to the Pod upon startup, or it can be stored in Allas and downloaded during the startup or on demand when needed. Storing the data in Allas requires an extra logic in the application (or in a preload script) that understands where the data is and how to retrieve it.

## Use `.dockerignore`

`.dockerignore` works in the same way as `gitignore` does, creates a black list of files that will not be added to the image. This way is possible to exclude files that are not needed to run the application.

