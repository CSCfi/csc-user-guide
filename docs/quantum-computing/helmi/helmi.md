# Technical details about Helmi

## Architecture and Topology

Helmi is a 5 qubit Quantum Computer co-developed by VTT and IQM using superconducting qubits. The qubits are arranged in a **star shaped** topology, with the central qubit being Qubit 3 (QB3) connected to the other 4 qubits. This means that any two-qubit gate will work most efficiently between QB3 and any other qubit whereas one-qubit gates can be mapped to any of the 4 surrounding qubits. 

<p align="center">
    <img src="../../../img/helmi_mapping.png" alt="Helmi's node mapping">
</p>

### Native Gates

Helmi's native gates are the two-qubit Control-Z and a the one-qubit rotational gate around the x-y plane. 

### Defining topology and gates in Qiskit and Cirq

To define the features of Helmi in Qiskit and Circ, for example for transpiling, use the following definitions: 


|              |      Helmi      |                                                   Qiskit                                                   |                                 Cirq                                 |
|--------------|:---------------:|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| Basis Gates  | CZ + Rx, Ry, Rz |                                          `basis_gates=['r', 'cz']`                                         |   `ops.PhasedXPowGate, ops.XPowGate, ops.YPowGate, ops.CZPowGate()`  |
| Connectivity | Star Shaped     |                                     `[[2, 0], [2, 1], [2, 3], [2, 4]]`                                     |                  `({1, 3}, {2, 3}, {4, 3}, {5, 3})`                  |
| Mapping      |                 | `virtual_qubits=qc_decomposed.qubits`<br>`qubit_mapping={virtual_qubits[0]:'QB1',virtual_qubits[1]:'QB3'}` | Dictionary `qubit_mapping={'NamedQubit1':'QB1','NamedQubit2':'QB3'}` |



## Further Reading

* [Specific instructions for the LUMI Helmi partition](../helmi_accounts/)
* [Getting started with Helmi](../helmi_quick/)



