# Using RStudio or Jupyter notebooks in Puhti 

[RStudio](https://www.rstudio.com/) and [Jupyter notebooks](https://jupyter.org/) are convinient ways for developing and running R or Python code. 
The R or Python code is run on compute node within an [interactive session](../../computing/running/interactive-usage.md), but the tools itself are used  via a local web browser. So, there is no
need to use NoMachine.

Using RStudio or Jupyter Notebooks involves creating a SSH tunnel from local PC to compute-node, and as compute nodes are not accessible from internet 
the tunnel needs to go through a login node. This is not possible with Windows PowerShell (it does not support jump servers), and therefore it not is 
not suitable for RStudio or Jupyter notebooks in Puhti. 
SSH tunnelling requires that you have [set up SSH-keys](../../computing/connecting.md#setting-up-ssh-keys). 

* With Linux, macOS and MobaXterm the SSH tunnelling works by default.
* PuTTy requires filling in the settings to PuTTy tabs, so it is a slower and more complicated, but possible.

## The workflow for using RStudio or Jupyter notebooks in Puhti

* Start interactive session
* Load suitable modules and start RStudio or Jupyter notebook server
* Create SSH tunnel from your PC to Puhti compute node
* Open RStudio or Jupyter notebook in local web browser

### 1. Start interactive session
Start interactive session, for example with `sinteractive -i`. For more options and maximum limits see the [interactive usege page.](../../computing/running/interactive-usage.md)

### 2. Load module and start RStudio or Jupyter notebook server
In the interactive session run:

**RStudio**
```text
module load r-env-singularity
start-rstudio-server
```
This set up works with any [r-env-singularity module](../../apps/r-env-singularity.md), but does not work with [r-env-depricated](../../apps/r-env.md) modules.

**Jupyter notebook**
```
module load python-data 
start-jupyter-server
```
Also some other [Python modules](../../apps/python.md) include Jupyter Notebook. You can use also [own custom Python environment with Jupyter Notebook](#custom-python-environment-with-jupyter-notebook)

***

This will start the RStudio or Jupyter notebook server on the compute node and print out the instructions for next steps. 

Keep this terminal open as long as you are working, to keep the RStudio or Jupyter notebook server running.

### 3. Create SSH tunnel from your PC to Puhti compute node
* With Linux, MacOS ja MobaXterm, open a second SSH terminal on your local machine (do not connect to Puhti yet) and 
run the SSH tunnelling command printed out by RStudio or Jupyter Notebooks start-up script. 
For example `ssh -N -L 8787:localhost:42896 -J john@puhti.csc.fi john@r07c49.bullx`
* With Putty see the [SSH tunnelling with PuTTy](#ssh-tunnelling-with-putty) instructions.
* The command does not print out anything specific, unless you get some error, you likely succeeded.

Keep also this terminal open as long as you are working, to have remote access to RStudio.

### 4. Open RStudio or Jupyter notebook in local web browser 
* Open a web browser on your local machine and copy the URL printed out by the start-up script. For example: `http://localhost:8787/`  
* For RStudio, insert the credentials printed out by the start-up script.

### 5. Close the session
Once you have finished: 

* Exit RStudio or Jupyter notebook server by entering `Ctrl + C` in the interactive terminal session on Puhti. 
* Close (`exit`) also the interactive session. 
* Close SSH tunnel with `Ctrl + C`.

## Custom Python environment with Jupyter notebook

If you want to use a custom conda environment with Jupyter notebook, the
following workflow could be used (adapted to your situation):

```bash
# Set up PROJAPPL environment variable, where to install your conda environment. 
# Add your project here
export PROJAPPL=/projappl/project_xxx
# Activate conda commands
module load bioconda
# Create conda environment with your packages
# It is important to include notebook package
conda create --name gromacs-tutorials -c conda-forge -c bioconda gromacs=2020.4 matplotlib nglview notebook numpy requests pandas seaborn  
# Activate the new conda environment
source activate gromacs-tutorials
# Start Jupyter kernel, you will see a separate kernel with name "gromacs"
python -m ipykernel install --user --name gromacs-tutorials --display-name "gromacs" 
# load one of those packages that have jupyter
module load python-data
# Launch jupyter
start-jupyter-server 
```

## SSH tunnelling with PuTTy
Both RStudio and Jupyter Notebooks print out also PuTTy instructions that have to be copied to PuTTy settings. The port numbers and compute node name may change from session to session.

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
2. Set up SSH tunneling from login node to compute node in **Putty -> Connection -> SSH**: 
    - Remote command: `ssh -N -L 8889:localhost:8889 john@r07c49.bullx`
3: `Open` to start connection.
