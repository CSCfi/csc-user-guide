# CP2K

Versatile ab initio and classical molecular dynamics. CP2k is suited for large parallel quantum chemistry calculations, in
particular for AIMD.

[TOC]

## Available

* Puhti: 6.1

## License

CP2k is freely available under the GPL license.

## Usage

Check which versions are recommended:

    module avail cp2k

You can find all installed versions with:

    module spider cp2k

With each new project make sure that your job can efficiently
utilize all the cores you request in the batch script.

**Example batch script for Puhti using MPI-only parallelization**

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

## References

CP2K prints out a list of relevant publications towards the end of the
log file. Choose and cite the ones relevant to the methods you've used.

## More Information

* CP2K online manual: <http://manual.cp2k.org/>
* CP2K home page: <http://www.cp2k.org/>
