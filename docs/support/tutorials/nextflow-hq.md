# High-throughput Nextflow workflow using HyperQueue

The [Slurm executor of Nextflow](https://www.nextflow.io/docs/latest/executor.html#slurm)
is not suitable for large workflows involving tens of thousands of processes on HPC
systems. This is due to the usage of individual jobs/job steps that bloat the Slurm log
and degrade the performance of the batch job scheduler. To maximize throughput and
performance, we recommend the Nextflow workflow tasks to be run using the
[HyperQueue](../../apps/hyperqueue.md) meta-scheduler as the
executor. This page provides an example batch script for this purpose.

!!! Note
    Whenever you're unsure how to run your workflow efficiently, don't hesitate
    to [contact CSC Service Desk](../contact.md).

## Example batch script on Mahti supercomputer

```bash
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --account=project_xxxx   
#SBATCH --nodes=3
#SBATCH --exclusive
#SBATCH --time=00:10:00

# Load the required modules
module load hyperqueue
module load nextflow

# Create a per job directory
wrkdir=$PWD/WRKDIR-$SLURM_JOB_ID
mkdir -p $wrkdir/.hq-server

# Set the directory which hyperqueue will use 
export HQ_SERVER_DIR=$wrkdir/.hq-server

# Make sure nextflow uses the right executor and
# knows how much it can submit.
echo "executor {
  queueSize = $(( 128*SLURM_NNODES ))
  name = 'hq'
  cpus = $(( 128*SLURM_NNODES )) 
}" > $wrkdir/nextflow.config


# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers in the background and wait for them to start
srun --cpu-bind=none --hint=nomultithread --mpi=none -N $SLURM_NNODES -n $SLURM_NNODES  hq worker start --cpus=128 &

hq worker wait "${SLURM_NTASKS}"

# Copy main.nf to the work directory if needed 
cp main.nf $wrkdir

cd $wrkdir

# run the nextflow pipeline here 
nextflow run main.nf ...

# Make sure we exit cleanly once nextflow is done
hq worker stop all
hq server stop
```

Where `main.nf` would be the nextflow script you want to run. Note that this batch script
creates a per job directory and copies the nextflow script there before starting. 

```
$ ls
example_jobscript.sh main.nf 
$ sbatch example_jobscript.sh
Submitted batch job 137
$ ls
example_jobscript.sh main.nf WRKDIR-137
$ ls WRKDIR-137
main.nf work
```

## More information

* [General guidelines for high-throughput computing in CSC's HPC
  environment](../../computing/running/throughput.md)
* [Basic](https://yetulaxman.github.io/Biocontainer/tutorials/nextflow_tutorial.html)
  and [advanced Nextflow tutorials for Puhti](nextflow-puhti.md)
* [Official Nextflow documentation](https://www.nextflow.io/docs/latest/index.html)
* [Official HyperQueue documentation](https://it4innovations.github.io/hyperqueue/stable/)
* [More information on CSC-specific HperQueue documentation](../../apps/hyperqueue.md)
