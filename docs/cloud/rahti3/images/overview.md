<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/images/overview/)

# Docker images

A Docker image is a file which is built up normally by an instructional file named **Dockerfile**. An Docker image is immutable, i.e. existing image file cannot be modified, but one can create a new layer to it & thus have a modified version of image suitable to him.

Docker containers are the running instances of Docker images. To avoid confusions, lets have a quick walkthrough over Docker image & containers using cooking example:

* Dockerfile could be regarded as the ingredients list.
* Docker Images are ingredients mixed together.
* Docker Container is cooked delicious meal: The final end product!

To better explain these analogies, let's follow some examples.

First, in order to run a docker image one can use the docker client on the host machine (provided that it is installed):

```sh
docker run -it centos
```

This will, if the image is not cached locally, first pull (or download) the latest centos image, then look for the predefined entry point, and finally a container is run with an interactive session. The output will be something like:

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

* Then it is the path for the image, in this case it is `/library`. Again docker is assuming it, this path is reserved to "official base images", or in other words common Linux distributions, from where other images are based on.

* Next, you have the image name itself, `centos`. There are a lot of other "base images" in `docker.io/library`, like for example, `ubuntu` or `alpine`.

* Finally, it is the tag, `latest`. This is the default tag for an image, but an image can have any given name for a tag. This is used to differentiate between version of the same image. Examples for `centos` are: `8`, `7`, `8.1.1911`, and lots more. The contents of a given tag can change with time, `latest` will be always the most updated version. But other tags are left unchanged after they are released.

Official page of [CentOS](https://hub.docker.com/_/centos) on Docker hub provide us more details how different tagged versions of official CentOS image is build. So author used following **Dockerfile** created our `centos:latest` image:

```sh
FROM scratch
ADD centos-8-x86_64.tar.xz /

LABEL org.label-schema.schema-version="1.0" \
    org.label-schema.name="CentOS Base Image" \
    org.label-schema.vendor="CentOS" \
    org.label-schema.license="GPLv2" \
    org.label-schema.build-date="20200611"

CMD ["/bin/bash"]
```

## Advanced image internals

Many times author of Docker images don't necessarily provide details of Dockerfile which were used to build Docker images. It is therefore good idea to inspect images from unknown sources. You can see the detailed information of image internal using `docker inspect`. The output is a JSON object, that can be processed using standard tools like `jq`, see an example at the bottom of this page.

This allows to see interesting data about the image, like the environment, the entry point, initial command, the layers, and many more.

```bash
$ docker inspect centos
[
  {
    "Id": "sha256:831691599b88ad6cc2a4abbd0e89661a121aff14cfa289ad840fd3946f274f1f",
    "RepoTags": [
      "docker.io/centos:8",
      "docker.io/centos:latest"
    ],
    "RepoDigests": [
      "docker.io/centos@sha256:4062bbdd1bb0801b0aa38e0f83dece70fb7a5e9bce223423a68de2d8b784b43b"
    ],
    "Parent": "",
    "Comment": "",
    "Created": "2020-06-17T00:22:25.47282687Z",
    "Container": "0a6b8cbdee7218d1da84145e867c8ce1c36d226a5cfca208125d08ac56f7c5af",
    "ContainerConfig": {
      "Hostname": "0a6b8cbdee72",
      "Domainname": "",
      "User": "",
      "AttachStdin": false,
      "AttachStdout": false,
      "AttachStderr": false,
      "Tty": false,
      "OpenStdin": false,
      "StdinOnce": false,
      "Env": [
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
      ],
      "Cmd": [
        "/bin/sh",
        "-c",
        "#(nop) ",
        "CMD [\"/bin/bash\"]"
      ],
      "ArgsEscaped": true,
      "Image": "sha256:72ff1748d360d0069c91508ca3ffde0d7748989c75d193eee3b0e85c62557efa",
      "Volumes": null,
      "WorkingDir": "",
      "Entrypoint": null,
      "OnBuild": null,
      "Labels": {
        "org.label-schema.build-date": "20200611",
        "org.label-schema.license": "GPLv2",
        "org.label-schema.name": "CentOS Base Image",
        "org.label-schema.schema-version": "1.0",
        "org.label-schema.vendor": "CentOS"
      }
    },
    "DockerVersion": "18.09.7",
    "Author": "",
    "Config": {
      "Hostname": "",
      "Domainname": "",
      "User": "",
      "AttachStdin": false,
      "AttachStdout": false,
      "AttachStderr": false,
      "Tty": false,
      "OpenStdin": false,
      "StdinOnce": false,
      "Env": [
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
      ],
      "Cmd": [
        "/bin/bash"
      ],
      "ArgsEscaped": true,
      "Image": "sha256:72ff1748d360d0069c91508ca3ffde0d7748989c75d193eee3b0e85c62557efa",
      "Volumes": null,
      "WorkingDir": "",
      "Entrypoint": null,
      "OnBuild": null,
      "Labels": {
        "org.label-schema.build-date": "20200611",
        "org.label-schema.license": "GPLv2",
        "org.label-schema.name": "CentOS Base Image",
        "org.label-schema.schema-version": "1.0",
        "org.label-schema.vendor": "CentOS"
      }
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Size": 215320025,
    "VirtualSize": 215320025,
    "GraphDriver": {
      "Name": "overlay2",
      "Data": {
        "MergedDir": "/var/lib/docker/overlay2/a17bcaace42e15b7c026e1503296d6d59d3a71b80b0487a0ec9e931f79cdc459/merged",
        "UpperDir": "/var/lib/docker/overlay2/a17bcaace42e15b7c026e1503296d6d59d3a71b80b0487a0ec9e931f79cdc459/diff",
        "WorkDir": "/var/lib/docker/overlay2/a17bcaace42e15b7c026e1503296d6d59d3a71b80b0487a0ec9e931f79cdc459/work"
      }
    },
    "RootFS": {
      "Type": "layers",
      "Layers": [
        "sha256:eb29745b8228e1e97c01b1d5c2554a319c00a94d8dd5746a3904222ad65a13f8"
      ]
    }
  }
]
```
