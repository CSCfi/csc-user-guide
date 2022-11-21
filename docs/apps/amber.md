---
tags:
  - Academic
---

# Amber

Amber is a molecular dynamics package including a number of additional
tools for more sophisticated analysis and in particular NMR structure
refinement.

[TOC]

## Available

* Puhti: 20, 20-cuda, 22, 22-cuda
* Mahti: 20, 20-cuda

## License

Amber can be used on CSC servers by all not-for-profit institute and
university researchers irrespective of nationality or location. Look for
the [academic license text here](http://ambermd.org/LicenseAmber22.pdf).

## Usage

See available versions and how to load Amber by running:
  
```bash
module spider amber
```

The `module load` command will set `$AMBERHOME` and put the AmberTools binaries
in the path. Run Amber production jobs in the batch queues, see below. Lightweight
system preparation can be done on the login node as well (short serial AmberTools
jobs).

!!! info "Python modules"
    Please use the Amber22 modules on Puhti if you intend to run the Python
    scripts distributed with AmberTools. These are not available in the older
    modules.

Molecular dynamics jobs are best run with `pmemd.CUDA`. They are much faster
on GPUs than on CPUs. Please note that using `pmemd.CUDA` requires a module
with the `-cuda` extension.

!!! warning "Note"
    Run only GPU aware binaries in the GPU partitions. If you're unsure,
    check with `seff <slurm_jobid>` that GPUs _were_ used and that the job
    was significantly faster than without GPUs.

Our tests show that for medium-sized systems the most efficient setup
is one GPU card and one CPU core. An example batch script for Puhti
would be:

```bash
#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --partition=gputest
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --account=<project>
#SBATCH --gres=gpu:v100:1

# 1 task, 1 thread, 1 GPU

module purge
module load gcc/9.4.0 openmpi/4.1.4
module load amber/22-cuda

srun pmemd.cuda -O -i mdin -r restrt -x mdcrd -o mdout
```

!!! info "Note"
    If you want to use more than one GPU, perform scaling tests to verify that the
    jobs really become faster. The rule of thumb is that when you double the resources,
    the job duration should decrease at least 1.5-fold. For overall performance info,
    consult the [Amber benchmark scaling details](http://ambermd.org/GPUPerformance.php).
    Typically, best efficiency is achieved with 1 GPU. For example, the Cellulose NPT
    benchmark does not scale to multiple GPUs, but it is still massively faster on a
    single GPU than the CPU version (see below).

![Amber scaling on GPUs and CPUs on Mahti](../img/cellulose-amber.png 'Amber
scaling on GPUs and CPUs on Mahti')

You can find example inputs from the Amber20 tests directory:

```bash
ls $AMBERHOME/test
```

The non-CUDA aware binaries, *e.g.* AmberTools, can be run as batch jobs in the
following way (on Puhti):

```bash
#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --account=<project>

# 1 task

module purge
module load gcc/9.4.0 openmpi/4.1.4
module load amber/22

srun paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

!!! info "Note"
    `pmemd.CUDA` is way faster than `pmemd.MPI`, so use a CPU-version only in
    case you cannot use the GPU-version. If Amber performance is not fast
    enough, consider using [Gromacs](gromacs.md), which can make use of more
    CPU cores (*i.e.* scales further). In particular, for large scale or very
    long MD simulations consider using a better scaling MD engine.

### Interactive jobs

Sometimes it is more convenient to run small jobs, like system preparations,
interactively. To prevent excessive load on the login node, these kinds of jobs
should be run as interactive batch jobs. You can request a shell on a compute
node from the [Puhti Web Interface](../../computing/webinterface/), from the
command line with [sinteractive](../computing/running/interactive-usage.md),
or manually access to a single core with:

```bash
srun -n 1 -p test -t 00:05:00 --account=<project> --pty /bin/bash
```

Once you have been allocated resources (you might need to wait), you can run *e.g.*
the `paramfit` task directly with:

```bash
paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

## References

When citing Amber22 or AmberTools22, please use the following:

D.A. Case, H.M. Aktulga, K. Belfon, I.Y. Ben-Shalom, J.T. Berryman, S.R. Brozell,
D.S. Cerutti, T.E. Cheatham, III, G.A. Cisneros, V.W.D. Cruzeiro, T.A. Darden,
R.E. Duke, G. Giambasu, M.K. Gilson, H. Gohlke, A.W. Goetz, R. Harris, S. Izadi,
S.A. Izmailov, K. Kasavajhala, M.C. Kaymak, E. King, A. Kovalenko, T. Kurtzman,
T.S. Lee, S. LeGrand, P. Li, C. Lin, J. Liu, T. Luchko, R. Luo, M. Machado,
V. Man, M. Manathunga, K.M. Merz, Y. Miao, O. Mikhailovskii, G. Monard, H. Nguyen,
K.A. O'Hearn, A. Onufriev, F. Pan, S. Pantano, R. Qi, A. Rahnamoun, D.R. Roe,
A. Roitberg, C. Sagui, S. Schott-Verdugo, A. Shajan, J. Shen, C.L. Simmerling,
N.R. Skrynnikov, J. Smith, J. Swails, R.C. Walker, J. Wang, J. Wang, H. Wei,
R.M. Wolf, X. Wu, Y. Xiong, Y. Xue, D.M. York, S. Zhao, and P.A. Kollman (2022),
Amber 2022, University of California, San Francisco.

* [More on citations](http://ambermd.org/CiteAmber.php)

## More Information

[The Amber home page](http://ambermd.org/) has an extensive manual
and useful tutorials.
