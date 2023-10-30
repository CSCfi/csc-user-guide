# Keeping docker images small

It is important to keep docker images small. The smaller the image is, the faster it will be pulled, speeding up deployments, both in production and development environments. In addition, bigger images get deleted from the nodes cache sooner. The maximum size for an image stored in Rahti's internal registry is 5GB. Images over 1GB are already considered very big images.

## Be mindful about what is added to the image

The first way to keep an image small is to by simply not adding unnecessary files. When developing is common to install full sources of libraries or other dependencies, for example the Linux kernel headers. These sources are not anymore necessary in production deployments.

## Keep data out of the image

Images should only contain the application's runtime. This means that the data needed to run the application should not be added to the image. This way not only the image is smaller, but we avoid a rebuild when the data changes. The data can be stored in an [external volume](../../../rahti4/storage/persistent/) (PVC) that will be attached to the Pod upon startup, or it can be stored in [Allas](../../../../data/Allas/) and downloaded during the startup or on demand when needed. Storing the data in Allas requires an extra logic in the application (or in a pre-load script) that understands where the data is and how to retrieve it.
data can be stored in a external volume (PVC) that will be attached to the Pod upon startup, or it can be stored in

## Reduce the number of layers

For every `Dockerfile` instruction (`RUN`, `COPY`, `CMD`, `EXPOSE`, ...), a new layer is added to the docker image. Each layer is stored as the difference from the previous one. This means that if some data is added in one layer, but removed in the next, the image will still contain said data. In order to see how much data each layer adds to the image, you may use:

`docker history image_name`

There are 3 approaches to reduce the number of layers:

* Combine layers in the `Dockerfile`. Sometimes there are several `RUN` instructions one after the other. They can be easily combined by using `&&`:

```Dockerfile
RUN apt update

RUN apt install git
```

will become:

```Dockerfile
RUN apt update && \
    apt install git
```

* Use multi stage builds (This feature was introduced in docker v17.05). The idea behind multi stage builds is to have several `FROM` commands in the same `Dockerfile`, each `FROM` starts a new stage in the build and does not carry the files from the previous stage, but allows copying files from the previous stages. The pattern used here is, to build the application in the first stage, and then in the second stage copy only the compiled application, leaving behind the sources and other compilation sub-products that we do not need to run the application. For example:

```Dockerfile
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

The example was taken from the [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/) article in Docker's documentation.

* Use [docker squash](https://github.com/jwilder/docker-squash). Docker squash is a user made tool to combine all layers that adds files into a single one:

```sh
docker save b7ec51bbc38f | sudo docker-squash -t squash -verbose | docker load
```

For more information, please check the documentation in the repository.

## Use a small base image

When creating an image, choosing the base image is an important task. There are almost always multiple base images available for certain need. These base images can be very different in content, maintenance, security, size, etc. It is a good practice to evaluate the available images and do some comparisons between them. It is often not a good idea to take the first random image you find and put it to production. One base image that is very commonly used and has lots of documentation available is [Alpine Linux](https://www.alpinelinux.org).

> Alpine Linux is a security-oriented, lightweight Linux distribution based on **musl libc** and **busybox**.

Currently the base image for Alpine (`docker.io/alpine`) is only 5.61 MB. For comparison, the sizes of Ubuntu's and CentOS' base images are 72.9 MB and 209 MB respectively. The biggest drawback that Alpine has versus other base images is that some applications are not compatible with [musl libc](https://en.wikipedia.org/wiki/Musl) and require `glibc`. Alpine will also have a smaller selection of software available in the repositories than Ubuntu or CentOS.

## Use `.dockerignore`

`.dockerignore` works in the same way as `gitignore` does, creates a black list of files that will not be added to the image. This way is possible to exclude files that are not needed to run the application.
