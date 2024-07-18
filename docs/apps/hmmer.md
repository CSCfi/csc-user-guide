---
tags:
  - Free
---

# HMMER

Hidden Markov Models (HMM) are mathematical tools that can be used to describe and analyze related or similar sequence areas. 
HMM-models can be derived from multiple sequence alignments so that they contain position specific information about the 
probabilities of having certain nucleotides or amino acids in each position of an alignment.

The HMMER package contains tools to create and modify sequence alignment based HMM-models, use them to do database searches and extend sequence alignments.

Database searches with HMM profiles can require very long computing times in normal computers.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Puhti: 3.2.1, 3.3.2, 3.4

## Usage

To use default version of HMMER on Puhti, load the biokit module:

```bash
module load biokit
```

If you want to use some other version, load the particular version of the HMMER module. For example:

```bash
module load hmmer/3.2.1
```

After this, the command line options of each `hmmer` command can be checked with option `-h`. For example:

```bash
hmmsearch -h
```

### Pfam database

On Puhti, you can use Pfam-A database with HMMER commands. You can also create your own HMM databases.
For example, comparing a protein sequence against a Pfam-A HMM-database could be performed with the following commands.

First, open an interactive batch job session and load biokit:

```bash
sinteractive -m 4G -c 4
module load biokit
```

With native HMMER, you can speed up the `hmmpfam` and `hmmserach` commands by using several
processors. The number of processors, e.g. 4, to be used is indicated with option `--cpu 4`,
but the number is better replaced with an environment variable which already has it, *i.e.* 
`$SLURM_CPUS_PER_TASK`, so it's always in sync with the batch script request:

```bash
hmmscan --cpu $SLURM_CPUS_PER_TASK $PFAMDB/pfam_a.hmm protein.fasta > result.txt
```

In Puhti, HMMER jobs should be run as interactive batch jobs or normal batch jobs. Here is an example batch job file using 4 processor cores:

```bash
#!/bin/bash 
#SBATCH --job-name=hmmer_job
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=4
#SBATCH --account=project_123456
#SBATCH --mem=8000

module load biokit
hmmscan --cpu $SLURM_CPUS_PER_TASK $PFAMDB/pfam_a.hmm protein.fasta > result.txt
```

The job is submitted with command (where *batch_job_file* is the name of your batch job file):

```bash
sbatch batch_job_file
```

For more information on running batch jobs, see the [Computing User Guide](../computing/running/getting-started.md).

## More information

* [HMMER user guide](http://eddylab.org/software/hmmer/Userguide.pdf)
