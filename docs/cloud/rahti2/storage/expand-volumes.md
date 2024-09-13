# Expand a volume

As dynamic volume expansion is not activated, if one edits directly in the `YAML` object the size of the volume, an error like this will be returned:

```sh
(...)
# * spec: Forbidden: spec is immutable after creation except resources.requests for bound claims
(...)
```

Then a more artisanal procedure must be followed:

* Create a new volume with the desired size

![Create a new volume](../../img/Create-new-volume.png)

* Scale down the deployment that mounts the volume that is being resized.

![Scale down](../../img/Scale-down.png)

* Mount the old and new volume in another Pod. The best option is to create a new deployment, create a file called `two-volumes.yaml` and replace the names of both volumes:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: two-volumes
spec:
  replicas: 1
  selector:
    matchLabels:
      app: two-volumes
  template:
    metadata:
      labels:
        app: two-volumes
    spec:
      containers:
      - image: cscfi/nginx-okd:plus
        name: two-volumes
        ports:
        - containerPort: 8081
          protocol: TCP
        volumeMounts:
        - mountPath: /new
          name: new-volume
        - mountPath: /old
          name: old-volume
      volumes:
      - name: new-volume
        persistentVolumeClaim:
          claimName: new-volume
      - name: old-volume
        persistentVolumeClaim:
          claimName: old-volume
```

```sh
oc create -f two-volumes.yaml
```

* Sync the data

```sh
oc rsh deploy/two-volumes rsync -vrlpD /old/ /new/
```

* Delete that new Pod

```sh
oc delete deploy/two-volumes
```

* Exchange volumes in the deployment that was mounting the volume, it is at **template > spec > volumes** under `claimName`.

```sh
oc edit deploy/<name of deployment>
```

* Finally scale up the deployment.

In order to check the procedure worked, you may enter in a `Pod` that is mounting the volume and check the new size.
