# HMMER

## Description

Hidden Markov Models (HMM) are mathematical tools that can be used to describe and analyze related or similar sequence areas. 
HMM-models can be derived from multiple sequence alignments so that they contain position specific information about the 
probabilities of having certain nucleotides or amino acids in each position of an alignment.

The HMMER package contains tools to create and modify sequence alignmnet based HMM-models, use them to do database searches and extend sequence alignments.

Database searches with HMM profiles can require very long computing times in normal computers.

## Available
Version on CSC's Servers

*   Puhti: HMMER 3.3.2

## Usage

To use HMMER in Puhti, load the biokit module:
```text
module load biokit
```
After this the command line options of each hmmer command can be checked with option `-h`. For example:
```text
hmmsearch -h
```

### Pfam database

In Puhti you can use Pfam_A database with HMMER commands. You can also create your own HMM databases.
For example, comparing a protein sequence against a Pfam-A HMM-database could be performed with following commands.

First, open an interactive batch job session and load biokit:

```text
sinteractive -m 4G -c 4
module load biokit
```
With native HMMER, you can speed up the `hmmpfam` and `hmmserach` commands by using several processors. The number of processors to be used is indicated with option `--cpu number`.
```text
hmmscan --cpu 4 $PFAMDB/pfam_a.hmm protein.fasta > result.txt
```
In Puhti, HMMER jobs should be run as interactive batch jobs or normal batch jobs. Here is an example batch job file using 4 processor cores:

```text
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
#

module load biokit
hmmscan --cpu 4 $PFAMDB/pfam_a.hmm protein.fasta > result.txt
```

The job is submitted with command (where *batch_job_file* is the name of your batch job file):

```text
sbatch batch_job_file
```
For more information on running batch jobs see the [Computing User Guide](../computing/running/getting-started.md).

## Help

* [HMMER user guide](http://eddylab.org/software/hmmer/Userguide.pdf)
