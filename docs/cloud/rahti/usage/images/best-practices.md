# Keeping container images small

It is important to keep container images small. Smaller images download faster, which reduces startup 
time for Pods in Kubernetes and improves the responsiveness of scaling operations. They also use less storage in 
registries and on cluster nodes, which matters in multi-tenant environments like Rahti. Moreover, a smaller image 
contains fewer packages and files, which reduces the potential attack surface and lowers the chance of including 
outdated or vulnerable components. This makes maintenance easier and improves overall security. Because smaller images 
contain only what the application actually needs, they are more predictable, easier to debug, and simpler to reproduce
across environments. Rahti's registry has an image size limit of 5 GiB.


## Use a minimal base image

Start with the smallest image that still provides what you need. Images like Alpine, UBI-minimal, or Distroless include 
only essential components, which significantly reduces the size of the final image and lowers the attack surface. Example:

```Dockerfile
FROM alpine:3.19
```


## Use multi-stage builds

Build your application in one stage that contains compilers and build tools, and copy only the final binary or required 
output into a much smaller runtime stage. This prevents large toolchains from ending up in the final image. Example:

```Dockerfile

FROM golang:1.21 AS builder
WORKDIR /app
COPY ../../images .
RUN go build -o app

FROM alpine:3.19
COPY --from=builder /app/app /usr/local/bin/app
CMD ["app"]
```

## Clean up package manager caches and temporary files

Package managers leave behind metadata, caches, and temporary files. Cleaning these in the same layer where they're 
created prevents them from being stored permanently in the image. Make sure to delete the temporray files in the same 
layer (i.e., the same `RUN` instruction). As cleaning them in another RUN command will add a new layer which still 
bloats the image. Example:

```Dockerfile
...
RUN apk add --no-cache build-base
```

## Use a **.dockerignore** file

The `.dockerignore` file allows you to exclude files like source control metadata, documentation, artifacts, and other 
unnecessary files reduces the build context and keeps them out of your image. This speeds up builds and avoids adding
unwanted content. Example:

```Dockerfile
.git
node_modules
tests/
docs/
*.log
```

## Install only what the application needs

Adding tools, debuggers, shells, or libraries “just in case” increases the image size and security risk. 
Stick to the minimal set of dependencies your application actually needs. Example:

**Bad (bloated image)**:

```Dockerfile
RUN apt-get update && apt-get install -y curl vim net-tools
```

**Better**:

```Dockerfile
RUN apt-get update && apt-get install -y curl
```


## Combine related commands into fewer layers.

Every **RUN** instruction creates a new layer. If you install packages in one layer and clean them in another, 
the unwanted content remains in earlier layers. Combining commands prevents this. Example:


**Bad (bloated image)**:

```Dockerfile

RUN apt-get update
RUN apt-get install -y python3
RUN rm -rf /var/lib/apt/lists/*
```

**Better (all in one layer)**:

```Dockerfile
RUN apt-get update && apt-get install -y python3 \
    && rm -rf /var/lib/apt/lists/*
```


## Keep data out of the image

Images should only contain the application's runtime. This means that the data needed to run the application should not 
be added to the image. In this way, not only the image is smaller, but we avoid a rebuild when the data changes. 
The data can be stored in an [external volume](../storage/storage_overview.md) that will be attached to the Pod upon startup, 
or it can be stored in a remote object storage like [LUMI-O](../../../../storage/lumio/index.md) and downloaded during
the startup or on demand when needed.
