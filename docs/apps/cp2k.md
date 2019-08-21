# CP2K

Versatile ab initio and classical molecular dynamics. CP2k is suited for large parallel quantum chemistry calculations, in
particular for AIMD.

[TOC]

## Available

* Puhti: 6.1

## License

CP2k is freely available under the GPL license.

## Usage

Check which versions are available:

    module spider cp2k

In your batch script load all required modules shown with spider:

    module load intel/19.0.4 hpcx-mpi/2.4.0 cp2k/6.1

Loading the module points you to the installation directory, which has
example submit commands for different parallelization schemes. Before
each project make sure that your job can utilize all the cores you
request in the batch script!

**Example batch script for Puhti using MPI-only parallelization**

```
#!/bin/bash
#SBATCH -J cp2k-test
#SBATCH -t 00:10:00
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=2000
#SBATCH --partition=parallel
#SBATCH --account=project_200XXX

module load intel/19.0.4  hpcx-mpi/2.4.0 cp2k/6.1
export CP2K_DATA_DIR=$CP2K_INSTALL_ROOT/share/data

srun cp2k.popt H2O-32.inp > H2O-32.out

```

**Example batch script for Sisu using mixed MPI/OpenMP parallelization**

!!! note
    Mixed parallelization speeds up simulations only in few cases. Always
    perform a scaling test for each new system and simulation type.
    Preinstalled version not yet available on Puhti.
```

TO BE FIXED...

#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --no-requeue
#SBATCH --ncpus-per-task=2
#SBATCH --tasks-per-node=20

module load cp2k
export CP2K_DATA_DIR=/appl/chem/cp2k/data

# check if all resources would be used
echo $SLURM_NNODES

input=input_bulk_HFX_3
ht=1                   # no hyperthreading
t=12                   #threads per process, 12 is optimal for big hybrid functional jobs
alps_param="-ss -cc numa_node"  # additional ALPS parameters
exec="cp2k.psmp"

#--------------------------------------------------------------------
#---------------------DO NOT TOUCH-----------------------------------
#Compute and set  stuff, do not change
nodes=$SLURM_NNODES
#puhti has 2 x 20 cores
cores_per_node=40
total_units=$(echo $nodes $cores_per_node $ht | gawk '{print $1*$2*$3}')
units_per_node=$(echo $cores_per_node $ht | gawk '{print $1*$2}')
tasks=$(echo $total_units $t  | gawk '{print $1/$2}')
tasks_per_node=$(echo $units_per_node $t  | gawk '{print $1/$2}')
export OMP_NUM_THREADS=$t
#---------------------DO NOT TOUCH-----------------------------------
#-------------------------------------------------------------------

# Launch the OpenMP job to the allocated compute node
echo "Running $exec on $tasks mpi tasks, with $t threads per task on $nodes nodes ($ht threads per physical core)"

srun -n $tasks -N $tasks_per_node -d $OMP_NUM_THREADS -j $ht $alps_param $exec ${input}.inp > ${input}.out
```

**Example batch script for Taito**

```
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH -J cp2k
#SBATCH --ntasks-per-node=24
#SBATCH --nodes=4
#SBATCH --partition=parallel

module load cp2k-env
export CP2K_DATA_DIR=/appl/chem/cp2k/data

# 4 * 24 = 96 cores

srun cp2k.popt H2O-64.inp > H2O-64.out
```

## References

CP2K prints out a list of relevant publications towards the end of the
log file. Choose and cite the ones relevant to the methods you've used.

## More Information

* CP2K online manual: <http://manual.cp2k.org/>
* CP2K home page: <http://www.cp2k.org/>
