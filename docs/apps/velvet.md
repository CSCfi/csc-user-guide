---
tags:
  - Free
---

# Velvet

Velvet is a sequence assembler for very short reads.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available

- Puhti: 1.2.10
- [Chipster](https://chipster.csc.fi) graphical user interface

## Usage

On Puhti, the Velvet commands are initialized with the command:

```bash
module load biokit
```

`velveth` (and the corresponding colorspace version `velveth_de`) helps you construct the dataset for the `velvetg` program. Velveth takes in a number of sequence ﬁles, produces a hashtable, then outputs two files in an output directory, Sequences and Roadmaps, which are necessary to Velvetg. The syntax is as follows:

```bash
velveth output_directory hash_length  [[-file_format][-read_type] filename]
```

For example:

```bash
velveth assembly_dir 21 -shortPaired data/reads.fa
```

`velvetg` (and the corresponding colorspace version `velvetg_de`) is the core of Velvet where the de Bruijn graph is built and then manipulated. The syntax of `velvetg` is:

```bash
velvetg output_directory -options parameters
```

A `velvetg` command could look like:

```bash
velvetg assembly_dir -cov_cutoff 5 -read_trkg yes -amos_file yes
```
 
When Velvet was compiled on Puhti, the maximum allowed k-mer length was defined. The longer the maximum k-mer is, the more memory Velvet will need (regardless of the k-mer length that is actually used). Because of that we provide several versions of Velvet, listed in the table below. On Puhti, the default maximum k-mer length that can be used in the hash table is 100 bases. However, it is recommended to use the version that has the shortest possible max k-mer length. For example, for k-mer length 40, you should use `velveth_maxk50` and `velvetg_maxk50`.

### Velvet programs available on Puhti

| Program 	   | max. k-mer length | type |
|------------------|-------------------|------|
| `velveth` 	   | 100 	       |normal|
| `velvetg` 	   | 100 	       |normal|
| `velveth_maxk75`   | 75 	       |normal|
| `velvetg_maxk75`   | 75 	       |normal|
| `velveth_maxk50`   | 50 	       |normal|
| `velvetg_maxk50`   | 50 	       |normal|
| `velveth_maxk35`   | 35 	       |normal|
| `velvetg_maxk35`   | 35 	       |normal|
| `velveth_de` 	   | 100 	       |colorspace|
| `velvetg_de` 	   | 100 	       |colorspace|
| `velveth_de_maxk75`| 75 	       |colorspace|
| `velvetg_de_maxk75`| 75 	       |colorspace|
| `velveth_de_maxk50`| 50 	       |colorspace|
| `velvetg_de_maxk50`| 50 	       |colorspace|
| `velveth_de_maxk35`| 35 	       |colorspace|
| `velvetg_de_maxk35`| 35 	       |colorspace|

On Puhti, the Velvet jobs should be executed through the batch job system. Below is sample batch job file for Velvet:

```bash
#!/bin/bash
#SBATCH --job-name=velvet
#SBATCH --output=put=output_velvet2.txt
#SBATCH --error=errors_velvet2.txt
#SBATCH --account=<project>
#SBATCH --time=4-00:00:00
#SBATCH --ntasks=1
#SBATCH --partition=longrun
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=64G

module load biokit
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_THREAD_LIMIT=$SLURM_CPUS_PER_TASK

velveth_maxk50 assembly_folder 45 -shortPaired -fastq temp.fastq
velvetg_maxk50 assembly_folder -ins_length 400
```

In the batch job file above, the job reserves 4 computing cores (`--cpus-per-task=4`) and 64 GB of memory for four days (`--time=4-00:00:00`). Velvet can utilize thread-based parallel computing. After the setup command `module load biokit`, the number of cores to be used in the Velvet run is defined with the environment variables `$OMP_NUM_THREADS` and `$OMP_THREAD_LIMIT`. In this script these variables are set by using the environment variable `$SLURM_CPUS_PER_TASK` that contains the value defined with `--cpus-per-task` (which, in this example, has the value 4).

The batch job can be launched with the command:

```bash
sbatch script_file_name
```

More information about running batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).

## More information

More information about Velvet can be found from:

* [Velvet GitHub repository](https://github.com/dzerbino/velvet/)
