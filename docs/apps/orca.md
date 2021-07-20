# ORCA

[ORCA](https://orcaforum.kofo.mpg.de/app.php/portal ) is an ab initio quantum chemistry program package that contains modern electronic structure methods including density functional theory, many-body perturbation, coupled cluster, multireference methods, and semi-empirical quantum chemistry methods. Its main field of application is larger molecules, transition metal complexes, and their spectroscopic properties. ORCA is developed in the research group of [Frank Neese](https://en.wikipedia.org/wiki/Frank_Neese). The free version is available only for academic use at academic institutions. 

[TOC]

## License
 
ORCA users should register, agree to the EULA , download and install a private copy of the program (via [https://orcaforum.kofo.mpg.de/app.php/portal](https://orcaforum.kofo.mpg.de/app.php/portal))
The free version is available only for academic use at academic institutions.

## Usage

- Download the ORCA 5.0.0, Linux, x86-64, shared-version, `orca_5_0_0_linux_x86-64_shared_openmpi411.tar.xz`
- Move the downloaded file to your computing project's application area (/projappl/<proj\>) on Puhti
- Unpack the package, `tar xf orca_5_0_0_linux_x86-64_shared_openmpi411.tar.xz`
- Example parallel batch script for Puhti

```
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --account=<your billing project>
#SBATCH --time=0:30:00 # time as hh:mm:ss
#SBATCH --job-name=orca-5.0
#SBATCH --error=jobfile.err%J
#SBATCH --output=jobfile.out%J
module purge
module load intel/19.0.4 hpcx-mpi/2.4.0 intel-mkl/2019.0.4
export ORCADIR=<path to your ORCA directory>/orca_5_0_0_linux_x86-64_shared_openmpi411
export LD_LIBRARY_PATH=$ORCADIR:$LD_LIBRARY_PATH
$ORCADIR/orca orca_5.0.inp > orca_5.0.out
```
!!! note
    Please remember to adjust %pal nproc in your input file according to the total number of requested MPI tasks (nodes * ntasks-per-node) 

## References

Cite your work with the following references:

The generic reference for ORCA is:
- Neese, F. (2012) The ORCA program system, Wiley Interdiscip. Rev.: Comput. Mol. Sci., 2, 73-78.

Please do not only cite the above generic reference, but also cite in addition the original
papers that report the development and ORCA implementation of the methods you have used in
your studies! The publications that describe the functionality implemented in ORCA are
given in the manual.

## More information
-   [ORCA Forum (login with the same credentials as you used for downloading)](https://orcaforum.kofo.mpg.de/app.php/portal)
-   [ORCA Tutorials](https://www.orcasoftware.de/tutorials_orca/)
-   [Release notes](https://orcaforum.kofo.mpg.de/viewtopic.php?f=51&t=7564)


