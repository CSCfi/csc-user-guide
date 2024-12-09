# Multistage builds

The idea behind _multistage builds_ is to make it easy to build smaller container images by facilitating the exclusion of intermediate build files from the final product.

Smaller container images take less space on disk, meaning they take less time to download and deploy. During the compilation of software, it is common to need a compiler, several library dependencies, and intermediate objects that will not be needed during the execution of the program. Multistage builds allow you to define two or more docker build stages in the same `Dockerfile`. They will be executed in order one after the other, and each "stage" will be able to copy files from the previous ones. This way, we can easily and in the same build process, build the software and then keep only the files that we actually need for the execution.

## Usage

First create a new go project or have an existing go initialize project.

* To initialize a new go project as an example:

```sh
go mod init example.com/go-server
```

Take this `Dockerfile`:

* `Dockerfile`:

```Dockerfile
FROM golang:1.18.3-stretch as builder

RUN mkdir -p /go/src/server
WORKDIR /go/src/server

COPY go.mod go.sum ./
RUN go mod download && go mod verify 

COPY . .

RUN CGO_ENABLED=0 go build server.go

FROM alpine:edge

RUN mkdir /app
COPY --from=builder /go/src/server/server /app/server
CMD ["/app/server"]
```

and this code (golang):

* `server.go`:

```
package main

import (
    "fmt"
    "strings"
    "net/http"
    "github.com/pborman/uuid"
)

func main() {
    http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
        uuidWithHyphen := uuid.NewRandom()
        uuid := strings.Replace(uuidWithHyphen.String(), "-", "", -1)
        fmt.Fprintf(w, "Welcome to my website!\n")
        fmt.Fprintf(w, uuid)
    })

    fmt.Print("Starting server in port 8080...\n")

    http.ListenAndServe(":8080", nil)
}
```
Then run `go mod tidy`, which will download all the dependencies that are required in your source files and update `go.mod` file with that dependency. In this case it will download `github.com/pborman/uuid`.

The `dockerfile` can be divided into two parts (or stages), each starting by the `FROM` instruction:

1. `FROM golang:1.18.3-stretch as builder`, uses the official golang image containing everything we need to compile the code. It is labeled as `builder`. We copy `go.mod and go.sum` and download the package dependencies to the "working directory". We copy the whole "working directory", including the code with `COPY . .`, and finally compile the code with `RUN CGO_ENABLED=0 go build server.go`.
2. `FROM alpine:edge`, uses the minimal distribution `alpine`. In the line `COPY --from=builder /go/src/server/server /app/server` the compiled program and only the compiled program is copied from the previous stage (`build`).

In order to test this build process, put the two files in the same directory and name them `Dockerfile` and `server.go`. Then run the command:

```sh
docker build . -t go-server
```

This will produce the image called `go-server:latest`. To check the size of the image just run:

```sh
$ docker images go-server
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
go-server    latest    173c922261a3   16 minutes ago   12.1MB
```

it should give you approximately 12MB, which is more than half (~7MB) is the compiled code.

If you pull the image `golang:1.18.3-stretch` (the one we used for building the code) and check its size, you will see that it is approximately `890 MB`.

```sh
$ docker images golang:1.18.3-stretch
REPOSITORY   TAG              IMAGE ID       CREATED       SIZE
golang       1.18.3-stretch   6ee1deda35bd   12 days ago   890 MB
```

This same small image (`go-server:latest`) is of course also achievable by other methods. You can build the code outside of docker and then copy it to the `alpine` image. You can mount the code directory into the build image, build it and then again copy the compiled product into the `alpine` image. But none of these methods are as easy and compact as this one.

## Usage in Rahti 2

In order to test this in Rahti 2, one only needs to login in Rahti 2, select the correct project, and run:

```sh
oc new-build https://github.com/cscfi/multi-stage-build.git

```

**NOTE**: The code must be in a git repository and Rahti 2 must be able to clone it.

The end result will be an image called `multi-stage-build` stored in the internal Rahti 2 registry of the project you selected. This image can then be used in a Rahti 2 deployment using the image stream option when deploying an image.

## Upstream documentation

* [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)
