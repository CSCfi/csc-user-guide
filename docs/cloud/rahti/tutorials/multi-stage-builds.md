<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/tutorials/multi-stage-builds/)

# Multistage builds

The idea behind _multistage builds_ is to make it easy to build smaller container images by facilitating the exclusion of intermediate build files from the final product.

Smaller container images take less space on disk, meaning they take less time to download and deploy. During the compilation of software, it is common to need a compiler, several library dependencies, and intermediate objects that will not be needed during the execution of the program. Multistage builds allow you to define two or more docker build stages in the same `Dockerfile`. They will be executed in order one after the other, and each "stage" will be able to copy files from the previous ones. This way, we can easily and in the same build process, build the software and then keep only the files that we actually need for the execution.

## Usage

Take this `Dockerfile`:

* `Dockerfile`:

```Dockerfile
FROM golang:1.12.6-stretch as builder

RUN mkdir -p /go/src/server
WORKDIR /go/src/server

COPY . .

RUN go get .
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

The `dockerfile` can be divided into two parts (or stages), each starting by the `FORM` instruction:

1. `FROM golang:1.12.6-stretch as builder`, uses the official golang image containing everything we need to compile the code. It is labeled as `builder`. We copy the whole "working directory", including the code with `COPY . .`, we then get the dependencies `RUN go get .`, and finally compile the code with `RUN CGO_ENABLED=0 go build server.go`.
2. `FROM alpine:edge`, uses the minimal distribution `alpine`. In the line `COPY --from=builder /go/src/server/server /app/server` the compiled program and only the compiled program is copied from the previous stage (`build`).

In order to test this build process, put the two files in the same directory and name them `Dockerfile` and `server.go`. Then run the command:

```sh
docker build . -t go-server
```

This will produce the image called `go-server:latest`. To check the size of the image just run:

```sh
$ docker images go-server
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
go-server    latest    514583ab6fa1   17 hours ago   13MB
```

it should give you approximately 13MB, which is more than half (~7MB) is the compiled code.

If you pull the image `golang:1.12.6-stretch` (the one we used for building the code) and check its size, you will see that it is approximately `774MB`.

```sh
$ docker images golang:1.12.6-stretch
REPOSITORY   TAG              IMAGE ID       CREATED       SIZE
golang       1.12.6-stretch   9fe4cdc1f173   2 years ago   774MB
```

This same small image (`go-server:latest`) is of course also achievable by other methods. You can build the code outside of docker and then copy it to the `alpine` image. You can mount the code directory into the build image, build it and then again copy the compiled product into the `alpine` image. But none of these methods are as easy and compact as this one.

## Usage in Rahti

In order to test this in Rahti, one only needs to login in Rahti, select the correct project, and run:

```sh
oc new-build https://github.com/lvarin/multi-stage-build.git
```

**NOTE**: The code must be in a git repository and Rahti must be able to clone it.

The end result will be an image called `multi-stage-build` stored in the internal Rahti registry of the project you selected. This image can then be used in a Rahti deployment using the image stream option when deploying an image.

## Upstream documentation

* [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)
