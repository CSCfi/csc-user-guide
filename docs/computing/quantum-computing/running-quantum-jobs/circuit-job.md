# Example job

A minimal Bell pair circuit, run on a quantum computer. Replace `<CORTEX_URL>` and `<QUANTUM_COMPUTER_ID>` with the values from [Runtime identifiers](../devices/overview.md) on your device's page. `<CORTEX_URL>` is the name of an environment variable set by the `fiqci-vtt-*` module.

## Import packages

=== "Qiskit"

    Load the module with `module load fiqci-vtt-qiskit`.

    ```python
    import os
    from iqm.qiskit_iqm import IQMProvider
    from qiskit import QuantumCircuit, QuantumRegister, transpile
    ```

=== "Cirq"

    Load the module with `module load fiqci-vtt-cirq`.

    ```python
    import os
    from iqm.cirq_iqm.iqm_sampler import IQMSampler
    ```

## Get the backend

!!! info "VLQ backend"
    The syntax for fetching the VLQ backend is different. See the [VLQ page](../devices/vlq.md) for instructions.

=== "Qiskit"

    Load the module with `module load fiqci-vtt-qiskit`.

    ```python
    import os
    from iqm.qiskit_iqm import IQMProvider

    cortex_url = os.getenv("<CORTEX_URL>")
    provider = IQMProvider(cortex_url, quantum_computer="<QUANTUM_COMPUTER_ID>")
    backend = provider.get_backend()
    ```

=== "Cirq"

    Load the module with `module load fiqci-vtt-cirq`.

    ```python
    import os
    from iqm.cirq_iqm.iqm_sampler import IQMSampler
    import cirq

    cortex_url = os.getenv("<CORTEX_URL>")
    sampler = IQMSampler(cortex_url, quantum_computer="<QUANTUM_COMPUTER_ID>")
    ```


## Define a quantum circuit

=== "Qiskit"

    ```python
    qreg = QuantumRegister(2, "QB")
    circuit = QuantumCircuit(qreg, name="Bell pair circuit")
    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.measure_all()

    transpiled_circuit = transpile(circuit, backend=backend)
    ```

=== "Cirq"

    ```python
    qubits = cirq.NamedQubit.range(2, prefix="QB")
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),
        cirq.CNOT(qubits[0], qubits[1]),
        cirq.measure(*qubits, key="m"),
    )
    ```

## Transpile the circuit

Transpiling compiles the circuit into a compatible format with the backend. This includes translating into supported gates and complying with the backends topology.

=== "Qiskit"

    ```python
    transpiled_circuit = transpile(circuit, backend=backend)
    ```

=== "Cirq"

    ```python
    routed_circuit, _, _ = sampler.device.route_circuit(circuit)
    decomposed_circuit = sampler.device.decompose_circuit(routed_circuit)
    ```

## Submit to the backend

=== "Qiskit"

    ```python
    job = backend.run(transpiled_circuit, shots=1000)
    print("Job ID:", job.job_id())

    print(job.result().get_counts())
    ```

=== "Cirq"

    ```python
    result = sampler.run(decomposed_circuit, repetitions=1000)
    print("Job ID:", result.metadata.job_id)

    print(result.histogram(key="m"))
    ```

!!! warning "Save your Job ID!"
    There is currently no way to list previous job IDs, so always print your job ID after submission and save it somewhere. The same applies to the calibration set ID.

## Submitting through LUMI

For submitting jobs see [Running quantum jobs](overview.md#access-models).

## Further reading
* [Batch jobs](./access-models/batch.md)
* [Interactive jobs](./access-models/batch.md)
* [Jupyter notebook](./access-models/jupyter-notebook.md)
* [Additional examples (fiqci-examples)](https://github.com/FiQCI/fiqci-examples){ target=_blank }
