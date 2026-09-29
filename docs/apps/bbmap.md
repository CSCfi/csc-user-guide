---
tags:
  - Free
catalog:
  name: BBMap
  description: BBTools short-read aligner and sequence-processing suite
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BBMap

BBMap is part of the BBTools suite, a collection of fast tools for DNA and RNA-seq
data. In addition to the `bbmap.sh` short-read aligner, the suite includes tools such
as `bbduk.sh` (adapter/quality trimming and filtering), `reformat.sh` (format
conversion), `bbmerge.sh` (read merging) and many others.

[TOC]

## License

Free to use and open source under the [BSD 3-Clause (LBNL) license](https://bitbucket.org/berkeleylab/jgi-bbtools/src/master/license.txt).

## Available

* Roihu: 39.59, via the `bio-apps` module.

## Usage

BBMap is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BBMap module:

```bash
module load bio-apps/v202603
module load bbmap/39.59
```

The BBTools programs are individual shell scripts, for example:

```bash
bbmap.sh in=reads.fq ref=genome.fa out=mapped.sam
bbduk.sh in=reads.fq out=clean.fq ref=adapters.fa ktrim=r k=23 mink=11 hdist=1
```

The module sets the `BBMAP_RESOURCES` environment variable, which points to the
bundled reference files such as adapter and contaminant sequences (for example
`$BBMAP_RESOURCES/adapters.fa`).

The BBTools scripts try to detect the available memory automatically, which on a
shared cluster node can request more than you reserved. On Roihu you should set the
Java heap size explicitly with `-Xmx` to match your Slurm memory reservation, and set
the number of threads with `threads=`.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bbduk
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load bbmap/39.59

bbduk.sh -Xmx15g threads=$SLURM_CPUS_PER_TASK \
    in=reads.fq out=clean.fq \
    ref=$BBMAP_RESOURCES/adapters.fa ktrim=r k=23 mink=11 hdist=1
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BBTools home page](https://bbmap.org/)
* [BBTools user guide](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/)
