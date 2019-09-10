# iPyrad

## Description

ipyrad is an interactive toolkit for assembly and analysis of restriction-site associated genomic data sets (e.g., RAD, ddRAD, GBS) for population genetic and phylogenetic studies.



## Available

-   Puhti:  0.9.11



## Usage

In Puhti, iPyrad can be taken in use as a _bioconda_ environment:

```text
module load bioconda
conda env list
source activate ipyrad
```

Ipyrad processing is typically started with command:
```text
ipyrad -n taskname
```

This creates a new parameter file (params-_taskname_.txt) that should be edited according to your analysis case.

For example in the case of job called _run1_:

```text
ipyrad -n run1
nano params-run1.txt
```

Once the parameter file is ready, you can start the actual ipyrad analysis. In Puhti login nodes you should run just really small taskas and not use more that one computing core with ipyrad. Thus you should add definition `-c 1` to the ipyrad command:

ipyrad -p params-run1.txt -s 1234567 -c 1

## Running heavy ipyrad jobs in Puhti

If you are analyzing large datasets, it is recommended that you run the jobs is several phases. Some steps of the ipyrad analysis can utilize parallel computing. To speed up the processing you could run these analysis steps as batch jobs.

The first two steps are typically executed rather quickly and you can run them interactively in Puhti login nodes. For example in the case of job run1:
```text
ipyrad -p params-run1.txt -s 12 -c 1
```

The third step of the ipryrad analysis runs a clustering for each sample set. Before starting this step, study first the content of the _jobname_edits directory created by the step 2. To check how many samples will be analyzed you can for example count the rows in the file s2_rawedit_stats.txt.

For example
```text
cd run1_edits
ls -l
wc -l s2_rawedit_stats.txt
```
The number of samples is the maximum number of parallel processes you should use in the parallel batch jobs. In practice you should use a value that is about half of the number of samples. For example, if you have 24 samples in the _edits directory, then you could consider using 12-16 cores.

The parallelization implementation of ipyrad requires that you always have only one ipyrad "task" running in one node. This means that you should always have parameter batch job parameter `--ntasks-per-node` set to one. However you can define that this task uses several cores with `--cpus-per-task`. For example, if you would assign the number of batch job tasks to 2 (`-n 2`) and number of cores used by one task to 8( `--cpus-per-task=8`) your job would use 2*8=16 cores. 

This number of cores is then given to the ipyrad command with option `-c`. Further, if you are using more than one node you should define that MPI is in use (--MPI) and that the commands of the pipeline are executed using only one computing core (`-t`).

In the sample case here we will use 16 cores in one node. If the run time is expected to be more than 3 days the job should be submitted to small partition (#SBATCH -p longrun). In this case we reserve 168 hours ( 7 days). Further, in step 3 the clustering commands are executed using only one thread (-t 1 ).
```text

#!/bin/bash -l
###
## name of your job
#SBATCH -J ipyrad
#SBATCH -e ipyrad_err_%j
#SBATCH -o ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH -t 72:00:00
#SBATCH -n 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH -p small


module load bioconda
source activate ipyrad
ipyrad -p params-run1.txt -s 3 -c 20 -t 1 

```


The batch job is launched with command
```
sbatch ipyrad_batch_job_file.sh
```
Once the job has finished you could run the next step by replacing `-s 3` with `-s 4` etc.

For the setps 4-7 maximum of 8 cores is recommended. Thread assigning option should not be set so that ipyrad can't use the default settings.

```text
#!/bin/bash -l
###
## name of your job
#SBATCH -J ipyrad
#SBATCH -e ipyrad_err_%j
#SBATCH -o ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH -t 72:00:00
#SBATCH -n 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH -p small

module load bioconda
source activate ipyrad
ipyrad -p ipyrad-run1.txt -s 4567 -c 8 -t 1 
```

More information about runnig batch jobs can be found from the [batch job section of the Puhti user guide](https://docs.csc.fi/#computing/running/getting-started/).

## Using cPouta for very long ipyrad jobs

The maximum run time in Puhti is 14 days. In some cases running the ipyrad analysis step 3 may take even longer time. In those cases you can use the cPouta cloud service to set up your own virtual machine. Check using-cpouta-for-biosciences for more details.


After that you can start Qiime2 with command:
```text
qiime
```

Please check Qiime2 home page for more instructions.

Note that many Qiime tasks involve heavy computing. Thus these tasks should be executed as
batch jobs.

For example the batch job script below runs the denoising step of the
[QIIME moving pictures tutorial](https://docs.qiime2.org/2019.7/tutorials/moving-pictures/#option-1-dada2 )
as a batch job using eight cores.

```text
#!/bin/bash
#SBATCH --job-name=qiime_denoise
#SBATCH --account=<project> 
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --out=qiime_out_8
#SBATCH --err=qiime_err_8
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --partition=small

#set up qiime
module load bioconda
source activate qiime2-2019.7

# run task
srun qiime dada2 denoise-single \
  --i-demultiplexed-seqs demux.qza \
  --p-trim-left 0 \
  --p-trunc-len 120 \
  --o-representative-sequences rep-seqs-dada2.qza \
  --o-table table-dada2.qza \
  --o-denoising-stats stats-dada2.qza \
  --p-n-threads $SLURM_CPUS_PER_TASK
``` 

In the example above _<project>_ sould be replaced with your project name. You can use `csc-workspaces` to check your Puhti projects.
Maximum running time is set to 1 hour (`--time=01:00:00`). As QIIME2 uses threads based parallelization, the process is considered as one job that
 should be executed within one node (`--ntasks=1`, `--ntasks=1`). The job reserves eight cores `--cpus-per-task=8` that 
can use in total up to 16 GB of memory  (` --mem=16G`). Note that the nubmer of cores to be used needs to be defined in 
actual qiime command too. That is done with Megahit option `--p-n-threads`. In this case we use $SLURM_CPUS_PER_TASK 
variable that contains the _cpus-pre-task_ value ( we could as well use `--p-n-threads 8` but then we have to remember 
to change the value if the number of reserved CPUs is changed).

The job is submitted to the to the batch job system with `sbatch` command. For example, if the batch job
file is named as _qiime_job.sh_ then the submission command is: 
```text
sbatch qiime_job.sh 
```
More information about runnig batch jobs can be found from the [batch job section of the Puhti user guide](https://docs.csc.fi/#computing/running/getting-started/).



## Manual

*   [QIIME2 home page](https://qiime2.org/)




