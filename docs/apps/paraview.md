# ParaView

ParaView is an open source, powerful software for scientific visualization. Under the hood, it uses VTK library, in python wrapping. [NoMachine](nomachine.md) is recommended for smooth interactive use. ParaView is available on Puhti.

ParaView is designed to run parallel tasks, and consists of one client and one or several servers (pvservers). There are many ways to run ParaView, to suit different needs. The following examples cover most cases.  

## Standalone mode

The most straightforward way to use ParaView is to run it in standalone mode. This mode is sufficient for basic visualization tasks and is a good starting point also for more complex tasks.

Standalone ParaView needs no pvserver reservation. **Note that ParaView should not be run on the login node.** You can use `sinteractive -i` command to reserve one CPU and up to 16 GB memory for your interactive session. When resources become available, the session is directed to a compute node. Load module and start ParaView  
```
module purge
module load paraview/5.8.1-paraview
paraview
```
If you need more resources, use `srun` and give session parameters as a one-liner. The following reserves 32 GB memory for one CPU, for one hour
```
srun --partition=small --time=01:00:00 --mem=32G --account=<project> --x11=first --pty bash
```
When directed to a compute node, load module and start ParaView like in the example above.  

If your model has complex geometry, interaction becomes slow and lag in screen updates is noticeable. ParaView has a tick box option to use OSPRay renderer for faster screen re-draws. (Note that switching between the default and OSPRay rendering modes can be slow.) Even when using one CPU, OSPRay rendering is much faster.

OSPRay is capable of using more than one CPU as threads, to further accelerate screen updates. Threads are reserved as *cpus-per-task*. The following example reserves 5 threads for rendering, and uses in total 32 GB of memory distributed between the CPU's. Note that most other functions of ParaView are not threaded, so they still use only one CPU  
```
srun --ntasks=1 --cpus-per-task=5 --partition=small --time=01:00:00 --mem=32G --account=<project> --x11=first --pty bash
```
As previously, once directed to a compute node, load module and start ParaView.  

## Parallel mode - client using several servers (pvservers) and threads  
For demanding jobs, ParaView can be run in parallel mode: one client and many pvservers, each running on separate CPUs. The client connects to one of the pvservers, which communicates with the rest of the pvservers.  

Note that if most of the work is done by only one pvserver, using parallel setup can actually make ParaView run slower, due to extra time taken to parse data from different CPUs. You can check how much each pvserver is being used by opening *Memory Inspector* window in ParaView (file menu: *View/Memory Inspector*). ParaView's *D3*-filter can be used to distribute work more evenly between the cores.  

The example script *para581-multi.sh*, below, starts several pvservers and one client (front-end), and connects them. (After copying a script, check that is has execute permission - use `chmod u+x` to grant it.) The script needs no editing. Resources should be reserved via `salloc` command. Reservation is for the client and the pvservers combined. *Ntasks* is the number of pvservers plus one client, and *cpus-per-task* is the number of threads for each of these tasks, so the number of CPUs reserved is *ntasks x cpus-per-task*. *Mem* is the combined memory used by all. The script reserves one GB memory for the client, and the rest is divided between the pvservers.  

The `salloc` example below allocates resources for one client and nine pvservers, each with two threads, so 20 CPUs are reserved. Nine GB memory in total is allocated for the pvservers, and one GB for the client. (ParaView's OSPRay renderer uses threads, while most of the other ParaView's functions benefit more of pvservers.) **Note that all these `salloc` parameters need to be explicitly given,** otherwise the script *para581-multi.sh* will not work  
```
salloc --nodes=1 --ntasks=10 --cpus-per-task=2 --mem=10G --time=01:00:00 --partition=small --account=<project> para581-multi.sh
```
While the client connects to the servers, you may get a few warnings *connect failed, retrying*, which you can ignore. However, if the last message was *Creating default builtin connection*, connection did eventually fail, and the client is operating without any pvservers. If this happens, check that you have included all the necessary job parameters in your `salloc` command.  

#### Script *para581-multi.sh*:  
```
#!/bin/bash
######################################################
### This script starts paraview servers and client ###
### and connects them using a unique random port.  ###
### Run the script via salloc. All job parameters  ###
### are copied from the salloc command, no editing ###
### of this script is needed.                      ###
######################################################

export XDG_RUNTIME_DIR=$HOME
export KNOB_MAX_WORKER_THREADS=$SLURM_CPUS_PER_TASK
MACHINEFILE="nodes.${SLURM_JOB_ID}"
scontrol show hostnames ${SLURM_JOB_NODELIST} > $MACHINEFILE
FIRSTNODE=$(head -n 1 ${MACHINEFILE})
MYPORT=`comm -23 <(seq 22200 22299 | sort) <(ss -Htan | awk '{print $4}' | cut -d':' -f2 | sort -u) | shuf | head -n 1`
SERVER_NTASKS=$(( ${SLURM_NTASKS}-1 ))
SERVER_MEMORY=$(( ${SLURM_MEM_PER_NODE}-1000 ))
module purge
module load paraview/5.8.1-pvserverosmesa2
srun --nodes=1 --ntasks=$SERVER_NTASKS --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=$SERVER_MEMORY pvserver --server-port=$MYPORT &
srun --nodes=1 --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=1000 --x11=first /appl/opt/vis/paraview/paraView-5.8.1-client-builddir/bin/paraview --server-url=cs://$FIRSTNODE.bullx:$MYPORT &
wait
```

## ParaView using one graphics card, one pvserver, and many threads  
In cases where OSPRay does not work well enough, run ParaView on a GPU node, and reserve a graphics card for it.  

The script *para581-1GPU.sh* below starts and connects one client and one pvserver, and uses one GPU. (After copying a script, check that is has execute permission - use `chmod u+x` to grant it.) Resources reserved via `salloc` are for the client and the pvserver combined. *Cpus-per-task* is the number of threads. Ten or more threads is recommended. One GB of memory is allocated to the client, the rest goes to the pvserver.  

The following `salloc` command allocates ten threads to the client and ten to the pvserver, so 20 CPUs are reserved. 24 GB memory is allocated to the pvserver, and one GB to the client. **Note that all the parameters below need to be explicitly given,** otherwise the script *para581-1GPU.sh* will not work  
```
salloc --nodes=1 --ntasks=2 --cpus-per-task=10 --mem=25G --time=01:00:00 --partition=gpu --gres=gpu:v100:1 --account=<project> para581-1GPU.sh
```

#### Script *para581-1GPU.sh*:  
```
#!/bin/bash
######################################################
### This script starts ParaView on one GPU.        ###
### Run the script via salloc. All job parameters  ###
### are copied from the salloc command, no editing ###
### of this script is needed.                      ###
######################################################

export __EGL_VENDOR_LIBRARY_DIRS=/appl/opt/vis/paraview/nvidia/glvnd/egl_vendor.d
module purge
module load gcc/8.3.0 intel-mkl/2019.0.4

export LD_LIBRARY_PATH=/appl/opt/vis/paraview/nvidia/nvidia-driver:/appl/opt/vis/ospray/1.8.5-gl/lib64:/appl/opt/vis/ospray/embree-3.6.1.x86_64.linux/lib:/appl/opt/vis/dependencies/VisRTX-0.1.6-install/lib64:/appl/opt/vis/dependencies/nvidia-index-libs-2.4.20200124-linux/lib/:/appl/opt/vis/dependencies/NVIDIA-OptiX-SDK-6.0.0/lib64:/appl/opt/vis/dependencies/mdl-sdk-314800.830/linux-x86-64/lib:/appl/opt/vis/llvm/7.0.1/lib:/appl/opt/vis/dependencies/oidn-1.0.0-install/lib64:$LD_LIBRARY_PATH

MACHINEFILE="nodes.${SLURM_JOB_ID}"
scontrol show hostnames ${SLURM_JOB_NODELIST} > $MACHINEFILE
FIRSTNODE=$(head -n 1 ${MACHINEFILE})
MYPORT=`comm -23 <(seq 22300 22399 | sort) <(ss -Htan | awk '{print $4}' | cut -d':' -f2 | sort -u) | shuf | head -n 1`
SERVER_MEMORY=$(( ${SLURM_MEM_PER_NODE}-1000 ))

export GPU_DEVICE_ORDINAL=`srun -n1 printenv GPU_DEVICE_ORDINAL`
export GALLIUM_DRIVER="swr"
export KNOB_MAX_WORKER_THREADS=$SLURM_CPUS_PER_TASK
export XDG_RUNTIME_DIR=$HOME
echo "gpu_device_ordinal is ${GPU_DEVICE_ORDINAL}"

srun --gres=gpu:v100:1 --nodes=1 --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=$SERVER_MEMORY /appl/opt/vis/paraview/pvserver-5.8.1-EGL/bin/pvserver --egl-device-index=$GPU_DEVICE_ORDINAL --server-port=$MYPORT --disable-xdisplay-test --force-offscreen-rendering &
srun --gres=none --nodes=1 --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=1000 --x11=first /appl/opt/vis/paraview/paraView-5.8.1-client-builddir/bin/paraview --server-url=cs://${FIRSTNODE}.bullx:$MYPORT &
wait
```

## ParaView utilizing a full GPU node. Four pvservers use one GPU and ten CPUs each, client runs on a CPU node  
One full GPU node gets reserved for this job. Batch script *pvserver581-4GPU-node.sh* reserves all resources of a GPU node, starts four pvservers, each using one GPU and ten threads (CPUs), and sends an email message when the resources have been granted. When the pvservers are up and running, submit another script *para581-4GPU-client.sh*, below, to start ParaView client and connect it to the servers. (After copying a script, check that is has execute permission - use `chmod u+x` to grant it.)   

Note that the batch script *pvserver581-4GPU-node.sh* uses a separate configuration script *pvserver581-4GPU.conf*, which needs to be in the same directory.  

Edit the first section of the batch script *pvserver581-4GPU-node.sh* as follows. Set the time needed for the job, fill in your account project, and provide your email address to receive message when the job starts. As an option, without actually submitting the job yet, you can first run the script by using *test-only* parameter, to get an estimate of the queuing time. You can control (delay) the job start time by submitting with *begin* option. The job will not start before the given time. The rest of the script should not be edited.  

Submit the job via `sbatch` command  
```
sbatch pvserver581-4GPU-node.sh
```

#### Script *pvserver581-4GPU-node.sh*:  
```
#!/bin/bash -l
#####################################################
### This batch script runs 4 pvservers on 4 GPUs. ###
### When the job receives resources, start        ###
### ParaView client and connect to the servers.   ###
#####################################################
### Edit the following job parameters: ###
##########################################
# runtime in hours:minutes:seconds
#SBATCH --time=02:00:00
# use gpu partition (or gputest, for max 15 minutes)
#SBATCH --partition=gpu
# fill in your project number (mandatory)
#SBATCH --account=<project>
# remove the extra # and fill in your email address, to receive email when job starts
##SBATCH --mail-user=<email address>
#SBATCH --mail-type=BEGIN
### Optionally, if queues are long, you may want to control when your job starts.
### To activate the SBATCH commands, remove the extra # so that only one remains.
### "Test-only" does not submit a job, but returns an estimate of the queuing time
##SBATCH --test-only
### "Begin" submits the script, but the job will not start before the specified time
##SBATCH --begin=2021-07-28T10:00:00  # format is YYYY-MM-DD[THH:MM[:SS]]
###########################################
### Do not edit the rest of the script. ###
###########################################
#SBATCH --job-name job4GPU
#SBATCH --output=/users/%u/job4GPU_out #do not change this line
#SBATCH --error job4GPU_err_%j
### Job creates its own environment
#SBATCH --export=NONE
### reserve one full node (four GPUs)
#SBATCH --nodes=1
### one node has two sockets
#SBATCH --ntasks-per-socket=2
### 4 pvserver MPI processes (one per GPU)
#SBATCH --ntasks=4
### 10 threads for each MPI process (reserves all 40 CPUs)
#SBATCH --cpus-per-task=10
### reserve all four GPUs
#SBATCH --gres=gpu:v100:4
### reserve all memory
#SBATCH --mem=0

export SLURM_EXPORT_ENV=ALL
export __EGL_VENDOR_LIBRARY_DIRS=/appl/opt/vis/paraview/nvidia/glvnd/egl_vendor.d
export MODULEPATH_ROOT=/appl/spack/modulefiles/linux-rhel7-x86_64
export MODULEPATH=${MODULEPATH_ROOT}/Core:/appl/modulefiles
. /appl/spack/install-tree/gcc-4.8.5/lmod-7.8-tf4lqs/lmod/7.8/init/bash
module purge
module load paraview/5.8.1-pvserverEGL
export VTK_DEFAULT_EGL_DEVICE_INDEX=${GPU_DEVICE_ORDINAL}
export MYPORT=`comm -23 <(seq 22400 22499 | sort) <(ss -Htan | awk '{print $4}' | cut -d':' -f2 | sort -u) | shuf | head -n 1`
srun --multi-prog pvserver581-4GPU.conf
```

#### Configuration file for the above script, copy it to the same directory and name it *pvserver581-4GPU.conf*:  
```
0 bash -c '/appl/opt/vis/paraview/pvserver-5.8.1-EGL-mpi/bin/pvserver --egl-device-index=0 --server-port=$MYPORT'
1 bash -c '/appl/opt/vis/paraview/pvserver-5.8.1-EGL-mpi/bin/pvserver --egl-device-index=1 --server-port=$MYPORT'
2 bash -c '/appl/opt/vis/paraview/pvserver-5.8.1-EGL-mpi/bin/pvserver --egl-device-index=2 --server-port=$MYPORT'
3 bash -c '/appl/opt/vis/paraview/pvserver-5.8.1-EGL-mpi/bin/pvserver --egl-device-index=3 --server-port=$MYPORT'
```

When you receive email about your GPU node job, run the script *para581-4GPU-client.sh* below via `salloc`.  

The `salloc` command example reserves resources and starts ParaView client on a computing node, and connects it to four pvservers. It is assumed that the pvservers were started by the script *pvserver581-4GPU-node.sh* and are already running on a GPU node. Because the client is just a front end to the pvservers, it does not need much resources. Default resources of the `interactive` partition are sufficient, just define the length of your interactive session  
```
salloc --time=02:00:00 --partition=interactive --account=<project> para581-4GPU-client.sh
```
#### Script *para581-4GPU-client.sh*:  
```
#!/bin/bash
############################################################
### This script starts paraview client on a CPU node     ###
### and connects it to pvservers running on a GPU node.  ###
### It is assumed that script pvserver581-4GPU-node.sh   ###
### has been used for the GPU node reservation.          ###
### No editing of this script is needed.                 ###
############################################################

NODENAME=`grep "Accepting connection" ${HOME}/job4GPU_out | awk '{ print $NF }' | cut -d: -f 1`
PORT=`grep "Accepting connection" ${HOME}/job4GPU_out | awk '{ print $NF }' | cut -d: -f 2`
echo "ParaView server is running at node ${NODENAME} and port ${PORT}"
module purge
module load paraview/5.8.1-paraview
srun --x11=first /appl/opt/vis/paraview/paraView-5.8.1-client-builddir/bin/paraview --server-url=cs://${NODENAME}:${PORT}
```

## More Information

* [ParaView homepage](http://www.paraview.org/)
* [ParaView documentation and guide](http://www.paraview.org/documentation/)
* [ParaView Wiki](http://paraview.org/Wiki/ParaView)
* [ParaView Tutorial](http://www.paraview.org/Wiki/The_ParaView_Tutorial)
* [Search the ParaView users mailing list](http://paraview.markmail.org)
