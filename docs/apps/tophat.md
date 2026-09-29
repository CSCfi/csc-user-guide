---
tags:
  - Free
catalog:
  name: TopHat
  description: Splice junction mapper for RNA-Seq reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# TopHat

TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns RNA-Seq reads to mammalian-sized genomes using the ultra high-throughput short read aligner Bowtie, and then analyzes the mapping results to identify splice junctions between exons.

[TOC]

## License

Free to use and open source under [Boost Software License 1.0](https://github.com/DaehwanKimLab/tophat/blob/master/LICENSE).

## Available

* Roihu: 2.1.2, via the `bio-apps` module.

## Usage

TopHat is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the TopHat module:

```bash
module load bio-apps/v202603
module load tophat/2.1.2
```

Tophat jobs should be run as batch jobs. Below is a sample batch job file for running a TopHat job on Roihu:

```bash
#!/bin/bash
#SBATCH --job-name=tophat
#SBATCH --account=<project>
#SBATCH --output=out_%j.txt
#SBATCH --error=err_%j.txt
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

module load bio-apps/v202603
module load tophat/2.1.2

tophat -p $SLURM_CPUS_PER_TASK -o tophat_results Homo.sapiens_bwt2_index reads1.fq reads2.fq 
```

In the batch job example above, one task (`--ntasks=1`) is executed. The job uses 4 cores (`--cpus-per-task=4`) with 16 GB of memory (`--mem=16G`). The maximum duration of the job is 24 hours (`--time=24:00:00`). Change `--account` to match your own project name.

Note that we also need to tell TopHat to use the number of cores we reserved. In Tophat, this is done with the `-p` command-line argument. We can use system variable `$SLURM_CPUS_PER_TASK` to automatically match the reservation made with `--cpus-per-task`. This way we don't need to change the command-line if we change the reservation.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [TopHat Homepage](http://ccb.jhu.edu/software/tophat/index.shtml)
* [TopHat Manual](http://ccb.jhu.edu/software/tophat/manual.shtml)
