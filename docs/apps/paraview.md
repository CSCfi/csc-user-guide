---
tags:
  - Free
system:
  - www-puhti
  - www-lumi
---

# ParaView

ParaView is an open source, powerful software for scientific visualization. Under the hood, it uses the VTK library, in Python wrapping. We recommend the [HPC web interface remote desktops](../computing/webinterface/desktop.md) for interactive use.

!!! info "Running ParaView with GPU-accelerated graphics on Puhti and LUMI"
    You can now also enable [interactive visualization with GPU acceleration](../computing/webinterface/accelerated-visualization.md) for better
    performance. In this case, select _Accelerated visualization_ instead of _Desktop_
    in the Puhti web interface. On LUMI, select the _Desktop_ app and `lumid`
    partition ([more information](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/)).

ParaView is designed to run parallel tasks and consists of one client and one or several servers (pvservers). There are many ways to run ParaView to suit different needs.

## License

ParaView uses a [permissive BSD license](https://www.paraview.org/paraview-license/) that enables the broadest possible audience, including commercial organizations, to use the software, royalty free, for most purposes.

## Available

* Puhti: 5.10.1
* Mahti: 5.10.1
* LUMI: 5.8.0

## Usage

### Standalone mode

The most straightforward way to use ParaView is to run it in standalone mode. This mode is sufficient for basic visualization tasks and is a good starting point also for more complex tasks.

Standalone ParaView needs no pvserver reservation. **Note that ParaView should not be run on the login node**. You can use `sinteractive -i` command to reserve one CPU and up to 16 GB memory for your interactive session. When resources become available, the session is directed to a compute node. Load the module and start ParaView:

```bash
module purge
module load paraview/5.10.1-paraview
paraview
```

If you need more resources, use `srun` and give session parameters as a one-liner. The following reserves 32 GB memory for one CPU, for one hour:

```bash
srun --partition=small --time=01:00:00 --mem=32G --account=<project> --x11=first --pty bash
```

When directed to a compute node, load the module and start ParaView, as shown in the example above.

If your model has complex geometry, interaction becomes slow and lag in screen updates is noticeable. ParaView has a tick box option to use OSPRay renderer for faster screen re-draws. Note that switching between the default and OSPRay rendering modes can be slow. Even when using one CPU, OSPRay rendering is much faster.

OSPRay is capable of using more than one CPU as threads to further accelerate screen updates. Threads are reserved with `--cpus-per-task`. The following example reserves 5 threads for rendering, and uses in total 32 GB of memory distributed between the CPUs. Note that most other functions of ParaView are not threaded, so they still use only one CPU.

```bash
srun --ntasks=1 --cpus-per-task=5 --partition=small --time=01:00:00 --mem=32G --account=<project> --x11=first --pty bash
```

As previously shown, once directed to a compute node, load the module and start ParaView.  

### Parallel mode - client using several servers (pvservers) and threads

For demanding jobs, ParaView can be run in parallel mode: one client and many pvservers, each running on separate CPUs. The client connects to one of the pvservers, which communicates with the rest of the pvservers.  

Note that if most of the work is done by only one pvserver, using a parallel setup can actually make ParaView run slower, due to extra time taken to parse data from different CPUs. You can check how much each pvserver is being used by opening *Memory Inspector* window in ParaView (file menu: *View/Memory Inspector*). ParaView's *D3*-filter can be used to distribute work more evenly between the cores.  

The example script `para5101-multi.sh` below starts several pvservers and one client (front-end), and connects them. After copying the script, check that it has the necessary execute permission - use `chmod u+x` to grant it. The script needs no editing. Resources should be reserved via `salloc` command. Reservation is for the client and the pvservers combined. `--ntasks` is the number of pvservers plus one client, and `--cpus-per-task` is the number of threads for each of these tasks, so the number of CPUs reserved is `--ntasks` * `cpus-per-task`. `--mem` is the combined memory used by all. The script reserves one GB memory for the client, and the rest is divided between the pvservers.

The `salloc` example below allocates resources for one client and nine pvservers, each with two threads, so 20 CPUs are reserved. Nine GB memory in total is allocated for the pvservers, and one GB for the client. ParaView's OSPRay renderer uses threads, while most of the other ParaView functions benefit more of pvservers. **Note that all these `salloc` parameters need to be explicitly given,** otherwise the script `para581-multi.sh` will not work  

```bash
salloc --nodes=1 --ntasks=10 --cpus-per-task=2 --mem=10G --time=01:00:00 --partition=small --account=<project> para5101-multi.sh
```

While the client connects to the servers, you may get a few warnings (*connect failed, retrying*) which you can ignore. However, if the last message was *Creating default builtin connection*, connection did eventually fail, and the client is operating without any pvservers. If this happens, check that you have included all the necessary job parameters in your `salloc` command.  

#### Example script

```bash title="para5101-multi.sh"
#!/bin/bash 
######################################################
### This script starts paraview servers and client ###
### and connects them using a unique random port.  ###
### Run the script via salloc. All job parameters  ###
### are copied from the salloc command, no editing ###
### of this script is needed.                      ###
######################################################
export SLURM_EXACT=1
export XDG_RUNTIME_DIR=$HOME
export KNOB_MAX_WORKER_THREADS=$SLURM_CPUS_PER_TASK
export LP_NUM_THREADS=$SLURM_CPUS_PER_TASK
MACHINEFILE="nodes.${SLURM_JOB_ID}"
scontrol show hostnames ${SLURM_JOB_NODELIST} > $MACHINEFILE
FIRSTNODE=$(head -n 1 ${MACHINEFILE})
MYPORT=`comm -23 <(seq 22200 22299 | sort) <(ss -Htan | awk '{print $4}' | cut -d':' -f2 | sort -u) | shuf | head -n 1`
SERVER_NTASKS=$(( ${SLURM_NTASKS}-1 ))
SERVER_MEMORY=$(( ${SLURM_MEM_PER_NODE}-1000 ))
module purge
module load paraview/5.10.1-pvserverosmesa
srun --nodes=1 --ntasks=$SERVER_NTASKS --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=$SERVER_MEMORY pvserver --server-port=$MYPORT &
srun --nodes=1 --ntasks=1 --cpus-per-task=$SLURM_CPUS_PER_TASK --mem=1000 --x11=first /appl/opt/vis/paraview/paraview-5.10.1-mesa-client/bin/paraview --server-url=cs://$FIRSTNODE.bullx:$MYPORT &
wait
```

## More Information

* [ParaView homepage](http://www.paraview.org/)
* [ParaView documentation and guide](http://www.paraview.org/documentation/)
* [ParaView Wiki](http://paraview.org/Wiki/ParaView)
* [ParaView Tutorial](http://www.paraview.org/Wiki/The_ParaView_Tutorial)
* [Search the ParaView users mailing list](http://discourse.paraview.org)
