# NWChem
§
NWChem provides many different methods to compute the properties of molecular and periodic systems using standard quantum mechanical descriptions of the electronic wavefunction or density. In addition, NWChem has the capability to perform classical molecular dynamics and free energy simulations. These approaches may be combined to perform mixed quantum-mechanics and molecular-mechanics simulations.

## Available

-   Puhti: 6.8.1

## License
 - The code is distributed as open-source under the terms of the [Educational Community License version 2.0 (ECL 2.0)](https://opensource.org/licenses/ecl2.php ). 

## Usage

Initialise NWChem on Puhti like this:

```bash
module load nwchem/6.8.1
```


**Example batch script for Puhti **

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as hh:mm:ss

module load nwchem/6.8.1
export NWCHEM_RUN=$PWD/NWCHEM_RUN_$SLURM_JOB_ID
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
seff $SLURM_JOBID
```
!!! note
    Particularly some of the more advanced electron correlation calculations  can be very disk I/O intensive. Such jobs benefit from using the fast local storage on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

   
**Example batch script for Puhti using local disk**

```
#!/bin/bash
#SBATCH --partition=large
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as hh:mm:ss
#SBATCH --gres=nvme:100      # requested local disk space in GB 

module load nwchem/6.8.1
export NWCHEM_RUN=$LOCAL_SCRATCH
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
seff $SLURM_JOBID
```

## References

Please cite the following reference when publishing results obtained with NWChem:

M. Valiev, E.J. Bylaska, N. Govind, K. Kowalski, T.P. Straatsma, H.J.J. van Dam, D. Wang, J. Nieplocha, E. Apra, T.L. Windus, W.A. de Jong, "NWChem: a comprehensive and scalable open-source solution for large scale molecular simulations" [Comput. Phys. Commun. 181, 1477 (2010)]( https://www.sciencedirect.com/science/article/pii/S0010465510001438?via%3Dihub )

## More information
-   [NWChem:Main Page](http://www.nwchem-sw.org/index.php/Main_Page)
-   [NWChem User Documentation](https://github.com/nwchemgit/nwchem/wiki)
-   [NWChem Community Forum](http://www.nwchem-sw.org/index.php/Special:AWCforum)
