# Using OpenShift extensions

In this example, we explore OpenShift's extensions *DeploymentConfig*,
*ImageStream* and *BuildConfig* by creating the `serveapp` using them. The extensions'
role in the process:

* [BuildConfig](/cloud/rahti/tutorials/advanced_tutorial#buildconfig) objects build container images
  based on the source files.
* [ImageStream](/cloud/rahti/tutorials/advanced_tutorial#imagestream) objects abstract images and
  enrich them to streams that emit signals when they see that a new image is
  uploaded into them by e.g. BuildConfig.
* [DeploymentConfig](/cloud/rahti/tutorials/advanced_tutorial#deploymentconfig) objects create new
  [ReplicationControllers](/cloud/rahti/tutorials/elemental_tutorial#replicationcontroller) based on
  the new images.

## DeploymentConfig

DeploymentConfigs are objects that create
[ReplicationControllers](/cloud/rahti/tutorials/elemental_tutorial#replicationcontroller) according to
`spec.template`. They differ from ReplicationControllers in the sense that 
DeploymentConfig objects may start new ReplicationControllers based on the state of
`spec.triggers`. In the example below, the DeploymentConfig performs
an automatic rolling update when it gets triggered by an ImageStream named
`serveimagestream:latest`. For other update strategies, see "[Deployment
Strategies](https://docs.okd.io/latest/dev_guide/deployments/deployment_strategies.html)"
in the OpenShift documentation.

DeploymentConfig objects function similarly to deployments described in the
chapter [Background](/cloud/rahti/introduction/background) except that deployments
trigger updates only when `spec.template` is changed. Furthermore, deployment
is a pure Kubernetes concept, and DeploymentConfig is an OpenShift extension.

Recall that [ReplicationControllers](/cloud/rahti/tutorials/elemental_tutorial#replicationcontroller)
are objects that make sure that a requested number of replicas of the pod defined in the
`spec.template` is running.

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

In this case, the DeploymentConfig object listens to the *ImageStream* object
`serveimagestream:latest`.

## ImageStream

ImageStreams simplify image names and get triggered by a BuildConfig if new
images are uploaded to the registry. When a new image is
uploaded, it can trigger its listeners to act. In the case of our
DeploymentConfig, the action triggered would be to do an update for the pods
that it is meant to deploy.

A simple ImageStream object:

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

BuildConfig objects create container images according to specific rules. In
the following example, the _Docker_ strategy is used to build a trivial extension
of the `httpd` image shipped with OpenShift.

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
request the OpenShift cluster to build the image:

```bash
 oc start-build serveimg-generate
```

Other source strategies include `custom`, `jenkins` and `source`.
