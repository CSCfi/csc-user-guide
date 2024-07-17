---
tags:
  - Free
---

# Trinity

Trinity is used for _de novo_ reconstruction of transcriptomes from RNA-seq data. Trinity combines three 
independent software modules: **Inchworm**, **Chrysalis**, and **Butterfly**, applied sequentially to process 
large volumes of RNA-seq reads. Trinity partitions the sequence data into many individual de Bruijn graphs, each 
representing the transcriptional complexity at a given gene or locus, and then processes each graph independently 
to extract full-length splicing isoforms and to tease apart transcripts derived.

The Trinity module at CSC also includes TransDecoder and Trinotate tools to analyze the results of a Trinity run.

[TOC]

## License

Free to use and open source under [Broad Institute License](https://github.com/genome-vendor/trinity/blob/master/LICENSE).

## Available

Puhti: 2.8.5, 2.11.0, 2.13.2, 2.14.0, 2.15.1

## Usage

### Using Trinity

On Puhti, Trinity is set up with the command:

```bash
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools including
Trinity 2.8.5. If you want to use a newer version, e.g. 2.13.2, run the command:

```bash
module load trinty/2.13.2
```

Trinity should be used [interactively in a compute node](../computing/running/interactive-usage.md) 
or preferably through the batch job system. Below is an example batch job file for Trinity.

```bash
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

module load trinity/2.13.2

Trinity --seqType fq --max_memory 22G --left reads.left.fq --right \
reads.right.fq --SS_lib_type RF --CPU $SLURM_CPUS_PER_TASK \
--output trinity_run_out --grid_exec sbatch_commandlist
```

The batch script above reserves 6 computing cores from one node for the job. The maximal run time of the sample job here is 48 hours. 
About 4 GB of memory is reserved for each core so the total memory reservation is `6 * 4 GB = 24 GB`. On Puhti, you must use batch job option
`--account=` to define the project to be used. You should replace `project_1234567` used in the example with your own project. You can check your 
projects with command: `csc-projects`.

In the actual `Trinity` command the number of computing cores to be used (`--CPU`) is set using the environment variable `$SLURM_CPUS_PER_TASK`. 
This variable contains the value set by the `--cpus-per-task` Slurm option.

On Puhti, you can also use distributed computing to speed up the Trinity job. When the definition:

```bash
--grid_exec sbatch_commandlist
```

is added to the command, some phases of the analysis tasks are executed as a set of parallel sub-jobs. 
For large Trinity tasks the settings of the `sbatch_commandlist` tool are too limited. In these cases 
replace `sbatch_commandlist` with `sbatch_commandlist_trinity`.

```bash
--grid_exec sbatch_commandlist_trinity
```

When Trinity is executed with `--grid_exec` option, it generates a large amount of temporary files, and it 
is very likely that you will exceed the default limit of 100 000 files. Thus, it is advisable to apply for 
a larger file number quota for Puhti scratch before submitting large Trinity jobs. You can send the request
to [CSC Service Desk](../support/contact.md).

When the batch job file is ready, it can be submitted to the batch queue system with the command:

```bash
sbatch batch_job_file
```

Look here for [more information about running batch jobs](../computing/running/getting-started.md).

Please also check the [Trinity website](https://github.com/trinityrnaseq/trinityrnaseq/wiki) to get hints for estimating the required resources.

### Using autoTrinotate

You can analyze the results of your Trinity job with `autoTrinotate`. You need two files resulting from a successful Trinity assembly.

1. Fasta-formatted nucleotide sequence file containing the final contigs created by Trinity (`Trinity.fasta`)
2. gene-to-trans map for the input fasta file (`Trinity.fasta.gene_to_trans_map`)

Note that depending on the Trinity version, these names may have a prefix as defined with the `--output` option (e.g. `trinity_run_out.Trinity.fasta`).

Copy a template sqlite database for your analysis:

```bash
cp $TRINOTATE_HOME/databases/Trinotate.sqlite mydb.sqlite
```

You can then launch `autoTrinotate` with the command:

```bash
$TRINOTATE_HOME/auto/autoTrinotate.pl --Trinotate_sqlite mydb.sqlite --transcripts Trinity.fasta --gene_to_trans_map  Trinity.fasta.gene_to_trans_map --conf $TRINOTATE_HOME/auto/conf.txt --CPU  $SLURM_CPUS_PER_TASK
```

!!! warning "Note"
    autoTrinotate analysis can require a lot of resources, so you should execute the command
    in an [interactive session](../computing/running/interactive-usage.md) or as a batch job!

autoTrinotate produces an SQLite database file that can be further analyzed with the command:

```bash
$TRINOTATE_HOME/Trinotate
```

## More information

- [Trinity home page](https://github.com/trinityrnaseq/trinityrnaseq/wiki)
