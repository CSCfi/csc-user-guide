# Trinity

## Description

Trinity is used for _de novo_ reconstruction of transcriptomes from RNA-seq data. Trinity combines three 
independent software modules: **Inchworm**, **Chrysalis**, and **Butterfly**, applied sequentially to process 
large volumes of RNA-seq reads. Trinity partitions the sequence data into many individual de Bruijn graphs, each 
representing the transcriptional complexity at at a given gene or locus, and then processes each graph independently 
to extract full-length splicing isoforms and to tease apart transcripts derived.

The Trinity module at CSC also includes TransDecoder and Trinonate tools (in Taito only) to anlyze the results of a Trinity run.

## Available
Version on CSC's Servers

Puhti: 
Taito: 2.3.2 , 2.4.0, 2.5.1, 2.6.5, 2.6.6


## Using Trinity in Puhti and Taito

In Puhti, Trinity is set up with command:
```
module load biokit
```

In Taito Trinity is set up with commands
```
module load biokit/4.9.3
module load trinity
```
The biokit module sets up a set of commonly used bioinformatics tools. In Taito, Trinity needs a separate set up command too. The reason for this is that Trinity uses older version of SAMtools software (0.1.19) than what is the default in the biokit selection.

Trinity should be used using interactively in Taito-shell or preferably through the batch job system. Below is a sample batch job file for Trinity.
```
#!/bin/bash -l
#SBATCH -J trinity
#SBATCH -o output_%j.txt
#SBATCH -e errors_%j.txt
#SBATCH -t 48:00:00
#SBATCH -n 1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4000
#

module load biokit/4.9.3
module load trinity

Trinity --seqType fq --max_memory 22G --left reads.left.fq --right \
reads.right.fq --SS_lib_type RF --CPU $SLURM_CPUS_PER_TASK \
--output trinity_run_out --grid_exec sbatch_commandlist
```
The command script above reserves 6 computing cores from one node for the job. The maximal run time of the sample job here is 48 hours. About 4 GB of memory is reserved for each core so the total memory reservation is 6 * 4 GB= 24 GB. Note 1: since Trinity version 2.0 the memory is reserved with option --max_memory not -JM.

In the actual Trinity command the number of computing cores to be used (--CPU) is set using environment variable: $SLURM_CPUS_PER_TASK. This variable contains the value set the --cpus-per-task SLURM option.

In Puhti and Taito you can also use distributed computing to speed up the trinity job. When definition:
```
--grid_exec sbatch_commandlist
```
is added to the command, some phases of the analysis tasks are executed as a set of parallel subjobs. 
For large Trinity tasks the settings of the _sbatch_commandlist_ tool are too limited. In these cases 
replace _sbatch_commandlist_ with _sbatch_commandlist_trinity_.
```
--grid_exec sbatch_commandlist_trinity
```
When the batch job file is ready, it can be submitted to the batch queue system with command:
```
sbatch batch_job_file
```
More information about running batch jobs, can be found from the chapter three of the Taito user guide.

Please check the Trinity site to get hints for estimating the required resources,

 
## Using autoTrinotate in Taito

In taito you can analyse the results of your Trinity job with autoTrininotate.
You must first create Trinotate-SQLite database that will be used to store the results of your autoTrinotate.  
This database is created with command:
```
$TRINOTATE_HOME/admin/Build_Trinotate_SQLite_db.pl my_db_name
```
(Note that the command above is different as what is used in 
the Trinotate home page as the command has been slightly modified for Taito)

After these settings you can launch autoTrinotate with command:
```
$TRINOTATE_HOME/auto/autoTrinotate.pl --Trinotate_sqlite my_db_name.sqlite --transcripts transcripts.fasta --gene_to_trans_map gene_to_trans_map --conf $TRINOTATE_HOME/auto/conf.txt --CPU 4
```
Note that autoTrinotate analysis can require much resources so you should execute the command in Taito-shell or as batch job.

AutoTrioritontate produces a SQLite database file that can be further analyzed with command:
```
$TRINOTATE_HOME/Trinotate
```
## Manual

-    [Trinity home page](https://github.com/trinityrnaseq/trinityrnaseq/wiki)



 

 
