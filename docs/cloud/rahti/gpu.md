<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../rahti4/gpu/)

# GPU usage in Rahti

Kubernetes and by extension Rahti do not support GPUs and other external devices natively. Instead,
they allow access to such extended resources through custom device plugins which are responsible for
handling the advertisement and allocation setup of these extended resources.

The device plugin used in Rahti handles Nvidia GPU with the resource name `nvidia.com/gpu`. More on
how it is used in practice later.

Currently, Rahti has a very limited amount of A100/P100 GPUs. For this reason, your Rahti projects
will not have access to GPU by default. This means you will need to request a GPU quota by sending
a request to servicedesk@csc.fi stating the Rahti project/namespace you need the quota for.

The Rahti GPU comes with an Nvidia driver which includes the low-level shared libraries and headers
needed to access/program the GPU device as well as the Nvidia device monitoring tools such as Nvidia
-smi which are useful for gathering information on the usage of GPUs. These libraries and tools will
be mounted and be made available to the pod automatically by the system during its creation.

## Running GPU-enabled pods

As a first example let's create a pod which runs `nvidia-smi` command line utility that is designed
to be used for managing and monitoring NVIDIA GPU devices. This is the simplest example that can be
used to demonstrate the availability of GPU in your Rahti project.

To run the example you need to login to Rahti and switch to the project that you have an approved
GPU quota as:

```bash
oc login https://rahti.csc.fi:8443 --token=<your-token>
oc project <your-project>
oc describe limitranges core-resource-limits #to check your assigned GPU qouta
```

Then create a file with the following content:

```yaml
# gpu-example-1.yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-example-1
spec:
  restartPolicy: Never
  containers:
    - name: gpu-example-1
      image: "nvidia/cuda:11.6.0-base-ubi8"
      command: ["nvidia-smi"]
      resources:
        limits:
          nvidia.com/gpu: 1
```

And run the following command to start the pod:
```bash
oc apply -f gpu-example-1.yaml
```

Finally check the output of the execution from the pod (you might need to wait for a few seconds for
the pod creation to complete) and clean up after using:
```bash
oc logs gpu-example-1
```
```bash
oc delete pod gpu-example-1
```

As second example you can create a pod running Cuda based vector addition to demonstrate access to
GPU through a lower-level programming model/interface.

To run the second example create a pod definition file as:

```yaml
# gpu-example-2.yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-example-2
spec:
  restartPolicy: OnFailure
  containers:
    - name: gpu-example-2
      # https://github.com/kubernetes/kubernetes/blob/v1.7.11/test/images/nvidia-cuda/Dockerfile
      image: "k8s.gcr.io/cuda-vector-add:v0.1"
      resources:
        limits:
          nvidia.com/gpu: 1 # requesting 1 GPU
```

And run, check the log (you might need to wait for a few seconds for the task to complete), and clean
up after as:

```bash
oc apply -f gpu-example-2.yaml
```
```bash
oc logs gpu-example-2
```
```bash
oc delete pod gpu-example-2
```

As a final example, we show how a more complete system that uses GPU resources can be deployed on Rahti.
The example provides an API for training and deploying a text sentiment classification model. To
facilitate easier deployment, we use various Kubernetes resource definitions and their explanation
can be found in the general [Kubernetes basics page](../concepts/).  One of the main things to notice
in this example is the Dockerfile that packages the application. The Dockerfile uses an appropriate
base image (`FROM tensorflow/tensorflow:2.7.0-gpu`) which contains the right runtime CUDA libraries
for utilizing the GPU resource. This image can be built locally and be pushed to an image repository
that can be used during the deployment of the system. A`BuildConfig` Openshift resource can also be
used as is the case in this example.

To run the example use the following command:
```bash
oc process -f https://raw.githubusercontent.com/tdeneke/rahti-ml-examples/tf2-imdb-cuda/rahti-ml-example-cuda-template.yaml
| oc create -f -
```

You can then follow the deployment of the application and its components from the Rahti console or
using `oc status`, and interact with the application using the UI at <your-application-route>/docs.
The route your application has been deployed to can be found from the Rahti console or using `oc get routes`.

After exploring and testing the example deployment it should be cleaned up as:
```bash
oc delete all -l app=rahti-ml-examples
```

## Limitations
At the moment, it is not possible to request a fraction of GPU. At least, a single or more GPU has
to be requested. Also, keep in mind that the GPU resources are scarce and at times your GPU request
might stay in a pending state until resources become available system-wide.
