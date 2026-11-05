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
parallel. There are several ways to run ParaView on CSC systems, described
below.

[TOC]

## License

ParaView is distributed under the OSI-approved
[BSD 3-clause license](https://www.paraview.org/paraview-license/), which
allows free use, including commercial use.

## Available

* Roihu-CPU: 6.1.1
* Roihu Accelerated Visualization Desktop: 5.13.3
* LUMI web interface, *Desktop* app on the `lumid` partition: 5.9 and 5.11.
  ParaView can also be installed with EasyBuild, see [LUMI](#lumi).

!!! note "Different ParaView versions in different environments"
    The GPU-accelerated ParaView in the Roihu web interface (5.13.3) is older
    than the `paraview` modules on Roihu-CPU (6.1.1). Simple state files
    (`.pvsm`) can be opened in both versions, but a state that uses features
    added after 5.13 may not load in 5.13.3. If a state file does not load,
    rebuild the pipeline in that version, or save it as a Python script with
    *File* > *Save State* and the `.py` file type.

## Usage

### Choosing how to run ParaView

| Use case | Recommended approach |
| -------- | -------------------- |
| Interactive work, most datasets (no GPU acceleration) | [[Desktop](#desktop-cpu) in the Roihu web interface |
| Interactive work with GPU acceleration for larger datasets | [Accelerated visualization](#accelerated-visualization-gpu) in the Roihu web interface |
| Large datasets that need many CPU cores for reading and filtering | [Parallel mode](#parallel-mode-client-with-several-pvservers) with several pvservers |
| X11 Forwarding for small or non-interactive testing | [X11 forwarding from the command line](#x11-forwarding-from-the-command-line) |

### Desktop (CPU)

The [Desktop](../computing/webinterface/desktop.md) app runs on the Roihu CPU
nodes and renders on the CPU. Use it when you need ParaView 6.1.1 or do not
need GPU rendering.

1. Connect to the [Roihu web interface](../computing/webinterface/connecting.md)
   and select the *Desktop* app.
2. Select the `interactive` partition and the cores, memory and time you
   need. A good starting point can be 12 cores for ParaView and 16-24 GiB of memory, but this depends on your dataset complexity and size. The `interactive`
   partition allows up to 32 cores and 64 GiB of
   memory per job at maximum.
   
   If you need more, select the `small` partition (longer
   queueing times are possible). See
   [Available batch job partitions](../computing/running/batch-job-partitions.md).
3. Launch the desktop, open a terminal, and start ParaView:

    ```bash
    module purge
    module load paraview/6.1.1
    paraview
    ```

!!! warning "Do not use the applications menu entry in the Desktop app"
    The *ParaView (Accelerated)* entry in the applications menu works only in
    the [Accelerated visualization](#accelerated-visualization-gpu) app. In the
    Desktop app, start ParaView from a terminal as shown above.

The memory shown in the bottom-right corner of the ParaView window is the
memory of the whole compute node, not the amount reserved for your session.
If your session uses more memory than you reserved, the ParaView process is killed.

### Accelerated visualization (GPU)

The Accelerated visualization app runs ParaView on a Roihu visualization node
with an Nvidia L40 GPU, which gives much faster rendering than pure CPU
visualization.

1. Connect to the [Roihu web interface](../computing/webinterface/connecting.md).
2. Select the [Accelerated visualization](../computing/webinterface/accelerated-visualization.md) desktop
   app and specify the required resources. One GPU is reserved.
3. Click *Launch*. Your job is placed in the queue, and once it has been
   allocated resources, click *Launch Accelerated Visualization*.
4. Launch ParaView from *Applications* > *Visualization* >
   *ParaView (Accelerated)*, or search for it using the *Application Finder*.

![Launching ParaView in Roihu web interface accelerated desktop](../img/paraview_interactive_roihu.png 'Launching ParaView in Roihu web interface accelerated desktop')

Sessions run in the `vizinteractive` partition, which has a maximum
runtime of 12 hours. Each reserved GPU gives access to up to 32 CPU
cores and 183 GiB of memory, see
[the partition details](../computing/running/batch-job-partitions.md#vizinteractive).

### X11 forwarding from the command line

It is also possible to run the ParaView client over X11 forwarding, but this is
usually much slower than the web interface and is therefore discouraged. Log in
with X11 forwarding enabled (`ssh -X <username>@roihu-cpu.csc.fi`) and start an
[interactive session](../computing/running/interactive-usage.md) with at least
12 cores:

```bash
sinteractive --account <project> --cores 12
module purge
module load paraview/6.1.1
paraview
```

Alternatively, start ParaView directly with `srun`, for example in the `small`
partition:

```bash
module purge
module load paraview/6.1.1
srun --partition=small --account=<project> --time=01:00:00 \
     --ntasks=1 --cpus-per-task=12 --mem=24G --x11=first paraview
```

### Accelerated visualization

On Roihu's web interface, you can optionally choose to use the accelerated visualization desktop session to run more computationally
intensive visualization workloads.

The ParaView version available on Roihu's accelerated visualization partition is ParaView 5.13.3.

1. Connect to the [Roihu web interface](../computing/webinterface/connecting.md).
2. Select the [Accelerated Visualization](../computing/webinterface/accelerated-visualization.md)
   app of the web interface and specify the required resources.
3. Click the *Launch* button. Your job is placed in the queue, and once it has
   been allocated resources, click *Launch Accelerated Visualization*.
4. Launch ParaView from *Applications* > *Visualization* > *ParaView (Accelerated)* (or search
   for it using the *Application Finder*). Launching the software may take a
   few seconds, so be patient.

![Launching ParaView in Roihu web interface accelerated desktop](../img/paraview_interactive_roihu.png 'Launching ParaView in Roihu web interface accelerated desktop')

## Improving performance in interactive visualization

### Rendering performance on CPUs

Without a GPU, ParaView renders with Mesa's software OpenGL implementation
(`llvmpipe`), and interaction with complex geometry can be slow. For the
best interactive performance, use the
[Accelerated visualization](#accelerated-visualization-gpu) app. On CPU nodes,
you can alternatively switch to the OSPRay ray tracing mode in ParaView properties:

1. In the *Properties* panel, type `ray` in the *Search* box at the top of the
   panel, or scroll down to the *Rendering Backend* section.
2. Tick *Enable Ray Tracing*.
3. Select the *Back End*:
    * *OSPRay raycaster* is faster and suited for interactive work.
    * *OSPRay pathtracer* gives more realistic lighting and shadows, but is
      slower. Increase *Samples Per Pixel* or *Progressive Passes* for
      smoother images.

!!! note "ANARI rendering is not available on Roihu"
    The *Enable Rendering with ANARI* option in ParaView 6.1.1 does not
    currently work on Roihu. Leave it unticked.

`llvmpipe`, OSPRay and the multithreaded VTK filters can use several
threads. Reserve the cores for your session as shown above. The thread counts
can be set before starting ParaView:

```bash
export LP_NUM_THREADS=$(nproc)       # Mesa llvmpipe rendering threads
export OSPRAY_NUM_THREADS=$(nproc)   # OSPRay ray tracing threads
export VTK_SMP_MAX_THREADS=$(nproc)  # threads for multithreaded VTK filters
paraview
```

Some ParaView filters are multithreaded, but much of the data processing runs
on a single core. To process large data in parallel, use several pvservers as
described below.

## LUMI

ParaView is not preinstalled as a module on LUMI. There are two ways to use it:

* **LUMI web interface (recommended):** start the *Desktop* app of the
  [LUMI web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/)
  on the `lumid` partition, whose nodes have GPUs for visualization, and start
  ParaView from the applications menu. ParaView on LUMI desktop does not work on partitions other than LUMI-D.
* **Your own installation:** the
  [LUMI Software Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/p/ParaView/)
  provides an EasyBuild recipe for installing ParaView as your own module.
  This is meant for users who need a configuration that the web interface
  does not offer. Building takes a long time, and the instructions for
  running it with GPU acceleration are on the same page.

## More Information

* [ParaView homepage](http://www.paraview.org/)
* [ParaView documentation and guide](http://www.paraview.org/documentation/)
* [ParaView Wiki](http://paraview.org/Wiki/ParaView)
* [ParaView Tutorial](http://www.paraview.org/Wiki/The_ParaView_Tutorial)
* [Search the ParaView users mailing list](http://discourse.paraview.org)
