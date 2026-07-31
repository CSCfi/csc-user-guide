---
tags:
  - Free
catalog:
  name: ANGSD
  description: Analysis of next-generation sequencing data under genotype uncertainty
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ANGSD

ANGSD analyses next-generation sequencing data, from mapped reads to imputed genotype
probabilities, taking genotype uncertainty into account instead of relying on called
genotypes. This makes it especially useful for low- and medium-depth sequencing data.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail angsd` after loading `bio-apps`.

## License

Free to use and open source, released under a mix of
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html) and
[MIT](https://opensource.org/license/mit) licenses across the codebase.

## Usage

On Roihu, ANGSD is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load angsd
```

The basic syntax is:

```bash
angsd -bam bamlist.txt -out result -GL 1 -doMajorMinor 1 -doMaf 1
```

ANGSD parallelises over threads with `-nThreads`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=angsd
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load angsd

srun angsd -bam bamlist.txt -out result -GL 1 -doMajorMinor 1 -doMaf 1 \
    -nThreads $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch angsd_job.sh`.

## More information

* [ANGSD home page](https://github.com/ANGSD/angsd)
* [ANGSD documentation wiki](https://www.popgen.dk/angsd/index.php/ANGSD)
* [CSC Service Desk](../support/contact.md)
