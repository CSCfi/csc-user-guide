# Data storage for machine learning

This guide explains how to store your data efficiently for machine learning
applications on CSC's supercomputers. It is part of our [Machine learning
guide](ml-guide.md).

## Where to store data?

CSC's supercomputers have three types of shared disk areas: **home**,
**projappl** and **scratch**. You can [read more about the disk areas
here](../../computing/disk.md). For [LUMI check the data storage
section here](https://docs.lumi-supercomputer.eu/storage/). In
general, keep your code and software in **projappl** and datasets,
logs and calculation outputs in **scratch**. The **home** directory is
not intended for data analysis and computing, and you should only
store small personal files there.

In addition, [LUMI has a shared **flash** storage
area](https://docs.lumi-supercomputer.eu/storage/) which is faster to
access than scratch. Flash is meant only for temporary storing the
data for processing, and the [flash area has higher cost than using
normal scratch
storage](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/#flash-storage-lumi-f-billing).

It is recommended to store big datasets in the [Allas object
store](../../data/Allas/index.md), and download them to your project's
scratch directory prior to starting your computation. For example:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
swift download <bucket-name> your-dataset.tar
```

Anything that needs to be stored for a longer time (project life-time)
should be copied back to Allas. The [scratch disk area will be
regularly cleaned of old files](clean-up-data.md), and should not be used to store
anything important long-term.

Some CPU nodes and all GPU nodes on Puhti and Mahti (but *not* LUMI)
also have fast local NVMe drives with at least 3.6 TB disk space. This
space is available only during the execution of the Slurm job, and is
cleaned up afterwards. For data intensive jobs it is often worthwhile
to copy the data to the NVMe at the start of the job and then to store
the final results on the scratch drive at the end of the job. [See
below for more information on how to use the fast local NVMe
drive](#fast-local-drive).


## Using the shared file system efficiently

The training data for machine learning models often consists of a huge number of
files. A typical example is training a neural network with tens of thousands of
relatively small JPEG image files. Unfortunately the Lustre file system used in
`/scratch`, `/projappl` and users' home directories does not perform
well with random access of a lot of files or when performing many
small reads. In addition to slowing down the computation it may also
in extreme cases **cause noticeable slowdowns for all users of the
supercomputer, sometimes making the entire supercomputer unusable for
hours**.

!!! note

    Please **do not read a huge number of files from the shared file system**.
    Use the fast local drives or package your data into larger files
    for sequential access instead!

For further reading, see CSC's [technical description of the Lustre
filesystem](../../computing/lustre.md) and our general tutorial on [how to
achieve better I/O performance on Lustre](lustre_performance.md).


### More efficient data format

Many machine learning frameworks support formats for packaging your
data more efficiently. Common formats include [TensorFlow's
TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) and
[WebDataset](https://webdataset.github.io/webdataset/) for PyTorch.
Other examples include using
[HDF5](https://towardsdatascience.com/hdf5-datasets-for-pytorch-631ff1d750f5),
or [LMDB](http://deepdish.io/2015/04/28/creating-lmdb-in-python/)
formats, or even humble ZIP-files, e.g., via Python's
[zipfile](https://docs.python.org/3/library/zipfile.html) library.
See also [an example of creating TFRecord files from an image
dataset](https://github.com/CSCfi/machine-learning-scripts/blob/master/notebooks/tf2-pets-create-tfrecords.ipynb).

The main point with all of these formats is that instead of many
thousands of small files you have one or a few bigger files, which are
much more efficient to access and read sequentially. Don't hesitate to
[contact our service desk](../contact.md) if you need advice about how
to access your data more efficiently.


### Fast local drive (Puhti and Mahti only)

If you really need to access the individual small files, you can use
the fast NVMe local drive that is present in GPU nodes on Puhti and
Mahti. In brief, you just need to add `nvme:<number-of-GB>` to the
`--gres` flag in your submission script, and then the fast local
storage will be available in the location specified by the environment
variable `$LOCAL_SCRATCH`. Here is an example run that reserves 100 GB
of the fast local drive and extracts the dataset tar-package on that
drive before launching the computation:

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
