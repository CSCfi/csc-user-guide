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

Access to Helmi is only available through the FiQCI partition on LUMI, which provides a direct connection between a [LUMI-C
node](https://docs.lumi-supercomputer.eu/hardware/lumic/) and Helmi.

* [Further details on LUMI nodes](https://docs.lumi-supercomputer.eu/hardware/)

There is one queue in the Helmi partition corresponding to FiQCI projects: `q_fiqci`. 
Currently, the maximum run time of a quantum job is 2 hours.

| Name      | Max walltime | Max jobs |
| --------- | ------------ | -------- |
| _q_fiqci_ | _2 hours_    | _64_      |


## Storage areas

The Helmi partition uses the same storage policies as LUMI. You can find [further details on LUMI Storage here](https://docs.lumi-supercomputer.eu/storage/).

## Usage and Billing

Quantum computing projects work similarly to the regular LUMI system. The main differences are:

1. FiQCI projects use the `--partition=q_fiqci` partition instead of the regular LUMI-C `--partition=standard` and `--partition=small`.
2. The maximum job walltime is **2 hours**.
3. Usage is billed as QPU seconds **QPUs** in `q_fiqci`. 
4. The LUMI-Helmi computing environment has to be loaded separately. See [Running on Helmi](./running-on-helmi.md) for details.

Presently, running through the `q_fiqci` queue will consume QPU seconds for the amount of wall-time spent running in the `q_fiqci` queue.

!!! success "Querying your used QPUs"
    You can check your used QPUs using the `lumi-allocations` tool. 


Helmi-specific support can be reached via the [CSC Service Desk](../../../support/contact.md). Note that presently, user support is limited to technical issues.
