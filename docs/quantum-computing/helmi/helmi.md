# Technical details about Helmi

## Architecture and Topology

Helmi is a 5 qubit Quantum Computer manufactured by IQM using superconducting qubits. The qubits are arranged in a **star shaped** topology, with the central qubit being Qubit 3 (QB3) connected to the other 4 qubits. This means that any two qubit gate will work most efficiently between QB3 and any other qubit whereas 1 qubit gates can be mapped to any of the 4 surrounding qubits. 

<p align="center">
    <img src="../../../img/helmi_mapping.png" alt="Helmi's node mapping">
</p>


### Native Gates

Helmis basis gates are Control-Z and a Rotational gate around the x-y plane. This means that for the single qubits (QB1, QB2, QB4, QB5) have basis gates Rx, Ry and Rz and for the two qubit QB3 has controlled-Z as it's basis gate. In Qiskit this is implement via `basis_gates=['r', 'cz']` in the transpiler, whereas on Cirq the basis gates are implemented as `ops.PhasedXPowGate, ops.XPowGate, ops.YPowGate, ops.MeasurementGate` and `ops.CZPowGate()`. 


|              |      Helmi      |                                                   Qiskit                                                   |                                 Cirq                                 |
|--------------|:---------------:|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| Basis Gates  | CZ + Rx, Ry, Rz |                                          `basis_gates=['r', 'cz']`                                         |   `ops.PhasedXPowGate, ops.XPowGate, ops.YPowGate, ops.CZPowGate()`  |
| Connectivity | Star Shaped     |                                     `[[2, 0], [2, 1], [2, 3], [2, 4]]`                                     |                  `({1, 3}, {2, 3}, {4, 3}, {5, 3})`                  |
| Mapping      |                 | `virtual_qubits=qc_decomposed.qubits`<br>`qubit_mapping={virtual_qubits[0]:'QB1',virtual_qubits[1]:'QB3'}` | Dictionary `qubit_mapping={'NamedQubit1':'QB1','NamedQubit2':'QB3'}` |



## Further Reading

* [Specific instructions for the LUMI Helmi partition](../helmi_accounts/)
* [Getting started with Helmi](../helmi_quick/)



