---
tags:
  - Free
catalog:
  name: HMMER
  description: Toolkit to create and use sequence profile hidden Markov models
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HMMER

Hidden Markov Models (HMM) are mathematical tools that can be used to describe and analyze related or similar sequence areas. 
HMM-models can be derived from multiple sequence alignments so that they contain position specific information about the 
probabilities of having certain nucleotides or amino acids in each position of an alignment.

The HMMER package contains tools to create and modify sequence alignment based HMM-models, use them to do database searches and extend sequence alignments.

Database searches with HMM profiles can require very long computing times in normal computers.

[TOC]

## License

Free to use and open source under the [BSD 3-Clause License](https://github.com/EddyRivasLab/hmmer/blob/master/LICENSE).

## Available

* Roihu: 3.4, via the `bio-apps` module.

## Usage

HMMER is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the HMMER module:

```bash
module load bio-apps/v202603
module load hmmer/3.4
```

Check the available versions with:

```bash
module spider hmmer
```

After this, the command line options of each `hmmer` command can be checked with the option `-h`. For example:

```bash
hmmsearch -h
```

### Pfam database

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases (such as Pfam-A) at a central
    location on Roihu. This is still being set up. Until it is available, download
    and use your own copy of the database.

You can search a protein sequence against a Pfam-A HMM database, or against your own HMM databases.
After downloading a Pfam-A HMM file, prepare it for searching with `hmmpress`:

```bash
hmmpress Pfam-A.hmm
```

With native HMMER, you can speed up the `hmmscan` and `hmmsearch` commands by using several
processors. The number of processors, e.g. 4, to be used is indicated with the option `--cpu 4`,
but the number is better replaced with an environment variable which already has it, *i.e.* 
`$SLURM_CPUS_PER_TASK`, so it's always in sync with the batch script request.

You can run the search in an [interactive session](../computing/running/interactive-usage.md). On the Roihu `interactive` partition each reserved core provides 1.875 GB of memory (up to 32 cores / 60 GB / 36 hours), so request enough cores for the memory you need, for example:

```bash
sinteractive --account <project> --cores 4
module load bio-apps/v202603
module load hmmer/3.4
hmmscan --cpu $SLURM_CPUS_PER_TASK Pfam-A.hmm protein.fasta > result.txt
```

HMMER jobs should be run as interactive batch jobs or normal batch jobs. Here is an example batch job script using 4 processor cores:

```bash
#!/bin/bash 
#SBATCH --job-name=hmmer_job
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2000M

module load bio-apps/v202603
module load hmmer/3.4

hmmscan --cpu $SLURM_CPUS_PER_TASK Pfam-A.hmm protein.fasta > result.txt
```

Replace `<project>` with your CSC project (for example `project_2001234`).

The job is submitted with the command (where *batch_job_file.sh* is the name of your batch job file):

```bash
sbatch batch_job_file.sh
```

For more information on running batch jobs, see [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [HMMER user guide](http://eddylab.org/software/hmmer/Userguide.pdf)
