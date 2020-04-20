# Kraken

## Description

Kraken is a sequence classifier that assigns taxonomic labels to DNA sequences. 
Kraken examines the k-mers within a query sequence and uses the information within 
those k-mers to query a database. That database maps k-mers to the lowest common ancestor 
of all genomes known to contain a given k-mer.

## Version

Kraken 2.0.8 is available in Puhti

## Usage

Kraken in included in _biokit_ module. To set it up, run command:
```text
module load biokit
```
Now you kraken starts woth commmad `kraken2`. For example:
```text
kraken --help
```
There are serveral Kraken reference databases available in Puhti. By default Kraken uses the
_standard_ database  that is based on taxonomic information and complete genomes in RefSeq 
for the bacterial, archaeal, and viral domains, along with the human genome and a 
collection of known vectors (UniVec_Core).

Other available databases are:

|name  | Mem. request | description    | 
|------|--------------|-----------------|
|standard| 40 GB | NCBI taxonomic information, as well as the complete genomes in RefSeq for the bacterial, archaeal, and viral domains, along with the human genome and a collection of known vectors (UniVec_Core).|
|krak_microb| 64 GB | RefSeq backterial, archea, viral, fungi and protozoa |
|16S_Greengenes_k2db|  1 GB | Greengenes 16S data |
|16S_RDP_k2db | 1 GB | RDP 16S data |
|16S_SILVA132_k2db| 1 GB |Silva 132 16S data |
|16S_SILVA138_k2db| 1 GB |Silva 138 16S data |
| minikraken_8GB_20200312| 1 GB  |            |

Kraken is very memory intensive program. For example jobs with the standard Karken database require 40 GB of memory 
and thus kraken should in practice always be executed as a a batch job. Below is a sample Karaken job using 4 croes
40 GB of memopry and 6 hours or runtime:

```test
#!/bin/bash -l
#SBATCH --job-name=kraken2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=06:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --account=project_123456
#SBATCH --mem=40000
#

module load biokit
kraken2 -db standard --threads $SLURM_CPUS_PER_TASK input.fasta --output results.txt
```
You can submit the batch job file to the batch job system with command:

```
sbatch batch_job_file.bash
```
See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.


## More information

*   [Kraken home page](https://ccb.jhu.edu/software/kraken2/)
