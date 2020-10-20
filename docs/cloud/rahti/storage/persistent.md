# Persistent volumes

**Persistent volumes** are storage which persist during & after pod's lifetime.

Persistent volumes in Rahti are stored in a resilient storage such as CEPH, NFS or
GlusterFS. They are claimed by a pod using a **PersistentVolumeClaim**. When a
new claim is made, this can mean that either an existing volume is claimed or a
new one is created dynamically and given to the pod to use.

There are two storage classes available in Rahti:

 * *glusterfs-storage*. This kind of volume is a "Read Write Many" (RWX) type storage, this means multiple nodes can mount it in read nad write mode. This is the default class. It is the most flexible class, as allows any pod anywhere in the cluster to read and write files. The downside is a lower performance than the next class.
 * *standard-rwo*. This kind is a "Read Write Once" (RWO), meaning that only one node can mount the volume (in read-write mode). It is faster than glusterfs, but it is limited to a single node.

![PersistentVolumeClaim](/cloud/rahti/img/pods-and-storage-pvc.drawio.svg)

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

Above will request a 1 GiB persistent storage that can be mounted in read-write
mode by multiple nodes. Other access modes are ReadWriteOnce (Only one node can mount it read-write) and ReadOnlyMany (Multiple nodes can mount read-only).

Persistent storage can be requested also via the web console.

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

!!! warning
    When a Persistent Volume is deleted, the corresponding data is deleted **permanently**. It is highly recommended to make regular and versioned copies of the data to an independent storage system like [Allas](/data/Allas/using_allas/a_backup/).
