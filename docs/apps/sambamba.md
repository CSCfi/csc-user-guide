---
tags:
  - Free
catalog:
  name: Sambamba
  description: Fast parallel processing of SAM and BAM files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Sambamba

Sambamba is a tool for working with SAM and BAM files. It can sort, index, filter,
merge and slice BAM files, and mark duplicate reads, using several cores in parallel.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://github.com/biod/sambamba/blob/master/LICENSE).

## Available

* Roihu-CPU: 1.0.1, via the `bio-apps` module.

## Usage

Sambamba is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Sambamba module:

```bash
module load bio-apps/v202603
module load sambamba/1.0.1
```

Sambamba is run as `sambamba <command>`, where the command is, for example, `view`,
`sort`, `index`, `merge`, `slice`, `markdup`, `flagstat` or `depth`. Run a command
without arguments to see its options.

For example, sort a BAM file by position, mark duplicate reads and count the reads
by their flags:

```bash
sambamba sort -t 8 -m 14G -o sample.sorted.bam sample.bam
sambamba markdup -t 8 sample.sorted.bam sample.markdup.bam
sambamba flagstat -t 8 sample.markdup.bam
```

Always set the number of threads with `-t` to match the cores reserved for your
job. `-m` sets the total memory that `sambamba sort` may use (by default 2 GiB).

Sorting and marking duplicates in large BAM files take a long time, so run them as a
batch job, not on the login node.

`sort` and `markdup` write temporary files to `$TMPDIR`, which on shared compute
nodes is limited in size (see [disk areas](../computing/disk.md)). For large BAM
files, use [disaggregated storage](../computing/disk.md#disaggregated-storage) for the
temporary files instead, as shown after the example batch script.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=sambamba
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

module load bio-apps/v202603
module load sambamba/1.0.1

sambamba sort -t $SLURM_CPUS_PER_TASK -m 14G -o sample.sorted.bam sample.bam
sambamba markdup -t $SLURM_CPUS_PER_TASK sample.sorted.bam sample.markdup.bam
```

`-m 14G` leaves some of the 16 GiB reserved for the job free for Sambamba's own
overhead. Replace `<project>` with your CSC project (for example `project_2001234`).

For large BAM files, reserve disaggregated storage for the temporary files by adding
this line to the `#SBATCH` lines:

```bash
#SBATCH --bb="#BB_LUA SBF storagesize=100G path=/sbf/data"
```

Then add `--tmpdir /sbf/data` to the `sambamba sort` and `sambamba markdup` commands.
Reserve more space than the size of the input BAM, because `sort` writes its
temporary files with only light compression. Sambamba deletes the temporary files
when it finishes, so nothing needs to be copied back.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Sambamba GitHub repository](https://github.com/biod/sambamba)
