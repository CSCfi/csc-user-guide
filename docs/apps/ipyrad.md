# iPyrad

## Description

iPyrad is an interactive toolkit for assembly and analysis of restriction-site associated genomic data sets (e.g., RAD, ddRAD, GBS) for population genetic and phylogenetic studies.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

-   Puhti:  0.9.57


## Usage

In Puhti, iPyrad can be taken in use as a _bioconda_ environment.
To use software environments that are installed to Puhti using Conda (either by CSC or yourself), 
first define environment variable PROJAPPL to point to a directory of the project that 
you wish to use for your own conda environments.

Typically this is your _/projappl/project_name_ directory, but you can use scratch too. 
This definition is made with command _export_. For example for project_012345 the command would be:

```text
export PROJAPPL=/projappl/project_12345
```
After that you can activate bioconda environment and check the available conda environments:

```text
module load bioconda
conda env list
```
Now you can activate iPyrad enroment:
```text
source activate ipyrad-0.9.57
```
!!! Note
    The actual _ipyrad_ command should always be executed in a batch job environment.

For iPyrad tasks, that are not computationally heavy, an
[interactive batch job](../computing/running/interactive-usage.md) provides 
a good environment without queueing.

You can open an interactive batch job session with commands:

```text
sinteractive -m 16G
```

iPyrad processing can now be started with command:
```text
ipyrad -n taskname
```

This creates a new parameter file (params-_taskname_.txt) that should be edited according to your analysis case.

For example in the case of job called _run1_:

```text
ipyrad -n run1
module load nano
nano params-run1.txt
```

Once the parameter file is ready, you can start the actual iPyrad analysis. In interactive batch
jobs you can run small tasks that use just one computing core. Thus, you should add
definition `-c 1` to the ipyrad command:
```text
ipyrad -p params-run1.txt -s 1234567 -c 1
```

## Running heavy ipyrad jobs in Puhti

If you are analyzing large datasets, it is recommended that you run the iPyrad process is several phases. Some steps of the iPyrad analysis can utilize parallel computing. To speed up the processing you could run these analysis steps as normal batch jobs.

The first two steps are typically executed rather quickly and you can run them in an interactive batch job environment (see above). 
For example in the case of job _run1_:
```text
ipyrad -p params-run1.txt -s 12 -c 1
```

The third step of the ipryrad analysis runs a clustering for each sample set. Before starting this step, study first the content of the _jobname_edits_ directory created by the step 2. To check how many samples will be analyzed you can, for example, count the rows in the file _s2_rawedit_stats.txt_.

For example
```text
cd run1_edits
ls -l
wc -l s2_rawedit_stats.txt
```
The number of samples is the maximum number of parallel processes you should use in the parallel batch jobs. In practice you should use a value that is about half of the number of samples. For example, if you have 24 samples in the _edits directory, then you could consider using 12-16 cores.

The parallelization implementation of ipyrad requires that you always have only one ipyrad "task" running in one node. This means that you should always have parameter batch job parameter `--ntasks-per-node` set to one. However, you can define that this task uses several cores with `--cpus-per-task`. For example, if you would assign the number of batch job tasks to 2 (`-n 2`) and number of cores used by one task to 8( `--cpus-per-task=8`) your job would use 2*8=16 cores. 

This number of cores is then given to the iPyrad command with option `-c`. This is critical, as otherwise iPyrad will only use one core, even if it is requested from SLURM with `--cpus-per-task=8`. Further, if you are using more than one node you should define that MPI is in use (--MPI) and that the commands of the pipeline are executed using only one computing core (`-t`).

In the sample case here we will use 20 cores in one node. If the run time is expected to be more than 3 days the job should be submitted to longrun partition (#SBATCH --partition=longrun). In this case we reserve 72 hours ( 3 days). Further, in step 3 the clustering commands are executed using 20 cores (-c 20) each running one thread (-t 1 ).
```text
#!/bin/bash -l
#SBATCH --job-name=ipyrad_s3
--error=ipyrad_err_%j
#SBATCH --output=put=ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --partition=small

module load bioconda
source activate ipyrad
ipyrad -p params-run1.txt -s 3 -c 20 -t 1 
```


The batch job is launched with command
```
sbatch ipyrad_batch_job_file.sh
```
Once the job has finished you could run the next step by replacing `-s 3` with `-s 4` etc.

For the setps 4-7 a maximum of 8 cores is recommended. Thread assigning option should not be set so that iPyrad can't use the default settings.

```text
#!/bin/bash -l
#SBATCH --job-name=ipyrad_s4567
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=put=ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small

module load bioconda
source activate ipyrad
ipyrad -p ipyrad-run1.txt -s 4567 -c 8 -t 1 
```

More information about runnig batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).

## Using cPouta for very long ipyrad jobs

The maximum run time in Puhti is 14 days. In some cases running the ipyrad analysis step 3 may take even longer time. In those cases you can use the cPouta cloud service to set up your own virtual machine. Check [using-cpouta-for-biosciences](https://research.csc.fi/using-cpouta-for-biosciences) for more details.



## Manual

*   [ipyrad home page](https://ipyrad.readthedocs.io/)




