# Patterns

## Persistent storage

Persistent storage is requested in the cluster using `PersistentVolumeClaim` objects:

*`pvc.yaml`*

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: testing-pvc
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
```

Persistent storage can be requested also via the web console.

This will request a 1 GiB persistent storage that can be mounted in read-write
mode by multiple nodes.

The persistent volume can be used in a pod by specifying `spec.volumes`
(defines the volumes to attach) and `spec.containers.volumeMounts` (defines where
to mount the attached volumes in the container's filesystem):

*`pvc-pod.yaml`*:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod-vol
  labels:
    app: serveapp-vol
    pool: servepod-vol
spec:
  containers:
  - name: serve-cont
    image: "docker-registry.default.svc:5000/openshift/httpd"
    volumeMounts:
    - mountPath: /mountdata
      name: smalldisk-vol
  volumes:
  - name: smalldisk-vol
    persistentVolumeClaim:
      claimName: testing-pvc
```

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
to the `index.html` file on the shared volume.

The shared volume is defined in `spec.volumes` and "mounted" in
`spec.initContainers.volumeMounts` and `spec.containers.volumeMounts`.

## Jobs

*Jobs* are run-to-completion Pods, except that they operate on the same level
as ReplicationControllers, in the sense that they too define template for pod
to be launched instead of directly describing the pod. The difference is,
however, that *Jobs* are not restarted when they finish.

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

This job will name the pod automatically and the pod can be queried with
job-name label:

```bash
$ oc get pods --selector job-name=pi
NAME       READY     STATUS      RESTARTS   AGE
pi-gj7xg   0/1       Completed   0          3m
```

Thus the standard output of the job is:

```bash
$ oc logs pi-gj7xg
helloing so much here! Lets hello from /mountdata/hello.txt too:
this hello is from the initcontainer
```

There may be only one object of given name in the project namespace, thus the
job cannot be run twice unless the first instance of it is removed. The pod,
however, needs not to be cleaned.

## Passing configuration data to containers: ConfigMap and Secrets

**ConfigMaps** are useful in collecting configuration-type data in Kuberentes'
objects. Their contents are communicated to containers by environmental
variables or by volume mounts.

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

The following pod imports the value of `data.prop.a` to `DATA_PROP_A`
environment variable and creates files `data.prop.a`, `data.prop.b` and
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

The output log, given by command `oc logs confmap-cont` of this container
should be

```
fo=bar
baz=notbar
DATA_PROP_A=hello
```

**Secrets** behave much like ConfigMaps, but once created, they are stored in
base64 encoded form and their contents are not displayed by default with the
`oc describe` command. There is an example of a Secret in the Webhooks section.

## Webhooks

Rahti supports Generic, GitHub, GitLab and Bitbucket webhooks. They are
particularly useful in triggering builds. The syntax for BuildConfig is as
follows:

```yaml
spec:
  triggers:
  - type: GitHub
    github:
      SecretReference:
        name: webhooksecret
```

Now the Secret `webhooksecret` should have

```yaml
apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=    # "this_is_a_bad_token" in
metadata:                                           #  base64 encoding
  name: webhooksecret
  namespace: mynamespace     # set this to your project namespace
```

When the BuildConfig is configured to trigger from the webhook and the
corresponding secret exists, the webhook URL can be found by using (assuming we
added the webhook to `serveimg-generate`) `oc describe` command:

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

Finally, the GitHub WebHook payload url is the url above with `<secret>`
replaced with base64 decoded string of the value of `data.WebHookSecretKey`
above and the content type is `application/json`.

## Custom domain names and secure transport

Custom domain names and HTTPS secure data transport are implemented in the
Route object level. They are controlled with the keywords `spec.host` and
`spec.tls`.

The public DNS CNAME record of the custom domain name should point to `rahtiapp.fi`
and the custom DNS name is placed in the `spec.host` entry of the Route object:

*`route-with-dns.yaml`*:

```yaml
apiVersion: v1
kind: Route
metadata:
  labels:
    app: serveapp
  name: myservice
spec:
  host: my-custom-dns-name.replace.this.com
  to:
    kind: Service
    name: serve
    weight: 100
```

The TLS certificates and private keys are placed in the `spec.tls` field, for
example:

```yaml
apiVersion: v1
kind: Route
metadata:
  labels:
    app: serveapp
  name: myservice
spec:
  host: my-custom-dns-name.replace.this.com
  to:
    kind: Service
    name: serve
    weight: 100
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
    certificate: |-
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
    key: |-
      -----BEGIN PRIVATE KEY-----
      ...
      -----END PRIVATE KEY-----
```

This definition will create a Route with the private key placed in
`spec.tls.key` and the certificates placed in `spec.tls.certificate`. In this example,
the HTTP traffic is redirected to use the HTTPS protocol due to `Redirect` setting in
`spec.tls.insecureEdgeTerminationPolicy` and the TLS termination is handled by the
Route object, in the sense that the traffic coming from the Service `serve` is assumed
to be non-encrypted (`spec.tls.termination: edge`). Other termination policies
include:

* `passthrough`: Assume that the TLS-connection is terminated internally at the
  Pod and just forward the encrypted traffic
* `reencrypt`: Terminate the TLS-connection at the Router and open another
  secure connection which must be terminated at the Pod

!!! Caution

    Always treat contents of the field `spec.tls.key` in the Route objects with
    special case, since the private TLS key should be never exposed to
    non-trusted parties.

!!! Hint

    letsencrypt.org provides free and open certificates. Routes can be
    automated to be secure ones with a third party
    [openshift-acme controller](https://github.com/tnozicka/openshift-acme)
    by annotating the Route objects.

    Another way of utilizing the certificates provided by Let's Encrypt's is to
    use the [`certbot`](https://certbot.eff.org/) tool on the debug console and
    renewing the certificate with, e.g., CronJob controller.
