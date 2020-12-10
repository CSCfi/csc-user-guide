# RAPIDS

Suite of libraries for data analytics and machine learning on GPUs.

## Available

The `rapids` module is available on Puhti only.  Currently supported RAPIDS versions:

- 0.16 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `0.16-sng`
- 0.15 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `0.15-sng`
- 0.14 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `0.14-sng`
- 0.11

Contains the [RAPIDS](https://rapids.ai/) suite (including [cuDF](https://github.com/rapidsai/cudf), [cuML](https://github.com/rapidsai/cuml), [cuGraph](https://github.com/rapidsai/cugraph), and [XGBoost](https://rapids.ai/xgboost.html)) for Python with GPU support via CUDA.

Modules ending with `-sng` are based on NVIDIA's optimized container
images from
[NGC](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai).

!!! note 

    In Singularity-based modules you need to launch Python with `singularity_wrapper`, see [here for a usage example](../support/tutorials/gpu-ml.md#singularity).

If you find that some package is missing, you can often install it yourself with `pip install --user`, or `singularity_wrapper exec pip install --user` in Singularity-based modules. If you think that some important RAPIDS-related package should be included in the module provided by CSC, you can send an email to <servicedesk@csc.fi>.

## License

RAPIDS is licensed under [Apache License 2.0](https://rapids.ai/community.html)

## Usage

To use this software on Puhti, initialize it with:

```text
module load rapids
```

to access the default version.

This will show all available versions:

```text
module avail rapids
```

To check the exact packages and versions included in the loaded module you can run:

```text
list-packages
```

!!! note 

    Note that Puhti login nodes are not intended for heavy computing, please use slurm batch jobs instead. See our [instructions on how to use the batch job system](../computing/running/getting-started.md).

### Local storage

The GPU nodes in Puhti have fast local storage which is useful for IO-intensive applications.  See our [general instructions on how to take the fast local storage into use](../computing/running/creating-job-scripts-puhti.md#local-storage).

## More information

- [RAPIDS Docs](https://docs.rapids.ai/)
- [RAPIDS Sample Notebooks](https://github.com/rapidsai/notebooks)
