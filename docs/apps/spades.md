---
tags:
  - Free
catalog:
  name: SPAdes
  description: Genome assembly
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SPAdes

SPAdes is a short read assembler for small genomes. SPAdes works with Illumina or IonTorrent reads and is capable of providing hybrid assemblies using PacBio, Oxford Nanopore and Sanger reads.

SPAdes (`spades.py`) includes several separate modules:

* BayesHammer – read error correction tool for Illumina reads, which works well on both single-cell and standard datasets.
* IonHammer – read error correction tool for IonTorrent data, which also works on both types of data.
* SPAdes – iterative short-read genome assembly module; values of K are selected automatically based on the read length and dataset type.
* MismatchCorrector – a tool which improves mismatch and short indel rates in resulting contigs and scaffolds; this module uses the BWA tool [Li H. and Durbin R., 2009]; MismatchCorrector is turned off by default, but we recommend turning it on.

We recommend running SPAdes with BayesHammer/IonHammer to obtain high-quality assemblies. However, if you use your own read correction tool, it is possible to turn error correction module off. It is also possible to use only the read error correction stage if you wish to use another assembler.

In addition to the general purpose SPAdes there are specific SPAdes parameter sets for:

* Coronaspades (`coronaspades.py`)
* Metaviralspades (`metaviralspades.py`)
* Rnaviralspades (`rnaviralspades.py`)
* Metagenomics (`metaspades.py`)
* Plasmid assembly (`plasmidspades.py`)
* RNA-Seq assembly (`rnaspades.py`)

See the [SPAdes documentation](https://ablab.github.io/spades/installation.html) for more details.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available

* Roihu: 4.2.0, via the `bio-apps` module.

## Usage

SPAdes is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SPAdes module:

```bash
module load bio-apps/v202603
module load spades/4.2.0
```

For usage help, use command:

```bash
spades.py -h
```

Assembly tasks can be very resource demanding and, therefore, you should never run real SPAdes jobs on the login nodes.
For any real analysis task, we recommend running SPAdes as a batch job.

Sample SPAdes batch job file:

```bash
#!/bin/bash
#SBATCH --job-name=SPAdes
#SBATCH --account=<project>
#SBATCH --output=spades_out_%j
#SBATCH --error=spades_err_%j
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

module load bio-apps/v202603
module load spades/4.2.0

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK 
srun spades.py --pe1-1 reads_R1.fastq.gz --pe1-2 reads_R2.fastq.gz -t $SLURM_CPUS_PER_TASK -o SpadesResult
```

In the example above `<project>` should be replaced with your project name. You can use `csc-projects` to check your CSC projects.
Maximum running time is 
set to 12 hours (`--time=12:00:00`). As SPAdes uses thread-based parallelization, the process is considered as one job that should be executed within one node (`--ntasks=1`, `--nodes=1`). The job reserves eight cores `--cpus-per-task=8` that can use in total up to 32 GB of memory (`--mem=32G`). Note that the number of cores to be used needs to be defined with both `$OMP_NUM_THREADS` environment variable and in the actual `spades.py` command (option `-t`). In this case, we use `$SLURM_CPUS_PER_TASK` variable that contains the `--cpus-per-task`
value. We could as well use `export OMP_NUM_THREADS=8` and `-t 8`, but then we have to remember to change the values if the number of the reserved CPUs is changed.

The job is submitted to the batch job system with `sbatch` command. For example, if the batch job
file is named `spades_job.sh`, then the submission command is: 

```bash
sbatch spades_job.sh 
```

More information about running batch jobs can be found from [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

*	[SPAdes website](https://ablab.github.io/spades/)
*	[SPAdes GitHub repository](https://github.com/ablab/spades)
