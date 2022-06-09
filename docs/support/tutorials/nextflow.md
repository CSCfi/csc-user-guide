# High throughput nextflow workflow using hyperqueue


## Example batch script
```
#!/bin/bash
#SBATCH --partition medium
#SBATCH --account project_2001659 
#SBATCH -N 3
#SBATCH --exclusive
#SBATCH --time=00:10:00


# Load the required modules
module load hyperqueue
module load nextflow


# Create a per job directory
mkdir WRKDIR-$SLURM_JOB_ID
mkdir $PWD/WRKDIR-$SLURM_JOB_ID/.hq-server

# Set the directory which hyperqueue will use 
export HQ_SERVER_DIR=$PWD/WRKDIR-$SLURM_JOB_ID/.hq-server


# Make sure nextflow uses the right executor and
# knows how much it can submit.
echo "executor {
  queueSize = $(( 128*SLURM_NNODES ))
  name = 'hq'
  cpus = $(( 128*SLURM_NNODES )) 
}" >  WRKDIR-$SLURM_JOB_ID/nextflow.config


cp main.nf WRKDIR-$SLURM_JOB_ID
hq server start &
srun --cpu-bind=none --hint=nomultithread --mpi=none -N $SLURM_NNODES -n $SLURM_NNODES -c 128 hq  worker start --cpus=128 &

num_up=$(hq  worker list | grep RUNNING | wc -l)
while true; do

    echo "Checking if workers have started"
    if [[ $num_up -eq $SLURM_NNODES ]];then
        echo "Workers started"
        break
    fi
    echo "$num_up/$SLURM_NNODES workers have started"
    sleep 1
    num_up=$(hq worker list | grep RUNNING | wc -l)

done



cd WRKDIR-$SLURM_JOB_ID
time nextflow -Dnxf.pool.maxThreads=5000 -Dnxf.pool.type=sync run main.nf
hq server stop
```
