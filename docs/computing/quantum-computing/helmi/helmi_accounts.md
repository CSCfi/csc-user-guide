# Specific instructions for the FiQCI partition on LUMI

The FiQCI partition of LUMI provides access to the Helmi quantum computer. Acces is granted for users belonging to projects that have been granted QPU resources. In addition to running jobs on Helmi via LUMI, users can also use the general LUMI system and software stack including using simulators. 


## LUMI Helmi projects vs. regular LUMI projects

When applying for a new project in MyCSC for accessing the FiQCI QPU partition, under "Select LUMI **access mode**", select the "Development" option. From here fill in the applied **resources** QPUm. You will need to mention "Helmi" in the description of program codes, methods and research objectives. You will also need to read and accept the Helmi General Terms of Use before your project is accepted.

!!! info "Pilot Phase"
	During the pilot phase, approved projects will get 24 hours of access to the FiQCI Partition.
	[More details about the Pilot Phase](../lumi-helmi-pilot-phase/). 

* [Creating a new project in MyCSC](/accounts/how-to-create-new-project/)
* [How to create Finnish LUMI projects](/accounts/how-to-create-new-project/#how-to-create-finnish-lumi-projects)


## The FiQCI partition `q_fiqci`

The FiQCI partition consists of a single LUMI-C node with 128 CPU cores and 256 GiB of memory, directly connected to Helmi. 

* [Further details on LUMI nodes](https://docs.lumi-supercomputer.eu/computing/systems/lumic/)

There is one queue in the Helmi partition corresponding to FiQCI projects: `q_fiqci`. Currently, the maximum run time of a quantum job is 30 minutes.

| Name     | Max walltime | Max jobs          | Max resources/job  |
| -------- | ------------ | ----------------- | ------------------ |
| _q_fiqci_| _30 mins_    |   _1_             | _1 node_           |


## Storage areas

The Helmi partition uses the same storage policies as LUMI.

|                       | Quota | Max files | Expandable   | Backup | Retention        |
|:---------------------:|-------|-----------|:------------:|--------|------------------|
| User<br>Home          | 20 GB | 100k      | No           | Yes    | User lifetime    |
| Project<br>Persistent | 50 GB | 100k      | Yes<br>500GB | No     | Project lifetime |
| Project<br>Scratch    | 50 TB | 2000k     | Yes<br>500TB | No     | 90 days          |

* Your home directory (`$HOME`) that can contain up to 20 GB of data. It is intended to store user configuration files and personal data. The user home directory is purged once the user account expires.
* Your project persistent storage is used to share data amongst the members of a project and is located at `/project/project_<project-number>`. **The project persistent directory is purged once the project expires.**
* Your project scratch is intended as temporary storage for input, output or checkpoint data of your application. Please remove the files that are no longer needed by your project on a regular basis.

## Usage and Billing

Quantum computing projects work similarly to the regular LUMI system. The main differences are:

1. FiQCI projects use the `--partition=q_fiqci` partition instead of the regular LUMI-C `--partition=standard` and `--partition=small`
2. The maximum job walltime is **30 mins**
3. Usage is billed QPUm in `q_fiqci`. 
4. The LUMI-Helmi software stack is loaded through `module use /appl/local/quantum/modulefiles` and `module load helmi_` for Qiskit or Cirq. These can be viewed through `module avail`. 

Presently, running through the `q_fiqci` queue will consume QPU minutes for the amount of wall-time spent running in the `q_fiqci` queue.

Storage is billed by volume as well as time. The billing units are TB-hours. For the regular scratch file system, 1TB that stays for 1 hour on the filesystem, consumes 1TB-hour.


Helmi-specific support can be reached via the [CSC Service Desk](/support/contact/). Note that presently, user support is largely limited to issues related to access.
