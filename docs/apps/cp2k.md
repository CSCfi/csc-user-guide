# CP2K

Versatile ab initio and classical molecular dynamics. CP2k is suited for large parallel quantum chemistry calculations, in
particular for AIMD.

[TOC]

## Available

* Taito: 4.1, 5.1
* Sisu: 4.1, 5.1, 6.1 (with Plumed)

## License

CP2k is freely available under the GPL license.

## Usage

Check which versions are available:

    module avail cp2k

In your batch script, give:

    module load cp2k

Loading the module points you to the installation directory, which has
example submit commands for different parallelization schemes. Before
each project make sure that your job can utilize all the cores you
request in the batch script!

**Example batch script for Sisu using MPI-only parallelization**

```
#!/bin/bash -l
#SBATCH --time=00:05:00
#SBATCH -J CP2K
#SBATCH --partition=test
#SBATCH --nodes=8

(( ncores = SLURM_NNODES * 24 ))
# this calculates the number of cores based on reserved nodes above (-N flag for Slurm)
export CP2K_DATA_DIR=/appl/chem/cp2k/data

module load cp2k

# 8 nodes, 24 cores per node = 192 processes
# choose parameters carefully

aprun -n $ncores cp2k.popt H2O-32.inp > H2O-32_n${ncores}.out
```

**Example batch script for Sisu using mixed MPI/OpenMP parallelization**

!!! note
    Mixed parallelization speeds up simulations only in few cases. Always
    perform a scaling test for each new system and simulation type.

```
#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH -J CP2K
#SBATCH --partition=test
#SBATCH --nodes=8
#SBATCH --no-requeue

module load cp2k
export CP2K_DATA_DIR=/appl/chem/cp2k/data

input=input_bulk_HFX_3
ht=1                   # no hyperthreading
t=12                   #threads per process, 12 is optimal for big hybrid functional jobs
alps_param="-ss -cc numa_node"  # additional ALPS parameters
exec="cp2k.psmp"

#--------------------------------------------------------------------
#---------------------DO NOT TOUCH-----------------------------------
#Compute and set  stuff, do not change
nodes=$SLURM_NNODES
#sisu has 2 x 12 cores
cores_per_node=24
total_units=$(echo $nodes $cores_per_node $ht | gawk '{print $1*$2*$3}')
units_per_node=$(echo $cores_per_node $ht | gawk '{print $1*$2}')
tasks=$(echo $total_units $t  | gawk '{print $1/$2}')
tasks_per_node=$(echo $units_per_node $t  | gawk '{print $1/$2}')
export OMP_NUM_THREADS=$t
#---------------------DO NOT TOUCH-----------------------------------
#-------------------------------------------------------------------

# Launch the OpenMP job to the allocated compute node
echo "Running $exec on $tasks mpi tasks, with $t threads per task on $nodes nodes ($ht threads per physical core)"

aprun -n $tasks -N $tasks_per_node -d $OMP_NUM_THREADS -j $ht $alps_param $exec ${input}.inp > ${input}.out
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
