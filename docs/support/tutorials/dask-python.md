# Dask tutorial

[Dask](https://dask.org/) is a versatile Python library for scalable analytics. When using Dask, two main decisions have to be made for running code in Parallel. 

1. **How to make the code parallel?** Dask provides several options, inc [Dask DataFrames](https://docs.dask.org/en/stable/dataframe.html), [Dask Arrays](https://docs.dask.org/en/stable/array.html) and [Dask Delayed](https://docs.dask.org/en/stable/delayed.html). This decision depends on the type of analyzed data and already existing code. Additionally Dask has support for scalable machine learning with [DaskML](https://ml.dask.org/).
2. **How to run the parallel code?** Again Dask supports several options: default local cluster and many different [Distributed Clusters](https://distributed.dask.org/en/stable/) for [Cloud](https://docs.dask.org/en/latest/deploying-cloud.html), [Kubernetes](https://docs.dask.org/en/latest/deploying-kubernetes.html) and [supercomputers](https://docs.dask.org/en/latest/deploying-hpc.html) etc. This depends on available hardware. Changing from one cluster to another is code-wise relatively easy. So when starting with Dask, it is recommended to first use a local cluster and go to more advanced Distributed Clusters after understanding the basics.

In this tutorial we use Delayed functions. Delayed functions are useful in parallelising existing code. This approach delays function calls and creates a graph of the computing process. From the graph, Dask can then divide the work tasks to different workers whenever parallel computing is possible. Two options suitable for supercomputers are provided for running Dask clusters: single node using a local cluster and multiple nodes using SLURMCluster.

Keep in mind that the other ways of code parallelisation might suit better in different use cases. For Dask DataFrames, see [CSC dask-geopandas example](https://github.com/csc-training/geocomputing/edit/master/python/dask_geopandas) and for Dask Arrays [CSC STAC example with Xarray](https://github.com/csc-training/geocomputing/edit/master/python/STAC). 

## Single-node parallellisation with delayed functions and a local cluster

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
```python
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

## Multi-node parallellisation with delayed functions and SLURMCluster

To achieve parallellisation over multiple HPC computing nodes, use SLURMCluster from [Dask-Jobqueue library](https://jobqueue.dask.org/en/latest/).

The workflow with this approach is that you first submit a master job, which then submits further worker SLURM jobs to the queuing system. 
Once at least some worker SLURM jobs have started, the master sets up a Dask cluster with Dask workers. 
It also distributes the work to the workers and waits for their results. Dask workers do the actual computing.
In one worker SLURM job, Dask can have 1 or several workers.

The master SLURM job can have limited resources (1 core, little memory), but it should reserve enough time for all analysis to end, plus potential queuing time for worker SLURM jobs. 

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

### Run the Dask example. We also give script the project name and number of worker SLURM jobs
srun python dask_multinode.py <YOUR-PROJECT>
```

The worker jobs are defined inside the Python file started by master SLURM job, for further details see: [Dask Jobqueue configurations documentation](https://jobqueue.dask.org/en/latest/configuration-setup.html).

* `cores` - How many cores per node to use? In bigger jobs one worker SLURM job should fill the whole HPC node, ie 40 cores in Puhti.
* `processes` - How many Python processes per node to use?
* `memory`- How much memory per node to use? This should be enough for all Dask workers in that node. If unsure, try with cores*6Gb.
* `walltime` - Reserve enough time as one worker may handle several delayed functions, if the number of workers is smaller than the number of delayed functions.

__simple python script__
```python
import sys
from dask_jobqueue import SLURMCluster
from dask.distributed import Client
from dask import delayed
from dask import compute

### Input arguments
project_name = sys.argv[1]

# The number of SLURM worker jobs. Practically, how many nodes you want to use. 
num_of_slurm_worker_jobs = sys.argv[2]

### Create the SLURMCluster and define the resources for each of the SLURM worker jobs. 
### Note, that this is the reservation for ONE SLURM worker job.

cluster = SLURMCluster(
    queue = "small", 
    account = project_name,
    cores = 4,
    processes = 2, 
    memory = "12GB",
    walltime = "01:00:00", 
    interface = 'ib0',
)

### This launches the cluster (submits the worker SLURM jobs)
cluster.scale(num_of_slurm_worker_jobs)
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
When the worker SLURM jobs finish, they will be displayed as CANCELLED on SLURM, which is intended as the master job cancels them.

## Dask with Jupyter 

For better understanding of how Dask splits the computations internally, the computations can be followed from [Dask Dashboard](https://docs.dask.org/en/stable/diagnostics-distributed.html) or [JupyterLab Dask extension](https://github.com/dask/dask-labextension). Dask Dashboard should be available whenever Dask is available, JupyterLab Dask extension requires extra installations (in Puhti it is available in [geoconda](../../apps/geoconda.md) module). 

Both `LocalCluster` and `SLURMCluster` type clusters work. When [starting JupyterLab session](../../computing/webinterface/jupyter.md) in Puhti web interface, pay attention to computing resource reservation: 

* If using `LocalCluster`, reserve computing resources for it, notice the [interactive job](../../computing/running/interactive-usage.md) limits. Bigger resource requests are possible with `small` partition in Puhti. With `LocalCluster` maximum of one HPC node can be used, so 40 cores in Puhti.
* If using `SLURMCluster`, at this phase only master node resources are reserved, 1 core should be enough.

### Dask Dashboard on separate browser tab

* Create new cluster from Python code.
* Open [Dask Dashboard](https://docs.dask.org/en/latest/dashboard.html) in a separate browser tab. The URL is something like this: `https://puhti.csc.fi/rnode/r07c51.bullx/8787/status`. Replace the node name (`r07c51.bullx`), with the node used in your job, visible in URL of your Jupyter page, and the port number (`8787`), given in the printout after cluster is created on Dashboard row.

Info tab does not work in this set-up, but other tabs should work.

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
- [Dask tutorials](https://tutorial.dask.org/index.html)
- [Dask examples](https://examples.dask.org/)
- [Full examples of Dask used in Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti/06_parallel_dask)
- [CECAM, High Throughput Computing with Dask course materials](https://www.cecam.org/workshop-details/1022)
- [ENCCS Dask for scalable analytics lesson](https://enccs.github.io/hpda-python/dask/)
- [NCAR Dask tutorial](https://ncar.github.io/dask-tutorial/README.html)

