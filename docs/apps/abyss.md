---
tags:
  - Free
catalog:
  name: ABySS
  description: De novo, parallel, paired-end sequence assembler
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ABySS

ABySS (Assembly By Short Sequences) is a de novo sequence assembler designed for short paired-end reads and genomes of all sizes.
It supports memory-efficient Bloom-filter assembly and a legacy MPI mode.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/bcgsc/abyss/blob/master/LICENSE).

## Available

* Roihu: 2.3.10, via the `bio-apps` module.

## Usage

ABySS is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the ABySS module:

```bash
module load bio-apps/v202603
module load abyss/2.3.10
```

Assemblies are run with the `abyss-pe` driver. A minimal paired-end assembly uses a
k-mer size (`k`), an output name (`name`) and the input reads (`in`):

```bash
abyss-pe k=64 B=2G name=assembly in='reads1.fq.gz reads2.fq.gz'
```

For larger assemblies, ABySS recommends Bloom-filter mode, enabled by setting the B memory budget. The appropriate value of B depends primarily on genome size. MPI mode is still available but is considered legacy upstream.

### Example batch script

Assembly jobs are resource demanding and should be run as batch jobs. Below is a sample multithreaded batch job script using Bloom-filter mode:

```bash
#!/bin/bash
#SBATCH --job-name=abyss
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load abyss/2.3.10

abyss-pe k=64 B=2G j=$SLURM_CPUS_PER_TASK \
    name=assembly \
    in='reads1.fq.gz reads2.fq.gz'
```

Replace `<project>` with your CSC project (for example `project_2001234`).

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ABySS home page](https://www.bcgsc.ca/resources/software/abyss)
* [ABySS GitHub repository](https://github.com/bcgsc/abyss)
