# Technical details about Helmi

## Architecture and Topology

Helmi is a 5 qubit Quantum Computer manufactured by IQM. The qubits are laid out in a **star shaped** topology, with the central qubit being Qubit 3 (QB3) connected to the other 4 qubits. This means that any two qubit gate will work most efficiently between QB3 and any other qubit whereas 1 qubit gates can be mapped to any of the 4 surrounding qubits. 

<!-- !["Helmi's node mapping"](../img/helmi_mapping.png) -->

<p align="center">
    <img src="../../img/helmi_mapping.png" alt="Helmi's node mapping">
</p>


### Native Gates

Helmis basis gates are Control-Z and a Rotational gate around the x-y plane. In Qiskit this is implement via `basis_gates=['r', 'cz']` in the transpiler, whereas on Cirq the basis gates are implemented as `ops.PhasedXPowGate, ops.XPowGate, ops.YPowGate, ops.MeasurementGate` and `ops.CZPowGate()`. 


|   | Helmi     | Qiskit    | Cirq  |
|---    |---    |---    |---    |
| Basis Gates   | CZ + R(\(\theta\))     | `basis_gates=['r', 'cz']`     | `NATIVE_GATES = (ops.PhasedXPowGate, ops.XPowGate, ops.YPowGate, ops.MeasurementGate)`<br>`NATIVE_GATE_INSTANCES = (ops.CZPowGate())`     |
| Connectivity  | Star Shaped   | `[[2, 0], [2, 1], [2, 3], [2, 4]]`    | `({1, 3}, {2, 3}, {4, 3}, {5, 3})`    |
| Mapping   |   | `virtual_qubits=qc_decomposed.qubits`<br>`qubit_mapping={virtual_qubits[0]:'QB1',virtual_qubits[1]:'QB3'}`    | Dictionary `qubit_mapping={'Alice':'QB1','Bob':'QB3'}`    |



## Further Reading

* [Specific instructions for the LUMI Helmi partition](../../accounts/helmi/)
* [Getting started with Helmi](../../support/tutorials/helmi_quick/)

<!-- ## Acessing Helmi via LUMI




The Helmi software stack provides some useful tools in mapping programs to this specific topology. [For more details see "Running on Helmi"](../running/running-on-helmi/).  


 -->



