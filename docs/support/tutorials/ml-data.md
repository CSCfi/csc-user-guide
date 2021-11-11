# Data storage for machine learning

It is recommended to store big datasets in [Allas](../../data/Allas/index.md),
and download them to your project's [scratch directory](../../computing/disk.md)
prior to starting your computation. Example:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
swift download <bucket-name> your-dataset.tar
```

!!! note

    Please **do not read a huge number of files from the shared file system**, use
    fast local disk or package your data into larger files instead!


Many machine learning tasks, such as training a model, require reading a huge
number of relatively small files from the drive. Unfortunately the Lustre-shared
file systems (e.g. `/scratch`, `/projappl` and users' home directories) do not
perform very well when opening a lot of files, and it also causes noticeable
slowdowns for all users of the supercomputer. Instead, consider more efficient
approaches, including:

- packaging your dataset into larger files 
- taking into use the [NVME fast local
  storage](../../computing/running/creating-job-scripts-puhti.md#local-storage)
  on the GPU nodes
- using a SquashFS image (Singularity-only)

## More efficient data format

Many machine learning frameworks support formats for packaging your data more
efficiently. For example [TensorFlow's
TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) format. Other
examples include using
[HDF5](https://towardsdatascience.com/hdf5-datasets-for-pytorch-631ff1d750f5),
or [LMDB](http://deepdish.io/2015/04/28/creating-lmdb-in-python/) formats, or
even humble ZIP-files, e.g., via Python's
[zipfile](https://docs.python.org/3/library/zipfile.html) library. The main
point with all of these is that instead of many thousands of small files you
have one, or a few bigger files, which are much more efficient to access and
read linearly. Don't hesitate to [contact our service
desk](https://www.csc.fi/contact-info) if you need advice about how to access
your data more efficiently.


## Fast local drive

If you really need to access the individual small files, you can use the fast
local drive that is present in every GPU node. In brief, you just need to add
`nvme:<number-of-GB>` to the `--gres` flag in your submission script, and then
the fast local storage will be available in the location specified by the
environment variable `$LOCAL_SCRATCH`. Here is an example run that reserves 100
GB of the fast local drive and extracts the dataset tar-package on that drive
before launching the computation:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1,nvme:100

tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH

srun python3 myprog.py --input_data=$LOCAL_SCRATCH <options>
```

Note that you need to communicate somehow to your own program where to find the
dataset, for example with a command line argument. Also see our [general
instructions on how to take the fast local storage into
use](../../computing/running/creating-job-scripts-puhti.md#local-storage).

If you are running a multi-node job (see next section), you need to modify the
`tar` line so that it is performed on each node separately:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 \
    tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH
```

## Using SquashFS

If you are running one of our [Singularity-based modules](#singularity), you can package your
dataset into a SquashFS image and mount it so it's visible to the code as a
normal directory. See [our documentation on how to mount datasets with
SquashFS](../../computing/containers/run-existing.md#mounting-datasets-with-squashfs)
for the details.

