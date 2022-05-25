# Computing environment 

## Puhti web interface beta updated to release 8 25.5.2022

* A new [Accelerated Visualization app](../../../computing/webinterface/accelerated-visualization/) has been added for running applications with GPU acceleration.
* Improved the main dashboard page layout.
* Improved login page layout.
* Added more visible warnings about home directory quota.
* Added CSC User guides links to all apps.
* Open onDemand version updated to 2.0.24.

## Puhti has been updated with additional local disks

Fast local NVMe disks can be used to speed up single node workloads that do a lot of read and write operations on data sets that fit on the disks. Especially small reads and writes, and operations on a large amount of files is much faster on the local disks than on the parallel file system. Now 48 nodes with 192 GiB of memory, and 12 nodes with 768 GiB of memory have been equipped with local disks that have a size of 1490 GiB. Later in 2022 all the big memory nodes with 1,5TiB of memory will be upgraded with 6 TiB disks. These are in addition to the original 40 CPU nodes and 80 GPU nodes with 3600 GiB NVMes.  See [Puhti technical details](../../../computing/systems-puhti/) for a detailed list of all nodes.



## Mahti operating system updated to RHEL8, 4.5.2022

The operating system of Mahti has been updated from Red Hat Enterprise Linux (RHEL) 7 to RHEL8.

* Pre-installed software and libraries including the documentation have been updated.
* Users should also recompile their own codes for the new OS.
* Some older versions of applications are not available anymore.

Please note that old login nodes (mahti-login1 and mahti-login2) are not available
and new login nodes also have new names, mahti-login11 and mahti-login12.
Also the ssh keys of login nodes have changed and check sums of new keys are:

| SHA256 checksum                             | Key                                |
|---------------------------------------------|------------------------------------|
| WC9Lb5tmKDzUJqsQjaZLvp9T7LTs3aMUYSIy2OCdtgg | ssh_host_ecdsa_key.pub (ECDSA)     |
| tE+1jA4Et1enbbat1V3dMRWlLtJgA8t7ZrkyIkU4ooo | ssh_host_ed25519_key.pub (ED25519) |
| 0CxM3ECpD2LhAnMfHnm3YaXresvHrhW4cevvcPb+HNw | ssh_host_rsa_key.pub (RSA)         |

When logging into mahti.csc.fi for the first time after the RHEL8 upgrade, you will
encounter a warning saying "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!".
This is completely expected, and you do not need to worry about it.
The warning will disappear if you remove mahti.csc.fi from your `known_hosts` file.
You can run the following command: `ssh-keygen -R mahti.csc.fi` or you can remove the
offending line with your favourite text editor. The warning message will print which
line number is the problematic one.

After removing the offending line, log in again as normal, check that the fingerprint that
is offered by the server matches one of the above checksums, and type "yes" to continue
connecting. After this you should be able to connect to mahti.csc.fi normally.

## Puhti web interface beta updated to release 7 23.3.2022

* [Jupyter for courses](../../../computing/webinterface/jupyter-for-courses/) app now supports creating course environments for projects.
* Added Puhti usage graphs to dashboard.
* Added cookie policy and accessibility statement pages.
* Some UI fixes and small bug fixes.
* Open onDemand version updated to 2.0.23.

## Puhti web interface beta updated to release 6 2.2.2022

* Possible to select slurm reservation for applications
* New Jupyter app for courses.
* Open onDemand version updated to 2.0.22.

## Puhti web interface beta updated to release 5

* Added new TensorBoard app for visualizing TensorFlow runs.
* When launching apps, only partitions available for the selected project are visible now.
* Rclone app has been removed.
* Open onDemand version updated to 2.0.20.

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

