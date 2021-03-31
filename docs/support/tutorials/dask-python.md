# Dask tutorial

[Dask](https://dask.org/) is a versatile Python library for scalable analytics. It provides multiple different ways of parallelisation for the most common analytics libraries like NumPy, pandas and scikit-learn. You can also parallelise other Python workflows with Dask.

In this tutorial two different Puhti-tested approaches are explained in detail but be in mind that Dask provides other ways of parallelisation that might suit you better.

## Single-node parallellisation with delayed functions

Delayed functions are useful in parallelising existing code. This approach delays functions calls and creates a graph of the computing process. From the graph Dask can then divide the work tasks to different workers whenever parallel computing is possible.

This way you can utilize one full computing node's worth of CPUs (40 in Puhti)

__batch job file__
```
#!/bin/bash
#SBATCH --job-name=DaskSingleNode
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G
#SBATCH --partition=small

### Load the python-data module
module load python-data

### Run the Dask example
srun python dask_singlenode.py 
```


__simple python script__
```
from dask import delayed
from dask import compute

list_of_delayed_functions = []
datasets =['/data/dataset1','/data/dataset2','/data/dataset3','/data/dataset4']

def processDataset(dataset):
    ### Do something to the dataset 
    results = dataset
    return results

for dataset in datasets:
    list_of_delayed_functions.append(delayed(processDataset)(dataset))

### This starts the execution with the resources available
compute(list_of_delayed_functions)

```

## Multi-node parallellisation with SlurmCluster

To achieve parallellisation over multiple computing nodes, you need to define a different kind of Dask cluster than a local one. A SLURMCluster is a viable option in Puhti as it uses Slurm as its queuing system. The workflow with this approach is that you first submit a master job with little resources and a lot of time, which then submits the worker jobs to the queuing system itself and waits for their results.

__master job batch job file__
```
#!/bin/bash
#SBATCH --job-name=DaskMultinode
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --partition=small

### Load the python-data module
module load python-data

### Run the Dask example. We also give script the project name and number of worker jobs
srun python dask_multinode.py <YOUR-PROJECT> 4
```

__simple python script__
```
import sys
from dask_jobqueue import SLURMCluster
from dask.distributed import Client
from dask import delayed
from dask import compute

### Input arguments
project_name = sys.argv[1]
num_of_worker_jobs = sys.argv[2]

### Create the SLURMCluster and define what resources to ask for each of the worker job. Notice the local_directory
cluster = SLURMCluster(
    queue = "small",
    project = project_name,
    cores = 1,
    memory = "8GB",
    walltime = "00:10:00",
    interface = 'ib0',
    local_directory = "/scratch/<YOUR-PROJECT>/temp"
)

### This launches the cluster (submits the worker jobs)
cluster.scale(number_of_workers)
client = Client(cluster)

list_of_delayed_functions = []
datasets =['/data/dataset1','/data/dataset2','/data/dataset3','/data/dataset4']

def processDataset(dataset):
    ### Do something to the dataset 
    results = dataset
    return results

for dataset in datasets:
    list_of_delayed_functions.append(delayed(processDataset)(dataset))

### This starts the execution with the resources available
compute(list_of_delayed_functions)
```

### References 

- [Dask homepage](https://dask.org/)
- [Dask examples](https://examples.dask.org/)
- [Full examples of Dask used in Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti/05_parallel_dask)