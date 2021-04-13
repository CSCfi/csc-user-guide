# Spades

## Description

SPAdes is a short read assebler for small genomes. SPAdes works with Illumina or IonTorrent reads and is capable of providing hybrid assemblies using PacBio, Oxford Nanopore and Sanger reads.

SPAdes (`spares.py`) includes several separate modules:

*    BayesHammer – read error correction tool for Illumina reads, which works well on both single-cell and standard data sets.
*    IonHammer – read error correction tool for IonTorrent data, which also works on both types of data.
*    SPAdes – iterative short-read genome assembly module; values of K are selected automatically based on the read length and data set type.
*    MismatchCorrector – a tool which improves mismatch and short indel rates in resulting contigs and scaffolds; this module uses the BWA tool [Li H. and Durbin R., 2009]; MismatchCorrector is turned off by default, but we recommend to turn it on (see SPAdes options section).

We recommend to run SPAdes with BayesHammer/IonHammer to obtain high-quality assemblies. However, if you use your own read correction tool, it is possible to turn error correction module off. It is also possible to use only the read error correction stage, if you wish to use another assembler. See the SPAdes options section. 

In addition to the general purpose spades there spcific Spadesw parameter sets for:
*   Coronaspades (coronaspades.py)
*   Metaviralspades (metaviralspades.py)
*   Rnaviralspades (rnaviralspades.py)
*   Metagenomics ([metaspades.py](https://genome.cshlp.org/content/27/5/824.short))
*   Plasmid assembly ([plasmidspades.py](https://www.biorxiv.org/content/10.1101/048942v3))
*   RNA-Seq assembly ([rnaspades.py](http://cab.spbu.ru/files/release3.13.1/rnaspades_manual.html))
*   Assemblly with Illumina TruSeq data ([truspades.py](http://cab.spbu.ru/files/release3.13.1/truspades_manual.html)) 

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available

Version on CSC's Servers

-   Puhti: 3.15.0

## Usage

In Puhti, SPAdes is activated by loading the _biokit_ environment.

```text
module load biokit
```
For usage help use command:
```text
spades.py -h
```
Assembly tasks can be very resource demanding. Because of that you should not run real SPAdes jobs in the login nodes of Puhti.
For any real analysis task we recommend running SPAdes as a batch job.


Sample SPAdes batch job file:
```text
#!/bin/bash
#SBATCH --job-name=SPAdes
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output==spades_out
#SBATCH --error=sprdes_err
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=small


module load biokit
srun spades.py --pe1-1 reads_R1.fastq.gz --pe1-2 reads_R2.fastq.gz -t $SLURM_CPUS_PER_TASK -o SpadesResult

```
In the example above _<project>_ could be replaced with your project name. You can use `csc-workspaces` to check your Puhti projects.
Maximum running time is 
set to 12 hours (`--time=12:00:00`). As SPAdes uses threads based parallelization, the process is considered as one job that should be executed within one node (`--ntasks=1`, `--nodes=1`). The job reserves eight cores `--cpus-per-task=8` that can use in total up to 32 GB of memory  (`--mem=32G`). Note that the number of cores to be used needs to be defined in actual _spades.py_ command
too. That is done with _spades.py_ option `-t`. In this case we use $SLURM_CPUS_PER_TASK variable that contains the _cpus-pre-task_ 
value. We could as well use `-t 8` but then we have to remember to change the value if number of the reserved CPU:s is changed.


The job is submitted to the to the batch job system with `sbatch` command. For example, if the batch job
file is named as _spades_job.sh_ then the submission command is: 
```text
sbatch spades_job.sh 
```
More information about running batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).




## Manual

*   [SPAdes home page](http://cab.spbu.ru/software/spades/)





