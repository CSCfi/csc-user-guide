# ParaView

ParaView is an open source, versatile software for scientific visualization. [NoMachine](https://docs.csc.fi/apps/nomachine/) is recommended for smooth interaction. ParaView is available on Puhti.


## Serial use

The simplest way to run ParaView on Puhti is the combined client-server standalone mode. In this mode ParaView uses one and the same CPU for data processing and image rendering. This mode is sufficient for most visualization tasks.

ParaView must not be run on the login node unless in client mode only, as in the last example. Reserve resources for an interactive session on a compute node as in the following example

```
srun --partition=test --time=00:10:00 --mem-per-cpu=2G --account=<project> --x11=first --pty bash
```
Choose the parameters to suit your needs but note that *--pty* parameter must precede *bash*. When the resources become available, your session is directed to a compute node. Load module and start paraview.

```
module load paraview
paraview
```


## ParaView with OSPRay threads

If the model you are working with has heavy geometry, lag in screen updates becomes noticeable. ParaView has a tick box option to use OSPRay renderer for faster screen re-draws. When using ParaView's OSPRay rendering option, more CPUs can be used for rendering. OSPRay is thread based, and the number of threads are determined by the *cpus-per-task* parameter. One thread corresponds to one CPU, so 40 threads are available in one node. The following example reserves 20 threads for rendering, and uses in total 20 GB of memory distributed between the CPU's. Note that all the other functions of ParaView still use one CPU only.

```
srun --partition=test --time=00:10:00 --mem=20G --nodes=1 --ntasks=1 --cpus-per-task=20 --account=<project> --x11=first --pty bash
```


## More Information

* [ParaView homepage](http://www.paraview.org/)
* [ParaView documentation and guide](http://www.paraview.org/documentation/)
* [ParaView Wiki](http://paraview.org/Wiki/ParaView)
* [ParaView Tutorial](http://www.paraview.org/Wiki/The_ParaView_Tutorial)
* [Search the ParaView users mailing list](http://paraview.markmail.org)
