# Specific instructions for the FiQCI partition on LUMI

The FiQCI partition within LUMI provides access to quantum processing units (QPUs) for users belonging to projects with allocated QPU resources. In addition to executing quantum workloads via LUMI, users can leverage the full LUMI infrastructure, including its software stack and quantum simulators, for development, testing, and hybrid quantum-classical workflows.

!!! info "View status of the quantum computers"
	You can check the status of the connection here: [https://fiqci.fi/status](https://fiqci.fi/status)


## LUMI Quantum Computing projects vs. regular LUMI projects

Quantum computing projects are slightly different from standard LUMI projects. The main difference is, that you need to apply for quantum resources in addition to CPU, GPU, and storage.
More information about applying for quantum computing projects can be found from [here](./projects.md).

## The FiQCI partition `q_fiqci`

The `q_fiqci` partition on LUMI is dedicated to quantum computing workloads. It provides a direct connection between a [LUMI-C
node](https://docs.lumi-supercomputer.eu/hardware/lumic/) and the FiQCI quantum computers.

* [Further details on LUMI nodes](https://docs.lumi-supercomputer.eu/hardware/)

There is one queue in the LUMI partition corresponding to FiQCI projects: `q_fiqci`. 
Currently, the maximum run time of a quantum job is 2 hours.

| Name      | Max walltime | Max jobs |
| --------- | ------------ | -------- |
| _q_fiqci_ | _2 hours_    | _64_      |


## Storage areas

The `q_fiqci` partition uses the same storage policies as LUMI. You can find [further details on LUMI Storage here](https://docs.lumi-supercomputer.eu/storage/).

## Usage and Billing

Quantum computing projects work similarly to the regular LUMI system. The main differences are:

1. The dedicated quantum computing partition of LUMI is `q_fiqci`.
2. The maximum job walltime is **2 hours**.
3. Usage is billed as QPU seconds **QPUs**.
4. The LUMI-Fiqci computing environment has to be loaded separately. See [Running on quantum jobs](./running-quantum-jobs.md) for details.


Support can be reached via the [CSC Service Desk](../../support/contact.md) for LUMI related issues or at [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi) for FiQCI and quantum computing services related issues.
