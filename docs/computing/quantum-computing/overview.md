---
search:
  boost: 4
---

# Overview

Quantum computers differ from their classical counterparts when it comes to the basic 
computational operators. Before QPUs can be utilized, they require tailor-made programs 
and algorithms. The [Finnish Quantum-Computing Infrastructure](https://fiqci.fi) FiQCI provides access to
quantum computing resources through CSC's service portals.

## Helmi

**5 Qubit Quantum Computer**

Helmi, the first Finnish quantum computer, is co-developed by VTT and IQM Quantum Computers. Presently, Helmi provides 5 qubits. With Helmi, users can run quantum programs and algorithms on a real, physical device.

Access to Helmi is provided through the LUMI supecomputer environment. Users will need to apply for a quantum computing project on LUMI, which gives access to Helmi through the LUMI job scheduler (SLURM). Applying for a project is done through [MyCSC](../../../accounts/how-to-create-new-project/).

For further reading:

* [A more technical description about Helmi](./helmi/helmi-specs.md).
* [Specific instructions for the LUMI Helmi partition](./helmi/fiqci-partition.md)
* [Getting started with Helmi](./helmi/helmi-from-lumi.md)
* [LUMI Documentation page](https://docs.lumi-supercomputer.eu/)


## Kvasi

**The Quantum Learning Machine**

Kvasi is an advanced quantum computer simulator/emulator. With Kvasi, the user can explore and develop algorithms 
for quantum computers. Read here [detailed instructions on how to access](../quantum-computing/kvasi/kvasi.md)

Kvasi provides an ecosystem for developing and simulating quantum algorithms in both 
ideal and realistic, noisy conditions. With Kvasi, you can optimize your algorithm 
for a specific hardware (QPU), with specific qubit connectivity and basic gate operations.

The algorithms can be developed either at a level close to the hardware, using 
the Atos Quantum Assembler (AQASM) language, or using a higher level, Python based 
language and ready-made libraries. The QLM comes with several ready-made examples.
You can also download and run locally [myQLM](../quantum-computing/kvasi/kvasi.md#myqlm) - a light-weight version of the 
QLM ecosystem.


