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
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=4
#SBATCH --nodes=2
#SBATCH --partition=test
#SBATCH --account=<project>

module purge
module load cp2k/7.1-intel

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export MKL_DEBUG_CPU_TYPE=5

srun cp2k.psmp H2O-32.inp > H2O-32.out
```
### Performance notes

**Mahti:**

* Tests show, that using a version linked with ELPA (like the one above) is
  significantly faster with (metallic) systems that require large matrix diagonalizations
  for SCF
* Mixed parallization is efficient: choose tasks and threads so that they add up to 128
  (physical) cores available per node
* Test for optimal run parameters for your model system and method
* There are additional versions available at `/appl/soft/chem/cp2k/7.1_elpa`, please
  see corresponding `README.txt`, but the one above is the fastest found so far


## References

CP2K prints out a list of relevant publications towards the end of the
log file. Choose and cite the ones relevant to the methods you've used.

## More Information

* CP2K online manual: <http://manual.cp2k.org/>
* CP2K home page: <http://www.cp2k.org/>
