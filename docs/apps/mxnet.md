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

To check the exact packages and version included a specific module, you can run for example:

```text
module help mxnet/1.5.0
```

!!! note 

    Note that Puhti login nodes are not intended for heavy
    computing. Please use slurm batch jobs instead.

## More information

- [MXNet Python Tutorials](https://mxnet.apache.org/versions/master/tutorials/index.html#python-tutorials)
- [MXNet Python API](https://mxnet.apache.org/versions/master/api/python/index.html)
