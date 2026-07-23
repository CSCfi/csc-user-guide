!!! warning "Q20 Service in MyCSC"
    There are currently some issues with the Q20 service for projects that have Q20 allocations. If you cannot find the Aalto-Q20 service or are otherwise experiencing issues please contact the CSC Service Desk at [servicedesk@csc.fi](mailto:servicedesk@csc.fi).

# Pulse level access

Pulse level access gives the user a lower level of control over their quantum jobs. Instead of only defining jobs via circuits using gates with pulse level access the user has control over the control pulses of the quantum computer. Pulse level access to both VTT Q50 and Aalto Q20 is enabled through the IQM Pulla python package. IQM Pulla is already installed in the module for each quantum computer. Below you'll find an overview on running pulse level jobs from LUMI on the available quantum computers. For more advanced documentation on using IQM Pulla see [IQM's documentation](https://docs.iqm.tech/iqm-pulla/index.html)


## Load the environment

```bash
module use /appl/local/quantum/modulefiles    
module load fiqci-vtt-qiskit
```

## Import packages

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

=== "Q20"

    ```
    Q20_CORTEX_URL = os.getenv('Q20_CORTEX_URL')

    p = Pulla(Q20_CORTEX_URL, quantum_computer="radiance20")
    
    q20_provider = IQMProvider(Q20_CORTEX_URL, quantum_computer="radiance20")
    backend = provider.get_backend()

    ```

=== "Q50"

    ```
    Q50_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    p = Pulla(Q50_CORTEX_URL, quantum_computer="q50")

    q50_provider = IQMProvider(Q50_CORTEX_URL, quantum_computer="q50")
    backend = provider.get_backend()
    ```

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

## Visualise pulse scheduling

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

## Running through LUMI

For instructions on running the job on LUMI you can use the example batch script below.

=== "Q20"

    ```bash
    #!/bin/bash

    #SBATCH --job-name=pulsejob   # Job name
    #SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
    #SBATCH --partition=small   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)

    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit

    export DEVICES=("rediance20")
    source $RUN_SETUP
    python your_python_script.py
    ```

=== "Q50"

    ```bash
    #!/bin/bash

    #SBATCH --job-name=pulsejob   # Job name
    #SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
    #SBATCH --partition=small   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)

    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit

    export DEVICES=("q50")
    source $RUN_SETUP
    python your_python_script.py
    ```

Alternatively you can submit interactive jobs using `srun`

=== "Q20"

    ```bash
    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit/"
    export DEVICES=("radiance20")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python your_python_script.py"
    ```

=== "Q50"

    ```bash
    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit/"
    export DEVICES=("q50")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python your_python_script.py"
    ```