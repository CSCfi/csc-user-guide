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

### Create the SLURMCluster and define what resources to ask for each of the worker job. 
### Notice the local_directory and python, python path must be adjusted to used module.
### To find out Python path, run: 
### module load xx
### which python

cluster = SLURMCluster(
    queue = "small",
    project = project_name,
    cores = 1,
    memory = "8GB",
    walltime = "00:10:00",
    interface = 'ib0',
    local_directory = "/scratch/<YOUR-PROJECT>/temp",
    python = "/appl/so../cont_conda/python-data-2022-04-ubi8.5/bin/python"
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

## Dask with Jupyter 

For better understanding of how Dask splits the computations internally, the computations can be followed from [Dask Dashboard](https://docs.dask.o../stable/diagnostics-distributed.html) or [JupyterLab Dask extension](https://github.com/dask/dask-labextension). Dask Dashboard should be available whenever Dask is available, JupyterLab Dask extension requires extra installations (in Puhti it is available in [geoconda](../apps/geoconda.md) module). 

Both `LocalCluster` and `SLURMCluster` type clusters work. When [startin JupyterLab session](../computing/webinterface/jupyter.md) in Puhti web interface, pay attention to computing resource reservation: 

* If using `LocalCluster`, reserve computing resources for it, notice the [interactive job](../computing/running/interactive-usage.md) limits. Bigger requests are sent to usual queueing system. Max. 40 cores.
* If using `SLURMCluster`, at this phase only master node resources are reserved, 1 core should be enough.

### Dask Dashboard on separate browser tab

* Create new cluster from Python code.
* Open Dask Dashboard in a separate browser tab. The URL is something like this: `https://puhti.csc.fi/rnode/r07c51.bullx/8787/status`. Replace the node name (`r07c51.bullx`), with the node used in your job, visible in URL of your Jupyter page, and the port number (`8787`), given in the printout after cluster is created on Dashboard row.

Dask Dashboard Info tab does not work in this set-up.

### JupyterLab Dask extension

This currently only works when starting the cluster from the extension (not if the cluster is created within the notebook (e.g. together with the client)): 

1. Click on Dask logo in left sidebar. 
2. Click `+NEW`, which creates a new blue box `LocalCluster` where you can find all information about the newly created cluster.
3. Click `<>`, which will create a new cell at cursor position in currently open notebook with all code needed to connect your notebook to the running cluster via a client.   
4. Adapt your Client as needed, while keeping the address that is suggested by Dask extension.
5. Run that cell to connect your notebook via the client to the running cluster.
6. Find all available dashboards from the extension (orange boxes) and activate the ones you want with a click (draging allows you to dock multiple dashboard tabs side by side).

Please note:

* It may take some time for the dashboards to load and show you any information in the tabs, be patient.
* If you restart the kernel of your notebook, the cluster will stay active but you will need to re-connect it to the notebook the same way as described above.

***
Another option would be to use [Jupyter opened the SSH tunnelling way](rstudio-or-jupyter-notebooks.md) with an extra tunnel for the Jupyter Dashboard port.

## References and further reading

- [Dask homepage](https://dask.org/)
- [Dask examples](https://examples.dask.org/)
- [Full examples of Dask used in Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti/05_parallel_dask)
- [CECAM, High Throughput Computing with Dask course materials](https://www.cecam.org/workshop-details/1022)
- [ENCCS Dask for scalable analytics lesson](https://enccs.github.io/HPDA-Python/dask/)
