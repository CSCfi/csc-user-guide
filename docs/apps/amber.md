# Amber

Amber is a molecular dynamics package which has as number of additional
tools for more sophisticated analysis and in particular for NMR
structure refinement.

[TOC]

## Available

* Puhti: 20, 20-cuda
* Mahti: 20, 20-cuda

## License

Amber can be used on CSC servers by all not-for-profit institute and
university researchers irrespective of nationality or location. Look for
the [academic license text here](http://ambermd.org/LicenseAmber20.pdf).

## Usage

See available versions and how to load Amber by running:
  
```bash
module spider amber
```

The `module load` command will set `$AMBERHOME` and put the AmberTools binaries
in the path. Run Amber production jobs in the batch queues, see below. Lightweight
system preparation can be done on the login node as well (short serial AmberTools
jobs).

Molecular dynamics jobs are best run with `pmemd.CUDA`. They are much faster
on GPGPUs than on CPUs. Please note that using `pmemd.CUDA` requires a different
module, `amber/20-cuda`, but it does not have all the AmberTools available.

!!! note
    Run only GPU aware binaries in the gpu partition. If you're unsure,
    check with `seff <slurm_jobid>` that GPU has been used, and the job
    was significantly faster than without GPUs.

Our tests show that for moderate sized systems the most efficient setup
is one V100 GPGPU card and one CPU core. An example batch script for Puhti
would be:

```bash
#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --partition=gputest
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --account=<project>
#SBATCH --gres=gpu:v100:1

# 1 task, 1 thread, 1 GPGPU

module purge
module load gcc/9.4.0 openmpi/4.1.4
module load amber/20-cuda

srun --gres=gpu:v100:1 pmemd.cuda -O -i mdin -r restrt -x mdcrd -o mdout
```

!!! note
    If you want to use more than one GPU, perform scaling tests to verify that
    the jobs really become faster. The rule of thumb is that when you double the
    resources, the job duration should decrease at least 1.5 fold. For overall
    performance info, consult [Amber benchmark scaling details](http://ambermd.org/GPUPerformance.php). Typically, best efficiency is achieved with 1 GPU.
    For example, the Cellulose NPT benchmark does not scale to multiple GPUs, but
    it is still massively faster on a single GPU than the CPU version (see below).

![Amber scaling on GPUs and CPUs on Mahti](../img/cellulose-amber.png 'Amber
scaling on GPUs and CPUs on Mahti')

You can find example inputs from the Amber tests directory:

```bash
ls $AMBERHOME/test
```

The non-CUDA aware binaries, e.g. AmberTools can be run as batch jobs e.g. in
the following way (on Puhti):

```bash
#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --account=<project>

# 1 task

module purge
module load gcc/9.4.0 openmpi/4.1.4
module load amber/20

srun paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

!!! note
    `pmemd.CUDA` is way faster than `pmemd.MPI`, so use a CPU-only version only
    in case you cannot use the CUDA version. If Amber performance is not fast
    enough, consider using [Gromacs](gromacs.md), which can make use
    of more CPU cores (i.e. scales further). In particular, for large scale or
    very long MD simulations consider using a better scaling MD engine.

### Interactive jobs

Sometimes it is more convenient to run small jobs, like system preparations,
interactively. To prevent excessive load on the login node, these kinds of jobs
should be run as interactive batch jobs. You can request a shell on a compute
node with [sinteractive](../computing/running/interactive-usage.md) or manually
access to a single core with:

```bash
srun -n 1 -p test -t 00:05:00 --account=<project> --pty /bin/bash
```

Then, once you have the resources (you might need to wait),
you can run the `paramfit` task directly with:

```
paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

## References

When citing Amber or AmberTools please use the following:

D.A. Case, K. Belfon, I.Y. Ben-Shalom, S.R. Brozell, D.S. Cerutti, 
T.E. Cheatham, III, V.W.D. Cruzeiro, T.A. Darden, R.E. Duke, 
G. Giambasu, M.K. Gilson, H. Gohlke, A.W. Goetz, R. Harris, 
S. Izadi, S.A. Izmailov, K. Kasavajhala, A. Kovalenko, R. Krasny, 
T. Kurtzman, T.S. Lee, S. LeGrand, P. Li, C. Lin, J. Liu, T. Luchko, 
R. Luo, V. Man, K.M. Merz, Y. Miao, O. Mikhailovskii, 
G. Monard, H. Nguyen, A. Onufriev, F.Pan, S. Pantano, R. Qi, 
D.R. Roe, A. Roitberg, C. Sagui, S. Schott-Verdugo, J. Shen, 
C.L. Simmerling, N.R.Skrynnikov, J. Smith, J. Swails, R.C. Walker, 
J. Wang, L. Wilson, R.M. Wolf, X. Wu, Y. Xiong, Y. Xue, D.M. York 
and P.A. Kollman (2020), AMBER 2020, University of California, San Francisco.

* [More on citations](http://ambermd.org/CiteAmber.php)

## More Information

[The Amber home page](http://ambermd.org/) has an extensive manual
and useful tutorials.
