# Using RStudio or Jupyter Notebook in Puhti 

[RStudio](https://www.rstudio.com/) and [Jupyter notebooks](https://jupyter.org/) are convenient options for developing and running R or Python code. 
The R or Python code is run on a compute node within an [interactive session](../../computing/running/interactive-usage.md), but the tools themselves are used via a local web browser.

There are two ways to use RStudio Server or Jupyter Notebook on Puhti.

1. The first (and easiest) option is to use [the Puhti web interface](../../computing/webinterface/index.md).

2. The second option is to create a SSH tunnel from a local PC to a compute node. As compute nodes are inaccessible via the Internet, 
the tunnel needs to go through a login node. This is not possible with Windows PowerShell (it does not support jump servers), and therefore it is 
not suitable for RStudio or Jupyter Notebook in Puhti. 
SSH tunnelling requires that you have [set up SSH keys](../../computing/connecting/ssh-keys.md). 

With Linux, macOS and MobaXterm the SSH tunnelling works by default. PuTTy requires filling in the settings to PuTTy tabs, so it is slower and more complicated, but possible.

## Workflow for using RStudio or Jupyter Notebook in Puhti

**Using the Puhti Web Interface**

* For instructions on this, [see the Puhti web interface documentation.](../../computing/webinterface/index.md)

**Using SSH tunneling**

* Start interactive session
* Load suitable modules and start RStudio or Jupyter Notebook server
* Create SSH tunnel from your PC to Puhti compute node
* Open RStudio or Jupyter Notebook in local web browser

More detailed information on the different steps to launch RStudio or Jupyter Notebook using SSH tunneling is provided in the following. 

## Instructions for SSH tunneling

### 1. Start interactive session
Start an interactive session, for example with `sinteractive -i`. For more options and maximum limits see the [interactive usage page.](../../computing/running/interactive-usage.md)

### 2. Load module and start RStudio or Jupyter Notebook server
In the interactive session run:

**RStudio**
```text
module load r-env
start-rstudio-server
```
This set up works with any [r-env module](../../apps/r-env.md).
It is also possible to launch a multi-threaded RStudio session using `start-rstudio-server-multithread`, if you have specified multiple cores when starting an interactive session. 
Details on using threading with R can be found on the [r-env main page](../../apps/r-env.md#improving-performance-using-threading).

**Jupyter**

Jupyter notebooks can be used with the traditional Jupyter Notebook or the more advanced JupyterLab server.

Jupyter Notebook:

```
module load python-data 
start-jupyter-server
```

JupyterLab:
```
module load python-data 
start-jupyterlab-server
```

It is also possible to use some other pre-installed [Python module](../../apps/python.md) than `python-data`, if it includes Jupyter. You can also use your [own custom Python environment with Jupyter Notebook.](#custom-python-environment-with-jupyter-notebook)

***

This will start the RStudio, Jupyter Notebook or JupyterLab server on the compute node and print out the instructions for next steps. 

Keep this terminal open as long as you are working, to keep the RStudio or Jupyter Notebook server running.

### 3. Create SSH tunnel from your PC to Puhti compute node
* With Linux, MacOS and MobaXterm, open a second SSH terminal on your local machine (do not connect to Puhti yet) and 
run the SSH tunnelling command printed out by the RStudio or Jupyter Notebook start-up script. 
For example `ssh -N -L 8787:localhost:42896 -J john@puhti.csc.fi john@r07c49.bullx`
* With PuTTy see the [SSH tunnelling with PuTTy](#ssh-tunnelling-with-putty) instructions.
* The command does not print out anything specific, unless you get some error, you likely succeeded.

Also keep this terminal open for as long as you are working to have remote access to RStudio.

### 4. Open RStudio or Jupyter Notebook in local web browser 
* Open a web browser on your local machine and copy the URL printed out by the start-up script. For example: `http://localhost:8787/`  
* For RStudio, insert the credentials printed out by the start-up script.

### 5. Close the session
Once you have finished: 

* Exit RStudio or Jupyter Notebook server by entering `Ctrl + C` in the interactive terminal session on Puhti. 
* Close (`exit`) also the interactive session. 
* Close SSH tunnel with `Ctrl + C`.

## Custom Python environment with Jupyter Notebook

If you want to use a custom Conda environment with Jupyter Notebook, the
following workflow could be used (adapted to your situation):

```bash
# Set up PROJAPPL environment variable, where to install your Conda environment. 
# Add your project here
export PROJAPPL=/projappl/project_xxx
# Activate Conda commands
module load bioconda
# Create Conda environment with your packages
# It is important to include the notebook package
conda create --name gromacs-tutorials -c conda-forge -c bioconda gromacs=2020.4 matplotlib nglview notebook numpy requests pandas seaborn  
# Activate the new Conda environment
source activate gromacs-tutorials
# Start Jupyter kernel, you will see a separate kernel with name "gromacs"
python -m ipykernel install --user --name gromacs-tutorials --display-name "gromacs" 
# load one of those packages that have Jupyter
module load python-data
# Launch Jupyter
start-jupyter-server 
```

## SSH tunnelling with PuTTy
Both RStudio and Jupyter Notebook also print out PuTTy instructions that have to be copied to PuTTy settings. The port numbers and compute node name may change from session to session.

```
    PuTTy:
    ssh -N -L 8889:localhost:8889 john@r07c49.bullx
    Set Source (8889) and Destination (localhost:8889) in:
    PuTTy -> Connection -> SSH -> Tunnels
```

1. Set up SSH tunneling to a login node with PuTTy. Add port forwarding in **PuTTy -> Connection -> SSH -> Tunnels** : 
    - Source port: `8889`. 
    - Destination: `localhost:8889` 
    - Keep the type as 'Local'.
    - Click 'Add'.
2. Set up SSH tunneling from login node to compute node in **PuTTy -> Connection -> SSH**: 
    - Remote command: `ssh -N -L 8889:localhost:8889 john@r07c49.bullx`
3: `Open` to start connection.
