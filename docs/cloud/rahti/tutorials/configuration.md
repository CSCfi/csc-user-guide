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

## Secret

Secrets behave much like ConfigMaps, with the differnce that once created they are stored in _base64_ encoded form, and their contents are not displayed by default in the command line or in the web interface.

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

### Edit a secret

The process to edit a secret is not trivial. The idea is to retrieve the secret JSON definition, decode it, edit it, and then encode it back and replace it.

* First you need to retrieve the different files/secrets inside the secret (the examples use jq to process the JSON files, but it can be done without it):

```sh
oc get secrets $SECRET_NAME -o json | jq ' .data | keys '
```

* Then choose one of the options and get the file/secret itself:

```sh
oc get secrets $SECRET_NAME -o json >secret.json
jq '.data.$KEY_NAME ' secret.json | base64 -d >$KEY_NAME.file
```

* Edit the file with any editor.

* Encode the new file and replace the previous value in the JSON file:

```sh
B64=$(base64 $KEY_NAME.file -w0)
jq " .data.$KEY_NAME = \"$B64\" " secret.json
oc replace -f secret.json
```

As you can the process can be a bit ofuscated.

