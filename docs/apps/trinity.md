# Trinity

## Description

Trinity is used for _de novo_ reconstruction of transcriptomes from RNA-seq data. Trinity combines three 
independent software modules: **Inchworm**, **Chrysalis**, and **Butterfly**, applied sequentially to process 
large volumes of RNA-seq reads. Trinity partitions the sequence data into many individual de Bruijn graphs, each 
representing the transcriptional complexity at at a given gene or locus, and then processes each graph independently 
to extract full-length splicing isoforms and to tease apart transcripts derived.

The Trinity module at CSC also includes TransDecoder and Trinotate tools to anlyze the results of a Trinity run.

[TOC]

## License

Free to use and open source under [Broad Institute License]https://github.com/genome-vendor/trinity/blob/master/LICENSE).

## Available
Version on CSC's Servers

Puhti: 2.13.2, 2.11.0, 2.8.5


## Using Trinity 


In Puhti, Trinity is set up with command:
```text
module load biokit
```
The biokit module sets up a set of commonly used bioinformatics tools including
trinity 2.8.5. If want to use version 2.13.2, run command:

```text
module load trinty/2.13.2
```

Trinity should be used used [interactively in a compute node](../computing/running/interactive-usage.md) 
or preferably through the batch job system. Below is an example batch job file for Trinity.

```text
#!/bin/bash 
#SBATCH --job-name=trinity
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=48:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=6
#SBATCH --mem=24000
#SBATCH --account=project_1234567
#
#

module load trinity/2.13.2

Trinity --seqType fq --max_memory 22G --left reads.left.fq --right \
reads.right.fq --SS_lib_type RF --CPU $SLURM_CPUS_PER_TASK \
--output trinity_run_out --grid_exec sbatch_commandlist
```
The command script above reserves 6 computing cores from one node for the job. The maximal run time of the sample job here is 48 hours. 
About 4 GB of memory is reserved for each core so the total memory reservation is `6 * 4 GB = 24 GB`. In Puhti, you must use batch job option
`--account=` to define the project to be used. You should replace _project_1234567_ used in the example,  with your own project. You can check your 
projects with command: `csc-workspaces`.

In the actual Trinity command the number, of computing cores to be used (--CPU) is set using environment variable: `$SLURM_CPUS_PER_TASK`. 
This variable contains the value set the `--cpus-per-task` SLURM option.

In Puhti you can also use distributed computing to speed up the trinity job. When definition:
```text
--grid_exec sbatch_commandlist
```
is added to the command, some phases of the analysis tasks are executed as a set of parallel subjobs. 
For large Trinity tasks the settings of the _sbatch_commandlist_ tool are too limited. In these cases 
replace _sbatch_commandlist_ with _sbatch_commandlist_trinity_.
```text
--grid_exec sbatch_commandlist_trinity
```
When Trinity is executed with _--grid_exec_ option in generates large amount of temporary files and it 
is very likely, that you will exceed the default limit of 100 000 files. Thus it is advisable to apply for 
a larger file number quota for Puhti scratch before submitting large Trinity jobs. You can send the request
to servicedesk@csc.fi.


When the batch job file is ready, it can be submitted to the batch queue system with command:
```text
sbatch batch_job_file
```
Look here for [more information about running batch jobs](../computing/running/getting-started.md).

Please check the Trinity site to get hints for estimating the required resources,

## Using autoTrinotate

You can analyse the results of your Trinity job with `autoTrininotate`. You need two files, resulting from a successful Trinity assembly.
    1. Fasta formatted nucleotide sequence file containing the final contigs created by Trinity (Trinity.fasta)
    2. gene-to-trans map for the input fasta file (Trinity.fasta.gene_to_trans_map)

You can launch autoTrinotate with command:

```bash
$TRINOTATE_HOME/auto/autoTrinotate.pl --Trinotate_sqlite $TRINOTATE_HOME/databases/Trinotate.sqlite --transcripts Trinity.fasta --gene_to_trans_map  Trinity.fasta.gene_to_trans_map --conf $TRINOTATE_HOME/auto/conf.txt --CPU  $SLURM_CPUS_PER_TASK
```
!!! Note
    autoTrinotate analysis can require much resources so you should execute the command in
    with [sinteractive](../computing/running/interactive-usage.md) or as a batch job.

AutoTrinotate produces an SQLite database file that can be further analyzed with command:

```bash
$TRINOTATE_HOME/Trinotate
```
## Manual

-    [Trinity home page](https://github.com/trinityrnaseq/trinityrnaseq/wiki)



 

 
