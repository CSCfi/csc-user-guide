# Creating images

## Building images localy

It is possible to build images localy, three steps are needed.

First a `Dockerfile` must be written, for example this:

```Dockerfile
FROM centos

RUN yum install -y git
CMD ["bash"]
```

This simply install `git` over `centos` and sets the default command as `bash`. The image will then have 3 layers (FROM, RUN and CMD), each of then doing changes over the previous. See the [Dockerfile](https://docs.docker.com/engine/reference/builder/) reference docs.

Then, the following command must be used to build the image:

```bash
docker build . -t docker.io/user/name:tag
```

And finally, to publish the image:

```bash
docker push docker.io/user/name:tag
```

## Using Rahti to build container images

This assumes that you have authorized a Rahti command line session and created
a project in Rahti. Instructions for that are shown in Chapter [Command line
tool usage](../usage/cli.md#cli-cheat-sheet).

**Steps:**

Create Rahti specific definitions with `oc new-build` command. Be sure
not to be in a directory under git version control:

```bash
$ oc new-build --to=my-hello-image:devel --name=my-hello --binary
```

Move to the directory that has `Dockerfile` and build-files:
```bash
$ cd my-docker-build
$ ls
Dockerfile  hello-world.jl
```

Start build with `oc start-build` command from build artifacts in current
directory and output the build process to local terminal:
```bash
$ oc start-build my-hello --from-dir=./ -F
```

The image will appear in the Rahti registry console
[registry-console.rahti.csc.fi/registry](https://registry-console.rahti.csc.fi),
and it will be visible to internet at
*docker-registry.rahti.csc.fi/build-tutorial/my-hello:devel* for docker
compatible clients.

For command line usage with docker compatible clients, the docker repository
password will be the access token shown when authorizing Rahti command line
session and user name can be `unused`.

The Docker CLI tool login instructions are also shown in the [Rahti registry
console](https://registry-console.rahti.csc.fi).
