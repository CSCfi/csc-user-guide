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
* Mahti: 20, 20-cuda, 22, 22-cuda
* LUMI: 22-cpu, 22-gpu

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
    Please use the Amber22 modules on Puhti/Mahti if you intend to run the Python
    scripts distributed with AmberTools. These are not available in the older modules,
    nor on LUMI. As AmberTools is also distributed through Conda, another alternative
    is to install and create a containerized environment for the scripts yourself using
    [Tykky](../computing/containers/tykky.md) or the
    [LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

Molecular dynamics jobs are best run with `pmemd.cuda`. They are much faster
on GPUs than on CPUs. Please note that using `pmemd.cuda` requires a module
with the `-cuda` extension. Similarly, on LUMI one should use `pmemd.hip` (or
`pmemd.hip.MPI` for multi-GPU simulations), which requires loading a module
with the `-gpu` extension.

!!! warning "Note"
    Run only GPU aware binaries in the GPU partitions. If you're unsure,
    check with `seff <slurm_jobid>` that GPUs *were* used and that the job
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
    jobs really become faster and use a binary with `.cuda.MPI` or `.hip.MPI` extension.
    The rule of thumb is that when you double the resources, the job duration should
    decrease at least 1.5-fold. For overall performance info, consult the [Amber benchmark
    scaling details](http://ambermd.org/GPUPerformance.php). Typically, best efficiency
    is achieved with 1 GPU. For example, the Cellulose NPT benchmark does not scale well
    to multiple GPUs, but it is still massively faster on a single GPU than the CPU
    version (see diagram below).

You can find example inputs from the Amber20 tests directory:

```bash
ls $AMBERHOME/test
```

The non-GPU aware binaries, *e.g.* AmberTools, can be run as batch jobs in the
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
    `pmemd.cuda` and `pmemd.hip` are way faster than `pmemd.MPI`, so use a
    CPU-version only in case you cannot use the GPU-version. If Amber performance
    is not fast enough, consider using [Gromacs](gromacs.md), which can make use
    of more CPU cores (*i.e.* scales further). In particular, for large scale or
    very long MD simulations consider using a better scaling MD engine. An alternative
    is to [run ensemble simulations using multi-pmemd](#high-throughput-computing-with-amber).

### Interactive jobs

Sometimes it is more convenient to run small jobs, like system preparations,
interactively. To prevent excessive load on the login node, these kinds of jobs
should be run as interactive batch jobs. You can request a shell on a compute
node from the [Puhti Web Interface](../computing/webinterface/index.md), from the
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

### Amber on LUMI

Amber can be loaded into use on LUMI with:

```bash
module use /appl/local/csc/modulefiles
module load amber/22-gpu
# or
module load amber/22-cpu
```

!!! info "Note"
    You need to run the `module use` command to modify your `$MODULEPATH`,
    otherwise modules pre-installed by CSC cannot be accessed.

Example batch job script for LUMI-G:

```bash
#!/bin/bash -l
#SBATCH --partition=small-g
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --time=01:00:00
#SBATCH --account=<project>

module purge
module use /appl/local/csc/modulefiles
module load amber/22-gpu

srun pmemd.hip.MPI -O -i mdin.GPU -o mdout.GPU -p Cellulose.prmtop -c Cellulose.inpcrd
```

A performance comparison of Amber on CPUs and GPUs on Puhti, Mahti and LUMI is shown
in the bar plot below. Note how the performance of a single GPU on all systems is an
order of magnitude better than a full Mahti CPU node (128 cores).

![Amber scaling on GPUs and CPUs on Puhti, Mahti and LUMI](../img/cellulose-amber.png 'Amber
scaling on GPUs and CPUs on Puhti, Mahti and LUMI')

!!! info "GPU binding on LUMI"
    For best performance, *multi-GPU* simulations on LUMI-G are likely to
    benefit from GPU binding. For background and instructions, see the
    [LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding).

General batch script examples for [LUMI-G](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)
and [LUMI-C](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumic-job/) are available in the LUMI
documentation.

### High-throughput computing with Amber

Similar to [Gromacs multidir](../support/tutorials/gromacs-throughput.md),
Amber has a built-in "multi-pmemd" functionality, which allows you to run multiple
MD simulations within a single Slurm allocation. This is an efficient option in cases
where you want to run many similar, but independent, simulations. Typical use cases
are enhanced sampling methods such as umbrella sampling or replica exchange MD. Also,
since Amber simulations do not scale that well to multiple GPUs, multi-pmemd can be
used as a straightforward method to accelerate sampling by launching several differently
initialized copies of your system, all running simultaneously on a single GPU each.

!!! info "Note"
    GPU resources on Puhti and Mahti are scarce, so we recommend running large-scale multi-pmemd
    simulations only on LUMI. LUMI-G has a massive GPU capacity available, which is also [more
    affordable in terms of BUs](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/)
    compared to Puhti and Mahti.

An example multi-pmemd batch script for LUMI-G is provided below.

```bash
#!/bin/bash -l
#SBATCH --partition=standard-g
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --gpus-per-node=8
#SBATCH --time=01:00:00
#SBATCH --account=<project>

module purge
module use /appl/local/csc/modulefiles
module load amber/22-gpu

srun pmemd.hip.MPI -ng 16 -groupfile groupfile
```

In this example, 16 copies of a system are run concurrently within a single Amber job,
each using 1 GPU. From the perspective of Slurm, each node on LUMI-G contains 8 GPUs,
so 2 nodes are requested in total. The input, output, topology and coordinate files
for the respective simulations are defined in a so-called `groupfile`:

```bash
-O -i mdin.GPU -o mdout000.GPU -p system000.prmtop -c system000.inpcrd
-O -i mdin.GPU -o mdout001.GPU -p system001.prmtop -c system001.inpcrd
-O -i mdin.GPU -o mdout002.GPU -p system002.prmtop -c system002.inpcrd
-O -i mdin.GPU -o mdout003.GPU -p system003.prmtop -c system003.inpcrd
-O -i mdin.GPU -o mdout004.GPU -p system004.prmtop -c system004.inpcrd
-O -i mdin.GPU -o mdout005.GPU -p system005.prmtop -c system005.inpcrd
-O -i mdin.GPU -o mdout006.GPU -p system006.prmtop -c system006.inpcrd
-O -i mdin.GPU -o mdout007.GPU -p system007.prmtop -c system007.inpcrd
-O -i mdin.GPU -o mdout008.GPU -p system008.prmtop -c system008.inpcrd
-O -i mdin.GPU -o mdout009.GPU -p system009.prmtop -c system009.inpcrd
-O -i mdin.GPU -o mdout010.GPU -p system010.prmtop -c system010.inpcrd
-O -i mdin.GPU -o mdout011.GPU -p system011.prmtop -c system011.inpcrd
-O -i mdin.GPU -o mdout012.GPU -p system012.prmtop -c system012.inpcrd
-O -i mdin.GPU -o mdout013.GPU -p system013.prmtop -c system013.inpcrd
-O -i mdin.GPU -o mdout014.GPU -p system014.prmtop -c system014.inpcrd
-O -i mdin.GPU -o mdout015.GPU -p system015.prmtop -c system015.inpcrd
```

See the [Amber manual](https://ambermd.org/doc12/Amber22.pdf) for further details
on multi-pmemd.

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
