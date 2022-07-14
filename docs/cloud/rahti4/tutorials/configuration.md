
In general, applications require some sort of contextual information as input.
Such contexts are often provided in the form of configuration files, command-line
arguments, and environment variables. Therefore, when containerizing applications
and creating images we need to decouple the generic image content from the
customizable configuration information. This is mainly done to keep the
containerized applications portable. Kubernetes and Openshift have two types
of abstractions called Secrets and ConfigMaps that can be used to inject
contextual information (configuration) into containers during startup and
avoid hardcoding them in images. A good example use case for ConfigMaps and
Secrets are application (service) admin passwords and their configuration files.
Service passwords can be set as Secrets and added to containers as environment
variables, and configuration files can be stored as ConfigMaps that can be
mounted under containers as files on startup.

!!! Note

    It is highly recommended to check out the basic [Kubernetes and Openshift concepts](../../concepts/) 
    before moving on, especially if you are not familiar with them already. You can also practice [deploying a simple static webserver](../elemental_tutorial/) 
    to get some hands-on experience. 

## ConfigMap

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

### Create a ConfigMap

ConfigMaps can be created in various ways. If we have a ConfigMap object definition
as listed above in `configmap.yaml`, then, an instance of it can be created using
the `oc create -f configmap.yaml` command. You can also use the more specific
command `oc create configmap <configmap_name> [options]` to create an instance
of a ConfigMap from directories, specific files, or literal values.
For example, if you have a directory with files containing the data needed to
populate a ConfigMap as follows:

```sh
$ ls example-dir
data.prop.a
data.prop.b
data.prop.long
```

You can then create a ConfigMap similar to the one defined in `configmap.yaml` as:

```sh
oc create configmap my-config-map \
    --from-file=example-dir/
```

This command also works with files instead of directories.

### Use a ConfigMap

The following pod imports the value of `data.prop.a` to the `DATA_PROP_A`
environment variable and creates the files `data.prop.a`, `data.prop.b` and
`data.prop.long` inside `/etc/my-config`:

*`configmap-pod.yaml`*:

```yaml
kind: Pod
apiVersion: v1
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

Deploy the pod using `oc create -f configmap-pod.yaml` command. The output log, provided with the command `oc logs my-config-map-pod` of this container,
should be:

```
fo=bar
baz=notbar
DATA_PROP_A=hello
```

## Secret

Secrets behave much like ConfigMaps, with the difference that once created they are stored in *base64* encoded form, and their contents are not displayed by default in the command line or in the web interface.

*`secret.yml`*:

```yaml
apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=
metadata:
  name: webhooksecret
  namespace: mynamespace     # set this to your project namespace
```

### Create a secret

As with any other OpenShift/Kubernetes objects, Secrets can also be created from a Secret object definition.
For the definition listed above as `secret.yaml`, a Secret instance can be created using
the `oc create -f secret.yaml` command. You can also use the more specific command `oc create secret [flags] <secret_name> [options]`
to create an instance of a Secret from directories, specific files, or literal values.
For example, if you have a file  called `WebHookSecretKey` containing a secret key  you can
use it to create an instance of a secret similar to the one specified in the previous `secret.yaml` file
as follows:

```sh
oc create secret generic webhooksecret \
   --from-file=WebHookSecretKey
```

### Edit a secret

The process to edit a secret is not trivial. The idea is to retrieve the secret JSON definition, decode it, edit it, and then encode it back and replace it.

* First you need to retrieve the different files/secrets inside the secret (the examples use jq to process the JSON files, but it can be done without it):

```sh
oc get secrets <SECRET_NAME> -o json | jq ' .data | keys '
```

* Then choose one of the options and get the file/secret itself:

```sh
oc get secrets <SECRET_NAME> -o json >secret.json
jq '.data.<KEY_NAME>' -r secret.json | base64 -d > <KEY_NAME>.file
```

* Edit the file with any editor.

* Encode the new file and replace the previous value in the JSON file:

```sh
B64=$(base64 <KEY_NAME>.file -w0)
jq " .data.<KEY_NAME> = \"$B64\" " secret.json
oc replace -f secret.json
```

As you can see the process can be a bit obfuscated.
