# How to transfer data to Rahti?

As discussed in the [available storage options](/cloud/rahti4/storage/) article, it is possible store data using a persistent volume, or using a object storage service like [Allas](/data/Allas/).

## to a Persistent Volume

In order to move data to Rahti, the best method is to use the command line tool `oc rsync`. From its manual:

```bash
$ oc rsync
Copy local files to or from a pod container

This command will copy local files to or from a remote container. It only copies the changed files
using the rsync command from your OS. To ensure optimum performance, install rsync locally. In UNIX
systems, use your package manager. In Windows, install cwRsync from https://www.itefix.net/cwrsync.
```

First of all, it is required to [install oc](/cloud/rahti4/usage/cli/).

Once `oc` is installed, the process is:

* Create the `PersistentVolumeClaim` (PVC) to store the data in Rahti. You may use the web interface or directly the command line. In this example we will use the command line. A simple way to create a `1Gi` volume called `testing-pvc` is:

```bash
$ echo 'apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: testing-pvc
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 1Gi' | oc create -f -
```

* Mount the PVC into a POD with `rsync` installed. It is possible to use any image that has the command `rsync` installed. If you have no access to such an image, `oc rsync` will work also with an image with `tar` installed (`centos` and `ubuntu ` images come with `tar installed).

* Finally, use `oc rsync` to synchronize a local directory with a directory in the pod:

```bash
oc rsync ./local/dir/ POD:/remote/dir
```

If the local data changes, you may just run the same command again. If the image has `rsync installed, only the data that has changed will be copied over to the PVC.

## to Allas object storage

See [using Allas with Rclone](/data/Allas/using_allas/rclone/) for a guide on how to copy the data to Allas. Once the data is in Allas, you can use any *Swift* or *S3* compatible client or library, like `rclone`, to use the data in you application.

