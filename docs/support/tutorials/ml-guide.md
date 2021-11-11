# Machine learning at CSC

This guide attempts to help users wishing to use machine learning at CSC to find
the most suitable service, for example GPU-accelerated supercomputing or cloud
services.

This guide also contains several in-depth tutorials on various advanced aspects
of machine learning usage on CSC.

## CSC's supercomputers

For most machine learning needs [CSC's supercomputers, Puhti and
Mahti](../../computing/overview.md), are the way to go. Both are clusters of
hundreds of computers, some of which offer GPU-acceleration. The supercomputers
are multi-user systems, so individual users have limited rights to install
software, and as with any shared resource one must follow the [usage
policy](../../computing/overview.md#usage-policy) so that the service can remain
usable.

If you are a new user, please read at least:

* [How to access Puhti and Mahti](../../computing/overview.md),
* [How to submit computing jobs](../../computing/running/getting-started.md). 

Also check our related in-depth tutorials:

* [Using GPUs for machine learning on CSC's Supercomputers](gpu-ml.md)
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

For model deployment, the [**Rahti**](../../cloud/rahti/index.md) contained
cloud service might be used, however, it currently doesn't offer GPU support.
See some examples of [how to deploy machine learning models on
Rahti](https://github.com/CSCfi/rahti-ml-examples).

*TODO*

* MLOps (MLflow, Rahti deployment) - in which section?
