# Specific instructions for the FiQCI partition on LUMI

The FiQCI partition of LUMI provides access to the Helmi quantum computer. Access is granted for users belonging to projects that have been granted QPU resources. In addition to running jobs on Helmi via LUMI, users can also use the general LUMI system and software stack including using simulators. 

!!! info "View status of Helmi"
	You can check the status of the connection here: [https://fiqci.fi/status](https://fiqci.fi/status)


## LUMI Helmi projects vs. regular LUMI projects

Helmi projects are slightly different from standard LUMI projects. The main difference is, that you will
need to apply for quantum resources in addition to CPU, GPU, and storage.

!!! info "Pilot Phase"
	During the pilot phase, approved projects will get 24 hours of access to the FiQCI Partition.
	[See the Call text for details](https://fiqci.fi/_posts/2022-11-01-Helmi-pilot/). 

## The FiQCI partition `q_fiqci`

Access to Helmi is only available through the FiQCI partition on LUMI, which provides a direct connection between a LUMI-C
node (with 128 cores and 256 GB RAM) and Helmi.

* [Further details on LUMI nodes](https://docs.lumi-supercomputer.eu/hardware/)

There is one queue in the Helmi partition corresponding to FiQCI projects: `q_fiqci`. 
Currently, the maximum run time of a quantum job is 15 minutes.

| Name      | Max walltime | Max jobs | Max resources/job |
| --------- | ------------ | -------- | ----------------- |
| _q_fiqci_ | _15 mins_    | _1_      | _1 node_          |


## Storage areas

The Helmi partition uses the same storage policies as LUMI.

|                       | Quota | Max files |  Expandable  | Backup | Retention        |
| :-------------------: | ----- | --------- | :----------: | ------ | ---------------- |
|     User<br>Home      | 20 GB | 100k      |      No      | Yes    | User lifetime    |
| Project<br>Persistent | 50 GB | 100k      | Yes<br>500GB | No     | Project lifetime |
|  Project<br>Scratch   | 50 TB | 2000k     | Yes<br>500TB | No     | 90 days          |

* Your home directory (`$HOME`) that can contain up to 20 GB of data. It is intended to store user configuration files and personal data. The user home directory is purged once the user account expires.
* Your project persistent storage is used to share data amongst the members of a project and is located at `/project/project_<project-number>`. **The project persistent directory is purged once the project expires.**
* Your project scratch is intended as temporary storage for input, output or checkpoint data of your application. Please remove the files that are no longer needed by your project on a regular basis.

* [Further details on LUMI Storage](https://docs.lumi-supercomputer.eu/storage/)

## Usage and Billing

Quantum computing projects work similarly to the regular LUMI system. The main differences are:

1. FiQCI projects use the `--partition=q_fiqci` partition instead of the regular LUMI-C `--partition=standard` and `--partition=small`.
2. The maximum job walltime is **15 mins**.
3. Usage is billed as QPU seconds **QPUs** in `q_fiqci`. 
4. The LUMI-Helmi computing environment has to be loaded separately. See [Running on Helmi](../running-on-helmi/) for details.

Presently, running through the `q_fiqci` queue will consume QPU seconds for the amount of wall-time spent running in the `q_fiqci` queue.

!!! success "Querying your used QPUs"
    You can check your used QPUs using the `lumi-allocations` tool. 

Storage is billed by volume as well as time. The billing units are TB-hours. For the regular scratch file system, 1 TB that stays for 1 hour on the filesystem, consumes 1 TB-hour.

Helmi-specific support can be reached via the [CSC Service Desk](/support/contact/). Note that presently, user support is limited to technical issues.
