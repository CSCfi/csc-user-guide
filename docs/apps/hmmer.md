# HMMER

## Description

Hidden Markov Models (HMM) are mathematical tools that can be used to describe and analyze related or similar sequence areas. 
HMM-models can be derived from multiple sequence alignments so that they contain position specific information about the 
probabilities of having certain nucleotides or amino acids in each position of an alignment.

The HMMER package contains tools to create and modify sequence alignmnet based HMM-models, use them to do database searches and extend sequence alignments.

Database searches with HMM profiles can require very long computing times in normal computers.


## HMMER programs
	
| HMMER program | 	Description  |
|---------------|----------------|
|hmmalign 	| Align sequences with an HMM|
|hmmbuild 	| Build HMM  |
|hmmconvert |Convert between HMM formats |
|hmmemit 	| Extract HMM sequences |
|hmmfetch |	Extract HMM from a database |
|hmmpress |	Index an HMM database |
|hmmscan |	Align single sequence with a HMM database |
|hmmsearch | Search sequence database with an HMM |
|hmmsim | Collect profile HMM score distributions on random sequences |
|hmmstat |Display summary statistics for a profile file |
|jackhmmer |	Iteratively search a protein sequence against a protein database |
| phmmer |Search a protein sequence against a protein database |

 
## Available
Version on CSC's Servers

*   Puhti: HMMER 3.2.1

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

In Puhti you can use Pfam_A and Pfam_B databases with HMMER commands. For example comparing protein sequence against a Pfam-A HMM-database can be performed with command:

```text
hmmscan $HMMERDB/Pfam-A.hmm sekvenssi.fasta
```
With native HMMER, you can speed up the hmmpfam and hmmserach commands by using several processors. The number of processors to be used is indicated with option --cpu number. We recommend that you do not use more than four processors.
```text
hmmscan --cpu 4 $HMMERDB/Pfam-A.hmm protein.fasta > result.txt
```
In Puhti HMMER jobs should be run as batch jobs. Here is an example batch job file usinf 4 processor cores:

```text
#!/bin/bash 
#SBATCH --job-name=hmmer_jon
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
hmmscan --cpu 4 $HMMERDB/Pfam-A.hmm protein.fasta > result.txt
```

The job is submitted with command (where batch_job_file is the name of you batch job file):

```text
sbatch batch_job_file
```
For more information on running batch jobs see the [Computing User Guide](../computing/running/getting-started/).
