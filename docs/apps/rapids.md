---
tags:
  - Free
---

# RAPIDS

Suite of libraries for data analytics and machine learning on GPUs.

!!! info "News"

    **5.10.2022** Due to Puhti's update to Red Hat Enterprise Linux 8
    (RHEL8), **the number of supported RAPIDS versions has been reduced.**
    Please [contact our servicedesk](../support/contact.md) if you really
    need access to older versions.

    **5.5.2022** Due to Mahti's update to Red Hat Enterprise Linux 8 (RHEL8),
    older versions of RAPIDS are no longer fully supported. Please
    [contact our servicedesk](../support/contact.md) if you really need access
    to older versions.

    **4.2.2022** All old RAPIDS versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/tutorials/conda.md).


## Available

RAPIDS is available on both Puhti and Mahti. Currently supported
RAPIDS versions:

- 22.04, based on [RAPIDS official Docker images](https://hub.docker.com/r/rapidsai/rapidsai/): `22.04`

Contains the [RAPIDS](https://rapids.ai/) suite (including
[cuDF](https://github.com/rapidsai/cudf),
[cuML](https://github.com/rapidsai/cuml),
[cuGraph](https://github.com/rapidsai/cugraph), and
[XGBoost](https://rapids.ai/xgboost.html)) for Python with GPU support via CUDA.

If you find that some package is missing, you can often install it yourself with
`pip install --user`. See
[our Python documentation](../support/tutorials/python-usage-guide.md) for
more information on how to install packages yourself. If you think that some
important RAPIDS-related package should be included in the module provided by
CSC, please [contact our servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known
as Singularity). Wrapper scripts have been provided so that common
commands such as `python`, `python3`, `pip` and `pip3` should work as
normal. For other commands, you need to prefix them with
`apptainer_wrapper exec`. For more information, see
[CSC's general instructions on how to run Apptainer containers](../computing/containers/run-existing.md).

## License

RAPIDS is licensed under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Usage

To use this software, initialize it with:

```bash
module load rapids
```

to access the default version.

To see all the available versions, run:

```bash
module avail rapids
```

To check the exact packages and versions included in the loaded module, you can run:

```bash
list-packages
```

!!! warning "Note" 

    Login nodes are not intended for heavy computing, please use
    Slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

### Local storage

The GPU nodes have fast local storage which is useful for I/O-intensive
applications. See our [general instructions on how to take the fast local
storage into
use](../computing/running/creating-job-scripts-puhti.md#local-storage).

## More information

- [RAPIDS Docs](https://docs.rapids.ai/)
- [RAPIDS Sample Notebooks](https://github.com/rapidsai/notebooks)
