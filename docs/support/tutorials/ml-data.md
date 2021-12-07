# Data storage for machine learning

## Where to store data?

Puhti and Mahti have three types of disk areas: **home**, **projappl** and
**scratch**. You can [read more about the disk areas
here](../../computing/disk.md). In general keep you code and software in
**projappl** and datasets, logs and calculation outputs in **scratch**.

It is recommended to store big datasets in the [Allas object
store](../../data/Allas/index.md), and download them to your project's scratch
directory prior to starting your computation. Example:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
swift download <bucket-name> your-dataset.tar
```

Anything that needs to be stored for a longer time (project life-time) should be
copied back to Allas. CSC may at some point start cleaning the scratch drive so
that files older than 90 days will be automatically removed (this has not yet
been activated!).

Some CPU nodes and all GPU nodes also have a fast local NVME drive with at least
3.6 TB disk space. This space is available only during the execution of the
Slurm job, and is cleaned up afterwards. For data intensive jobs, it may still
be worth copying the data to the NVME at the start of the job and then storing
the final results on the scratch drive at the end of the job. [More information
on how to use the fast local NVME drive below](#fast-local-drive).


## Using the shared file system efficiently

Training machine learning models often require reading a huge number of
relatively small files from the shared drive. Unfortunately the Lustre-shared
file systems (e.g. `/scratch`, `/projappl` and users' home directories) do not
perform well when opening a lot of files or when performing many small reads. In
addition to slowing down the computation it may also in extreme cases **cause
noticeable slowdowns for all users of the supercomputer, sometimes making the
entire supercomputer unusable for hours**.

!!! note

    Please **do not read a huge number of files from the shared file system**, use
    fast local disk or package your data into larger files instead!

For further reading, see CSC's [technical description of the Lustre
filesystem](../../computing/lustre.md) and our general tutorial on [how to
achieve better I/O performance on Lustre](lustre_performance.md).

As a solution for machine learning applications, we recommend either **using
more efficent data formats**, such as TFRecords for TensorFlow, or **using the
fast local NVME drive**. These approaches are described in more detail below.


### More efficient data format

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
read linearly. Don't hesitate to [contact our service desk](../contact.md) if
you need advice about how to access your data more efficiently.


### Fast local drive

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

If you are running a [multi-node job](ml-multi.md), you need to modify the `tar`
line so that it is performed on each node separately:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 \
    tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH
```
