<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/images/creating/)

# Creating images

There are several reasons to make your own docker image, but mostly there are two. The application you want to run does not have a docker image available, or there is an image available, but it is not working on OpenShift. Due to the fact that OpenShift is designed to be a shared cluster, where users from different teams will run applications in the same hardware, OpenShift has to add limitations and runs things differently than in a standard Kubernetes cluster.

Rahti's registry has an image size limit of 5GB. The bigger is an image, the worse the experience is to work with it. It takes more time to pull, and it fills up the image's cache of the node faster. An image more than 1GB is already considered a very big image. See the article about [keeping docker images small](./keeping_docker_images_small.md)

## Building images locally

In this example we are going to use the [official nginx image](https://hub.docker.com/_/nginx) built over the [Alpine Linux](https://www.alpinelinux.org/) distribution, and make the necessary changes to make it work in OpenShift.

Three steps are needed to run build an image locally in a computer.

* First a `Dockerfile` must be written, for example this:

```Dockerfile
FROM nginx:alpine

# support running as arbitrary user which belongs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx && \
    chown nginx.root /var/cache/nginx /var/run /var/log/nginx && \
    # users are not allowed to listen on privileged ports
    sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/default.conf && \
    # Make /etc/nginx/html/ available to use
    mkdir -p /etc/nginx/html/ && chmod 777 /etc/nginx/html/ && \
    # comment user directive as master process is run as user in OpenShift anyhow
    sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html/
EXPOSE 8081

USER nginx:root
```

The `Dockerfile` is:

 1. Giving write permissions to the `root` group (not the `root` user) to several folders that nginx needs to write to (/var/cache/nginx, /var/run, /var/log/nginx, and /etc/nginx/html/). Applications are run using a random user and the `root` group.
 2. Changing the port where nginx listens to, as only root is allowed to listen on privileged ports (<1024).
 3. And finally comment out the `user` configuration directive.

 The original `nginx:alpine` image has 5 layers, and we will adding a new one (`RUN`).

A simpler example of `Dockerfile` could be:

```Dockerfile
FROM alpine

RUN apk add git
```

This is just installing git over `alpine`, and add also a new layer.

See the [Dockerfile](https://docs.docker.com/engine/reference/builder/) reference docs.

Then, the following command must be used to build the image `docker.io/user/name:tag`:

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
    * A Docker build using binary input will be created
      * The resulting image will be pushed to image stream tag "my-hello-image:devel"
      * A binary build was created, use 'start-build --from-dir' to trigger a new build

--> Creating resources with label build=my-hello ...
    imagestream.image.openshift.io "my-hello-image" created
    buildconfig.build.openshift.io "my-hello" created
--> Success
```

Then you need a `Dockerfile`, you can use any of the previous `Dockerfile` in the previous example, or any other one you may have around. In order to tell OpenShift to build the image, just `cd` to the folder where the `Dockerfile` is, and start build with the `oc start-build` command, it will take any file in the current directory and output the build process to local terminal:

```bash
oc start-build my-hello --from-dir=./ -F
```

The image will appear in the Rahti registry console
[registry-console.rahti.csc.fi/registry](https://registry-console.rahti.csc.fi),
and it will be visible to internet at
`docker-registry.rahti.csc.fi/<project-name>/my-hello:devel` for docker
compatible clients.

For command-line usage with docker compatible clients, the docker repository password will be the access token shown when authorizing Rahti command line session and user name can be `unused`.

The Docker CLI tool login instructions are also shown in the [Rahti registry
console](https://registry-console.rahti.csc.fi).

## Using the Source to Image mechanism

OpenShift allows to build and deploy code without writing a `Dockerfile`. This is called Source to Image or `s2i`. For example, use the official python sample code:

```bash
$ oc new-app https://github.com/OpenShiftDemos/os-sample-python.git
--> Found image 4e4d991 (2 weeks old) in image stream "openshift/python" under tag "3.8" for "python"

    Python 3.8 
    ---------- 
    Python 3.8 available as container is a base platform for building and running various Python 3.8 applications and frameworks. Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

    Tags: builder, python, python38, python-38, rh-python38

    * The source repository appears to match: python
    * A source build using source code from https://github.com/OpenShiftDemos/os-sample-python.git will be created
      * The resulting image will be pushed to image stream tag "os-sample-python:latest"
      * Use 'start-build' to trigger a new build
    * This image will be deployed in deployment config "os-sample-python"
    * Port 8080/tcp will be load balanced by service "os-sample-python"
      * Other containers can access this service through the hostname "os-sample-python"

--> Creating resources ...
    imagestream.image.openshift.io "os-sample-python" created
    buildconfig.build.openshift.io "os-sample-python" created
    deploymentconfig.apps.openshift.io "os-sample-python" created
    service "os-sample-python" created
--> Success
    Build scheduled, use 'oc logs -f bc/os-sample-python' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/os-sample-python' 
    Run 'oc status' to view your app.
```

The image will be found in Rahti's registry. Then do as suggested and expose the new application to the outside world:

```bash
$ oc expose svc/os-sample-python
route.route.openshift.io/os-sample-python exposed
```

In order to get the new route hostname do:

```bash
oc get route os-sample-python
```

If you enter the hostname in a browser, you will see the "Hello World!" message.

A new build can be triggered in the command line:

```bash
oc start-build os-sample-python
```

Or using [webhooks](/cloud/rahti/tutorials/webhooks/)

## Using the inline Dockerfile method

It is possible to create a new build using a Dockerfile provided in the command line. By doing this, the `Dockerfile` itself will be embedded in the Build object, so there is no need for an external Git repository.

```bash
oc new-build -D $'FROM centos:7'
```

In this example, we will build an image that is a copy of `CentOS 7`.

It is also possible to create a build from a given `Dockerfile`:

```bash
cat Dockerfile | oc new-build -D -
```
