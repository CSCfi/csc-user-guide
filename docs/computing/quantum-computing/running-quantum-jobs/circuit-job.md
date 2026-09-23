# Example job

A minimal Bell pair circuit, run on a quantum computer. Replace `<CORTEX_URL>` and `<QUANTUM_COMPUTER_ID>` with the values from [Runtime identifiers](../devices/overview.md) on your device's page. `<CORTEX_URL>` is the name of an environment variable set by the `fiqci-vtt-*` module.

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

    cortex_url = os.getenv("<CORTEX_URL>")
    sampler = IQMSampler(cortex_url, quantum_computer="<QUANTUM_COMPUTER_ID>")
    ```

## Define and run your circuit

=== "Qiskit"

    ```python
    from qiskit import QuantumCircuit, QuantumRegister, transpile

    shots = 1000

    qreg = QuantumRegister(2, "QB")
    circuit = QuantumCircuit(qreg, name="Bell pair circuit")
    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.measure_all()

    transpiled_circuit = transpile(circuit, backend=backend)

    job = backend.run(transpiled_circuit, shots=shots)
    print("Job ID:", job.job_id())

    print(job.result().get_counts())
    ```

=== "Cirq"

    ```python
    import cirq

    shots = 1000

    qubits = cirq.NamedQubit.range(2, prefix="QB")
    circuit = cirq.Circuit(
        cirq.H(qubits[0]),
        cirq.CNOT(qubits[0], qubits[1]),
        cirq.measure(*qubits, key="m"),
    )

    result = sampler.run(circuit, repetitions=shots)
    print("Job ID:", result.metadata.job_id)

    print(result.histogram(key="m"))
    ```

!!! warning "Save your Job ID!"
    There is currently no way to list previous job IDs, so always print your job ID after submission and save it somewhere. The same applies to the calibration set ID.

## Submitting through LUMI

For submitting jobs see [Running quantum jobs](overview.md/#access-models).

## Further Reading
* [Batch jobs](./access-models/batch.md)
* [Interactive jobs](./access-models/batch.md)
* [Jupyter notebook](./access-models/jupyter-notebook.md)
* [Additional examples (fiqci-examples)](https://github.com/FiQCI/fiqci-examples){ target=_blank }
