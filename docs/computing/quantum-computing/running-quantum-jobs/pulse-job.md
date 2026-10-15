# Pulse level access

Pulse level access gives the user a lower level of control over their quantum jobs. Instead of only defining jobs via circuits using gates with pulse level access the user has control over the control pulses of the quantum computer. Pulse level access to both VTT Q50, Aalto Q20, and VLQ is enabled through the IQM Pulla python package. IQM Pulla is already installed in the module for each quantum computer. Below you'll find an overview on running pulse level jobs from LUMI on the available quantum computers. For more advanced documentation on using IQM Pulla see [IQM's documentation](https://docs.iqm.tech/iqm-pulla/index.html){ target=_blank }

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
from iqm.pulla.pulla import Pulla
from iqm.pulla.utils_qiskit import qiskit_to_pulla, sweep_job_to_qiskit
```

## Define Pulla client and backend

```python

DEVICE_CORTEX_URL = os.getenv('<CORTEX_URL>')

p = Pulla(DEVICE_CORTEX_URL, quantum_computer="<QUANTUM_COMPUTER_ID>")

provider = IQMProvider(DEVICE_CORTEX_URL, quantum_computer="<QUANTUM_COMPUTER_ID>")
backend = provider.get_backend()
```

!!! "VLQ Pulla backend"
    For VLQ see the [VLQ page](../devices/vlq.md) for instructions for fetching the VLQ Pulla backend as well as loading the VLQ module.

## Define a quantum circuit

```python
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.measure_all()
```

## Transpile to backend

```python
qc_transpiled = transpile(qc, backend=backend, optimization_level=3)
```

## Convert to Pulla

```python
circuits, compiler = qiskit_to_pulla(p, backend, qc_transpiled)

shots = 100
settings = compiler.get_settings(circuits=circuits)
settings.set_shots(shots)

job_definition, context = compiler.compile(circuits, settings=settings)
```

## Visualise pulse scheduling (optional)

Optionally it is possible to visualise the pulse scheduling before submitting the job.

```python
from iqm.pulse.playlist.visualisation.base import inspect_playlist
from IPython.core.display import HTML

HTML(inspect_playlist(job_definition.sweep_definition.playlist, [0]))
```

## Submit through Pulla

```python
job = p.submit_playlist(job_definition, context=context)
job.wait_for_completion()
qiskit_result = sweep_job_to_qiskit(job, shots=shots)

print(f"Raw results:\n{job.result().circuit_measurement_results}\n")
print(f"Qiskit result counts:\n{qiskit_result.get_counts()}\n")
```

## Submitting through LUMI

For submitting jobs see [Running quantum jobs](overview.md#access-models).

## Further Reading
* [Batch jobs](./access-models/batch.md)
* [Interactive jobs](./access-models/batch.md)
* [Jupyter notebook](./access-models/jupyter-notebook.md)
* [Additional examples (fiqci-examples)](https://github.com/FiQCI/fiqci-examples){ target=_blank }
