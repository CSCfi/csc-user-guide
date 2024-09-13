# Which directory should I use to analyze many small files?
                   
An [interactive batch job](../../computing/running/interactive-usage.md) on
Puhti allows you to start a shell session on a compute node with up to:

* 8 cores
* 76 GB of memory
* 7 days of run time
* 720 GB of *fast local scratch disk*

To launch an interactive session on Puhti, execute the command:

```bash
sinteractive -i
```

One of the useful features of interactive batch jobs on Puhti is the NVMe-based
[fast local scratch area](../../computing/disk.md#temporary-local-disk-areas)
(`$LOCAL_SCRATCH`) that you may request. The "normal" Lustre-based
project-specific directories *scratch* and *projappl* can store large amounts
of data and are accessible to all nodes of Puhti. However, these directories
are
[inefficient for managing thousands of files](../../computing/running/throughput.md#inputoutput-efficiency).

Generally, you should avoid workflows that require creating large amounts of
small files. If you anyhow need to work with thousands of files, you should
consider using the NVMe-based temporary local disk areas, either through normal
or interactive batch jobs. The local scratch area is node-specific and visible
only to the batch job that requests it. After the job ends, the local scratch
is purged. Because of this, you need to always first import your dataset to the
local disk, and when you finish, copy the data you want to preserve back to
some more permanent storage place such as scratch or Allas.

To demonstrate the efficiency of the local scratch area, let's study a sample
directory called `big_data`. The directory contains about 100 GB of data in
120 000 files. Initially, the data is packaged as a single tar archive in the
scratch directory of project 2001234 (`/scratch/project_2001234/big_data.tar`)

First, we launch an interactive batch job with 2 cores, 4000 MB of memory and
250 GB of fast local temporary disk space.

```bash
sinteractive --cores 2 --mem 4000 --tmp 250
```

The analysis is then done in three steps:

1. Move to the local scratch area using the environment variable
   `$LOCAL_SCRATCH` and extract the tar package:
   ```bash
   cd $LOCAL_SCRATCH
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
for all users. To demonstrate the difference, below is an execution time
comparison for running the three steps above in `$LOCAL_SCRATCH` and in a
regular Lustre-based scratch directory. The response times of `$LOCAL_SCRATCH`
are rather stable, but in the scratch directory the execution times will vary
a lot based on the current total load on the Lustre file system.

| Step                    | `$LOCAL_SCRATCH` | `/scratch` |
|-------------------------|-----------------:|-----------:|
|1. Opening tar file      | 2m 8s            | 4m 12s     |
|2. Processing            | 9m 42s           | 21m 58s    |
|3. Creating new tar file | 2m 25s           | 42m 21s    |
|Total                    | 14m 15s          | 1h 8m 31s  |

[More information about temporary local disk areas](../../computing/disk.md#temporary-local-disk-areas).
