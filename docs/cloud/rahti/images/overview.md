# Docker images

A docker image is similar to a VM image, in the sense that they are a set of packaged files. But the way docker images are used and created, differs greatly from VM images. To better explain this, let's follow some examples.

First, in order to use a docker image one only must do:

```sh
docker run -it centos
```

(provided `docker` is installed)

This will, if the image is not cached localy, first pull (or download) the latest centos image, then look for the predefined entry point, and finally a container is run with an interactive session. The output will be something like:

```sh
Unable to find image 'centos:latest' locally
Trying to pull repository docker.io/library/centos ... 
latest: Pulling from docker.io/library/centos
Digest: sha256:4062bbdd1bb0801b0aa38e0f83dece70fb7a5e9bce223423a68de2d8b784b43b
Status: Downloaded newer image for docker.io/centos:latest
[root@3e7667e83d13 /]#
```

The name in this example is `centos`, but as we can see, it is expanded first to `centos:latest` and then to `docker.io/library/centos:latest`, the different parts are:

* A domain name `docker.io`, this is the domain name of the docker registry where the image is located. If the domain name is not included, docker assumes it is default public docker registry, `docker.io`. But there are other registries, for example  `registry-console.rahti.csc.fi` is Rahti's private docker registry.

* Then it is the path for the image, in this case it is `/library`. Again docker is asuming it, this path is reserved to "official base images", or in other words common Linux distributions, from where other images are based on.

* Next, you have the image name itself, `centos`. There are a lot of other "base images" in `docker.io/library`, like for example, `ubuntu` or `alpine`.

* Finaly, it is the tag, `latest`. This is the default tag for an image, but an image can have any given name for a tag. This is used to differentiate between version of the same image. Examples for `centos` are: `8`, `7`, `8.1.1911`, and lots more. The contents of a given tag can change with time, `latest` will be always the most updated version. But other tags are left unchanged after they are released.
