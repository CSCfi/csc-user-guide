# Specific instructions for the LUMI Helmi partition


The LUMI Helmi partition is currently only available for FiQCI users in projects that have been granted access. In addition to running jobs on Helmia via LUMI, users can also use the general LUMI system and software stack including using simulators. 



## LUMI Helmi projects vs. regular LUMI projects

When applying for a new project in MyCSC for the Helmi partition, under "Select LUMI **access mode**", select the "Quantum" option. 

<!-- Maybe insert image here? -->

!!! failure "Pilot Phase"
	During the pilot phase, approved projects will **only** get 24 hours of access to the LUMI Partition.
	[More details about the Pilot Phase](../lumi-helmi-pilot-phase). 

* [Creating a new project in MyCSC](../how-to-create-new-project)
* [How to create Finnish LUMI projects](../how-to-create-new-project/#how-to-create-finnish-lumi-projects)


<!-- ===
* Can a Quantum project use the Helmi partition AND LUMI-C partition for example?
* What about other LUMI Partitions? E.g they want to use Jupyter-notebook LUMI-D?
* Integration with Kvasi or just mention Kvasi?  -->



## LUMI Helmi partition

The LUMI Helmi partition consists of a single LUMI-C node with 128 CPU cores and 256 GiB of memory that is directly connected to Helmi for submitting jobs through. [This is described in more detail on the LUMI-C page](https://docs.lumi-supercomputer.eu/computing/systems/lumic/). 
<!-- 
* Can this node make use of Classical HPC pre processing or just for submitting jobs to Helmi?  -->

There is one queue in the Helmi partition corresponding to FiQCI projects: `q_fiqci`. Currently the maximum job size for the queue is 1 node or 128 CPU cores with a maximum run time of 15 minutes. 

!!! failure "Pilot Phase"
	LUMI Helmi users will only have access to the **q_fiqci** partition. For regular LUMI-C queues a separate project will have to be made. 
	[More details about the Pilot Phase](../lumi-helmi-pilot-phase). 



<!-- The debug, small and largemem partitions are available for allocation by resources. This means that you can request a sub-node allocation: you can request only part of the resources (cores and memory) available on the compute node. This also means that your job may share the node with other jobs. -->


| Name     | Max walltime | Max jobs          | Max resources/job  |
| -------- | ------------ | ----------------- | ------------------ |
| _q_fiqci_| _15 mins_    |   _1_             | _1 node_           |


LUMI Helmi users can also apply to have [access to Kvasi](../../computing/kvasi/) the Quantum Learning Machine and [access to Mahti](../../computing/mahti/) as a separate project to use as a simulation and testing environment. 

<!-- Currently this is accessible directly through direct connection to Kvasi, however, this will soon be integrated with LUMI.  -->

## Storage areas

The Helmi partition uses the same storage policies as LUMI. There is no difference. 

|                       | Quota | Max files | Expandable   | Backup | Retention        |
|:---------------------:|-------|-----------|:------------:|--------|------------------|
| User<br>Home          | 20 GB | 100k      | No           | Yes    | User lifetime    |
| Project<br>Persistent | 50 GB | 100k      | Yes<br>500GB | No     | Project lifetime |
| Project<br>Scratch    | 50 TB | 2000k     | Yes<br>500TB | No     | 90 days          |

* Your home directory (`$HOME`) that can contain up to 20 GB of data. It is intended to store user configuration files and personal data. The user home directory is purged once the user account expire.
* Your project persistent storage is used to share data amongst the members of a project and is located at `/project/project_<project-number>`. The project persistent directory is purged once the project expires.
* Your project scratch is intended as temporary storage for input, output or checkpoint data of your application. 
* Scratch automatic cleaning is not currently active. Please remove the files that are no longer needed by your project on a regular basis if you don't want to run out of TB-hours.

<!-- * Is there going to be a global quota? Add here if yes
* Cleaning of unsued files policy on LUMI? Add here relevant info
* LUMI-P? -->

## Usage

<!-- * Will helmi users have specific LUMI login nodes? If yes add here -->

LUMI Helmi works similarly to the regular LUMI system, the main difference being that 

1. FiQCI projects use the `--partition=q_fiqci` partition instead of the regular LUMI-C, `--partition=standard` and `--partition=small`


Helmi specific support can be reached either via the regular CSC user support [servicedesk@csc.fi](mailto:servicedesk@csc.fi). LUMI specific support such as connecting or storage is available from the [LUMI user support team (LUST)](https://lumi-supercomputer.eu/user-support/need-help/account/).

## Billing

<!-- On LUMI a project is allocated CPU-core-hours for computing and TB-hours for storage. This is different from Puhti and Mahti where Billing Units (BUs) are used and consist of CPU-core-hours and TB-hours as well as other factors. 

In the standard partition the entire node will always be allocated. In practice, 128 core-hours are billed for every allocated node and per hour even if your job has requested less than 128 cores per node.

For example, 16 nodes for 12 hours: 

```
16 nodes x 12 hours x 128 core-hour = 24576 core-hours
```

In the small partition you are billed per allocated core or if you are 
above a certain threshold per chunk of 2GB of memory. Here is the formula that 
is used for billing:

```
corehours = max(ncore, ceil(mem/2GB)) x time
``` -->

Running through the `q_fiqci` queue will consume QPU seconds for the amount of seconds it takes to run the job on the Helmi QPU. This is in addition to the CPUh which will be billed to the project when the LUMI Helmi Node is reserved. 


For example, 1 node for 1 hour : 

```
1 node x 1 hour x 128 core-hour  = 128 core-hours + 3600 QPU-seconds
```

Currently all class


<!-- BU equation -->

Storage is billed by volume as well as time. The billing units are TB-hours. For the regular scratch file system, 1TB that stays for 1 hour on the filesystem, consumes 1TB-hour.

