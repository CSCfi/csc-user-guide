# Allas storage in Rahti

More information about [Allas](../../../data/Allas/index.md)  

## Backup to Allas

There are different ways to backup to Allas from Rahti. We will show you two examples:  
  - The first one is using another pod to copy the content of your persistent volume to Allas.  
  - The second one is a bash script that you have to execute from your local machine.

## First example: using another pod

For this first example, we assume that we have a `nginx` deployment running with a `PersistentVolumeClaim`. We provide the files for testing purposes.

First, we build a nginx image with this Dockerfile: (since it's not possible to use the regular `nginx` image in OpenShift)  

```Dockerfile
FROM nginx:stable

ENV LISTEN_PORT=8080

# support running as arbitrary user which belogs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx

# users are not allowed to listen on priviliged ports
RUN sed -i.bak "s/listen\(.*\)80;/listen ${LISTEN_PORT};/" /etc/nginx/conf.d/default.conf

# comment user directive as master process is run as user in OpenShift anyhow
RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

EXPOSE 8080
```

Then you can deploy this `nginx` with this Deployment file:   

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
        image: <your_custom_nginx_image>
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
  storageClassName: standard-rwo
```

The deployment is using a `PersistentVolumeClaim` for our example.  

Now we have our running `nginx` pod, we want want to copy the content of the PVC to Allas. We will use a new deployment with a `rclone` Docker image.  

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

_Replace `{ACCESS_KEY_ID}` and `{SECRET_ACCESS_KEY}` by your own credentilas._ 

Create a `rclone.sh` script:  

```sh
#!/bin/sh -e

rclone copy "/mnt/" "default:{BUCKET}"

echo "Done!"
```

_Replace `{BUCKET}` by the target bucket where you want to backup your files._  

Then, you have to create your own custom `rclone` Docker image:  

```Dockerfile
FROM rclone/rclone

COPY rclone.conf /.rclone.conf
COPY rclone.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/rclone.sh
```

Once all this done, you can deploy your `rclone` pod. You can use this example:  

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
      claimName: nginx-pvc # Must match the PVC name that you want to backup
```

!!! Warning  
    If your `PersistentVolumeClaim` is `ReadWriteOnce`, you have to scale down the `nginx` deployment to let the pod running rclone mount the volume.  
    Use this command to proceed: `oc scale --replicas=0 deploy/nginx`  
    If your `PersistentVolumeClaim` is `ReadWriteMany`, there is no need to scale down your deployment.  
    You can verify with this command: `oc get pvc`. You should see either `RWO` or `RWX`.

The pod will run and backup the content of your PVC to Allas. Don't forget to scale up your origin deployment (`oc scale --replicas=1 deploy/nginx`)

There are PROS and CONS with this solution:  
- PROS: You run the pod in your Rahti project  
- CONS: If your PVC is `ReadWriteOnce`, a downtime is necessary.  
