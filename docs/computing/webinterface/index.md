# Web interfaces for Puhti and Mahti

## Intro

The web interfaces for Puhti and Mahti at [www.puhti.csc.fi](https://www.puhti.csc.fi) and
[www.mahti.csc.fi](https://www.mahti.csc.fi) can be used to access the supercomputers using only a
web browser.

**Features available in both the Puhti and Mahti web interfaces:**

- View, download and upload files
- Open a shell on the login node
- Open a persistent shell on a compute node
- View running batch jobs
- View disk quotas and project status
- Launch interactive apps and connect to them directly from the browser:
    - Desktop with apps such as Maestro and VMD
    - Julia-Jupyter
    - Jupyter
    - Jupyter for courses: An interactive Jupyter session specifically for courses
    - TensorBoard
    - Visual Studio Code


**Features available in Mahti only:**

- View, download, upload and move files between Allas, Mahti and your local computer


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

The shell apps can be found under Pinned apps or on the top navbar under the _Tools_ section.
There are two different shells.

The _Login node shell_ launches a normal linux shell on one of the login nodes.
Any command that is running when the login shell browser tab is closed will stop.
Note that the same rules apply here as during a normal ssh session.
**Login nodes are only for light pre/postprocessing** (see [Usage policy](/computing/usage-policy)).

The _Compute node shell_ launches a persistent shell on a compute node for heavier commands that should not be run on login nodes.
The persistent shell will keep running even if you close your browser or lose internet connection.


### Files

The file browser can be opened using the _Files_ section on the top navbar (this displays a list of all project disk areas), or using 
the shortcut to the home folder at the bottom of the front page. In the file browser
you can upload/download files, create new files and directories, or open a shell in the current directory. 

!!! note
    Keep the tab with the file browser open while the file transfer is in progress to ensure that it completes successfully.
    Uploaded files will overwrite existing files with the same name without prompting.
    Currently the maximum size for individual file uploads is 10GB

Clicking on a file will open it in view only mode, for more options like editing, renaming and deleting, use the button with three dots next to the filename.   

The file browser comes with a basic text editor. Some important notes on that:

- If no changes have been made, the _save_ button is grayed out.
- There is no _save-as_ feature
- If a read-only file is opened no indication will be given to the user but no changes will be applied

#### Using Allas

In the Mahti web interface, the [Allas object storage service](../../computing/allas) can be
accessed using the file browser.

To configure authentication for Allas it is recommended that you use the _Cloud storage configuration_ app available in the web interface.
Once you open the app, you will be prompted to enter your CSC password.
After you have authenticated using your password, you will be able to create both S3 and Swift connections, also known as remotes, to Allas.
The remotes are only valid for a single project, but you can create remotes for all of your projects.
The created remotes will be visible in the _Files_ dropdown in the navbar and in the file browser.
!!! note
    The Swift and S3 protocols are not fully compatible with each other, particularly with files larger than 5 GB.
    For more details about the differences between the protocols, see [Allas protocols](../../data/Allas/introduction/#protocols).

Additionally, LUMI-O is also supported for use through the file browser and can be configured by
running _allas-conf_ as `allas-conf --lumi`.
After running the command, the web interface server must be restarted, which can be done by clicking
_Restart web server_ in the _Help_ menu in top right section of the navbar.
Once the server has been restarted, the `lumi-o` remote will be available in the _Files_ dropdown
in the navbar and in the file browser.

Configured remotes that are not accessible, for example, due to expired authentication or network
connection issues, are not be visible in the _Files_ dropdown menu.

The file browser works the same way when accessing Allas as it does when accessing the shared
filesystem on Mahti.
Note that uploading large files from your local computer to Allas is currently not recommended due
to technical limitations.

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


### Project view

Using the project view under the _Tools_ section on the top navbar, you can view 
current disk and project billing unit quotas on the supercomputers. For more information see [project-view](project-view.md).
