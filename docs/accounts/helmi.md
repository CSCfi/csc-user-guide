# Specific instructions for the LUMI Helmi partition


The LUMI Helmi partition is currently only available for FiQCI users in projects that have been granted access. In addition to running jobs on Helmi via LUMI, users can also use the general LUMI system and software stack including using simulators. 



## LUMI Helmi projects vs. regular LUMI projects

When applying for a new project in MyCSC for the Helmi partition, under "Select LUMI **access mode**", select the "Helmi" option. 

<!-- Maybe insert image here? -->

!!! failure "Pilot Phase"
	During the pilot phase, approved projects will **only** get 24 hours of access to the LUMI Partition.
	[More details about the Pilot Phase](../lumi-helmi-pilot-phase/). 

* [Creating a new project in MyCSC](../how-to-create-new-project/)
* [How to create Finnish LUMI projects](../how-to-create-new-project/#how-to-create-finnish-lumi-projects)


<!-- ===
* Can a Quantum project use the Helmi partition AND LUMI-C partition for example?
* What about other LUMI Partitions? E.g they want to use Jupyter-notebook LUMI-D?
* Integration with Kvasi or just mention Kvasi?  -->



## LUMI Helmi partition

The LUMI Helmi partition consists of a single LUMI-C node with 128 CPU cores and 256 GiB of memory that is directly connected to Helmi for submitting jobs through. 


* [Further details on LUMI nodes](https://docs.lumi-supercomputer.eu/computing/systems/lumic/).


There is one queue in the Helmi partition corresponding to FiQCI projects: `q_fiqci`. Currently the maximum job size for the queue is 1 node or 128 CPU cores with a maximum run time of 15 minutes. In addition to `q_fiqci`, users can submit jobs to the regular LUMI-C queues, however this will consume additional CPUh. 


| Name     | Max walltime | Max jobs          | Max resources/job  |
| -------- | ------------ | ----------------- | ------------------ |
| _q_fiqci_| _15 mins_    |   _1_             | _1 node_           |
| standard | 2 days       | 120 (100 running) | 512 nodes          |
| debug    | 30 minutes   |   1 (1 running)   | 4 nodes            |
| small    | 3 days       | 220 (200 running) | 4 nodes            |
| largemem | 1 day        |  30 (20 running)  | 1 nodes            |


LUMI Helmi users can also apply to have [access to Kvasi](../../computing/kvasi/) the Quantum Learning Machine and [access to Mahti](../../computing/systems-mahti/) as a separate project to use as a simulation and testing environment. 

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

## Usage and Billing

<!-- * Will helmi users have specific LUMI login nodes? If yes add here -->

LUMI Helmi works similarly to the regular LUMI system, the main difference being that 

1. FiQCI projects use the `--partition=q_fiqci` partition instead of the regular LUMI-C, `--partition=standard` and `--partition=small`
2. There is only 1 LUMI-C node and the maximum job walltime is **15 mins**
3. Usage is billed in CPUh and QPUs in `q_fiqci`. 

Running through the `q_fiqci` queue will consume QPU seconds for the amount of seconds it takes to run the job on the Helmi QPU. This is in addition to the CPUh which will be billed to the project when the LUMI Helmi Node is reserved. 


For example, 1 node for 1 hour : 

```
1 node x 1 hour x 128 core-hour  = 128 core-hours + 3600 QPU-seconds
```


<!-- BU equation -->

Storage is billed by volume as well as time. The billing units are TB-hours. For the regular scratch file system, 1TB that stays for 1 hour on the filesystem, consumes 1TB-hour.


Helmi specific support can be reached either via the regular CSC user support [servicedesk@csc.fi](mailto:servicedesk@csc.fi). LUMI specific support such as connecting or storage is available from the [LUMI user support team (LUST)](https://lumi-supercomputer.eu/user-support/need-help/account/).