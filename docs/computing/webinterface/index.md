# Web interfaces for Puhti and Mahti

## Intro

The web interfaces for Puhti and Mahti at
[www.puhti.csc.fi](https://www.puhti.csc.fi) and
[www.mahti.csc.fi](https://www.mahti.csc.fi) can be used to access the
supercomputers using only a web browser. A web interface for LUMI is also
available at [www.lumi.csc.fi](https://www.lumi.csc.fi), see the
[LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/webui/) for
more details.

!!! warning "Scope"
    The HPC web interfaces are best suited for **interactive workloads** that
    consume a **modest amount of computational resources**. Some examples are
    **pre- and post-processing of data** in Jupyter Notebooks using
    **at most a few tens of CPU cores**, **small-scale AI/ML experiments**
    using a **single GPU**, and **data visualization** tasks.

    Please note that the interactive applications in the web interfaces are
    **not** suitable for **multi-node** and **multi-GPU jobs**. Such workloads
    should ideally be carried out as standard
    [batch jobs](../running/getting-started.md). If you are new to batch jobs
    and command-line usage of the HPC environment, we recommend the
    [CSC Computing Environment](https://csc-training.github.io/csc-env-eff/)
    self-learning materials to learn how to get the most out of CSC's
    supercomputers.

## Available features

- **Features available in both the Puhti and Mahti web interfaces:**
    - View, download, upload and move files between Allas, the supercomputer
      and your local computer
    - Open a shell on the login node
    - Open a persistent shell on a compute node
    - View running batch jobs
    - View disk quotas and project status
    - Launch interactive apps and connect to them directly from the browser:
        - Desktop with apps such as Maestro and VMD
        - Julia-Jupyter
        - Jupyter
        - Jupyter for courses: An interactive Jupyter session specifically for
          courses
        - MLflow
        - TensorBoard
        - Visual Studio Code
- **Apps available in Puhti only:**
    - Accelerated visualization with applications:
        - Blender
        - COMSOL
        - ParaView
        - VMD
    - RStudio
    - MATLAB

### Shell

The _Shell_ apps can be used to access the command-line of a supercomputer via
the web interface. You can either open a connection to the login nodes, or a
more persistent shell to the compute nodes. For more details, see the
[Shell](shell.md) page.

### File browser

The _Files_ app can be used to manage your files on the supercomputer and
access storage services such as Allas and IDA. For more information, check the
[Files and storage services](file-browser.md) page.

### Active jobs

Recent and running batch jobs can be viewed using the _Jobs_ section in the top
navbar and selecting _Active jobs_. Here you can view the current status of
your jobs and what kind of resources were requested. Deleting a running job
will cancel the job. 

In the future, it may become possible to submit batch jobs through the web
interface, but for now the recommended way to launch standard batch jobs is
using `sbatch` from the shell.

### Project view

Using the _Project view_ under the _Tools_ section in the top navbar, you can
view  current disk and project billing unit quotas on the supercomputers. For
more information, see the [Project view](project-view.md) page.

### Interactive apps

_Interactive apps_ are programs that can be launched and run on the compute
nodes and provide a graphical user interface. These are apps such as Jupyter
Notebook, RStudio and Visual Studio Code. For a full list of applications and
specific instructions, see the [Interactive apps](apps.md) page.

!!! info-label
    If an interactive app does not start, or does not work as expected, you can
    delete the session and try to launch the app again. See also
    [Troubleshooting](apps.md#troubleshooting).

### Partitions and resources

!!! warning-label
    Only a few partitions of Puhti and Mahti are available for use in the web
    interfaces. Some apps also have a more limited set of partitions available
    than others.

In the **Puhti web interface**, the `interactive`, `small`, `test`, `gpu` and
`gputest` partitions are available. Selecting the `gpu` or `gputest` partition
will allocate one Nvidia V100 GPU. See the
[Puhti partitions page](../running/batch-job-partitions.md#puhti-partitions)
for general information about queues on Puhti.

In the **Mahti web interface**, the `interactive` and `gpusmall` partitions are
available. Selecting the `gpusmall` partition will allocate a split Nvidia A100
GPU (a100_1g.5g) with 1/7th of the compute capacity of a full A100. For more
details about the split GPUs on Mahti, see the
[Mahti partitions page](../running/batch-job-partitions.md#mahti-partitions).
