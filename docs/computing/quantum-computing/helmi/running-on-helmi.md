# Running on Helmi

!!! info "Give feedback!"
    **All feedback is highly appreciated**, please comment on your
    experience to [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi).

## Running Jobs

Jobs can be submitted to the `q_fiqci` queue by specifying `--partition=q_fiqci` in batch scripts.

Helmi currently supports submitting jobs using Qiskit or Cirq. Qiskit and Cirq scripts can only be submitted as ordinary python files.
To submit and run jobs on Helmi you need to use the correct environment on LUMI.

* First, run `module use /appl/local/quantum/modulefiles`. The available modules will now show up on `module avail`.
* Second, depending on if you want to use the Qiskit or Cirq environment, run:
    * `module load helmi_qiskit` or
    * `module load helmi_cirq`


`helmi_qiskit` and `helmi_cirq` provide pre-made python environments to directly run on Helmi.
If you wish to add your own python packages to the pre-made python environment you can do so with `python -m pip install --user package`.


!!! info "Creating your own python environment"
    Users can create their own python environment if they wish. The only prerequisite is to load the `helmi_standard` module.
    To create your own environment the [container wrapper tool](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/) is recommended.

The current supported software versions on helmi are:

| Software | Module_name | Versions |
|----------|-------------|----------|
| Cirq on IQM | cirq_iqm | >= 14.0, < 15.0 |
| Qiskit on IQM | qiskit_iqm | >= 13.0, < 14.0 |
| IQM client | iqm_client | >= 17.1, < 18.0 |
| Cortex CLI | iqm_cortex_cli | >= 5.8, < 6.0 |

Here is an example batch script to submit jobs on Helmi

```bash
#!/bin/bash

#SBATCH --job-name=helmijob   # Job name
#SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
#SBATCH --partition=q_fiqci   # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --mem-per-cpu=2G       # memory allocation
#SBATCH --cpus-per-task=1     # Number of cores (threads)
#SBATCH --time=00:15:00         # Run time (hh:mm:ss)

module use /appl/local/quantum/modulefiles

# uncomment correct line:
# module load helmi_qiskit
# or
# module load helmi_cirq

python your_python_script.py
```

The batch script can then be submitted with `sbatch`. You can also submit interactive jobs through `srun`.

```bash
srun --account=project_<id> -t 00:15:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py
```

The `helmi_*` module sets up the correct python environment to use Qiskit or Cirq in conjunction with Helmi.

!!! info "Running on Helmi"
    When submitting a job on Helmi, the user's slurm_job_account (project on which the job is run) is mapped to the project_id and this information is transferred to VTT for accounting purposes.

### Qiskit

To load the Qiskit module use `module load helmi_qiskit`.

In Qiskit python scripts you will need to include the following:

```python
import os

from qiskit import QuantumCircuit, execute
from iqm.qiskit_iqm import IQMProvider

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')  # This is set when loading the module

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

shots = 1000  # Set the number of shots you wish to run with

# Create your quantum circuit.
# Here is an example
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

print(circuit.draw(output='text'))

job = execute(circuit, backend, shots=shots)  # execute your quantum circuit
counts = job.result().get_counts()
print(counts)
```

### Cirq

To load the Cirq module use `module load helmi_cirq`.

```python
import os

import cirq
from iqm.cirq_iqm import Adonis
from iqm.cirq_iqm.iqm_sampler import IQMSampler

adonis = Adonis()

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')  # This is set when loading the module

sampler = IQMSampler(HELMI_CORTEX_URL)

shots = 1000

# Create your quantum circuit
# Here is an example
q1, q2 = cirq.NamedQubit('QB1'), cirq.NamedQubit('QB2')
circuit = cirq.Circuit()
circuit.append(cirq.H(q1))
circuit.append(cirq.CNOT(q1, q2))
circuit.append(cirq.measure(q1, q2, key='m'))
print(circuit)

decomposed_circuit = adonis.decompose_circuit(circuit)
routed_circuit, initial_mapping, final_mapping = adonis.route_circuit(decomposed_circuit)

# Optionally print mapping
# print(routed_circuit)
# print(initial_mapping)
# print(final_mapping)

result = sampler.run(routed_circuit, repetitions=shots)
print(result.histogram(key='m'))
```

## Additional examples

An additional [set of examples can be found here](https://github.com/FiQCI/helmi-examples).
The examples emphasize the difference between running on a simulator and a real physical quantum computer,
and how to construct your circuits for optimum results on Helmi. The repository also contains some useful
scripts for submitting jobs.


## Simulated test runs

As quantum resources can be scarce, it is recommended that you prepare the codes and algorithms you intend to run on Helmi in advance. To help with this process, [`qiskit-on-iqm` provides a fake noise model backend](https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html#noisy-simulation-of-quantum-circuit-execution). You can run the fake noise model backend locally on your laptop for simulation and testing.

A set of Qiskit and Cirq examples and scripts for guidance in using the LUMI-Helmi partition are also available. [You can find these here](https://github.com/FiQCI/helmi-examples).

## Job Metadata

Additional metadata about your job can be queried directly with Qiskit. For example:

```python

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

#Retrieving backend information
print(f'Native operations: {backend.operation_names}')
print(f'Number of qubits: {backend.num_qubits}')
print(f'Coupling map: {backend.coupling_map}')

job = execute(circuit, backend, shots=shots)
result = job.result()
exp_result = result._get_experiment(circuit)

print("Job ID: ", job.job_id())  # Retrieving the submitted job id
print(result.request.circuits)  # Retrieving the circuit request sent
print("Calibration Set ID: ", exp_result.calibration_set_id)  # Retrieving the current calibration set id.
print(result.request.qubit_mapping)  # Retrieving the qubit mapping
print(result.request.shots)  # Retrieving the number of requested shots.

#retrieve a job using the job_id from a previous session
#old_job = backend.retrieve_job(job_id)
```
!!! info "Save your Job ID!"
    Note that there is currently no method to list previous Job ID's therefore it is recommended to always print your Job ID after job submission and save it somewhere!
    The same applies for the calibration set id.


## Figures of Merit

The figures of merit (or quality metrics set) may be necessary for publishing work produced on Helmi. It also gives an idea as to the current status of Helmi. In `helmi-examples` there is a helper script to get the calibration data including the figures of merit. The script can be found [here](https://github.com/FiQCI/helmi-examples/blob/main/scripts/get_calibration_data.py). This file can be added to your own python scripts and will return data in json format. Note that querying the latest calibration data may give an incomplete or outdated set of figures. Therefore calibration set IDs should be saved along with Job IDs.

Here is a brief description of the figures which are given when querying:

| Figure                          | Description                                                                                                                                                                           |     |     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| T1 Time (s)                     | The T1 time is called the longitudinal relaxation rate and describes how quickly the excited state of the qubit returns to its ground state.                                          |     |     |
| T2 Time (s)                     | The T2 time is called the transverse relaxation rate and describes loss of coherence of a superposition state.                                                                        |     |     |
| T2 Echo Time (s)                | The T2 echo time describes the loss of coherence of the superposition state of the qubit. It is more precise than the T2 Time as it is less susceptible to low-frequency noise.       |     |     |
| Single shot readout fidelity    | This describes the fidelity when performing single shot readouts of the qubit state. Single-shot readout prepares 50% of the qubit states in the excited and 50% in the ground state. |     |     |
| Single shot readout 01 error    | The error in assigning an excited state ('1') when the state is in the ground state ('0').                                                                                            |     |     |
| Single shot readout 10 error    | The error in assigning a ground state ('0') when the state is in the excited state ('1').                                                                                             |     |     |
| Fidelity 1QB gates averaged     | This is calculated from Randomized Benchmarking and describes the average gate fidelity when a random sequence of single qubit Clifford gates is applied.                             |     |     |
| Fidelity 2QB Cliffords averaged | This is calculated from Randomized Benchmarking, showing the average Clifford gate fidelity.                                                                                          |     |     |
| CZ gate fidelity                | The controlled-z gate fidelity calculated through interleaved randomized benchmarking, where the controlled-z gate is interleaved.                                                    |     |     |


For further information on the figures of merit contact the [CSC Service Desk](../../../../support/contact/), reachable at [servicedesk@csc.fi](mailto:servicedesk@csc.fi).


## Using Helmi on Lumi-web interface

The [LUMI Web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/) allows users to run quantum jobs on Helmi through a web interface. Details for logging in to the LUMI web interface can be read through the [LUMI Documentation page](https://docs.lumi-supercomputer.eu/firststeps/loggingin-webui/).

### Accessing Helmi

After successfully authenticating, you should now have access to your dashboard. Click on the Jupyter app, select your project and the partition as q_fiqci. If you have an active reservation, you can use it by selecting it under reservation.

It is recommended to use the 'Advanced settings'. Under the 'Custom init' option select Text, and under the 'Script to start' textbox enter the following script to configure the environment to use the quantum software stack.

```bash
module use /appl/local/quantum/modulefiles
module load helmi_qiskit # or module load helmi_cirq
```

<p align="center">
    <img src="../../../../img/helmi_with_lumi_web.png" alt="Helmi's with LUMI web">
</p>

Click on launch to start your Jupyter session. This will launch Jupyter using the command python -m Jupyter lab. If you are using Helmi during a quantum computing course, a custom environment may have been created specifically for the course. In this case, you can access Helmi using the Jupyter-for-courses app.

<p align="center">
    <img src="../../../../img/helmi_with_jupyter_for_courses_gui.png" alt="Helmi's with LUMI web">
</p>


## Further Reading
* [Lumi web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/)
* [Jupyter on Lumi web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/jupyter/)
