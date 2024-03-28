# Web interfaces for Puhti and Mahti

## Intro

The web interfaces for Puhti and Mahti at [www.puhti.csc.fi](https://www.puhti.csc.fi) and
[www.mahti.csc.fi](https://www.mahti.csc.fi) can be used to access the supercomputers using only a
web browser. A web interface for LUMI is also available at [www.lumi.csc.fi](https://www.lumi.csc.fi)
(see the [LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/webui/) for more details).

**Features available in both the Puhti and Mahti web interfaces:**

- View, download, upload and move files between Allas, the supercomputer and your local computer
- Open a shell on the login node
- Open a persistent shell on a compute node
- View running batch jobs
- View disk quotas and project status
- Launch interactive apps and connect to them directly from the browser:
    - Desktop with apps such as Maestro and VMD
    - Julia-Jupyter
    - Jupyter
    - Jupyter for courses: An interactive Jupyter session specifically for courses
    - MLflow
    - TensorBoard
    - Visual Studio Code

**Apps available in Puhti only:**

- Accelerated visualization with applications:
    - Blender
    - COMSOL
    - ParaView
    - VMD
- RStudio
- MATLAB

Everything still runs directly on the supercomputers, giving you all the resources and power
of a supercomputer, but easily accessible using only a web browser.


## Connecting

Using a web browser, go to [www.puhti.csc.fi](https://www.puhti.csc.fi) or [www.mahti.csc.fi](https://www.mahti.csc.fi). On the landing page, click on "Log in" and select an appropriate authentication provider. When logging in using your CSC user account, select CSC as the authentication provider and use the same username and password you use when connecting with `ssh`.
&nbsp;

![Puhti web interface login page](../../img/ood_login.png)

After successful authentication, you will see the dashboard.
&nbsp;

![Puhti web interface front page](../../img/ood_main.png)

From here you can browse your files on the supercomputer, start a shell, view running jobs or start one of the many available applications. The dashboard also contains some important system information.


## Available features

### Shell

The Shell apps can be used to access the supercomputer via the web interface. You can either open a
connection to the login nodes, or a more persistent shell to the compute nodes. For more details
about these, see the [Shell](shell.md) page.

### Files

The files app can be used to manage your files on the supercomputer, Allas, and IDA. For more
information, check the [File browser](file-browser.md) page.

### Active jobs

Recent and running batch jobs can be viewed using the _Jobs_ section on the top navbar and selecting _Active jobs_. Here you can view the current status of the job and what kind of resources were requested. Deleting a running job will cancel the job. 

In the future it will become possible to submit batch jobs through the web interface, but for now the recommended way is to launch the jobs using `sbatch` from the shell.   


### Interactive apps

Interactive apps are programs that can be launched and run on the compute nodes and provide a web interface.
These are apps such as Jupyter Notebook, RStudio and Visual Studio Code.

If the interactive app does not start or does not work as expected you can delete the session and try to launch the app again.


#### Launching an interactive app

The interactive apps can be found in the navigation bar under _Apps_, or on _My Interactive Sessions_ page.
After selecting an interactive app from the list you will be presented with a form to configure the session.
After submitting the app form, and the Slurm job for the app has finished queuing, the app will be
started and you will be able to connect to the application on the _My Interactive Sessions_ page.

For a list of applications and specific instructions see [apps](apps.md).

#### Partitions and resources

Only some of the partitions on the system are available for use in the web interfaces. Some apps
have a more limited set of partitions available than other apps.

In the Puhti web interface, the `interactive`, `small`, `test`, `gpu` and `gputest` partitions are available.
Selecting the `gpu` or `gputest` partition will allocate a Nvidia V100 GPU.

In the Mahti web interface, the `interactive` and `gpusmall` partitions are available. Selecting the
`gpusmall` partition will allocate a split Nvidia A100 GPU (a100_1g.5g). For more details about the
split GPUs, see the [Mahti partitions page](../running/batch-job-partitions.md#mahti-partitions).

### Project view

Using the project view under the _Tools_ section on the top navbar, you can view 
current disk and project billing unit quotas on the supercomputers. For more information see [Project view](project-view.md).
