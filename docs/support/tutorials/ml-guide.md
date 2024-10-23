---
title: Machine learning guide
---

# Machine learning guide

This guide aims to help users who wish to do machine learning using CSC's
computing resources.

## Machine learning guide subsections

In addition to this page, this guide contains the following subsections:

- [**Getting started with machine learning at CSC**](ml-starting.md)
- [**GPU-accelerated machine learning**](gpu-ml.md)
- [**Data storage for machine learning**](ml-data.md)
- [**Multi-GPU and multi-node machine learning**](ml-multi.md)
- [**Hyperparameter search**](hyperparameter_search.md)
- [**Managing machine learning workflows on CSC's supercomputers**](ml-workflows.md)
- &#127381; [**Working with large language models on supercomputers**](ml-llm.md)

## What CSC service to use?

CSC offers several services which might be relevant for machine learning users:

- [Supercomputers, Puhti, Mahti](../../computing/index.md) and
  [LUMI](https://docs.lumi-supercomputer.eu/) are multi-user clusters
  and offer the highest computing performance, including GPU
  acceleration in a centrally controlled software environment,

- [Pouta](../../cloud/pouta/index.md) offers your own virtual server with full
  control of the software environment, but restricted computing performance
  compared to supercomputers, 

- [Rahti](../../cloud/rahti/index.md) offers a more automatized container-based
  cloud environment, useful in particular for deploying web services.

**Our recommendation is to use CSC's supercomputers**, unless you need
a very complicated software environment, or work with sensitive
data. In those cases Pouta might be the right choice, and we also
offer the ePouta variant which is suited for cases with high security
requirements.

If you are developing a service, for example want to deploy a trained
model as a service, then Pouta or Rahti might be most relevant for
you.

If you are unsure about the right service to use, don't hesitate to
[contact our service desk](../contact.md) and explain your computing
needs.


## CSC's supercomputers

For most machine learning needs CSC's supercomputers are the way to
go. These are clusters of hundreds (or thousands) of computers, some
of which offer GPU-acceleration. The supercomputers are multi-user
systems, so individual users have limited rights to install software,
and as with any shared resource one must follow the [usage
policy](../../computing/usage-policy.md) so that the service can
remain usable.

CSC hosts two national supercomputers: Puhti and Mahti, and the
European LUMI supercomputer. If you are [unsure which supercomputer to
choose, read the discussion here](gpu-ml.md#puhti-mahti-or-lumi).

If you are a new user, please read [how to access Puhti and
Mahti](../../computing/index.md#accessing-puhti-and-mahti), and [how
to submit computing
jobs](../../computing/running/getting-started.md). If you have opted
for LUMI read the [LUMI Get Started
page](https://docs.lumi-supercomputer.eu/firststeps/).

Both [Puhti and Mahti have a web
interface](../../computing/webinterface/index.md) which can be
accessed via [www.puhti.csc.fi](https://www.puhti.csc.fi) and
[www.mahti.csc.fi](https://www.mahti.csc.fi), respectively. Via the
web interface, one can easily launch for example a Jupyter Notebook
session with TensorFlow or PyTorch.

Also check the subsections related to [efficient GPU
utilization](gpu-ml.md), [how to work with big data sets](ml-data.md),
and [multi-GPU and multi-node jobs](ml-multi.md).


## Cloud services

### Pouta

There are some use cases where the supercomputers are not the right solution,
and you may need a [virtual server on **Pouta**](../../cloud/pouta/index.md).
Typical examples include:

- very complex software environment,
- need for root access,
- computation involving sensitive data.

With Pouta you get your own virtual server, where you have root or administrator
access. [HPC and GPU flavors are
available](../../cloud/pouta/vm-flavors-and-billing.md#hpc-flavors) for heavy
computing needs, however, the computing resources will always be smaller than in
a supercomputer.

For computation involving highly sensitive data we also offer the ePouta variant
which is suited for cases with high security requirements. With ePouta the
virtual server will be integrated into your existing network infrastructure.

See our [Pouta documentation pages on how to apply for
access](../../cloud/pouta/index.md).


## Further reading in Docs CSC

* [Python parallel jobs](python-usage-guide.md#python-parallel-jobs)
* [Dask tutorial](dask-python.md)
* [High-throughput computing and workflows](../../computing/running/throughput.md)
