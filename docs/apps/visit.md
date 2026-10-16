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

For workloads requiring more performance out of VisIt, GPU-accelerated visualization is also available
on both Roihu and LUMI. On Roihu, select the
[Accelerated Visualization](../computing/webinterface/accelerated-visualization.md)
app instead of *Desktop*. On LUMI, select the *Desktop* app with the `lumid`
partition (see the [LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/)).

[TOC]

## License

VisIt is free also for commercial use and has been released under
[BSD Open Source License](https://github.com/visit-dav/visit/blob/develop/LICENSE)

## Available

* Roihu-CPU: 3.5.0
* Roihu Accelerated Visualization Desktop: 3.3.3
* LUMI: 3.2.2

## Usage

---

### Interactive usage in the web interface

=== "Roihu-CPU"

    Open the Roihu web interface and select **Apps → Desktop**.

    In a Desktop session, open up a terminal and type:

    ```bash
    module load visit/3.5.0
    visit
    ```

    **Parallel use:** To use two parallel engine processes:

    ```bash
    visit -l mpirun -np 2
    ```

    Note that running VisIt with many processors does not necessarily bring speed
    benefits.
    It will depend on VisIt's particular data reader if (and to what extent)
    the data can be distributed between the processors.

=== "Roihu accelerated"

    Select **Apps → Accelerated visualization** in the Roihu web
    interface and launch **VisIt (Accelerated)** from the top left applications menu.

=== "LUMI"

    Open the LUMI web interface and select **Apps → Desktop**.

    Use the `interactive` partition for CPU rendering or `lumid`
    for GPU-accelerated graphics. Launch VisIt from **Apps → Other**.

---

### X11 forwarding

You can also run the VisIt GUI over SSH with X11 forwarding, although the
Roihu Desktop app is recommended for better graphical performance and better responsiveness.
Connect to Roihu-CPU from a computer with an X11 server:

```bash
ssh -X <username>@roihu-cpu.csc.fi
```

Then load VisIt and start it on an allocated compute node:

```bash
module load visit/3.5.0
srun --ntasks=1 --cpus-per-task=2 --mem=4G \
     --time=00:20:00 --partition=interactive \
     --account=<project> --pty visit
```

See the [X11 forwarding instructions](../computing/connecting/ssh-unix.md)
and [interactive usage guide](../computing/running/interactive-usage.md)
for details. Replace `<username>` and `<project>` with your own credentials
and CSC project.

## More Information

* [VisIt homepage (source code, binaries, manuals and tutorials, example data files)](https://visit-dav.github.io/visit-website/)
* [User community website](http://visitusers.org)
