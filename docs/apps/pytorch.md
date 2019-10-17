# PyTorch

Machine learning framework for Python.

## Available

The `pytorch` module is available on Puhti only.  Currently supported PyTorch versions:

- 1.3.0
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

To check the exact packages and versions included in the loaded module you can run:

```text
list-packages
```

!!! note 

    Note that Puhti login nodes are not intended for heavy computing, please use slurm batch jobs instead. See our [instructions on how to use the batch job system](../computing/running/getting-started.md).

Example batch script for reserving one GPU and 10 CPUs in a single node:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1

module load pytorch/1.3.0
srun python3 myprog.py <options>
```

### Local storage

The GPU nodes in Puhti have fast local storage which is useful for IO-intensive applications.  See our [general instructions on how to take the fast local storage into use](../computing/running/creating-job-scripts.md#local-storage).  For example to use 100 GB of local storage, just change the `gres` line in the above batch script example to:

```bash
#SBATCH --gres=gpu:v100:1,nvme:100
```

## More information

- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)
