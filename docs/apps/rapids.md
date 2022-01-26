# RAPIDS

Suite of libraries for data analytics and machine learning on GPUs.

## Available

Rapids is available on Puhti and Mahti. Some older versions are available on
Puhti only. Currently supported RAPIDS versions:

- 21.12 using Singularity, based on [RAPIDS official Docker images](https://hub.docker.com/r/rapidsai/rapidsai/): `21.12`
- 0.16 using Singularity: `0.16-sng` (Puhti only)
- 0.15 using Singularity: `0.15-sng` (Puhti only)
- 0.14 using Singularity: `0.14-sng` (Puhti only)
- 0.11  (Puhti only)

Contains the [RAPIDS](https://rapids.ai/) suite (including
[cuDF](https://github.com/rapidsai/cudf),
[cuML](https://github.com/rapidsai/cuml),
[cuGraph](https://github.com/rapidsai/cugraph), and
[XGBoost](https://rapids.ai/xgboost.html)) for Python with GPU support via CUDA.

Modules ending with `-sng` are based on NVIDIA's optimized container images from
[NGC](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai).

If you find that some package is missing, you can often install it yourself with
`pip install --user`. If you think that some important RAPIDS-related package
should be included in the module provided by CSC, you can send an email to
<servicedesk@csc.fi>.

Some modules are Singularity-based. Wrapper scripts have been provided so that
common commands such as `python`, `python3`, `pip` and `pip3` should work as
normal. For more information, see [CSC's general instructions on how to run
Singularity containers](../computing/containers/run-existing.md).


## License

RAPIDS is licensed under [Apache License 2.0](https://rapids.ai/community.html)

## Usage

To use this software, initialize it with:

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

    Note that login nodes are not intended for heavy computing, please use
    slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

### Local storage

The GPU nodes have fast local storage which is useful for IO-intensive
applications. See our [general instructions on how to take the fast local
storage into
use](../computing/running/creating-job-scripts-puhti.md#local-storage).

## More information

- [RAPIDS Docs](https://docs.rapids.ai/)
- [RAPIDS Sample Notebooks](https://github.com/rapidsai/notebooks)
