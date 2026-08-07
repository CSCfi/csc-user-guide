---
tags:
  - Free
catalog:
  name: Trinity
  description: Transcriptome assembly tool
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
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

Roihu: 2.15.2

## Usage

### Using Trinity

Trinity is set up with the command:

```bash
module load trinity
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
#SBATCH --partition=small

module load trinity/2.15.2

Trinity --seqType fq --max_memory 22G --left reads.left.fq --right \
reads.right.fq --SS_lib_type RF --CPU $SLURM_CPUS_PER_TASK \
--output trinity_run_out 
```

The batch script above reserves 6 computing cores from one node for the job. The maximal run time of the sample job here is 48 hours. 
About 4 GB of memory is reserved for each core so the total memory reservation is `6 * 4 GB = 24 GB`. On Roihu, you must use batch job option
`--account=` to define the project to be used. You should replace `project_1234567` used in the example with your own project. You can check your 
projects with command: `csc-projects`.

In the actual `Trinity` command the number of computing cores to be used (`--CPU`) is set using the environment variable `$SLURM_CPUS_PER_TASK`. 
This variable contains the value set by the `--cpus-per-task` Slurm option.

!!! note "Option --grid-exec not currently available in Roihu"
The --grid-exec option is not currently available onRoihu.



When the batch job file is ready, it can be submitted to the batch queue system with the command:

```bash
sbatch batch_job_file
```

Look here for [more information about running batch jobs](../computing/running/getting-started.md).

Please also check the [Trinity website](https://github.com/trinityrnaseq/trinityrnaseq/wiki) to get hints for estimating the required resources.

!!! note "AutoTrinotate not currently available in Roihu"
AutoTrinotate is not currently available on Roihu. We are looking into adding it.


## More information

- [Trinity home page](https://github.com/trinityrnaseq/trinityrnaseq/wiki)
