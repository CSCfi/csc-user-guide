---
search:
  boost: 4
---

!!! warning "Q20 Service in MyCSC"
    There are currently some issues with the Q20 service for projects that have Q20 allocations. If you cannot find the Aalto-Q20 service or are otherwise experiencing issues please contact the CSC Service Desk at [servicedesk@csc.fi](mailto:servicedesk@csc.fi).


# Overview

Quantum computers differ from their classical counterparts when it comes to the basic 
computational operators. Before QPUs can be utilized, they require tailor-made programs 
and algorithms. The [Finnish Quantum-Computing Infrastructure](https://fiqci.fi) FiQCI provides access to
quantum computing resources through CSC's service portals.

## Quantum Computers

### Aalto Q20

Q20 is a 20 qubit IQM superconducting quantum computer operated by Aalto University.

Access to Q20 is provided through the LUMI supecomputer environment. Users will need to apply for a quantum computing project on LUMI, which gives access to Q20 through the LUMI job scheduler (SLURM). Refer to the [Open Call](https://fiqci.fi/resource-call) publication for detailed instructions on how to apply for a project with Q20 access.

### VTT Q50

Q50 is a 53-qubit quantum computer, also co-developed by VTT and IQM Quantum Computers.

Similar to Q20, Q50 is accessible through the LUMI supercomputer environment. Users will need to apply for a quantum computing project on LUMI. Upon approval, Q50 can be accessed using the LUMI job scheduler (SLURM).
Refer to the [Open Call](https://fiqci.fi/resource-call) publication for detailed instructions on how to apply for a project with Q50 access.


For further reading:

* [A more technical description about the quantum computers](./specs.md).
* [Specific instructions for the fiqci partition](./fiqci-partition.md)
* [Getting started with Q20/Q50](./access.md)
* [LUMI Documentation page](https://docs.lumi-supercomputer.eu/)


## Simulators

### Qiskit

The LUMI supercomputer now supports the simulation of quantum algorithms with up to 44 qubits using Qiskit, IBM’s open-source quantum computing framework. This capability enables researchers to explore and test large-scale quantum algorithms in preparation for quantum advantage.

For more details, refer to this [blog](https://fiqci.fi/publications/2025-04-01-LUMI-quantum-simulations-qiskit-aer)


