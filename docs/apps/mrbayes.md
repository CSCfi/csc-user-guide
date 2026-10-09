---
tags:
  - Free
catalog:
  name: MrBayes
  description: Program for inferring phylogenies using Bayesian methods
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MrBayes

MrBayes is a program for Bayesian inference on phylogenies.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu-CPU: 3.2.7a, via the `bio-apps` module.
* Roihu-GPU: 3.2.8 (GPU-accelerated through BEAGLE), via the `bio-apps` module.

## Usage

MrBayes is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MrBayes module:

```bash
module load bio-apps/v202603
module load mrbayes/3.2.7a
```

On the GPU nodes, load `mrbayes/3.2.8` instead; see [Running on GPUs](#running-on-gpus).

MrBayes is started with the `mb` command. The same MPI-enabled binary runs serially when started directly:

```bash
mb
```

and in parallel when launched with `srun` in a batch job. When using the parallel version, you should note that MrBayes assigns one chain to one core, so for optimal performance you should use as many cores as the total number of chains in your job. If, for example, you have specified `nchains=4`, `nruns=2`, you should use 4 * 2 = 8 cores.

## Batch jobs

Running a MrBayes analysis might take a considerable amount of CPU time and memory. It is, therefore, recommended to run it through the batch job system on Roihu. Shorter test runs can be run in interactive mode using [sinteractive](../computing/running/interactive-usage.md). The serial version is recommended for interactive use.

To run a batch job you need to:

1. Write a MrBayes command file (here `mb_com.nex`) or include a MrBayes command block in your `.nex` file. For details, see [Chapter 5.5.1 of the MrBayes manual](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).
2. Write a batch job script (here `mb_batch`)
3. Make sure you have all your input files (here `primates.nex`)
4. Submit your job into the queue

The MrBayes command file should include the commands you would type in MrBayes in interactive mode. This example
runs the analysis mentioned in [Chapter 2 of the MrBayes 3.2 manual](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).

```text
begin mrbayes;
    set autoclose=yes nowarn=yes;
    execute primates.nex;
    lset nst=6 rates=invgamma;
    mcmc nchains=4 nruns=2 ngen=20000 samplefreq=100 printfreq=100 diagnfreq=1000;
    sump;
    sumt;
end;
```

Below is an example batch job script for Roihu using 8 cores. We are using 8 cores since our example uses `nchains=4`, `nruns=2`, so 4 * 2 = 8.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --job-name=my_mrbjob
#SBATCH --error=my_mrbjob_err%j
#SBATCH --output=my_mrbjob_out%j
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000

module load bio-apps/v202603
module load mrbayes/3.2.7a

srun mb mb_com.nex >log.txt
```

To submit the job:

```bash
sbatch mb_batch
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Running on GPUs

On the Roihu GPU (GH200) nodes, MrBayes 3.2.8 is built with the
[BEAGLE](https://github.com/beagle-dev/beagle-lib) library with CUDA support, which
computes the likelihoods on the GPU. Log in to `roihu-gpu.csc.fi` and load the modules
there to get the GPU build:

```bash
module load bio-apps/v202603
module load mrbayes/3.2.8
```

To use the GPU, add this line to the start of your MrBayes block, before `execute`:

```text
set usebeagle=yes beagledevice=gpu;
```

BEAGLE can compute in single or double precision. To use double precision, add
`beagleprecision=double` to the same line:

```text
set usebeagle=yes beagledevice=gpu beagleprecision=double;
```

The `showbeagle` command lists the BEAGLE resources that MrBayes can use, so you can
check that the GPU is found.

The GPU speeds up the analysis mainly for large alignments with many unique site
patterns. For small datasets, the CPU version is usually as fast or faster.

Below is an example batch job script that runs the same 8 MPI processes as the CPU
example on one GPU. Here `mb_com_gpu.nex` is the command file from above with the
`set usebeagle=yes beagledevice=gpu;` line added. All MPI processes share the
reserved GPU.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --job-name=my_mrbjob_gpu
#SBATCH --error=my_mrbjob_err%j
#SBATCH --output=my_mrbjob_out%j
#SBATCH --partition=gpumedium
#SBATCH --time=01:00:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:gh200:1

module load bio-apps/v202603
module load mrbayes/3.2.8

srun mb mb_com_gpu.nex >log.txt
```

See the [GPU partitions](../computing/running/batch-job-partitions.md) for the
available GPU resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MrBayes home page](https://nbisweden.github.io/MrBayes/index.html)
* [Manual and other resources](https://nbisweden.github.io/MrBayes/manual.html)
