## EmptydDir

When local ephemeral (temporal) storage is needed, an emptyDir should be issued. It is local to the node, can be shared across several containers in the same Pod, it is very fast, but it will be **lost when the Pod is killed**. 

EmptyDir provides ephemeral temporal storage locally on the node where containers are run, on Rahti this is RAID-0 SSD storage. When the Pod is killed, the information in the emptyDir will be lost. It is declared directly in the Pod definition:

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
