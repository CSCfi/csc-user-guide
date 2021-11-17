# MXNet

Deep learning framework for Python.

## Available

The `mxnet` module is available on Puhti only.  Currently supported MXNet versions:

- 1.5.0

Includes [MXNet](https://mxnet.apache.org/) for Python with GPU support via CUDA.  Also includes all the packages from [Python Data](python-data.md).

If you find that some package is missing, you can often install it yourself with `pip install --user`.

If you think that some important MXNet-related package should be included in the module provided by CSC, you can send an email to <servicedesk@csc.fi>.

## License

MXNet is licensed under [Apache License 2.0](https://github.com/apache/incubator-mxnet/blob/master/LICENSE)

## Usage

To use this software on Puhti, initialize it with:

```text
module load mxnet
```

to access the default version.

This will show all available versions:

```text
module avail mxnet
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

- [MXNet Python Tutorials](https://mxnet.apache.org/api/python/docs/tutorials/)
- [MXNet Python API](https://mxnet.apache.org/versions/master/api/python/index.html)
