# Container Images

A container image is a packaged version of an application that includes everything it needs to run as a container: the application code,
its dependencies, libraries, and basic runtime environment. Images are built once and can be run consistently on 
any container platform like Rahti or even on local machines, ensuring that the application behaves the same across 
different environments.

Container images are built using a layered filesystem, where each layer represents a change to the image, such as 
adding files, installing packages, or modifying configuration. When these layers are stacked together, they form the 
complete container image. An image is immutable, because different layers of the filesystem are read-only. However, you can add more layers 
to the image, therefore, create modified version suitable for your use.

A container is a running instance of that image. When Kubernetes starts a Pod, it takes the image, adds a writable
layer on top of it, and runs the application inside an isolated environment. Multiple containers can be created from the same image.
Containers are the running instances of Docker images. 




## Instantiate an image

To better explain these concepts, let's follow some examples. First, in order to run images you will need to install a 
container engine like [Docker](https://docs.docker.com/engine/install/) or [Podman](https://podman.io/docs/installation),
in this bellow example we consider docker but the same commands works with podman. In a local terminal, run the
following command


```sh
docker run -p 80:80 nginx
```

You should see a similar output:

```sh
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
88770be1d442: Pull complete 
b89cf3ec7a3e: Pull complete 
bb8ecb62799c: Pull complete 
2254fb813b11: Pull complete 
40b6fc5618c6: Pull complete 
cf9a807fe41d: Pull complete 
cc57e8335c98: Pull complete 
Digest: sha256:553f64aecdc31b5bf944521731cd70e35da4faed96b2b7548a3d8e2598c52a42
Status: Downloaded newer image for nginx:latest
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/11/28 13:04:36 [notice] 1#1: using the "epoll" event method
2025/11/28 13:04:36 [notice] 1#1: nginx/1.29.3
2025/11/28 13:04:36 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2025/11/28 13:04:36 [notice] 1#1: OS: Linux 6.12.54-linuxkit
2025/11/28 13:04:36 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/11/28 13:04:36 [notice] 1#1: start worker processes
2025/11/28 13:04:36 [notice] 1#1: start worker process 29
2025/11/28 13:04:36 [notice] 1#1: start worker process 30
2025/11/28 13:04:36 [notice] 1#1: start worker process 31
2025/11/28 13:04:36 [notice] 1#1: start worker process 32
2025/11/28 13:04:36 [notice] 1#1: start worker process 33
2025/11/28 13:04:36 [notice] 1#1: start worker process 34
2025/11/28 13:04:36 [notice] 1#1: start worker process 35
2025/11/28 13:04:36 [notice] 1#1: start worker process 36
2025/11/28 13:04:36 [notice] 1#1: start worker process 37
2025/11/28 13:04:36 [notice] 1#1: start worker process 38
```

In this example, the name of the image to instantiate as a container is `nginx`. First, Docker checks if the image is 
cached locally, if not, Docker tries to pulls it from its default remote registry called Docker Hub. The logs show the 
process of pulling the different layers. Docker, then, creates a new container from the pulled image, by setting up 
the container filesystem (image layers + writable layer), and preparing isolated namespaces (process, network, etc.). 
Once done, Docker starts the container's main process (NGINX web server in the case of this image). It is possible to 
inspect the running containers using the following command:


```sh
docker ps
```

The output should be similar to:

```sh
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                 NAMES
4e6598415a0c   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 5 seconds   0.0.0.0:80->80/tcp, [::]:80->80/tcp   cranky_carver
```

You can see information about the running containers including the image used for creating them.


## Image tags


Image tags are labels used to identify different versions of a container image. A tag is added after the image name, 
separated by a colon. For example, in `nginx:1.25`, the tag is `1.25`. Tags allow you to specify exactly which version 
of an image you want to run. Common patterns include version numbers, release names, or special tags like `latest`.
If you do not specify a tag, the system assumes `:latest` as in our previous example.  In order to instantiate 
version 1.25 of NGINX server, simply run:

```sh
docker run -p 80:80 nginx:1.25
```

## Image architecture

Container images are built for a specific CPU architecture, such as amd64 (x86_64) or arm64. The architecture 
defines the type of machine the image can run on. An image built for one architecture cannot run on a different one, 
because the machine instructions inside the image are not compatible.

When building or pulling container images, the runtime chooses the correct architecture automatically if a 
multi-architecture image is available. Otherwise, you must ensure that the image’s architecture matches the machine 
running it.

You can inspect the architecture of an image using the following command:

```sh
docker image inspect nginx:latest --format='{{.Architecture}}'
```


!!! warning "Note"
    Images built on machines with architecture other than **amd64** are not runnable on Rahti. Either re-build them on 
    an **amd64** machine or convert them. You can also rebuild them directly in Rahti as described in the [next section](./creating.md).


## Image registries

An image registry is a service where container images are stored, managed, and distributed. Registries act as central 
repositories that engines like Docker, Podman, and Kubernetes use to pull the images needed to run containers. Registries
are organized into repositories, and each repository can contain multiple tagged versions of an image. 
For example, `nginx:1.25` and `nginx:latest` are two tags within the same repository called `nginx`.

Public registries, such as [Docker Hub](https://hub.docker.com/) or [Quay.io](https://quay.io/), host images that 
anyone can pull. Private registries require authentication and are commonly used to store internal or sensitive images. 
Kubernetes clusters like Rahti can pull from both public and private registries as long as the required credentials 
are provided. Moreover, Rahti provide its own [integrated registry](./integrated-registry.md) that allows 
you to store, pull, and publish your images.

## The Open Container Initiative (OCI) standard

The Open Container Initiative defines open standards for container technology. Its two main specifications are:

* OCI Image Format — how container images are structured.

* OCI Runtime Format — how containers are started and run.

Because Docker, Podman, Kubernetes, and most registries follow OCI standards, images built with one tool can be stored
and ran on any OCI-compliant platform. This ensures portability and compatibility across different container 
environments and technologies.

## Next steps

- [Creating an image](./creating.md) — build your own images, locally or directly in Rahti.
- [Rahti integrated registry](./integrated-registry.md) — store, pull, and publish images in your Rahti project.
- [Best practices](./best-practices.md) — recommendations to keep your images small, secure, and maintainable.
