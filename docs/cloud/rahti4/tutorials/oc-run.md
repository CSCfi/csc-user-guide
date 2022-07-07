# How to run an ad-hoc interactive container

It is sometimes useful to be able to run a random container image for debugging inside a project. `oc run` allows it by running in a single command:

```
$ oc run pod-name -it --rm --image=bash --restart=Never
If you do not see a command prompt, try pressing enter.
bash-5.1$
```

* `pod-name` can be any given name that does not exist already in the namespace.
* `-it` tells  `oc` to create an interactive session.
* `--rm` will make the Pod to be deleted after the session is over.
* `--image=bash` is the name of the image, in this case [library/bash](https://hub.docker.com/_/bash). It can be any given image, either public library image like `bash`, or a purpose build private image.
* `--restart=Never` will tell OpenShift to not restart the Pod when the session is over.
* If you would like to start a Pod with a different command than its default, you can do so by adding `-- [COMMAND] [args...] [flags]` at the end (e.g. `oc run pod-name  -it --rm --image=python --restart=Never -- bash`).
