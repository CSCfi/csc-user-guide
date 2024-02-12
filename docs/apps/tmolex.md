---
tags:
  - Academic
---

# TmoleX

TmoleX is an easy to use graphical user interface to handle
[TURBOMOLE](turbomole.md) calculations. TmoleX includes a structure builder
and tools for preparing [TURBOMOLE](turbomole.md) jobs and analyzing results.
TmoleX can also be used to submit and supervise [TURBOMOLE](turbomole.md) jobs
on CSC's supercomputers.
  
The free TmoleX Client version can be used from your local Windows, Linux, or
MacOS desktop to run [TURBOMOLE](turbomole.md) at CSC.

## Available

- Can be freely downloaded (requires registration) from the
  [Dassault Systèmes website](https://discover.3ds.com/free-download-biovia-turbomole-demo-version).
  This is a demo version that also includes a restricted version of TURBOMOLE.

## License

TmoleX can be downloaded freely, but the use of [TURBOMOLE](turbomole.md)
itself is restricted to non-profit research purposes by users affiliated with
academic (i.e. degree-granting) institutes.

## Usage

### Use via your browser

Go to [puhti.csc.fi](https://puhti.csc.fi/) using a web browser and login using
your CSC/Haka user account.

1. From there [launch a Desktop](../../computing/webinterface/desktop/#launching). 
2. Open a `Terminal` and load the TURBOMOLE module `module load turbomole/7.8`.
3. Start TmoleX with the command `TmoleX24`.
4. Select `New Project` and define a suitable project in the `File Name` slot
   (e.g. `/scratch/<yourproject>/my_tmolex_project`).
5. Define your system and type of calculation. 
6. Small jobs can be run interactively: Start Job -> Run (local)
7. Larger jobs should be run as batch jobs: Start Job -> Run (network). Example
   settings are given below. Note that passwordless connection doesn't work via
   the browser. Remember to save the settings using `Save Machine`.
 
### Install your own TmoleX

Install the TmoleX client on your local workstation. For details, see the
registration and download page at
[Dassault Systèmes website](https://discover.3ds.com/free-download-biovia-turbomole-demo-version).
With your version of TmoleX you can build your actual job locally and then
submit the job to Puhti. With the client you can monitor how the job proceeds.
When the job has completed you can retrieve the output and use your local
client to analyze the results.

Below are some example queue settings that can be used in TmoleX:

![Slurm settings](../img/tmolex_remote_settings.png)

Where the complete script to be inserted in the field "Script before job
execution" contains something like (modify according to your actual needs):

```bash
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4             # MPI tasks per node
#SBATCH --account=project_XXXXXX        # insert here the project to be billed 
#SBATCH --time=00:10:00                 # time as `hh:mm:ss`
source /appl/profile/zz-csc-env.sh
ulimit -s unlimited
export PARA_ARCH=MPI                    # use MPI
module load turbomole/7.8
export SLURM_CPU_BIND=none
export PARNODES=$SLURM_NTASKS           # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
```

Remember to save the settings using `Save Machine`. 

## More information

- [TURBOMOLE Documentation & How To](https://www.turbomole.org/turbomole/turbomole-documentation)
- [TmoleX tutorial](https://www.turbomole.org/wp-content/uploads/2019/10/Tutorial-tmolex-4-4.pdf)
- [TmoleX tuorial video](https://www.youtube.com/watch?v=EKH_m1IGb20)
