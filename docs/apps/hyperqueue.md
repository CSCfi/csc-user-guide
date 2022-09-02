# Hyperqueue

!!!warning Autoallocation
    The autoallocation feature available in HQ is still under development and buggy, don't use it as 
    it's very likely that the job queue will be filled with idling workers which just waste resources

Hyperqueue (HQ) is a tool for efficient sub-node task scheduling.
So instead of submitting each one of your computational task using sbatch or srun
you can instead allocate a large resource block and then use hyperqueue to submit your tasks. 


## Available

Mahti: 0.11.0 

## Usage 

``
module load hyperqueue
``

Hyperqueue works on a worker,server,client basis. So the server manages connections,
workers are started on compute nodes and execute commands which the client submitted to the server.
So kind of a slurm within slurm, but you have to start the server and workers yourselves.

### Starting the server

Note that the following instructions are assumed to be within a slurm job script where only full nodes are allocated, a full example
can be found at the bottom.

Specify where the hyperqueue server should be placed. All `hq` commands respect this variable
so make sure it's set before you call any `hq` commands. The server location can also be placed
using the command line flag `--server-dir /server/location`

```
export HQ_SERVER_DIR=/server/location
```

If the server directory is not specified it will default to the user home directory. Then
one has to be careful not to mix up separate computations. For simple cases which fit inside one slurm job
we recommend starting one server per job in some job specific directory. 

Start the server
```
hq server start & 
```
Here we place the server in the background so that we can continue


### Starting the workers

Start the workers
```
srun --cpu-bind=none --hint=nomultithread --mpi=none --ntasks-per-node=$SLURM_NNODES -c $SLURM_CPUS_PER_TASK hq worker start --cpus=$SLURM_CPUS_PER_TASK &
```
Again in the background so our script can continue. Hear we launch one worker per node with each worker
getting the full node. If you need HQ to be aware of other resources, e.g memory,local disk or GPUS, see the [Generic resource section](https://it4innovations.github.io/hyperqueue/v0.11.0/jobs/gresources/) in the official documentation.


After this we can start submitting jobs or alternatively wait for all the workers to connect to the server before submission.
This is generally good practice as we can notice issues with the workers early. 

Loop until all worker are online (note no timeout)

```
num_up=$(hq worker list | grep RUNNING | wc -l)
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
```

### Submitting jobs

!!!info Output
    By default hq creates one folder for each job where output is redirected
    You can use the --log,--stdout,--stderr flags to change this behavior.
    Note that it's not possible to direct output from multiple jobs into the same file
    As each submission will clear the file

See `hq submit --help` for full list of options.

`hq submit <hq_submit args> --cpus <n> <COMMAND/executable> <args to program>`

This is a non-blocking command in the same way as `sbatch`. 

Hyperqueue is not limited to running a single execution per submission. 
Using the `--array 1-N` flag we can start a program N times similar to how slurm array jobs work.

`hq submit --array 1-10 --cpus <n> <COMMAND>`. `<COMMAND>` Then has access to the environment variable `HQ_TASK_ID`
which is used to enumerate all the tasks. 

!!!info sbatch-hq
    For very simple submissions where you only want to run each line within a file with identical resources
    you can just use the csc utility tool `sbatch-hq`, and not have to care about hyperqueue. `module load sbatch-hq` 

When we have submitted everything we want, we need to wait for the jobs to finish, this can be done e.g with:

```
echo "WAITING FOR JOBS TO FINISH"
sleep 30
NOT_DONE=$(hq job list --all | grep "RUNNING\|PENDING")
while true; do
    echo "WAITING FOR JOBS TO FINISH "
    if [[ -z "$NOT_DONE" ]];then
        break
    fi
    sleep 30
    NOT_DONE=$(hq job list --all | grep "RUNNING\|PENDING")
done
```

Once we are done running all of our jobs, we shutdown the workers and server so that we don't get a false
error from slurm when the job ends

```bash
hq worker stop all
hq server stop
```

### Full example

```
#SBATCH --partition=medium
#SBATCH --account=<project>
#SBATCH --nodes=4
#SBATCH --cpus-per-task=128
#SBATCH --ntasks-per-node=1
#SBATCH --time=01:00:00

export SLURM_EXACT=1

# Load the required modules
module load hyperqueue

# Set the directory which hyperqueue will use 
export HQ_SERVER_DIR=$PWD/hq-server-$SLURM_JOB_ID
mkdir -p $HQ_SERVER_DIR

echo "STARTING HQ SERVER, log in $HQ_SERVER_DIR/HQ.log"
echo "===================="
hq server start &>> $HQ_SERVER_DIR/HQ.log &
echo "STARTING HQ WORKERS ON $SLURM_NNODES nodes"
echo "===================="
srun --cpu-bind=none --mpi=none hq worker start --cpus=$SLURM_CPUS_PER_TASK &>> $HQ_SERVER_DIR/HQ.log &

num_up=$(hq worker list 2>/dev/null | grep RUNNING | wc -l)
while true; do
    echo "WAITING FOR WORKERS TO START ( $num_up / $SLURM_NNODES )"
    if [[ $num_up -eq $SLURM_NNODES ]];then
        break
    fi
    sleep 1
    num_up=$(hq worker list | grep RUNNING | wc -l)
done


## Here you run your submit commands, workflow managers etc...



echo "WAITING FOR JOBS TO FINISH"                                
sleep 30                                                         
NOT_DONE=$(hq job list --all | grep "RUNNING\|PENDING")          
while true; do                                                   
    echo "WAITING FOR JOBS TO FINISH "                           
    if [[ -z "$NOT_DONE" ]];then                                 
        break                                                    
    fi                                                           
    sleep 30                                                     
    NOT_DONE=$(hq job list --all | grep "RUNNING\|PENDING")      
done                                                             

echo "===================="
echo "DONE"
echo "===================="
echo "SHUTTING DOWN HYPERQUEUE"
echo "===================="
hq worker stop all
hq server stop
```



### With workflow managers

If your workflow manager is using sbatch for each process execution and you have many short processes it's
advisable to switch to hyperqueue to improve throughput and decrease load on the system batch scheduler 


#### Snakemake

Using snakemakes `--cluster` flag we can use `hq submit` instead of `sbatch`

```
snakemake --cluster "hq submit --cpus {threads} .."
```

If you are porting a more complicated workflow from slurm, you can do argument
parsing and transformations programmatically using snakemakes [job properties](https://snakemake.readthedocs.io/en/stable/executing/cluster.html#job-properties)

#### Nextflow 

See a [separate tutorial](../support/tutorials/nextflow-hq.md) for instructions
how to use hyperqueue with nextflow


## More information

!!!info MPI
    Out of the box hyperqueue does not do mpi execution, but it's possible using a combination of the HQ feature "Multinode Tasks" and orterun/hydra/prrte.
    This way one can schedule mpi task at a node-level granularity.

[Full documentation for HQ](https://it4innovations.github.io/hyperqueue/v0.11.0/)
