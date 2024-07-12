## Volume snapshot provisioning

There are two ways to provision snapshots in Rahti2: by web interface and by using yaml files. 

# Prerequisites

- An active project in Rahti2
- No pods are using persistent volume claim (PVC) that you want to take a snapshot of.

# Procedure

1. Create a deployment
2. Create a PVC
3. Mount the PVC to deployment (in Rahti2 PVC is only created after that is mount to a deployment)
4. Unmount the PVC from deployment
5. Create a volume snapshot
6. Attach the PVC to volume snapshot

## Using web interface

After making sure that PVC is not attached to any pod, create a volume snapshot by clicking on 'Create VolumeSnapshot' in 'VolumeSnapshot'. 

![Create Snap Shot](../../img/CreateSnapshot.png)

To find volume snapshot, select 'Developer' view, click 'Project' in left hand side menu, in 'Invertory' section of 'Overview' tab last option is VolumeSnapshot. 

![Volume Snap Shot](../../img/Volumesnapshot.png)

Fill the required details. In PersistentVolumeClaim, select the PVC you want to attach, provide a name to volume snapshot, select the default snapshot class 'standard-csi' and click on 'create'.

![Enter the details of Snap Shot](../../img/EnterSnapshotDetails.png)


## Using YAML files

Create `snapshot.yaml` file to attach PVC to volume snapshot

```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: <name_of_volumesnapshot>
spec:
  source:
    persistentVolumeClaimName: <name_of_PVC>
  volumeSnapshotClassName: standard-csi
```

To list all the volume snapshots, use the command:

`oc get volumesnapshot`

To get the details of the volume snapshot that was created, enter the following command:

`oc describe volumesnapshot <your-volume-snapshot>`

Delete the volume snapshot by entering the following command:

`oc delete volumesnapshot <volumesnapshot_name>`

## Restore a volume snapshot

CSI Snapshot Controller Operator creates the following snapshot custom resource definitions (CRDs) in the snapshot.storage.k8s.io/v1 API group. The VolumeSnapshot CRD content can be used to restore the existing volume to a previous state. Create a `pvc-restore.yaml` file.

``` 
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim-restore
spec:
  storageClassName: csi-hostpath-sc
  dataSource:
    name: <name-of-snapshot> 
    kind: VolumeSnapshot 
    apiGroup: snapshot.storage.k8s.io 
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Here, in `spec.dataSource.name`, the name of the snapshot to use as source is provided.

## Use Case

Here, we are taking snapshot of the content for nginx deployment and restorting the data by the restore script. Follow the steps:

1. Create an nginx deployment.
2. Create a PVC name test-pvc.
3. Attach this PVC to the ngninx deployment.
4. Go to the pod created for this deployment and create a file name test.txt.
5. Take the snapshot of the PVC. 
6. Delete the PVC.
7. Restore the content by the volume snapshot.
8. Attach the restored PVC to the nginx deployment again.
9. Check the content of the PVC. 
10. You can see that the data is restored. 