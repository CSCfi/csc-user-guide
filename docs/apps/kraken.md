---
tags:
  - Free
---

# Kraken

Kraken is a sequence classifier that assigns taxonomic labels to DNA sequences. 
Kraken examines the k-mers within a query sequence and uses the information within 
those k-mers to query a database. That database maps k-mers to the lowest common ancestor 
of all genomes known to contain a given k-mer.

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/DerrickWood/kraken2/master/LICENSE).

## Available

- Puhti: 2.1.2 

## Usage

Kraken in included in the `biokit` module. To set it up, run the command:

```bash
module load biokit
```

This loads the Kraken2 package which can be started with the command `kraken2`. For example:

```bash
kraken2 --help
```

There are several Kraken2 reference databases available on Puhti. By default, Kraken2 uses the
`standard` database that is based on taxonomic information and complete genomes in RefSeq 
for the bacterial, archaeal, and viral domains, along with the human genome and a 
collection of known vectors (UniVec_Core).

Available databases in Puhti are:

|Name  | Mem. request | Description    | 
|------|--------------|-----------------|
|standard| 40 GB | NCBI taxonomic information, as well as the complete genomes in RefSeq for the bacterial, archaeal, and viral domains, along with the human genome and a collection of known vectors (UniVec_Core).|
|krak_microb| 44 GB | RefSeq bacterial, archea, viral, fungi and protozoa |
|16S_Greengenes_k2db|  1 GB | Greengenes 16S data |
|16S_RDP_k2db | 1 GB | RDP 16S data |
|16S_SILVA132_k2db| 1 GB |Silva 132 16S data |
|16S_SILVA138_k2db| 1 GB |Silva 138 16S data |
|minikraken_8GB_20200312| 1 GB  |            |

Using Kraken2 with a large reference database will require plenty on memory. For example, jobs with the standard Kraken2 database require 40 GB of memory. Thus, Kraken should in practice always be executed as a batch job. Below is a sample Kraken job using 4 cores 40 GB of memory and 6 hours of runtime:

```bash
#!/bin/bash -l
#SBATCH --job-name=kraken2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=06:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=4
#SBATCH --account=project_123456
#SBATCH --mem=40000

module load biokit
kraken2 -db standard --threads $SLURM_CPUS_PER_TASK input.fasta --output results.txt
```

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.bash
```

See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## More information

* [Kraken home page](https://ccb.jhu.edu/software/kraken2/)
