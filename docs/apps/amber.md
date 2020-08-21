# Amber

Amber is a molecular dynamics package which has as number of additional
tools for more sophisticated analysis and in particular for NMR
structure refinement.

[TOC]

## Available

* Puhti: 18, 18-cuda, 20, 20-cuda

## License

Amber can be used on CSC servers by all not-for-profit institute and
university researchers irrespective of nationality or location. Look for
the [academic license text here].

## Usage

Start using the AmberTools with the default version:
  
```
module load amber
```

Use `module spider amber` to see all available versions.
The `module load` command will set `$AMBERHOME` and put the AmberTools binaries in the path. Run Amber
production jobs in the batch queues, see below. Lightweight system preparation
can be done on the login node as well (short serial AmberTools jobs).

Molecular dynamics jobs are best run with `pmemd.CUDA`. They are much faster
on GPGPUs than on CPUs. Please note, that using `pmemd.CUDA` requires
a different module `amber/20-cuda`, but it does not have all the AmberTools available.
Our tests show that for moderate sized systems the most efficient setup
is one V100 GPGPU card and one CPU core. An example batch script would be:

```
#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --partition=gputest
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --account=<project>
#SBATCH --gres=gpu:v100:1

# 1 task, 1 thread, 1 GPGPU

module load amber/20-cuda

srun --gres=gpu:v100:1 pmemd.cuda.MPI -O -i mdin -r restrt -x mdcrd -o mdout
```

!!! note
    If you want to use more than one GPGPU, perform scaling tests to verify that
    the jobs really become faster. The rule of thumb is that when you double the resources,
    the job duration should shrink at least 1.5 fold.
    For overall performance info, consult [Amber benchmark scaling info].

You can find example inputs from the amber tests directory:

```
ls $AMBERHOME/test
```

The non-CUDA aware binaries, e.g. AmberTools can be run as batch jobs e.g. with the following way:

```
#!/bin/bash -l
#SBATCH --time=00:10:00
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --account=<project>

# 1 task

module load amber/20

srun paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

!!! note
    `pmemd.CUDA` is way faster than `pmemd.MPI`, so use a CPU-only 
    version only in case you cannot use the CUDA version. If Amber performance
    is not fast enough, consider using [Gromacs](gromacs.md), which can be
    an order of magnitude faster. In particular, for large scale or very long MD
    simulations consider using a better scaling MD engine.

### Interactive jobs

Sometimes it is more convenient to run small jobs, like system
preparations, interactively. To prevent excessive load on the login node, these
kinds of jobs should be run as interactive batch jobs. You can request
a shell on a compute node with 
[sinteractive](../computing/running/interactive-usage.md) or manually access to a single core with:

```
srun -n 1 -p test -t 00:05:00 --account=<project> --pty /bin/bash
```

Then, once you have the resources (you might need to wait), 
you can run the `paramfit` task directly with:

```
paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

## References

When citing Amber20 or AmberTools20 please use the following:

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

For Amber 2018:
  
D.A. Case, I.Y. Ben-Shalom, S.R. Brozell, D.S. Cerutti, T.E. Cheatham,
III, V.W.D. Cruzeiro, T.A. Darden, R.E. Duke, D. Ghoreishi, M.K. Gilson,
H. Gohlke, A.W. Goetz, D. Greene, R Harris, N. Homeyer, S. Izadi, A.
Kovalenko, T. Kurtzman, T.S. Lee, S. LeGrand, P. Li, C. Lin, J. Liu, T.
Luchko, R. Luo, D.J. Mermelstein, K.M. Merz, Y. Miao, G. Monard, C.
Nguyen, H. Nguyen, I. Omelyan, A. Onufriev, F. Pan, R. Qi, D.R. Roe, A.
Roitberg, C. Sagui, S. Schott-Verdugo, J. Shen, C.L. Simmerling, J.
Smith, R. Salomon-Ferrer, J. Swails, R.C. Walker, J. Wang, H. Wei, R.M.
Wolf, X. Wu, L. Xiao, D.M. York and P.A. Kollman (2018), AMBER 2018,
University of California, San Francisco.

* [More on citations](http://ambermd.org/CiteAmber.php)

## More Information

The Amber home page: [http://ambermd.org/](http://ambermd.org/) has an extensive manual
and useful tutorials.

  [academic license text here]: http://ambermd.org/LicenseAmber20.pdf
  [Amber benchmark scaling info]: http://ambermd.org/GPUPerformance.php
  [NoMachine remote desktop]: nomachine.md
