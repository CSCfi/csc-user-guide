# Machine learning at CSC

This guide aims to give help and pointers to users who wish to do machine
learning using CSC's computing resources.

## What CSC service to use?

CSC offers several services which might be relevant for machine learning users:

- [Supercomputers, Puhti and Mahti](../../computing/overview.md) are multi-user
  clusters and offer the highest computing perfomance, including GPU
  acceleration in a centrally controlled software environment,

- [Pouta](../../cloud/pouta/index.md) offers your own virtual server with full
  control of the software environment, but restricted computing performance
  compared to supercomputers, 

- [Rahti](../../cloud/rahti/index.md) offers a more automatised container-based
  cloud environment, useful in particular for deploying web services.

**Our recommendation is to use CSC's Puhti or Mahti supercomputers**, unless you
need a very complicated software environment, or work with sensitive data. In
those cases Pouta might be the right choice, and we also offer the ePouta
variant which is suited for cases with high security requirements.

If you are developing a service, for example want to deploy a trained model as a
service, then Pouta or Rahti might be most relevant for you. 

If you are unsure about the right service to use, don't hesitate to [contact our
service desk](../contact.md) and explain your computing needs.


## CSC's supercomputers

For most machine learning needs [CSC's supercomputers, Puhti and
Mahti](../../computing/overview.md), are the way to go. Both are clusters of
hundreds of computers, some of which offer GPU-acceleration. The supercomputers
are multi-user systems, so individual users have limited rights to install
software, and as with any shared resource one must follow the [usage
policy](../../computing/overview.md#usage-policy) so that the service can remain
usable.

If you are a new user, please read [how to access Puhti and
Mahti](../../computing/overview.md), and [how to submit computing
jobs](../../computing/running/getting-started.md).

Also check our related in-depth tutorials:

* [GPU-accelerated machine learning on CSC's supercomputers](gpu-ml.md)
* [Data storage for machine learning](ml-data.md)
* [Multi-GPU and multi-node machine learning jobs](ml-multi.md)

*TODO*

* Singularity-stuff for ML?
* Hyperparameter optimization
* Puhti web UI for ML?


## Cloud services

In some cases, a virtual server on [**Pouta**](../../cloud/pouta/index.md) might
make sense as it gives you more control over the software environment, but may
not be suitable for very heavy computing tasks as it offers less computing
resources than a supercomputer. Pouta has a limited amount of older NVIDIA P100
GPUs.

*TODO*

### MLOps

For model deployment, the [**Rahti**](../../cloud/rahti/index.md) contained
cloud service might be used, however, it currently doesn't offer GPU support.

* [How to utilize MLflow to train and serve your ML model](https://github.com/CSCfi/mlflow-openshift)
* [How to deploy machine learning models on Rahti](https://github.com/CSCfi/rahti-ml-examples)
