# Tools for high-throughput computing

High-throughput computing (HTC) means running lots of jobs
automatically using scripts or workflows.
Workflow automation saves human time and reduces manual
errors. Workflows can be very specific and if you can't find
one that suits your needs out-of-the-box, they may need a lot
of work before they bring benefit. However, the simplest ones
are easy to use. This section introduces some tools available
at CSC, but you can of course develop or install your own.

## General tools that run multiple jobs with one script

* [Array jobs](array-jobs.md) are a native Slurm tool to 
  submit several independent jobs with one command
* [GREASY](greasy.md) runs multiple job steps in a larger 
  allocation, and allows simple dependencies
* [DIY gnuparallel](../../support/tutorials/many.md) tutorial shows 
  how to efficiently run a very large number of serial jobs without 
  bloating the Slurm log
* [FireWorks](fireworks.md) is a flexible tool for defining, managing and executing workflows with multiple steps and complex dependencies

## Science specific workflow tools

* [Nextflow](../../support/tutorials/nextflow-puhti.md) singularity 
  container based bioinformatics pipelines on Puhti

## Workflow tools integrated into common simulation software

The following built-in tools allow running multiple simulations in parallel within a single Slurm job step. If you're using any of the applications below, please consider these as the first option for implementing your high-throughput workflows.

* [Gromacs multidir option](../../apps/gromacs.md#high-throughput-computing-with-gromacs)
* [FARMING mode of CP2K](../../apps/cp2k.md#high-throughput-computing-with-cp2k) (supports dependencies between subjobs)
* [LAMMPS multi-partition switch](../../apps/lammps.md#high-throughput-computing-with-lammps)
