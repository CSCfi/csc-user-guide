# Computing environment 

## Puhti web interface beta updated to release 4 30.11.2021 

* Can now use custom python environments for Jupyter notebooks, see [Jupyter documentation](../../../computing/webinterface/jupyter/).
* Added new **Compute node shell** app that gives a persistent shell on a compute node for commands that should not be run on login nodes.
* App cards show more information  about resource usage after job has finished (seff output)
* Can reset interactive forms to default settings
* Rclone app now alerts about missing Allas authentication
* Added terminal outside container to Desktop app
* Quota and BU warnings can now be hidden
* Open onDemand version updated to 2.0.19


## Puhti web interface beta updated to release 3 9.11.2021

* App cards show more information about resources and reason for shutting down the app to help troubleshoot issues.
* Various app improvements, especially Rclone.
* Increased timeouts for launching apps.
* Login fails now show an error message.

## Puhti web interface beta (release 2) is available 18.10.2021

An easy-to-use web interface for Puhti is now open for beta test use at <https://www.puhti.csc.fi>. The new user interface offers an easy way for new users to use Puhti, and for experienced users it makes access to some features quicker and easier. See [web interface](../../../computing/webinterface/) for details

## MPICH modules no longer work 4.5.2021 

As a consequence of the major network stack update done on Puhti during the service break, the MPICH installations on Puhti no longer work correctly and can not be easily fixed. Old versions of MPICH were installed as a last-resort option and they were using a communication library that has now been deprecated by the vendor. We advice you to recompile your software using either hpcx-mpi or intel-mpi. Please let us know if for some reason you can not at all work with either of the above mentioned mpi libraries.

MPICH version 3.4 with UCX support is going to be installed on Puhti later, but this will take some time.

## Slurm update and srun & behavior 4.5.2021

Running `srun prog &` on Puhti  will produce errors like  "step creation still disabled, retrying (Requested nodes are busy)" if `SLURM_EXACT=1` or `SLURM_OVERLAP=1` is not set. See <https://slurm.schedmd.com/srun.html> for details

