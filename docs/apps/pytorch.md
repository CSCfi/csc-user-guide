# PyTorch

Machine learning framework for Python.

## Available

The `pytorch` module is available on Puhti only.  Currently supported PyTorch versions:

- 1.2.0
- 1.1.0
- 1.0.1

Includes [PyTorch](https://pytorch.org/) and related libraries with GPU support via CUDA.  Also includes all the packages from [Python Data](python-data.md).

If you find that some package is missing, you can often install it yourself with `pip install --user`.

If you think that some important PyTorch-related package should be included in the module provided by CSC, you can send an email to <servicedesk@csc.fi>.

## License

PyTorch is BSD-style licensed, as found in the [LICENSE file](https://github.com/pytorch/pytorch/blob/master/LICENSE).

## Usage

To use this software on Puhti, initialize it with:

```text
module load pytorch
```

to access the default version.

This will show all available versions:

```text
module avail pytorch
```

To check the exact packages and version included a specific module, you can run for example:

```text
module help pytorch/1.2.0
```

!!! note 

    Note that Puhti login nodes are not intended for heavy
    computing. Please use slurm batch jobs instead.

## More information

- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)
