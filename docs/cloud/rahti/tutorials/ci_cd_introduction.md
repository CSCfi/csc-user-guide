<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/tutorials/ci_cd_introduction/)

# Introduction

Nowadays agile software development methodologies are being used to satisfy
the continuously changing requirements of a given software. The main aim of
agile software development is to continuously and quickly deliver new pieces
of software and improve customer satisfaction.  Continuous Integration and
Continuous Delivery (CI/CD) provides developers the necessary tools to streamline
and accelerate the speed at which they can deploy new code and become more agile.

In this tutorial, we will set up a simple CI/CD pipeline using the Kubernetes concepts
such as _ImageStream_, _BuildConfig_, and _DeploymentConfig_. Please refer to these Kubernetes
concepts in [Kubernetes and OpenShift concepts](/cloud/rahti/concepts/).

!!! Note

    In practice, CI/CD pipelines for complex applications involve the use of dedicated resources
    and tools such as Tekton and Jenkins. However, simple applications can be deployed the way
    described in this tutorial. The primary aim of this tutorial is to teach the core concepts of
    Kubernetes in terms of CI/CD.

## Preparation

Make sure you have the `oc` command line installed, and that you are logged in. Please
check the [command line tool installation](/cloud/rahti/usage/cli/) if you need help on that.

## Quick Start

We have written a hello world web application and defined the necessary Kubernetes objects to build
and deploy it to Rahti. The following steps will quickly get you started:

Clone the source repository for the sample application.

```
git clone https://github.com/CSCfi/rahti-bc-example.git
cd rahti-bc-example/
```

Login to Rahti if you haven't done so. You can copy your login command from the Rahti UI.

```
 oc login https://rahti.csc.fi:8443 --token=<your_token>
```

Make sure you are in the right project with `oc project` and if not you can create one
with `oc new-project <your-new-project-name>`.

We have all the necessary object definitions in the `rahti-bc-example` project under the `k8s-api-objs.yaml`.
Please refer to [Kubernetes and OpenShift concepts](/cloud/rahti/concepts/) to understand the objects
defined under `k8s-api-objs.yaml`. You can easily create these objects necessary for our CI/CD pipeline using
the `oc create` command as follows:

```
$ oc create -f k8s-api-objs.yaml
imagestream.image.openshift.io/dockerfile-example created
buildconfig.build.openshift.io/dockerfile-example created
deploymentconfig.apps.openshift.io/dockerfile-example created
service/dockerfile-example created
route.route.openshift.io/dockerfile-example created
```

At this point you have a simple CI\CD pipeline created. The next step
will be to kick off the build and let the pipeline handle the build and
deployment. You can trigger such an action using the `oc build` as follows:

```
oc start-build dockerfile-example --from-dir=./ -F
```

Once the pipeline finishes running you can visit your application deployment
by following the route which should look like `http://dockerfile-example-<your_project_name>.rahtiapp.fi/`.
This pipeline can be triggered again after any update to your application (e.g. update on `index.html`) and
the changes would reflect almost immediately. [Webhooks](/cloud/rahti/tutorials/webhooks/) can also be setup
to trigger the pipeline.

## Cleaning up

Once we are satisfied with the application, let us not keep it running in the
cluster but remove it with the command `oc delete`:

```bash
oc delete all --selector app=dockerfile-example
```

This will delete all objects with the label `app: dockerfile-example`.

## Conclusion

In this tutorial, a simple CI/CD pipeline to build and deploy a static web page was created mainly
using the Kubernetes objects _ImageStream_, _BuildConfig_, and _DeploymentConfig_. The pipeline
can be further extended using dedicated tools and resources as [Jenkins](https://docs.openshift.com/container-platform/3.11/dev_guide/dev_tutorials/openshift_pipeline.html),
[Tekton](https://www.openshift.com/learn/topics/pipelines), and [Webhooks](/cloud/rahti/tutorials/webhooks/).
