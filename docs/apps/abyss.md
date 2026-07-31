---
tags:
  - Free
catalog:
  name: ABySS
  description: De novo, parallel, paired-end sequence assembler for short reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ABySS

ABySS is a de novo sequence assembler for short paired-end reads, able to assemble
genomes ranging from small bacterial genomes up to human-sized genomes when run in its
parallel, MPI-based mode.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail abyss` after loading `bio-apps`.

## License

Free to use and open source under
[GPL v3 License](https://github.com/bcgsc/abyss/blob/master/LICENSE).

## Usage

On Roihu, ABySS is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load abyss
```

The basic syntax runs the `abyss-pe` driver script, which takes its parameters as
`key=value` pairs:

```bash
abyss-pe k=<kmer-size> name=<output-prefix> in='reads1.fq reads2.fq'
```

Heavier assemblies should be run as batch jobs. `abyss-pe` uses `j=<n>` to parallelise
its single-node steps over multiple threads. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=abyss
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load abyss

srun abyss-pe j=$SLURM_CPUS_PER_TASK k=64 name=asm in='reads1.fq reads2.fq'
```

Submit the job with `sbatch abyss_job.sh`. Larger genomes need more time and memory
than this example provides.

## More information

* [ABySS home page](https://www.bcgsc.ca/platform/bioinfo/software/abyss)
* [ABySS on GitHub](https://github.com/bcgsc/abyss)
* [CSC Service Desk](../support/contact.md)
