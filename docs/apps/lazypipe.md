# Lazypipe

## Description 

Lazypipe is a stand-alone pipeline for identifying viruses in host-associated or environmental samples. The main emphasis is on assembling, taxonomic binning and taxonomic profiling of bacterial/viral sequences.

## Usage

All components of Lazypipe pipeline are available in Puhti. The [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe) provides detailed instruction how to set up your own Lazypipe environment to Puhti, but this is not needed if you use the Lazypipe module that is loaded with commands:

```text
module load biokit
module load biopythontools
module load lazypipe
```
Now lazypipe starts with command:

```text
pipeline.pl
```

Normally you need to use the _pipeline.pl_ command only for testing. For real analysis tasks lazypipe module includes `sbatch-lazypipe` command that you can use instead. 

_sbatch-lazypipe_ is a help tool that automatically generates a batch job file for a Lazypipe run 
and submits it to batch job system of Puhti. The command uses the same command line options 
as the _pipeline.pl_ command. In addition _sbatch-lazypipe_ asks user to define batch job resources
(account, run time, memory, number of cores).

For example to execute the [Example 1]( https://www.helsinki.fi/en/projects/lazypipe/examples) from the
Lazypipe home page, you would first need to download the reads and reference genome to your scratch directory in Puhti
(in real cases you will get these input files from your own sources):

```text
mkdir /scratch/my_project/data
mkdir /scratch/my_project/genomes_host
cd /scratch/my_project/data/
wget https://bitbucket.org/plyusnin/lazypipe/downloads/M15.tar.gz
tar -xzvf M15.tar.gz 
cd /scratch/my_project/genomes_host
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/108/605/GCA_900108605.1_NNQGG.v01/GCA_900108605.1_NNQGG.v01_genomic.fna.gz
```
When you have the data available you can submit the task with commands:

```text
cd /scratch/my_project
module load biokit
module load biopythontools
module load lazypipe
sbatch-lazypipe -1 data/M15/M15_R1.fastq \
--hostgen genomes_host/GCA_900108605.1_NNQGG.v01_genomic.fna.gz \
--res results --label M15  --inlen 300 --pipe 1:7,9:11
```
When the _sbatch-lazypipe_ is executed, it interactively asks information that is
needed to construct a batch job. This includes following items (default values in brackets will be
use if no new value is defined):

   *   accounting project
   *   maximum duration of the job (default 24 hours )
   *   memory reservation ( default 8G)
   *   number of computing cores to use ( default 8 )
   *   email notifications
   
After that your Lazypipe task is submitted to the batch job system for execution.


## More information

*   [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe)


