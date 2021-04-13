# Velvet

## Description

Velvet is a sequence assembler for very short reads.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available

-   Puhti: 1.2.10
-   [Chipster](https://chipster.csc.fi) graphical user interface


## Usage

In Puhti the Velvet commands are initialized with command:
```text
module load biokit
```
`velveth` (and the corresponding colorspace version `velveth_de`) helps you construct the dataset for the following program,
`velvetg`. Velveth takes in a number of sequence ﬁles, produces a hashtable, then outputs two ﬁles in an output directory, Sequences and Roadmaps, which are necessary to velvetg. The syntax is as follows:

```text
velveth output_directory hash_length  [[-file_format][-read_type] filename]
```
For example
```text
velveth assembly_dir 21 -shortPaired data/reads.fa
```

Velvetg (and the corresponding colorspace version velvetg_de) is the core of Velvet where the de Bruijn graph is built and then manipulated. The syntax of velvetg is

```text
velvetg output_directory -options parameters
```
A velvetg command could look like:
```text
velvetg assebly_dir -cov_cutoff 5 -read_trkg yes -amos_file yes
```
 
When velvet was compiled in puhti, the maximum allowed kmer length was defined. The longer the maximum kmer is the more memory velvet will need (regardless of the kmer length that is actually used). Because of that we provide several versions of velvet, listed in the table below. In Puhti the default the maximum k-mer length, that can be used in the hash table, is 100 bases. However, it is recommended to use the version that has the shortest possible max kmer length. For example for kmer length 40 you should use velveth_maxk50 and velvetg_maxk50.


**Velvet programs available in Puhti**

| Program 	   | max. k-mer length | type |
|------------------|-------------------|------|
| velveth 	   | 100 	       |normal|
| velvetg 	   | 100 	       |normal|
| velveth_maxk75   | 75 	       |normal|
| velvetg_maxk75   | 75 	       |normal|
| velveth_maxk50   | 50 	       |normal|
| velvetg_maxk50   | 50 	       |normal|
| velveth_maxk35   | 35 	       |normal|
| velvetg_maxk35   | 35 	       |normal|
| velveth_de 	   | 100 	       |colorspace|
| velvetg_de 	   | 100 	       |colorspace|
| velveth_de_maxk75| 75 	       |colorspace|
| velvetg_de_maxk75| 75 	       |colorspace|
| velveth_de_maxk50| 50 	       |colorspace|
| velvetg_de_maxk50| 50 	       |colorspace|
| velveth_de_maxk35| 35 	       |colorspace|
| velvetg_de_maxk35| 35 	       |colorspace|

 


In Puhti, the velvet jobs should be executed through the batch job system. Below is sample batch job file for velvet.

```text
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

#
module load biokit
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_THREAD_LIMIT=$SLURM_CPUS_PER_TASK

velveth_maxk50 assembly_folder 45 -shortPaired -fastq temp.fastq
velvetg_maxk50 assembly_folder -ins_length 400
```

In the batch job file above, the job reserves 4 computing cores (--cpus-per-task=4) and 64 GB of memory for four days (-t 4-00:00:00). Velvet can utilize threads based parallel computing. After a set up command `module load biokit` the number of cores to be used in the Velvet run is defined with environment variables: `OMP_NUM_THREADS` and `OMP_THREAD_LIMIT`. In this script these variables are set by using the the environment variable `SLURM_CPUS_PER_TASK`, that contains the value defined with the --cpus-per-task,( which in this example has value: 4).

The batch job can be launched with command

```text
sbatch script_file_name
```

More information about runnig batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).



## Manual

More information about Velvet can be found from:

*    [Velvet home page](https://www.ebi.ac.uk/~zerbino/velvet/)




