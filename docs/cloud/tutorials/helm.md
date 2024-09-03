# How to package a Kubernetes application with Helm

[Helm](https://helm.sh/) is the "The package manager for Kubernetes", it allows the management of the life-cycle of a Kubernetes application (deploy, configure, upgrade, retire, ...). It is an **Infrastructure as Code** (IaC) tool, so it allows us to version control an application and follow its evolution along time, make identical copies (prod, preprod, dev, ...) and predictable upgrades, and of course share and publish the application. It is one of the main tools used upstream, if a tool has a "Kubernetes deployment" it is most likely going to be using Helm.

## Introduction

Helm packages applications into Charts. A Helm chart is a collection of `YAML` templates. In order to create a chart, one must first [install the Helm](https://helm.sh/docs/intro/install/) command line tool and install the [oc command line](../rahti2/usage/cli.md) tool. Once done, to continue:

Make sure you are logged in:

```sh
oc whoami
```

this should return your Rahti 2 username. Then create an example chart:

```sh
$ helm create example
Creating example
```

the result will be:

```sh
$ find example
example
example/Chart.yaml
example/templates
example/templates/tests
example/templates/tests/test-connection.yaml
example/templates/deployment.yaml
example/templates/service.yaml
example/templates/ingress.yaml
example/templates/hpa.yaml
example/templates/serviceaccount.yaml
example/templates/_helpers.tpl
example/templates/NOTES.txt
example/values.yaml
example/charts
example/.helmignore
```

It creates a mostly self-explanatory skeleton of a Chart. The structure is:

* The `Chart.yaml` file contains basic description values: `name`, `description`, `version`, ...
* The `values.yaml` file contains default values for the Chart and shows which parameters can be configured.
* The `.helmignore` contains the patterns to ignore, it is similar to `gitignore`. WE will not change this file.
* The `charts` folder contains the other charts that this one depends on. We will not use this feature.
* Finally the `templates` folder contains the different API Kubernetes objects to be deployed. The [templates engine syntax](https://helm.sh/docs/chart_template_guide/) allows for a great deal of configurability. It supports [Built-in Objects](https://helm.sh/docs/chart_template_guide/builtin_objects/) that for example show the current cluster capabilities, it supports external [values files](https://helm.sh/docs/chart_template_guide/values_files/) where each deployment of the application can have its own separate value file, it has an extensive list of [template functions](https://helm.sh/docs/chart_template_guide/function_list/), [flow control](https://helm.sh/docs/chart_template_guide/control_structures/), and more.

## Package a deployed application

Before we can start the process, we need to "clean up" the current Helm example chart.

1. Delete (or move anywhere else) all files inside the `templates` folder.

1. Empty the `values.yaml` file.

1. Edit `Chart.yaml` and fill up the values as needed.

!!! info "helm lint"

    The helm tool provides a `lint` command that will report any syntaxt issue with the current template.
    ```sh
    $ helm lint example
    ==> Linting example
    [INFO] Chart.yaml: icon is recommended

    1 chart(s) linted, 0 chart(s) failed
    ```

Now we can create the `YAML` files that contain the different parts of the application. As an example we will use a simple webserver with a volume attached to it. We will use an iterative process to create a copy of our current deployment. It is iterative because we will first create a simple, not configurable, and probably not working version, test it, come back and make it more complete and configurable, test it again, and so on.

1. List all the API Objects to get an idea of the different parts that it consists of:

	```sh
	$ oc get dc,deployment,pvc,secret,configmaps,service,route -o name
	deployment.apps/nginx
	persistentvolumeclaim/html
	secret/builder-dockercfg-h4cwh
	secret/builder-token-6fngh
	secret/builder-token-n2rdm
	secret/default-dockercfg-dqfxm
	secret/default-token-kfjlb
	secret/default-token-znxls
	secret/deployer-dockercfg-rpsxj
	secret/deployer-token-gnvzt
	secret/deployer-token-pvws5
	service/glusterfs-dynamic-ed156002-8a7e-11ed-b60d-fa163e0d8841
	service/nginx
	route.route.openshift.io/nginx
	```

1. From the list above, we are only interested in `deployment.apps`, `persistentvolumeclaim/html`, `service/nginx` and `route.route.openshift.io/nginx`. The rest are auto-generated like the `secret/` tokens or created by other objects like the `service/glusterfs-dynamic-ed156002-8a7e-11ed-b60d-fa163e0d8841` object was created as a result of the creation of the `persistentvolumeclaim/` (PVC) creation.

We will write templates one by one, starting with the Volume. There are two simple approaches to accomplish this task, "get and clean" or "recreate from template". We will first try the "get and clean" method.

### Get and clean

The idea of get and clean is simple, we will retrieve a `yaml` representation of an object running in the Kubernetes cluster and then delete all unnecessary information, like status and default configuration options.

#### Persistent Volume Claim

Get the PVC object in YAML format into the file `pvc.yaml`:

```sh
oc get persistentvolumeclaim/html -o yaml > pvc.yaml
```

Most of the information in the `YAML` retrieved is status information generated by OpenShift and can be deleted:

```diff
@@ -1,18 +1,7 @@
 apiVersion: v1
 kind: PersistentVolumeClaim
 metadata:
-  annotations:
-    pv.kubernetes.io/bind-completed: "yes"
-    pv.kubernetes.io/bound-by-controller: "yes"
-    volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/glusterfs
-  creationTimestamp: "2023-01-02T09:22:06Z"
-  finalizers:
-  - kubernetes.io/pvc-protection
   name: html
-  namespace: test
-  resourceVersion: "1771053847"
-  selfLink: /api/v1/namespaces/test/persistentvolumeclaims/html
-  uid: ed156002-8a7e-11ed-b60d-fa163e0d8841
 spec:
   accessModes:
   - ReadWriteOnce
@@ -20,10 +9,4 @@
     requests:
       storage: 1Gi
   storageClassName: glusterfs-storage
-  volumeName: pvc-ed156002-8a7e-11ed-b60d-fa163e0d8841
-status:
-  accessModes:
-  - ReadWriteOnce
-  capacity:
-    storage: 1Gi
-  phase: Bound
+status: {}
```

The main fields are **metadata > name**, **spec > resources > requests > storage**, and **spec > storageClassName**, and the result will be:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: standard-csi
status: {}
```

#### Deployment

The same process can be repeated for `deployment.apps/nginx`:

```sh
oc get deployment.apps/nginx -o yaml >deploy.yaml
```

* First, for the `image` used, we need to replace the `@sha256` hash by `:latest`. This way we will always get the actual latest version of the image. It is also possible to replace it by a specific version like `:1.23.3`.
* Then we will delete the status information. An example of "status" entries are `lastTransitionTime` and `creationTimestamp`. This has no place to be in a template as it is information 100% generated by Kubernetes about the current running object, not the one we want to create.
* Finally we will delete the auto-generated configuration options. An example of "configuration options" are the `rollingParams`. These configuration options are generated from the defaults of the Kubernetes cluster. It is also possible to keep these default options, so the user of the chart can change them before the creation is started, for example it could be necessary to increase the `timeoutSeconds` because the application takes more than 10 minutes to start.

```diff
@@ -1,44 +1,24 @@
 apiVersion: apps/v1
 kind: Deployment
 metadata:
   labels:
     app: nginx
   name: nginx
-  namespace: test
-  resourceVersion: "1771055913"
-  selfLink: /apis/apps.openshift.io/v1/namespaces/test/deployments/nginx
-  uid: a828c0db-8a7e-11ed-b60d-fa163e0d8841
 spec:
   replicas: 1
   selector:
     matchLabels:
       app: nginx
   strategy:
-    activeDeadlineSeconds: 21600
-    resources: {}
-    rollingParams:
-      intervalSeconds: 1
-      maxSurge: 25%
-      maxUnavailable: 25%
-      timeoutSeconds: 600
-      updatePeriodSeconds: 1
     type: RollingUpdate
   template:
     metadata:
-      annotations:
-        openshift.io/generated-by: OpenShiftWebConsole
-      creationTimestamp: null
       labels:
	       app: nginx
     spec:
       containers:
-      - image: bitnami/nginx@sha256:abe48bff022ec9c675612653292b2e685c91ce24bc4374199723c4f69603a127
-        imagePullPolicy: Always
+      - image: docker.io/bitnami/nginx:latest
	 name: nginx
	 ports:
	 - containerPort: 8080
@@ -46,21 +26,12 @@
	 - containerPort: 8443
	   protocol: TCP
	 resources: {}
-        terminationMessagePath: /dev/termination-log
-        terminationMessagePolicy: File
	 volumeMounts:
	 - mountPath: /opt/bitnami/nginx/html/
	   name: html
-      dnsPolicy: ClusterFirst
-      restartPolicy: Always
-      schedulerName: default-scheduler
-      securityContext: {}
-      terminationGracePeriodSeconds: 30
       volumes:
       - name: html
	 persistentVolumeClaim:
	   claimName: html
-  test: false
@@ -71,29 +42,5 @@
-   kind: ImageStreamTag
-   name: nginx:latest
-   namespace: test
-      lastTriggeredImage: bitnami/nginx@sha256:abe48bff022ec9c675612653292b2e685c91ce24bc4374199723c4f69603a127
-     type: ImageChange
```

The result being:

```yaml
apiVersion: apps.openshift.io/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: docker.io/bitnami/nginx:latest
        name: nginx
        ports:
        - containerPort: 8080
          protocol: TCP
        - containerPort: 8443
          protocol: TCP
        resources: {}
        volumeMounts:
        - mountPath: /opt/bitnami/nginx/html/
          name: html
      volumes:
      - name: html
        persistentVolumeClaim:
          claimName: html
```

### Recreate from template

For the two remaining objects: `service` and `route`, we will use the "recreate from template" method, where we start from a simple object and fill up the blanks with the configuration we need.

#### Route

This is a minimal route:

```yaml
apiVersion: v1
kind: Route
metadata:
  name: XXXX
spec:
  host: YYYY
  to:
    kind: Service
    name: ZZZZ
```

Where `XXXX` is the name of the route, `YYYY` is the host where the application will be configured to listen, and `ZZZZ` is the Service connected to it.

#### Service

A minimal possible service is:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: XXXX
spec:
  selector:
    app: YYYY
  ports:
  - nodePort: 0
    port: NNNN
    protocol: TCP
    targetPort: NNNN
```

Where `XXXX` is the name of the service we filled up in the Route, `YYYY` is the name of the deployment, and `NNNN` is the port the deployment is listening to.

### Test

The tests should be done in a separate namespace, and there are two approaches:

* Test them individually by:

    ```sh
    oc create -f pvc.yaml
    ```

    The command above will create a PVC object in the selected namespace. You should check that it works as expected. You can destroy it by:

    ```sh
    oc delete pvc/XXXX
    ```

    where `XXXX` is the name of the volume.

* Or all together in the Helm chart, by copying all the `yaml` files we created into the `templates` folder.

    * We can then install it:

    ```sh
    helm install test-name example/
    ```

    **Note:** With `--dry-run` you can preview what helm will deploy without making any change.

    * We can see the status of the installed chart by:

    ```sh
    $ helm ls
    NAME     	NAMESPACE    	REVISION	UPDATED                                	STATUS  	CHART        	APP VERSION
    test-name	test    	1       	2023-01-03 14:59:04.026623633 +0200 EET	deployed	example-0.1.0	1.16.0
    ```

    * After making a change in the chart templates we can upgrade it:

    ```sh
    $ helm upgrade test-name example
    Release "test-name" has been upgraded. Happy Helming!
    NAME: test-name
    LAST DEPLOYED: Tue Jan  3 15:54:15 2023
    NAMESPACE: test
    STATUS: deployed
    REVISION: 2
    TEST SUITE: None
    ```

    * And finally to destroy it:

    ```sh
    $ helm uninstall test-name
    release "test-name" uninstalled
    ```

### Configuration

One of the powerful aspects of Helm is the possibility to, instead of using hardwired values, parametrize them, or to use provided [built-in](https://helm.sh/docs/chart_template_guide/builtin_objects/) values. By removing hardwired values, we provide easy customization that will allow to use the template in more circumstances and for a longer period of time, for example by changing the template image. A user of the template just needs to worry about the `values.yaml` file and not how these values fit into the complexities of the Chart. Helm uses _Go templates_ to accomplish this.

The [built-in](https://helm.sh/docs/chart_template_guide/builtin_objects/) values can be very handy, but we will mention only two of sets of them:

* `Release` variables offer the basic information of this chart deployment. Information like the `Namespace` we are deploying this template to, or the `Name` of the Chart.
* `Capabilities` is a more advance feature that provides information about what API objects and that version the Kubernetes cluster supports. For example the version of Kubernetes, or if `Ingress` or `Route` are supported. These two pieces of information allow us to make more widely compatible templates, as different versions of Kubernetes will need slightly different options.

We can also define our own configuration variables. We will set up a default value and at the same time allow the `values.yaml` file to override it. Let's start with the Volume `yaml` file from previous steps:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: glusterfs-storage
status: {}
```

In this template we would like to parametrize at least two of the values: the `storage` size and the `storage class`. One allows the user to use more or less disk space, and the second allows to change the driver used for the storage. The resulting file would be something like this:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.storage.size | default "500Mi" }}
  storageClassName: {{ .Values.storage.class | default "glusterfs-storage" }}
status: {}
```

And then a `values.yaml` file like:

```yaml
storage:
  size: 1Gi
  class: glusterfs-storage
```

As you can see all variables in the `values.yaml` file can be found from `{{ .Values }}`. We have also set up a default of `500Mi` in the template itself using the `default` function, and configured a value of `1Gi` at `values.yaml`. In this example the storage of `1Gi` will be used, but if we removed the line `size: 1Gi`, the storage will be the default of `500Mi`.

Other values that might be interesting to configure:

* The `host` which the application will be available at.
* The `image` to use.
* The number of `replicas` for the application.

### Conditionals

It is possible to have conditionals in the templates, based on capabilities of the cluster, or in a configuration option. For example to activate `tls` or not

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
  host: {{ .Values.host }}
  {{ if eq .Values.tls "active" }}
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  {{ end }}
  to:
    kind: Service
    weight: 100
    name: nginx
status:
  ingress: []
```

Which needs to have an option in `values.yaml` like:

```yaml
tls: active
```

## Final product

The final chart will be:

```sh
$ find
.
./Chart.yaml
./templates
./templates/deployment.yaml
./templates/service.yaml
./templates/pvc.yaml
./templates/route.yaml
./values.yaml
./charts
./.helmignore
```

* `Chart.yaml`:

```yaml
apiVersion: v2
name: example
description: A Helm chart for Kubernetes
type: application

version: 0.1.0

appVersion: "1.16.0"
```

* `templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: Rolling
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: docker.io/bitnami/nginx:latest
        name: nginx
        ports:
        - containerPort: 8080
          protocol: TCP
        - containerPort: 8443
          protocol: TCP
        resources: {}
        volumeMounts:
        - mountPath: /opt/bitnami/nginx/html/
          name: html
      volumes:
      - name: html
        persistentVolumeClaim:
          claimName: html
```

* `templates/service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  selector:
    app: nginx
  ports:
  - nodePort: 0
    port: 8080
    protocol: TCP
    targetPort: 8080
```

* `templates/pvc.yaml`:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.storage.size | default "500Mi" }}
  storageClassName: {{ .Values.storage.class | default "glusterfs-storage" }}
status: {}
```

* `templates/route.yaml`:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
  host: {{ .Values.host }}
  {{ if eq .Values.tls "active" }}
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  {{ end }}
  to:
    kind: Service
    weight: 100
    name: nginx
status:
  ingress: []
```

* `./values.yaml`:

```yaml
image: bitnami/nginx:latest
host: example.2.rahtiapp.fi
tls: active

storage:
  size: 1Gi
  class: glusterfs-storage
```

## Using online Helm Repo  
### Adding a repo
It's also possible to install `repository` and then use them for deploying applications.  
For example [JupyterHub](https://z2jh.jupyter.org/en/stable/jupyterhub/installation.html), you can install the `repo` with this command:  
```sh
helm repo add jupyterhub https://hub.jupyter.org/helm-chart/
```

If you type this command:  
```sh
helm repo list   
```
You should see your newly added repostory.  

It also possible to check for updates (and update your `repo`) with this command:  
```sh
helm repo update
```

You can search and check the packages available:  
```sh
helm search repo jupyterhub
NAME                            CHART VERSION   APP VERSION     DESCRIPTION                    
jupyterhub/jupyterhub           3.1.0           4.0.2           Multi-user Jupyter installation                   
```
### Check values
When installing an online `repo`, you can check the default `values` used when you deploy it. For that, type the following command:  
```sh
helm show values jupyterhub/jupyterhub > values.yaml
```
[ArtifactHub](https://artifacthub.io/) is a good site where you can find packages

### Edit and install from a repo  
After exporting the default `values` you can edit or create a `config` file with your own values.  
Then, you can install the `Chart` using this command:  
```sh
helm install my-jupyterhub jupyterhub/jupyterhub -f config.yaml
```
