---
tags:
  - Free
catalog:
  name: RevBayes
  description: Bayesian phylogenetic inference with probabilistic graphical models
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# RevBayes

RevBayes is a program for Bayesian phylogenetic inference. Models are specified as
probabilistic graphical models in Rev, an interpreted language similar to R, which
makes it possible to build and combine a wide range of phylogenetic and evolutionary
models.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/revbayes/revbayes/blob/development/LICENSE).

## Available

* Roihu-CPU: 1.4.1, via the `bio-apps` module.

## Usage

RevBayes is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the RevBayes module:

```bash
module load bio-apps/v202603
module load revbayes/1.4.1
```

On Roihu, RevBayes is built with MPI support and the command is `rb-mpi`; there is
no separate `rb` command. Run a Rev script with:

```bash
rb-mpi my_analysis.Rev
```

Started without a script, `rb-mpi` opens the interactive Rev console. Run the console
and short tests in an [interactive session](../computing/running/interactive-usage.md),
not on the login node.

### Running in parallel

When launched with `srun` in a batch job, RevBayes divides the independent replicates
of an analysis (the `nruns` argument of `mcmc()` and `mcmcmc()`) and the stones of a
power-posterior analysis among the MPI processes. Use as many processes as there are
replicates, for example 4 processes for `nruns=4`.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=revbayes
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load revbayes/1.4.1

srun rb-mpi my_analysis.Rev
```

This example runs four MPI processes, one for each replicate of an analysis with
`nruns=4`. Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [RevBayes home page](https://revbayes.github.io)
* [RevBayes tutorials](https://revbayes.github.io/tutorials/)
