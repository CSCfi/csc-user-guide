# Patterns

## InitContainer

_InitContainer_ is a container in a pod that is intended run to completion before
the main containers are started. Data from the init containers can be
transferred to the main container using e.g. empty volume mounts.

*`pod-init.yaml`*:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  labels:
    app: serveapp
    pool: servepod
spec:
  volumes:
  - name: sharevol
    emptyDir: {}
  initContainers:
  - name: perlhelper
    image: perl
    command:
    - sh
    - -c
    - >
      echo Hello from perl helper > /datavol/index.html
    volumeMounts:
    - mountPath: /datavol
      name: sharevol
  containers:
  - name: serve-cont
    image: docker-registry.default.svc:5000/openshift/httpd
    volumeMounts:
    - mountPath: /var/www/html
      name: sharevol
```

Here we run an init container that uses the `perl` image and writes text
in the `index.html` file on the shared volume.

The shared volume is defined in `spec.volumes` and "mounted" in
`spec.initContainers.volumeMounts` and `spec.containers.volumeMounts`.

## Jobs

_Jobs_ are run-to-completion pods, except that they operate on the same level
as ReplicationControllers, in the sense that they too define the template for the pod
to be launched instead of directly describing the pod. The difference is,
however, that *jobs* are not restarted when they finish.

*`job.yaml`*:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      volumes:
      - name: smalldisk-vol
        emptyDir: {}
      containers:
      - name: pi
        image: perl
        command:
        - sh
        - -c
        - >
          echo helloing so much here! Lets hello from /mountdata/hello.txt too: &&
          echo hello to share volume too >> /mountdata/hello-main.txt &&
          cat /mountdata/hello.txt
        volumeMounts:
        - mountPath: /mountdata
          name: smalldisk-vol
      restartPolicy: Never
      initContainers:
      - name: init-pi
        image: perl
        command:
        - sh
        - -c
        - >
          echo this hello is from the initcontainer >> /mountdata/hello.txt
        volumeMounts:
        - mountPath: /mountdata
          name: smalldisk-vol
  backoffLimit: 4
```

This job names the pod automatically, and the pod can be queried with
a job-name label:

```bash
$ oc get pods --selector job-name=pi
NAME       READY     STATUS      RESTARTS   AGE
pi-gj7xg   0/1       Completed   0          3m
```

The standard output of the job:

```bash
$ oc logs pi-gj7xg
helloing so much here! Lets hello from /mountdata/hello.txt too:
this hello is from the initcontainer
```

There may only be one object with a given name in the project namespace, thus the
job cannot be run twice unless its first instance is removed. The pod,
however, needs not be cleaned.

## Passing configuration data to containers: ConfigMap and Secrets

**ConfigMaps** are useful in collecting configuration type data in Kubernetes
objects. Their contents are communicated to containers by environmental
variables or volume mounts.

*`configmap.yaml`*:

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: my-config-map
data:
  data.prop.a: hello
  data.prop.b: bar
  data.prop.long: |-
    fo=bar
    baz=notbar
```

The following pod imports the value of `data.prop.a` to the `DATA_PROP_A`
environment variable and creates the files `data.prop.a`, `data.prop.b` and
`data.prop.long` inside `/etc/my-config`:

*`configmap-pod.yaml`*:

```yaml
kind: Pod
apiVersion: Pod
metadata:
  name: my-config-map-pod
spec:
  restartPolicy: Never
  volumes:
  - name: configmap-vol
    configMap:
      name: my-config-map
  containers:
  - name: confmap-cont
    image: perl
    command:
    - /bin/sh
    - -c
    - |-
      cat /etc/my-config/data.prop.long &&
      echo "" &&
      echo DATA_PROP_A=$DATA_PROP_A
    env:
    - name: DATA_PROP_A
      valueFrom:
        configMapKeyRef:
          name: prop-a-config
          key: data.prop.a
          optional: true     # Run this pod even
    volumeMounts:            # if data.prop.a is not defined in configmap
    - name: configmap-vol
      mountPath: /etc/my-config
```

The output log, provided with the command `oc logs confmap-cont` of this container,
should be:

```
fo=bar
baz=notbar
DATA_PROP_A=hello
```

**Secrets** behave much like ConfigMaps, but once created, they are stored in
a _base64_ encoded form, and their contents are not displayed by default with the
command `oc describe`. There is an example of a secret in the _Webhooks_ section.

## Webhooks

Rahti supports Generic, GitHub, GitLab and Bitbucket webhooks. They are
particularly useful in triggering builds. The BuildConfig syntax:

```yaml
spec:
  triggers:
  - type: GitHub
    github:
      SecretReference:
        name: webhooksecret
```

Now the secret `webhooksecret` should have:

```yaml
apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=    # "this_is_a_bad_token" in
metadata:                                           #  base64 encoding
  name: webhooksecret
  namespace: mynamespace     # set this to your project namespace
```

When the BuildConfig is configured to trigger by the webhook and the
corresponding secret exists, the webhook URL can be found by using the command `oc describe` (assuming we
included the webhook in `serveimg-generate`):

```
$ oc describe bc/serveimg-generate
Name:                serveimg-generate
.
.
.
Webhook GitHub:
        URL:        https://rahti.csc.fi:8443/apis/build.openshift.io/v1/.../<secret>/github
.
.
.
```

Finally, the GitHub WebHook payload URL is the URL above with `<secret>`
replaced with the base64 decoded string of the value of `data.WebHookSecretKey`
above, and the content type is `application/json`.

