# Using Allas object storage in Rahti

Visit the [Allas](../../../../data/Allas/index.md) page for more information about the service itself.

## Backup to Allas

There are different ways to back up to Allas from Rahti. We will show you two examples:

  - The first one uses another Pod to copy the content of your PersistentVolume to Allas.
  - The second one is a bash script that you have to execute from your local machine.

For the first example, we will deploy an `nginx` deployment running with a `PersistentVolumeClaim`. We provide the files for testing purposes.

### Preparing an NGINX deployment

First, for our tutorial, we will build and deploy an NGINX server.

Since it is not possible to use the regular `nginx` image in Rahti, we [build](../images/creating.md) our own image with this Dockerfile:

```Dockerfile
FROM nginx:stable

ENV LISTEN_PORT=8080

# support running as arbitrary user which belongs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx

# users are not allowed to listen on privileged ports
RUN sed -i.bak "s/listen\(.*\)80;/listen ${LISTEN_PORT};/" /etc/nginx/conf.d/default.conf

# comment out the user directive, as the master process runs as an arbitrary user in OKD anyway
RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

EXPOSE 8080
```

If you build your image locally, don't forget to [push](../images/integrated-registry.md) it to your project, and to convert it to the `amd64` architecture if needed.

Then, you can deploy and expose this `nginx` server with this Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: <custom_nginx_image>
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
        ports:
          - containerPort: 8080
        volumeMounts:
        - name: myvol
          mountPath: /mnt
      volumes:
      - name: myvol
        persistentVolumeClaim:
          claimName: nginx-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  selector:
    app: nginx
  ports:
  - port: 8080

---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx-route
spec:
  host: ""
  path: /
  to:
    kind: Service
    name: nginx-svc
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nginx-pvc
spec:
  resources:
    requests:
      storage: 1Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: standard-csi
```

The deployment uses a `PersistentVolumeClaim` for our example. Save the file and use this command to deploy it: `oc apply -f {name_of_yaml_file}`.

Now that we have our `nginx` Pod running, we want to copy the content of the PVC to Allas. We will use a new deployment with an `rclone` Docker image.

### First example: using another Pod

Create a `rclone.conf` with your `access_key_id` and `secret_access_key`.

If you don't have `access_key_id` and `secret_access_key`, you need to source your Pouta project and then use this command to create credentials:

```sh
openstack ec2 credentials create
```

Once created, create your `rclone.conf` file:

```ini
[default]
type = s3
provider = Other
env_auth = false
access_key_id = {ACCESS_KEY_ID}
secret_access_key = {SECRET_ACCESS_KEY}
endpoint = a3s.fi
acl = private
```

_Replace `{ACCESS_KEY_ID}` and `{SECRET_ACCESS_KEY}` with your own credentials._

Create an `rclone.sh` script:

```sh
#!/bin/sh -e

rclone copy "/mnt/" "default:{BUCKET}"

echo "Done!"
```

_Replace `{BUCKET}` with the target bucket where you want to back up your files._

Then, you have to create your own custom `rclone` Docker image:

```Dockerfile
FROM rclone/rclone

COPY rclone.conf /.rclone.conf
COPY rclone.sh /usr/local/bin/
RUN chmod 755 /.rclone.conf
RUN chmod +x /usr/local/bin/rclone.sh
```

If you create your image locally, don't forget to [push](../images/integrated-registry.md) it to your project.

Once all of this is done, you can deploy your `rclone` Pod. You can use this example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rclone
spec:
  containers:
  - name: copys3
    image: <your_rclone_image>
    command: ["/usr/local/bin/rclone.sh"]
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
    volumeMounts:
    - name: vol-to-backup
      mountPath: /mnt/
  volumes:
  - name: vol-to-backup
    persistentVolumeClaim:
      claimName: nginx-pvc # Must match the PVC name that you want to back up
```

Save the file and use this command: `oc apply -f {name_of_yaml_file}`.

!!! warning

    If your `PersistentVolumeClaim` is `ReadWriteOnce`, you have to scale down the `nginx` deployment to let the Pod running rclone mount the volume. Use this command to proceed:

    ```bash
    oc scale --replicas=0 deploy/nginx
    ```

The Pod will run and back up the content of your PVC to Allas. Don't forget to scale your original deployment back up (`oc scale --replicas=1 deploy/nginx`) after the copy has finished.

This solution has pros and cons:

Pros:

  - You run the Pod in your Rahti project.

Cons:

  - If the PVC is `ReadWriteOnce`, downtime is necessary.

### Second example: using a bash script

For the following script to work, we assume that you have the `rclone` command-line program installed and that the Allas bucket has been created. The `rclone.conf` file should be set up on your local system as explained in [Configuring rclone](../../../../data/Allas/using_allas/allas-conf.md). An Allas bucket can also be created using rclone as described in [Using rclone with Allas](../../../../data/Allas/using_allas/rclone.md).

This script backs up an application deployed in Rahti. The example assumes that the application mounts its data at `/backup`, that is, `/backup` is the `mountPath` of the `volumeMounts` entry.

```bash
#!/usr/bin/env bash

# Set your pod name, source directory, and destination directory
if [[ -z $1 ]];
then
    echo "No Podname parameter passed."
    exit 22
else
     echo "The POD_NAME = $1 is set."
fi

POD_NAME=$1
SOURCE_DIR="/backup"
TIMESTAMP=$(date '+%Y%m%d%H%M%S') # Generate a timestamp
DEST_DIR="/tmp/pvc_backup_$TIMESTAMP.tar.gz" # Include the timestamp in the filename
RCLONE_CONFIG_PATH="your/path/to/rclone.conf"
S3_BUCKET="pvc-test-allas" # Your bucket name

# Echo function to display task messages
echo_task() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Function to handle errors
handle_error() {
  echo_task "Error: $1"
  exit 1
}

# Check if the pod exists
oc get pod "$POD_NAME" &>/dev/null
if [ $? -ne 0 ]; then
  echo_task "Pod $POD_NAME not found. Aborting backup."
  exit 1
fi

# Create a tar archive within the pod
echo_task "Creating a tar archive within the pod..."
oc exec "$POD_NAME" -- /bin/sh -c "tar -czf /tmp/pvc_backup.tar.gz -C $SOURCE_DIR ."
if [ $? -ne 0 ]; then
  handle_error "Failed to create a tar archive in the pod. Aborting backup."
fi

# Copy the tar archive to the local machine
echo_task "Copying the tar archive to the local machine..."
oc cp "$POD_NAME:/tmp/pvc_backup.tar.gz" "$DEST_DIR"
if [ $? -ne 0 ]; then
  handle_error "Failed to copy the tar archive to the local machine. Aborting backup."
fi
echo_task "Backup completed successfully. The archive is stored in $DEST_DIR."

# Use Rclone to copy the tarball to S3
echo_task "Copying the tarball to S3..."
rclone --config "$RCLONE_CONFIG_PATH" copy "$DEST_DIR" default:"$S3_BUCKET"
if [ $? -ne 0 ]; then
  handle_error "Failed to upload tarball to S3"
fi
echo_task "Backup completed successfully. The archive is stored in $S3_BUCKET/$(basename "$DEST_DIR")"

exit 0
```

If you need to clean up the tar archive files, you can add the following commands after storing the archive to Allas.

```bash
# Clean up the tar archive in the pod
oc exec "$POD_NAME" -- /bin/sh -c "rm /tmp/pvc_backup.tar.gz"

# Clean up the local temporary files, either every archive
rm -rf /tmp/pvc_backup*

# or only the archive created by this run
rm "$DEST_DIR"
```

The script can be run as follows, assuming the script name is `push_to_allas.sh` and it is executable:

```bash
./push_to_allas.sh "mypod-vol"
```

This solution has pros and cons:

Pros:

  - Simplicity: you are essentially treating the volume just like any other directory. It is straightforward to copy data from a directory to Allas.
  - Flexibility: you can select specific files or directories within the mount to copy to Allas, which is ideal for small files.

Cons:

  - Performance: this method can be slower, especially if the volume has a large number of files.

!!! warning "Storage performance"

    There are several considerations to take into account when using Allas regarding performance:

    - Small I/O operations can severely reduce storage performance. Given the same total size, a single large file will be faster than a lot of small ones. A simple solution might be to collect all the small files into one archive file, like a `tar` file.
    - As the storage pool is shared, latency might vary. Shared hardware means shared performance among different users.
    - Single-threaded I/O is slow; it is advisable to use multi-threaded I/O when possible.
