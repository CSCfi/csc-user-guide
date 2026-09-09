# Data storage for machine learning

This guide explains how to store your data efficiently for machine learning
applications on CSC's supercomputers. It is part of our
[Machine learning guide](ml-guide.md).

## Where to store data?

CSC's supercomputers have three types of shared disk areas: **home**,
**projappl** and **scratch**. You can
[read more about the disk areas for Roihu here](../../computing/roihu-disk.md). For
[LUMI check the data storage section here](https://docs.lumi-supercomputer.eu/storage/).
In general, keep your code and software in **projappl** and datasets,
logs and calculation outputs in **scratch**. The **home** directory is
not intended for data analysis and computing, and you should only
store small personal files there.

In addition, [LUMI has a shared **flash** storage area
LUMI-F](https://docs.lumi-supercomputer.eu/storage/#__tabbed_1_4)
which is faster to access than scratch. Note that [LUMI-F has higher
cost than using normal scratch
storage](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/#flash-storage-lumi-f-billing).

It is recommended to store datasets in the [Allas object
store](../../data/Allas/index.md), and download them to your project's
scratch directory prior to starting your computation. For example:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
s3cmd get s3://<bucket-name>/<your-dataset>.tar
```

Anything that needs to be stored for a longer time than 180 days
should be copied back to Allas. The [scratch disk area will be
regularly cleaned of old
files](clean-up-data.md#automatic-removal-of-files), and should not be
used to store anything important long-term.

Finally, if you are working with other projects that all need access
to the same common data, you might consider applying for a [dataset
project in Roihu](../../computing/roihu-dataset-project.md). A dataset
project is a good way to host data that is read from often but not
written often.

## Using the shared file system efficiently

The training data for machine learning models often consists of a huge
number of files. A typical example is training a neural network with
hundreds of thousands of relatively small image or text
files. Unfortunately the Lustre file system used in `/scratch`,
`/projappl` and users' home directories **does not perform well with
random access of a lot of files or when performing many small
reads**. In addition to slowing down the computation it may also in
extreme cases cause noticeable slowdowns for all users of the
supercomputer, sometimes making the entire supercomputer unusable for
hours.

!!! note
    Please **do not read a huge number of files from the shared file system**.
    Use the fast local drives or package your data into larger files
    for sequential access instead!

For further reading, see CSC's
[technical description of the Lustre filesystem](../../computing/lustre.md)
and our general tutorial on
[how to achieve better I/O performance on Lustre](lustre_performance.md).

### More efficient data format

Many machine learning frameworks support formats for packaging your data more
efficiently. Common formats include [TensorFlow's TFRecord][TFRecord] and
[WebDataset] for PyTorch. Other examples include using [HDF5], or [LMDB]
formats, or even humble ZIP-files, e.g., via Python's [zipfile] library.

The [LUMI AI guide][LUMI-AI-data] has a nice comparison of different
formats for use with PyTorch. See also
[an example of creating TFRecord files from an image dataset][tfrecord-example].

The main point with all of these formats is that instead of many
thousands of small files you have one or a few bigger files, which are
much more efficient to access and read sequentially. Don't hesitate to
[contact our service desk](../contact.md) if you need advice about how
to access your data more efficiently.

[TFRecord]: https://www.tensorflow.org/tutorials/load_data/tfrecord
[WebDataset]: https://github.com/webdataset/webdataset
[HDF5]: https://docs.h5py.org/en/stable/
[LMDB]: https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database
[zipfile]: https://docs.python.org/3/library/zipfile.html
[LUMI-AI-data]: https://github.com/Lumi-supercomputer/LUMI-AI-Guide/tree/main/03-file-formats#readme
[tfrecord-example]: https://github.com/CSCfi/machine-learning-scripts/blob/master/notebooks/tf2-pets-create-tfrecords.ipynb

### Fast local drive

If you really need to access the individual small files, you can use
the [fast NVMe local drive that is present in all compute nodes on
Roihu](../../computing/roihu-disk.md#compute-nodes). This area can be
accessed in the location specified by the environment variable
`$TMPDIR`, and for GPU jobs it has a maximum capacity of 150 GiB.

Here is an example run for Roihu that extracts the dataset tar-package
to `$TMPDIR` before launching the computation:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpumedium
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=72
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:gh200:1

tar xf /scratch/<your-project>/your-dataset.tar -C $TMPDIR

srun python3 myprog.py --input_data=$TMPDIR <options>
```

Note that you need to communicate to your own program where to find
the dataset, for example with a command line argument. Also see our
[general instructions on how to take the fast local storage into
use](../../computing/running/creating-job-scripts-roihu.md#local-temporary-storage).

If you are running a [multi-node job](ml-multi.md), you need to modify the `tar`
line so that it is performed on each node separately:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 \
    tar xf /scratch/<your-project>/your-dataset.tar -C $TMPDIR
```


### Disaggregated NVMe

Finally, if 150 GiB is not enough, [Roihu also supports disaggregated
NVMe](../../computing/roihu-disk.md#disaggregated-storage). This fast
storage capacity is provided over the network and will appear as local
scratch from within a Slurm job. The total capacity of the
disaggregated NVMe resource is 307.2 TB. Disaggregated NVMe is still
considered an experimental feature on Roihu, and is currently
available only on full node jobs.
