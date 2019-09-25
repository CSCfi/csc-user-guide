# Using OpenShift extensions

In this example we'll explore OpenShift's extensions *DeploymentConfig*,
*ImageStream* and *BuildConfig* by creating the `serveapp` using them. Their
role in the process is as follows:

* [BuildConfig](/cloud/rahti/tutorials/advanced_tutorial#buildconfig) objects build container images
  based on source files.
* [ImageStream](/cloud/rahti/tutorials/advanced_tutorial#imagestream) objects abstract images and
  enrich them to streams that emit signals when they see that a new image is
  uploaded into them by, e.g., BuildConfig.
* [DeploymentConfig](/cloud/rahti/tutorials/advanced_tutorial#deploymentconfig) objects create new
  [ReplicationControllers](/cloud/rahti/tutorials/elemental_tutorial#replicationcontroller) based on
  the new images.

## DeploymentConfig

DeploymentConfigs are objects that create
[ReplicationControllers](/cloud/rahti/tutorials/elemental_tutorial#replicationcontroller) according to
`spec.template`. They differ from ReplicationControllers in a sense that 
DeploymentConfig objects may start new ReplicationControllers based on the state of
`spec.triggers`. In the example below, the DeploymentConfig will perform
an automatic rolling update when it gets triggered by an ImageStream named
"serveimagestream:latest". For other update strategies see "[Deployment
Strategies](https://docs.okd.io/latest/dev_guide/deployments/deployment_strategies.html)"
in the OpenShift documentation.

DeploymentConfig objects function similarly to Deployments described in the
Chapter "[Background ](/cloud/rahti/introduction/background)" except that Deployments
trigger updates only when `spec.template` is changed. Furthermore, Deployment
is a pure Kubernetes concept and DeploymentConfig is an OpenShift extension.

Recall that [ReplicationControllers](/cloud/rahti/tutorials/elemental_tutorial#replicationcontroller)
are objects that make sure that a requested number of replicas of the pod defined in the
`spec.template` are running.

*`deploymentconfig.yaml`*:

```yaml
apiVersion: v1
kind: DeploymentConfig
metadata:
  labels:
    app: serveapp
  name: blogdeployment
spec:
  replicas: 1
  selector:
    app: serveapp
    deploymentconfig: blogdeployment
  strategy:
    activeDeadlineSeconds: 21600
    type: Rolling
  template:
    metadata:
      labels:
        app: serveapp
        deploymentconfig: blogdeployment
    spec:
      containers:
      - name: serve-cont
        image: "serveimagestream:latest"
  triggers:
  - type: ConfigChange
  - imageChangeParams:
      automatic: true
      containerNames:
      - serve-cont
      from:
        name: serveimagestream:latest
    type: ImageChange
```

In this case, the DeploymentConfig object will listen to *ImageStream* object
`serveimagestream:latest`.

## ImageStream

ImageStreams simplify image names and get triggered by a BuildConfig if new
images are being uploaded to the registry. In the case where a new image is
uploaded, it can trigger its listeners to act. In the case of our
DeploymentConfig, the action triggered would be to do an update for the pods
that it is meant to deploy.

A simple ImageStream object looks like this:

*`imagestream.yaml`*:

```yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  labels:
    app: serveapp
  name: serveimagestream
spec:
  lookupPolicy:
    local: false
```

## BuildConfig

A BuildConfig objects create container images according to specific rules. In
the following example the Docker strategy is used to build trivial extension
of `httpd` image shipped with openshift.

*`buildconfig.yaml`*:

```yaml
kind: "BuildConfig"
apiVersion: "v1"
metadata:
  name: "serveimg-generate"
  labels:
    app: "serveapp"
spec:
  runPolicy: "Serial"
  output:
    to:
      kind: ImageStreamTag
      name: serveimagestream:latest
  source:
    dockerfile: |
      FROM docker-registry.default.svc:5000/openshift/httpd
  strategy:
    type: Docker
```

After creating the build object (here named `serveimg-generate`), we can
request openshift cluster to build the image with

```bash
 oc start-build serveimg-generate
```

Other source strategies include `custom`, `jenkins` and `source`.
