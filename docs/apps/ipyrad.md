---
tags:
  - Free
catalog:
  name: iPyrad
  description: toolkit for population genetic and phylogenetic studies of restriction-site associated genomic data sets (e.g., RAD, ddRAD, GBS)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# iPyrad

iPyrad is an interactive toolkit for assembly and analysis of restriction-site associated genomic data sets (e.g., RAD, ddRAD, GBS) for population genetic and phylogenetic studies.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 0.9.102 (module `py-ipyrad`), via the `bio-apps` module.

## Usage

iPyrad is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the iPyrad module:

```bash
module load bio-apps/v202603
module load py-ipyrad/0.9.102
```

!!! info "Note"
    The actual `ipyrad` command should always be executed in a batch job environment.

For iPyrad tasks that are not computationally heavy, an
[interactive batch job](../computing/running/interactive-usage.md) provides 
a good environment without queuing in between tasks.

You can open an interactive batch job session with the command below. On the Roihu `interactive` partition each reserved core provides 1.875 GB of memory (up to 32 cores / 60 GB / 36 hours), so request enough cores for the memory you need — here 9 cores (about 17 GB):

```bash
sinteractive --account <project> --cores 9
```

iPyrad processing can now be started with the command:

```bash
ipyrad -n run1
```

This creates a new parameter file (`params-run1.txt`) that should be edited according to your analysis case, for example with a text editor such as `nano`.

Once the parameter file is ready, you can start the actual iPyrad analysis. In interactive batch
jobs you can run small tasks that use just one computing core. Thus, you should add
definition `-c 1` to the `ipyrad` command:

```bash
ipyrad -p params-run1.txt -s 1234567 -c 1
```

## Running heavy iPyrad jobs on Roihu

If you are analyzing large datasets, it is recommended that you run the iPyrad process in several phases. Some steps of the iPyrad analysis can utilize parallel computing. To speed up the processing, you could run these analysis steps as normal batch jobs.

The first two steps are typically executed rather quickly, and you can run them in an interactive batch job environment (see above). 
For example, in the case of job `run1`:

```bash
ipyrad -p params-run1.txt -s 12 -c 1
```

The third step of the iPyrad analysis runs a clustering for each sample set. Before starting this step, study first the content of the `run1_edits` directory created by step 2. To check how many samples will be analyzed, you can, for example, count the rows in the file `s2_rawedit_stats.txt`.

For example:

```bash
cd run1_edits
ls -l
wc -l s2_rawedit_stats.txt
```

The number of samples is the maximum number of parallel processes you should use in the parallel batch jobs. In practice, you should use a value that is about half of the number of samples. For example, if you have 24 samples in the `*_edits` directory, then you could consider using 12-16 cores.

The parallelization implementation of iPyrad requires that you always have only one iPyrad "task" running in one node. This means that you should always have the batch job parameter `--ntasks-per-node=1`. However, you can define that this task uses several cores with `--cpus-per-task`. For example, if you would assign the number of batch job tasks to 2 (`--ntasks=2`) and number of cores used by one task to 8 (`--cpus-per-task=8`), your job would use 2 * 8 = 16 cores. 

This number of cores (`--ntasks` * `--cpus-per-task`) is then given to the iPyrad command with option `-c`. This is critical, as otherwise iPyrad will only use one core, even if it is requested from Slurm with `--cpus-per-task=8`. Further, if you are using more than one node you should define that MPI is in use (`--MPI`) and that the commands of the pipeline are executed using only one computing core (`-t`).

In the sample case here, we will use 20 cores in one node. On Roihu, a single-node job in the `small` partition can run for up to 3 days; if the run time is expected to be longer, submit the job to the `longrun` partition (`#SBATCH --partition=longrun`, up to 10 days). Here we reserve 72 hours (3 days). Further, in step 3, the clustering commands are executed using 20 cores (`-c 20`), each running one thread (`-t 1`).

```bash
#!/bin/bash
#SBATCH --job-name=ipyrad_s3
#SBATCH --account=<project>
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=ipyrad_output_%j
#SBATCH --partition=small
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=128G

module load bio-apps/v202603
module load py-ipyrad/0.9.102

ipyrad -p params-run1.txt -s 3 -c 20 -t 1 
```

The batch job is launched with command:

```bash
sbatch ipyrad_batch_job_file.sh
```

Once the job has finished, you could run the next step by replacing `-s 3` with `-s 4` etc.

For the setups 4-7, a maximum of 8 cores is recommended. Thread assigning option should always be set, as the default settings of iPyrad are not suitable for batch jobs.

```bash
#!/bin/bash
#SBATCH --job-name=ipyrad_s4567
#SBATCH --account=<project>
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=ipyrad_output_%j
#SBATCH --partition=small
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=128G

module load bio-apps/v202603
module load py-ipyrad/0.9.102

ipyrad -p params-run1.txt -s 4567 -c 8 -t 1 
```

More information about running batch jobs can be found from [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md).

## Using cPouta for very long iPyrad jobs

The maximum run time on Roihu is 10 days (the `longrun` partition). In some cases, running the iPyrad analysis step 3 may take even longer. In those cases, you can use the
[cPouta cloud service](../cloud/pouta/index.md) to set up your own virtual machine.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ipyrad home page](https://ipyrad.readthedocs.io/)
