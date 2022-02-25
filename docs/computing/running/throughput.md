# Tools for high throughput computing

High troughput computing (HTC) means running lots of jobs
automatically using scripts or workflows.
Workflow automation saves human time and reduces manual
errors. Workflows can be very specific and if you can't find
one that suits your needs out-of-the-box, they may need a lot
of work before they bring benefit. However, the simplest ones
are easy to use. This section introduces some tools available
at CSC, but you can of course develop or install your own.

## Simple general tools that run multiple jobs with one script

* [Array jobs](array-jobs.md) are a native Slurm tool to 
  submit several independent jobs with one command
* [GREASY](greasy.md) runs multiple job steps in a larger 
  allocation, and allows simple dependencies
* [DIY gnuparallel](../../support/tutorials/many.md) tutorial shows 
  how to efficiently run a very large number of serial jobs without 
  bloating the Slurm log

## Science specific workflow tools

* [Nextflow](../../support/tutorials/nextflow-puhti.md) singularity 
  container based bioinformatics pipelines on Puhti
* [multidir option of Gromacs](../../apps/gromacs.md#high-throughput-computing-with-gromacs) allows running multiple concurrent simulations within one Slurm allocation
* [FARMING mode of CP2K](../../apps/gromacs.md#high-throughput-computing-with-gromacs) enables running multiple concurrent simulations within one Slurm allocation with optional dependencies between subjobs
