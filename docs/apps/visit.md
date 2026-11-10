---
tags:
  - Free
catalog:
  name: VisIt
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

# VisIt

VisIt is an open source, versatile software for scientific visualization.
VisIt is available on Roihu, and we recommend
[the Roihu web interface remote desktop](../computing/webinterface/desktop.md)
for running the GUI.

For workloads requiring more performance out of VisIt, GPU-accelerated
visualization is also available on both Roihu and LUMI. On Roihu, select the
[Accelerated Visualization](../computing/webinterface/accelerated-visualization.md)
app instead of *Desktop*. On LUMI, select the *Desktop* app with the `lumid`
partition (see the
[LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/)).

[TOC]

## Available

* Roihu-CPU: 3.4.1
* Roihu Accelerated Visualization Desktop: 3.3.3
* LUMI: 3.2.2

## License

VisIt is free also for commercial use and has been released under
[BSD Open Source License](https://github.com/visit-dav/visit/blob/develop/LICENSE).

## Usage

### Interactive usage in the web interface

=== "Roihu-CPU"

    Open the Roihu web interface and select **Apps → Desktop**. Reserve at
    least 4 cores and 8 GiB of memory, plus about two to three times the size
    of the data you open.

    In a Desktop session, open a terminal and type:

    ```bash
    module load visit/3.4.1
    visit
    ```

    **Parallel use:** to use four parallel compute engine processes within
    your Desktop session, reserve at least 4 cores and start VisIt with:

    ```bash
    visit -np 4 -l srun -la "--overlap"
    ```

=== "Roihu accelerated"

    Select **Apps → Accelerated visualization** in the Roihu web
    interface and launch **VisIt (Accelerated)** from the top left
    applications menu.

=== "LUMI"

    Open the LUMI web interface and select **Apps → Desktop**.

    Use the `interactive` partition for CPU rendering or `lumid`
    for GPU-accelerated graphics. Launch VisIt from **Apps → Other**.

### X11 forwarding

You can also run the VisIt GUI over SSH with X11 forwarding, although the
Roihu Desktop app is recommended for better graphical performance and
responsiveness. Connect to Roihu-CPU from a computer with an X11 server:

```bash
ssh -X <username>@roihu-cpu.csc.fi
```

Then start an interactive shell on a compute node and run VisIt there:

```bash
srun --account=<project> --partition=interactive --time=01:00:00 \
     --ntasks=4 --mem=8G --x11=first --resv-ports=0 --pty bash
module load visit/3.4.1
visit -np 4 -l srun -la "--overlap"
```

The `--resv-ports=0` option and `-la "--overlap"` are both needed for the
parallel compute engine. Without them, the engine waits for resources that the
interactive shell already holds. For a single engine process, start just
`visit`.

!!! warning "Run the whole of VisIt on compute nodes"
    Do not start VisIt on a login node and launch the compute engine on a
    compute node. Compute nodes cannot connect back to VisIt on the login
    node, so the engine fails with a networking error.

See the [X11 forwarding instructions](../computing/connecting/ssh-unix.md)
and [interactive usage guide](../computing/running/interactive-usage.md)
for details. Replace `<username>` and `<project>` with your own user name and
CSC project.

### Python scripting

VisIt has a Python 3.11 command-line interface with NumPy available. NumPy
also works in Python expressions and queries that run in the compute engine.
To run a script without the GUI:

```bash
module load visit/3.4.1
visit -nowin -cli -s my_script.py
```

!!! note "Rendering images requires a desktop session"
    VisIt on Roihu-CPU can only render images when a display is available.
    Run scripts that save images (`SaveWindow()`) in a terminal of a Desktop
    session or an X11-forwarded interactive session, not in a normal batch
    job. In batch jobs, scripts that only read, process, query or export data
    work. For rendering in batch jobs, consider
    [ParaView's `pvbatch`](paraview.md#batch-jobs-with-pvbatch).

### Supported file formats

VisIt reads a large number of file formats. The Roihu-CPU module includes,
among others, support for Silo, HDF5, NetCDF, ADIOS2, Conduit Blueprint,
MFEM and the VTK formats.

## More information

* [VisIt homepage (source code, binaries, manuals and tutorials, example data files)](https://visit-dav.github.io/visit-website/)
* [VisIt user manual](https://visit-sphinx-github-user-manual.readthedocs.io/)
* [User community website](http://visitusers.org)