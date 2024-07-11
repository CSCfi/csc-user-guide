---
tags:
  - Free
---

# TopHat

TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns RNA-Seq reads to mammalian-sized genomes using the ultra high-throughput short read aligner Bowtie, and then analyzes the mapping results to identify splice junctions between exons.

[TOC]

## License

Free to use and open source under [Boost Software License 1.0](https://github.com/DaehwanKimLab/tophat/blob/master/LICENSE).

## Available

-   Puhti: 2.1.1
-   [Chipster](https://chipster.csc.fi) graphical user interface

## Usage

On Puhti, TopHat is initialized with the command:

```bash
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including Bowtie2, TopHat2 and Cufflinks.

Tophat jobs should be run as batch jobs. Below is a sample batch job file for running a TopHat job on Puhti:

```bash
!/bin/bash
#SBATCH --job-name=tophat
#SBATCH --output=out_%j.txt
#SBATCH --error=err_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --partition=small
#SBATCH --account=project_1234567

module load biokit
tophat -p $SLURM_CPUS_PER_TASK -o tophat_results Homo.sapiens_bwt2_index reads1.fq reads2.fq 
```

In the batch job example above, one task (`--ntasks=1`) is executed. The job uses 4 cores (`--cpus-per-task=4`) with 16 GB of memory (`--mem=16G`). The maximum duration of the job is 24 hours (`--time=24:00:00`). Change `--account` to match your own project name.

Note that we also need to tell TopHat to use the number of cores we reserved. In Tophat, this is done with the `-p` command-line argument. We can use system variable `$SLURM_CPUS_PER_TASK` to automatically match the reservation made with `--cpus-per-task`. This way we don't need to change the command-line if we change the reservation.

See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [TopHat Homepage](http://ccb.jhu.edu/software/tophat/index.shtml)
* [TopHat Manual](http://ccb.jhu.edu/software/tophat/manual.shtml)
