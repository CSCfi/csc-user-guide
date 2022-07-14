<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/storage/ephemeral/)

# Ephemeral Storage (EmptydDir)

When local ephemeral (temporal) storage is needed, an `emptyDir` should be issued. It is local to the node, on Rahti this is RAID-0 SSD storage. It can be shared across several containers in the same Pod, and it the *fastest* filesystem available in Rahti, but it will be **lost when the Pod is killed or restarted**. It is declared directly in the Pod definition:

*`podWithEmptydDir.yaml`*:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
  labels:
    app: my-application
  spec:
    volumes:
    - name: volume-a
      emptyDir: {}
    containers:
    - name: container-a
      image: centos:7
      volumeMounts:
      - mountPath: /outputdata
        name: volume-a
    - name: container-b
      image: centos:7
      volumeMounts:
      - mountPath: /interm
        name: volume-a
```

![emptyDir](/cloud/rahti/img/pods-and-storage-emptydir.drawio.svg)
