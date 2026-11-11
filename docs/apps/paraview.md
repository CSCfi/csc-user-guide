---
tags:
  - Free
catalog:
  name: ParaView
  description: Free open-source visualization application
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - web_interfaces:
        - LUMI
        - Roihu
    - LUMI
    - Roihu
---

# ParaView

ParaView is an open-source application for interactive and batch scientific
visualization and data analysis. It is built on the
[VTK](https://vtk.org/) visualization toolkit and can be scripted with Python
(`pvpython`, `pvbatch`).

ParaView has a client–server architecture. The graphical client can do all the
work itself (*standalone* mode), or it can connect to one or more ParaView
servers (`pvserver` processes) that read, process and render the data in
parallel. There are several ways to run ParaView on CSC supercomputers,
described below.

[TOC]

## Available

* Roihu-CPU: 6.0.1
* Roihu Accelerated Visualization Desktop: 6.0.1, 5.13.3 (deprecated)
* LUMI web interface, *Desktop* app on the `lumid` partition: 5.9 and 5.11.
  ParaView can also be installed with EasyBuild, see [LUMI](#lumi).

!!! note "Deprecated ParaView version on Roihu accelerated"
    The 5.13.3 version of ParaView on Roihu Accelerated Visualization Desktop
    is subject for removal in the near future. Please ensure that your workflows
    and any existing ParaView state files created with this version are compatible
    with and can be opened using ParaView version 6.0.1.

## License

ParaView is distributed under the OSI-approved
[BSD 3-clause license](https://www.paraview.org/paraview-license/), which
allows free use, including commercial use.

## Usage

### Choosing how to run ParaView

| Use case | Recommended approach |
| -------- | -------------------- |
| Interactive work, most datasets (no GPU acceleration) | [Desktop](#desktop-cpu) in the Roihu web interface |
| Interactive work with GPU acceleration for larger datasets | [Accelerated visualization](#accelerated-visualization-gpu) in the Roihu web interface |
| Large datasets that need many CPU cores for reading and filtering | [Parallel mode](#parallel-mode-client-with-several-pvservers) with several pvservers |
| Scripted processing and rendering without a GUI | [Batch jobs with pvbatch](#batch-jobs-with-pvbatch) |
| Quick testing over SSH | [X11 forwarding from the command line](#x11-forwarding-from-the-command-line) |

### Desktop (CPU)

The [Desktop](../computing/webinterface/desktop.md) app runs on the Roihu-CPU compute
nodes and renders on the CPU cores there. Use it when you work with a small or medium sized
dataset where you do not need GPU rendering.

1. Connect to the [Roihu web interface](../computing/webinterface/connecting.md)
   and select the *Desktop* app.
2. Select the `interactive` partition and the cores, memory and time you need.
   A good starting point is 4–8 cores and 8 GiB of memory, plus about two to
   three times the size of the data you open. ParaView and the desktop itself
   need about 2 GiB before any data is loaded,
   so aim to **reserve 4 GiB of memory at the very least**.
   If you need more than `interactive` partition maximum of 32 cores and 64 GiB of
   memory, select the `small` partition (longer queueing times are possible). See
   [Available batch job partitions](../computing/running/batch-job-partitions.md).
3. Launch the desktop, open a terminal, and start ParaView:

    ```bash
    module load paraview/6.0.1
    paraview
    ```

The memory shown in the bottom-right corner of the ParaView window is the
memory of the whole compute node, not the amount reserved for your session.
If your session uses more memory than you reserved, the ParaView process is
killed without warning (the terminal shows `Killed`). Start a new session with
more memory in that case.

### Accelerated visualization (GPU)

The Accelerated visualization app runs ParaView on a Roihu visualization node
with an Nvidia L40 GPU, which gives much faster rendering than pure CPU
visualization. The ParaView version in this app is 6.0.1.

1. Connect to the [Roihu web interface](../computing/webinterface/connecting.md).
2. Select the
   [Accelerated visualization](../computing/webinterface/accelerated-visualization.md)
   desktop app and specify the required resources. One GPU is reserved.
3. Click *Launch*. Your job is placed in the queue, and once it has been
   allocated resources, click *Launch Accelerated Visualization*.
4. Launch ParaView from *Applications* > *Visualization* >
   *ParaView (Accelerated)*, or search for it using the *Application Finder*.
   Starting ParaView may take a few seconds.

![Launching ParaView in Roihu web interface accelerated desktop](../img/paraview_interactive_roihu.png 'Launching ParaView in Roihu web interface accelerated desktop')

Sessions run in the `vizinteractive` partition, which has a maximum
runtime of 12 hours. Each reserved GPU gives access to up to 32 CPU
cores and 183 GiB of memory, see
[the partition details](../computing/running/batch-job-partitions.md#vizinteractive).

### Parallel mode: client with several pvservers

For large datasets, run the ParaView client in a Desktop session and connect it
to a group of `pvserver` processes that read and process the data in parallel.

**Within the Desktop session.** Reserve enough cores for the session (for
example 8), open a second terminal and start the servers inside the same
allocation:

```bash
module load paraview/6.0.1
srun --overlap --ntasks=4 pvserver --server-port=22222
```

Wait for the line `Accepting connection(s): <node>:22222`. In the ParaView
client, select *File* > *Connect* > *Add Server*, enter the node name from that
line (for example `rc5283`) as *Host* and `22222` as *Port*, choose *Startup
Type* `Manual`, save, and click *Connect*. *View* > *Memory Inspector* shows
the server processes.

**On separate compute nodes.** If you need more cores than you have in a Desktop session,
start the servers as a batch job on Roihu-CPU and connect to them from the Desktop session
in the same way. Compute nodes can connect to each other by their host names.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --mem-per-cpu=2G
#SBATCH --time=01:00:00

module load paraview/6.0.1
srun pvserver --server-port=22222
```

The connection line with the node name is written to the job output file
(`slurm-<jobid>.out`).

!!! note
    Ensure that the ParaView client and the server are the same ParaView version.

### Batch jobs with pvbatch

`pvbatch` runs ParaView Python scripts without a GUI and renders off-screen, so
it works in normal batch jobs. It can also run in parallel with MPI, also
across several nodes:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --ntasks=8
#SBATCH --mem-per-cpu=2G
#SBATCH --time=00:30:00

module load paraview/6.0.1
srun pvbatch my_script.py
```

For example, a minimal script that renders an image:

```python
from paraview.simple import *

reader = OpenDataFile("data.vtu")
Show(reader)
Render()
SaveScreenshot("image.png", ImageResolution=[1920, 1080])
```

The easiest way to create a script is to build the pipeline in the GUI and
record it with *Tools* > *Start Trace*, or to save the state as a Python
script.

### X11 forwarding from the command line

It is also possible to run the ParaView client over X11 forwarding, but it is prone to
being choppy and has a high latency and slow responsiveness compared to the web interface
and so it should be seen as a secondary option to a normal Desktop session.
To use X11 forwarding, log in with X11 forwarding enabled (`ssh -X <username>@roihu-cpu.csc.fi`)
and start ParaView on a compute node:

```bash
module load paraview/6.0.1
srun --partition=interactive --account=<project> --time=01:00:00 \
     --ntasks=1 --cpus-per-task=4 --mem=8G --x11=first paraview
```

### Python

`pvpython`, `pvbatch` and the *Python Shell* in the GUI use Python 3.14 with
NumPy, Matplotlib, pandas and mpi4py preinstalled, so the *Programmable
Filter*, the *Python Calculator* and the *Python View* work out of the box.

### Saving images and animations

*File* > *Save Animation* writes image series (PNG, JPEG, TIFF, BMP) or
Ogg/Theora video (`.ogv`). Other video formats such as MP4 are not available
directly. Save a PNG series and convert it with FFmpeg:

```bash
module load ffmpeg
ffmpeg -framerate 24 -i anim.%04d.png -c:v mpeg4 -q:v 2 movie.mp4
```

Replace `anim` with the file name you used when saving the animation.

### Supported file formats

ParaView reads and writes the usual VTK formats (`.vti`, `.vtu`, `.vtp`,
legacy `.vtk`, VTKHDF, `.pvd`), XDMF (`.xmf`), CSV, STL, PLY, Exodus and CGNS,
among others. Readers for ADIOS2, openPMD and Catalyst are not included
in the Roihu-CPU build.

## Improving performance in interactive visualization

Without a GPU, ParaView renders with Mesa's software OpenGL implementation
(`llvmpipe`), and interaction with complex geometry or large datasets can be slow.
For the best interactive performance, use the
[Accelerated visualization](#accelerated-visualization-gpu) app.

`llvmpipe` automatically uses the number cores reserved for your session.

Some ParaView filters can use several threads. This is not enabled by
default; you can try it for large datasets by starting ParaView with:

```bash
export VTK_SMP_BACKEND_IN_USE=STDThread
export VTK_SMP_MAX_THREADS=$SLURM_CPUS_ON_NODE
paraview
```

Much of the data processing still runs on a single core. To process large data
in parallel, use [several pvservers](#parallel-mode-client-with-several-pvservers).

!!! note "Ray tracing is not available on Roihu-CPU"
    The ParaView 6.0.1 module on Roihu-CPU is built without OSPRay and ANARI,
    so the ray tracing options in the *Properties* panel are not available.
    Use [accelerated visualization](#accelerated-visualization-gpu)
    for higher performance.

## LUMI

ParaView is not preinstalled as a module on LUMI. There are two ways to use it:

* **LUMI web interface (recommended):** start the *Desktop* app of the
  [LUMI web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/)
  on the `lumid` partition, whose nodes have GPUs for visualization, and start
  ParaView from the applications menu. ParaView in the LUMI desktop does not
  work on partitions other than `lumid`.
* **Your own installation:** the
  [LUMI Software Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/p/ParaView/)
  provides an EasyBuild recipe for installing ParaView as your own module.
  This is meant for users who need a configuration that the web interface
  does not offer. Building takes a long time, and the instructions for
  running it with GPU acceleration are on the same page.

## More information

* [ParaView homepage](https://www.paraview.org/)
* [ParaView documentation, user guide and tutorials](https://docs.paraview.org/en/latest/)
* [ParaView discourse forum](https://discourse.paraview.org)
