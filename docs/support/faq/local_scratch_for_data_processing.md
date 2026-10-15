# Which directory should I use to analyze many small files?

An [interactive batch job](../../computing/running/interactive-usage.md) on
Roihu allows you to start a shell session on a CPU node with up to:

* 32 cores
* 64 GB of memory
* 36 hours of run time

To launch an interactive session on Roihu, execute the command:

```bash
sinteractive -i
```

The "normal" Lustre-based project-specific directories *scratch* and *projappl*
can store large amounts of data and are accessible to all nodes of Roihu.
However, these directories are
[inefficient for managing thousands of files](../../computing/running/performance-checklist.md#mind-your-io-it-can-make-a-big-difference).

Generally, you should avoid workflows that require creating large amounts of
small files. If you anyhow need to work with thousands of files, you should
consider using the
[NVMe-based temporary local disk areas](../../computing/disk.md#temporary-local-disk-areas),
either through normal or interactive batch jobs. These areas are node-specific
and visible only to the batch job that requests them. After the job ends, the
data is purged. Because of this, you need to always first import your dataset
to the local disk, and when you finish, copy the data you want to preserve back
to some more permanent storage place such as scratch or Allas.

Interactive CPU batch jobs launched with `sinteractive` on Roihu automatically
provide access to 20 GiB of
[fast local disk](../../computing/disk.md#temporary-local-disk-areas)
(`$TMPDIR`), which is suitable for processing small files efficiently. For
larger needs, users should instead request
[disaggregated storage](../../computing/disk.md#disaggregated-storage) using
`srun` directly, as shown further below.

To demonstrate the use of the disaggregated storage, let's study a sample
directory called `big_data`. The directory contains about 100 GB of data in
120 000 files. Initially, the data is packaged as a single tar archive in the
scratch directory of project 2001234 (`/scratch/project_2001234/big_data.tar`)

First, we launch an interactive batch job with 2 cores, 4000 MB of memory and
250 GB of disaggregated storage.

```bash
srun --partition=interactive --account=<project> --cpus-per-task=2 --mem=4000 --time=02:00:00 \
  --bb="#BB_LUA SBF storagesize=250G path=/sbf/data" --pty bash -i
```

The analysis is then done in three steps:

1. Move to the disaggregated storage area and extract the tar package:
   ```bash
   cd /sbf/data
   tar xf /scratch/project_2001234/big_data.tar
   ```

2. Run the analysis. This time we run a `for` loop that uses a command
   `transeq` to translate all fasta files found in the `big_data` directory
   into new protein sequence files:
   ```bash
   for ffile in $(find ./ | grep fasta)
   do
       transeq ${ffile} ${ffile}.pep
   done 
   ```
   In this example, about 52 000 fasta files were found. Thus, after the
   processing, the `big_data` directory now contains 52 000 more small files.
   The actual translation is a computationally light task, so most time is used
   just to open and close files (I/O).

3. When the processing is finished, we store the results back to the scratch
   directory as a new tar file:
   ```bash
   tar cf /scratch/project_2001234/big_data.pep.tar ./
   ```
   Now the results are safe in one file on scratch, and we can exit the
   interactive session.

The same analysis procedure could be done in the scratch directory too.
However, it is slow and may degrade the performance of the shared file system
for all users. Using disaggregated storage instead of a regular Lustre-based
scratch directory gives much more stable response times, since scratch
execution times will vary a lot based on the current total load on the Lustre
file system.

[More information about temporary local disk areas](../../computing/disk.md#temporary-local-disk-areas).
