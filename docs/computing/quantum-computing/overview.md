---
search:
  boost: 4
---

!!! warning "NOTE: QPU time tracking"
    Used QPU time does not yet display correctly in MyCSC. The usage is tracked correctly internally
    and we are working on correcting the time visible in MyCSC. See the [viewing QPU usage](./running-quantum-jobs.md/#viewing-qpu-usage-on-lumi) section for instructions on viewing your qpu-usage from the terminal.
    If you have questions you can contact us at
    [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi). 


# Overview

Quantum computers differ from their classical counterparts when it comes to the basic 
computational operators. Before QPUs can be utilized, they require tailor-made programs 
and algorithms. The [Finnish Quantum-Computing Infrastructure](https://fiqci.fi) FiQCI provides access to
quantum computing resources through CSC's service portals.

## Quantum Computers

### Helmi (VTT Q5)

Helmi, the first Finnish quantum computer, is co-developed by VTT and IQM Quantum Computers. It offers a 5-qubit system, enabling users to execute quantum programs and algorithms on a physical quantum device.

Access to Helmi is provided through the LUMI supecomputer environment. Users will need to apply for a quantum computing project on LUMI, which gives access to Helmi through the LUMI job scheduler (SLURM). Applying for a project is done through [MyCSC](../../accounts/how-to-create-new-project.md).


### VTT Q50

Q50 is a 53-qubit quantum computer, also co-developed by VTT and IQM Quantum Computers.

Similar to Helmi, Q50 is accessible through the LUMI supercomputer environment. Users will need to apply for a quantum computing project on LUMI. Upon approval, Q50 can be accessed using the LUMI job scheduler (SLURM).
Refer to the [Open Call](https://fiqci.fi/publications/2025-03-04-Q50-Call-1_2025) publication for detailed instructions on how to apply for a project with Q50 access.


For further reading:

* [A more technical description about the quantum computers](./specs.md).
* [Specific instructions for the fiqci partition](./fiqci-partition.md)
* [Getting started with Helmi/Q50](./access.md)
* [LUMI Documentation page](https://docs.lumi-supercomputer.eu/)


## Simulators

### Qiskit

The LUMI supercomputer now supports the simulation of quantum algorithms with up to 44 qubits using Qiskit, IBM’s open-source quantum computing framework. This capability enables researchers to explore and test large-scale quantum algorithms in preparation for quantum advantage.

For more details, refer to this [blog](https://fiqci.fi/publications/2025-04-01-LUMI-quantum-simulations-qiskit-aer)


