# Machine learning at CSC

## What CSC service to use?

If you need GPU-accelerated machine learning, CSC's supercomputers, Puhti and
Mahti, are usually the way to go. First, please read the [instructions on how to
access Puhti and Mahti](../../computing/overview.md), and [how to submit
computing jobs](../../computing/running/getting-started.md).

In some special cases, a virtual server on
[**Pouta**](../../cloud/pouta/index.md) might make sense as it also offers GPUs.
This gives you more control over the computing environment, but may not be
suitable for very heavy computing tasks. For model deployment, the
[**Rahti**](../../cloud/rahti/index.md) contained cloud service might be used,
however, it currently doesn't offer GPU support. See some examples of [how to
deploy machine learning models on
Rahti](https://github.com/CSCfi/rahti-ml-examples).

Links:

* [GPU-accelerated machine learning](gpu-ml.md).
