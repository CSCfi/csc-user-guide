# Pulse level access

Pulse level access gives the user a lower level of control over their quantum jobs. Instead of only defining jobs via circuits using gates with pulse level access the user has control over the control pulses of the quantum computer. Pulse level access to the available quantum computers is enabled through the IQM Client Python package. IQM Client with pulse level access is already installed in the module for each quantum computer. Below you'll find an overview on running pulse level jobs from LUMI on the available quantum computers. For more advanced documentation on using IQM Pulla see [IQM's documentation](https://docs.iqm.tech/iqm-pulla/index.html){ target=_blank }

!!! info "Device-specific values"
    The examples on this page use placeholders `<DEVICE_VALUE>`, `<QUANTUM_COMPUTER_ID>`, and `<CORTEX_URL>`. Replace them with the runtime identifiers for your target device, listed under "Runtime identifiers" on the [Aalto Q20](../devices/q20.md#runtime-identifiers) or [VTT Q50](../devices/q50.md#runtime-identifiers) page. For VLQ see the [VLQ instructions](../devices/vlq.md).

## Import packages

Load the module with `module load fiqci-vtt-qiskit`.

```python
import os

from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from iqm.iqm_client.util import print_env_vars
from iqm.qiskit_iqm import IQMProvider
from iqm.qiskit_iqm.pulse_level_utils import qiskit_to_iqm, sweep_job_to_qiskit
```

## Define Pulla client and backend

```python

DEVICE_CORTEX_URL = os.getenv('<CORTEX_URL>')

provider = IQMProvider(DEVICE_CORTEX_URL, quantum_computer="<QUANTUM_COMPUTER_ID>")
backend = provider.get_backend()
client = backend.client
```

!!! info "VLQ Pulla backend"
    For VLQ see the [VLQ page](../devices/vlq.md) for instructions for fetching the VLQ Pulla backend as well as loading the VLQ module.

## Run a job with pulse level access

```python
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.measure_all()

qc_transpiled = transpile(qc, backend=backend, optimization_level=3)

circuits, compiler = qiskit_to_iqm(backend, qc_transpiled)

shots = 100
settings = compiler.get_settings(circuits=circuits)
settings.set_shots(shots)

run_definition, context = compiler.compile(circuits, settings=settings)

job = client.submit_playlist(job_definition, context=context)
job.wait_for_completion()
qiskit_result = sweep_job_to_qiskit(job, shots=shots)

print(f"Raw results:\n{job.result().circuit_measurement_results}\n")
print(f"Qiskit result counts:\n{qiskit_result.get_counts()}\n")
```


## Submitting through LUMI

For submitting jobs see [Running quantum jobs](overview.md#access-models).

## Further reading
* [Batch jobs](./access-models/batch.md)
* [Interactive jobs](./access-models/batch.md)
* [Jupyter notebook](./access-models/jupyter-notebook.md)
* [Additional examples (fiqci-examples)](https://github.com/FiQCI/fiqci-examples){ target=_blank }
