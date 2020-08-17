# CP2K

Versatile ab initio and classical molecular dynamics. CP2k is suited for large parallel quantum chemistry calculations, in
particular for AIMD.

[TOC]

## Available

* Puhti: 6.1
* Mahti: 7.1

## License

CP2k is freely available under the GPL license.

## Usage

Check which versions are recommended:

    module avail cp2k

You can find all installed versions with:

    module spider cp2k

With each new project make sure that your job can efficiently
utilize all the cores you request in the batch script.

### Example batch script for Puhti using MPI-only parallelization

```
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --partition=large
#SBATCH --account=<project>

module load cp2k

srun cp2k.popt H2O-32.inp > H2O-32.out

```

### Example batch script for Mahti using mixed MPI-OpenMP parallelization

```
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --ntasks-per-node=32  # 2 - 128
#SBATCH --cpus-per-task=4     # 128 / ntasks-per-node
#SBATCH --nodes=2
#SBATCH --partition=test
#SBATCH --account=<project>

module purge
module load cp2k/7.1-elpa

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores

srun cp2k.psmp H2O-32.inp > H2O-32.out
```
### Performance notes

**Mahti:**

The following table shows average time [s] for one MD step for H2O-64 benchmark
in Mahti. The column headers show how many omp-threads were used per mpi-task.

Nodes|d1|d2|d4|d8
-|--|--|--|--
1|1.048|1.03|*0.97*|1.088
2|0.772|0.678|*0.578*|0.786
4|0.72|0.494|0.504|0.534

* For 64 water molecules, the best performance is obtained with 2 full nodes, 32 mpi-tasks,
  and 4 OMP-threads per task (like the [Mahti example](#example-batch-script-for-mahti-using-mixed-mpi-openmp-parallelization))
  For this system the performance does not scale beyond 2 nodes.
* Mixed parallization is efficient: choose tasks and threads so that they add up to 128
  (physical) cores available per node (or upto 40 on Puhti)
* Test for optimal run parameters for your model system and method
* A version linked with ELPA (like the one above) is
  significantly faster with (metallic) systems that require large matrix diagonalizations
  for SCF
* There are additional versions available at `/appl/soft/chem/cp2k/7.1_extra`, please
  see corresponding `README.txt`, but the one above is the fastest found so far

## References

CP2K prints out a list of relevant publications towards the end of the
log file. Choose and cite the ones relevant to the methods you've used.

## More Information

* CP2K online manual: <http://manual.cp2k.org/>
* CP2K home page: <http://www.cp2k.org/>
