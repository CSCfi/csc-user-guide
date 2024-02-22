# Technical details about Helmi

## Architecture and Topology

Helmi is a 5-qubit quantum computer co-developed by VTT and IQM using superconducting qubits. 
The qubits are arranged in a **star shaped** topology, with the central qubit being Qubit 3 (QB3) connected to the other 4 qubits. 
This means that any two-qubit gate will work between QB3 and any other qubit, 
whereas one-qubit gates can be mapped to any of the 4 surrounding qubits. 

<p align="center">
    <img src="../../../../img/helmi_mapping.png" alt="Helmi's node mapping">
</p>

### Native Gates

Helmi's native gates are the two-qubit controlled-z gate and the one-qubit phased x-rotation gate.

### Defining topology and gates in Qiskit and Cirq

The topology, supported instructions and backend specific metadata can be queried directly with [Qiskit on IQM](https://iqm-finland.github.io/qiskit-on-iqm/) or [Cirq on IQM](https://iqm-finland.github.io/cirq-on-iqm/). For example:

```python
# Qiskit
from iqm.qiskit_iqm import IQMProvider
provider = IQMProvider(iqm_server_url)
backend = provider.get_backend()
print(f'Native operations of the backend: {backend.operation_names}')
print(f'Coupling map of the backend: {backend.coupling_map}')
```

```python
# Cirq
from iqm.cirq_iqm import Adonis
adonis = Adonis()
print(adonis.metadata.qubit_set)
print(adonis.metadata.gateset)
print(adonis.metadata.nx_graph)
```


## Further Reading

* [Specific instructions for the LUMI Helmi partition](../fiqci-partition/)
* [Qiskit adapter for IQM devices](https://iqm-finland.github.io/qiskit-on-iqm/)
* [Cirq adapter for IQM devices](https://iqm-finland.github.io/cirq-on-iqm/)




