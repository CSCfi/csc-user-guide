---
tags:
  - Free
---

# MrBayes



MrBayes is a program for Bayesian inference on phylogenies.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Puhti: 3.2.7a

## Usage

To check the available versions, use:

```bash
module spider mrbayes
```

To load a specific version:

```bash
module load mrbayes/3.2.7a
```

After loading the module, the serial (i.e. single processor) version starts with the command:

```bash
mb
```

Parallel version starts with the command:

```bash
mb-mpi 
```

When using the parallel version, you should note that MrBayes assigns one chain to one core, so for optimal performance you should use as many cores as the total number of chains in your job. If, for example, you have specified `nchains=4`, `nruns=2` you should use 4 * 2 = 8 cores.

## Batch jobs

Running MrBayes analysis might take considerable amount of CPU time and memory. It is, therefore, recommended running it through the batch job system on Puhti. Shorter test runs can be run in interactive mode using [sinteractive](../computing/running/interactive-usage.md). The serial version is recommended for interactive use.

To run a batch job you need to:

1. Write a MrBayes command file (here `mb_com.nex`) or include a MrBayes command block in your `.nex` file. For details, see [Chapter 5.5.1 of the MrBayes manual](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).
2. Write a batch job script (here `mb_batch`)
3. Make sure you have all your input files (here `primates.nex`)
4. Submit your job into the queue

MrBayes command file should include the commands you would type in MrBayes in interactive mode. This example 
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

Below is an example batch job script for Puhti using 8 cores. We are using 8 cores since our example uses `nchains=4`, `nruns=2`, so 4 * 2 = 8.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --job-name=my_mrbjob
#SBATCH --error=my_mrbjob_err%j
#SBATCH --output=my_mrbjob_out%j
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=01:00:00
#SBATCH --partition=small

srun mb-mpi mb_com.nex >log.txt
```

To submit the job on Puhti:

```bash
sbatch mb_batch 
```

## More information

* [MrBayes home page](https://nbisweden.github.io/MrBayes/index.html)
* [Manual and other resources](https://nbisweden.github.io/MrBayes/manual.html)
