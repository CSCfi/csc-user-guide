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

Secrets behave much like ConfigMaps, with the differnce that once created they are stored in _base64_ encoded form, and their contents are not displayed by default in the command line or in the web interface. There is an example of a secret in the [Webhooks](/cloud/rahti/tutorials/webhooks/) section.
