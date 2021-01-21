# How to manually cache images in Rahti's registry

Since 2nd November 2020, docker hub has imposed a rate limit for image pulls. For Rahti this means a limit of 100 pulls every 6 hours. This limit can be easily reached and it prevents new applications to be deployed if the image is in docker hub.

The error looks like this:

```
Pulling image "docker.io/centos/python-38-centos7@sha256:da83741689a8d7fe1548fefe7e001c45bcc56a08bc03fd3b29a5636163ca0353" ...
pulling image error : toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
```

One solution is to [add docker hub credentials to a project](/cloud/rahti/tutorials/docker_hub_login/). Each docker hub account (even the free ones), has a limit of 200 pulls every 6 hours. Also the limit will be applied to the pulls made by that account, meanwhile before the limit was shared by all Rahti projects.

Other solution is to cache manually the image in Rahti's internal registry. The process is simple, go to <https://registry-console.rahti.csc.fi/registry>, there you must do two things:

1. Create an image in the project's space.

    ![Create Image](/cloud/rahti/img/create_image.png)

    ![Create Image II](/cloud/rahti/img/create_image2.png)

1. Find the login command and use it to login in the terminal.

    ![Login command](/cloud/rahti/img/login_registry.png)

## Update the image

* Pull the image from docker hub in your laptop, tag it with the name you just created, and push it to Rahti's registry. For example to cache `centos:7`:

```
docker pull centos:7
docker tag centos:7 docker-registry.rahti.csc.fi/$PROJECT/centos:7
docker push docker-registry.rahti.csc.fi/$PROJECT/centos:7
```

This has to be repeated for every time the upstream changes.

## Use the image

Go to your project's deployment, and edit it.

![Edit deployment](/cloud/rahti/img/edit_deployment.png)

Go to the Images section, make sure the option "Deploy images from an image stream tag" is clicked. Finally select the new image.

![Use cached image](/cloud/rahti/img/use_cached_image.png)

