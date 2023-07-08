# Running on Helmi

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
	To create your own environment the [Container Wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/) is recommended.

The current support software versions on helmi are:

```bash
Cirq on IQM 	cirq_iqm 	>= 11.9, < 12.0  # helmi_cirq has 11.9
Qiskit on IQM 	qiskit_iqm 	>= 8.3, < 9.0  # helmi_qiskit has 9.0
IQM client 	iqm_client 	>= 12.5, < 13.0
```


```bash
#!/bin/bash
 
#SBATCH --job-name=helmijob   # Job name
#SBATCH --account=project_<id>  # Project for billing
#SBATCH --partition=q_fiqci   # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
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

### Qiskit

To load the Qiskit module use `module load helmi_qiskit`.

In Qiskit python scripts you will need to include the following:

```python
import os
from qiskit_iqm import IQMProvider

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')  # This is set when loading the module

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

shots = 1000  # Set the number of shots you wish to run with

# Create your quantum circuit.

job = execute(circuit, backend, shots=shots)  # execute your quantum circuit
counts = job.result().get_counts()
print(counts)

# You can retrieve the job at a later date with backend.retrieve_job(job_id)
# Uncomment the following lines to get more information about your submitted job
# result = job.result()
# exp_result = job.result()._get_experiment(circuit)
# print("Job ID: ", job.job_id())
# print(result.request.circuits)
# print("Calibration Set ID: ", exp_result.calibration_set_id)
# print(result.request.qubit_mapping)
# print(result.request.shots)
```

### Cirq

To load the Cirq module use `module load helmi_cirq`.

Also Cirq requires `csc_qu_tools` to load the Helmi device. In Cirq decomposition 

```python
import os
from cirq_iqm.iqm_sampler import IQMSampler

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')  # This is set when loading the module

shots = 1000

result = sampler.run(circuit, repetitions=shots)

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

The figures of merit (or quality metrics set) may be necessary for publishing work produced on Helmi. It also gives an idea as to the current status of Helmi.

Users can use the `helmi-info` command once you have loaded either `helmi_qiskit` or `helmi_cirq` environments on LUMI. With the `-p` flag the figures of merit will be printed as a table. If you pass the `--output` flag and a location you can save the figures of merit in a `json` file format. Passing the `--date yyyy-mm-dd` flag will load the figures of merit from that date. For example: `helmi-info --date 2023-04-12 -p` or `helmi-info --output figures-of-merit.json --date 2023-04-12` will save the figures of merit from the date specified into a location specified. 

| Figure                              | Description                                                                                                                                                                                                      |     |     |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| T1 Time (μs)                        | The T1 time is called the longitudinal relaxation rate and describes how quickly the excited state of the qubit returns to its ground state.                                                                     |     |     |
| T2 Time (μs)                        | The T2 time is called the transverse relaxation rate and describes loss of coherence of a superposition state.                                                                                                   |     |     |
| T2 Echo Time (μs)                   | The T2 echo time describes the loss of coherence of the superposition state of the qubit. It is more precise than the T2 Time as it is less susceptible to low-frequency noise.                                  |     |     |
| Fidelity 1QB gates averaged (%)     | This is calculated from Standard Randomized Benchmarking and describes the average gate fidelity when a random sequence of single qubit Clifford gates is applied.                                               |     |     |
| Single shot RO fidelity (%)         | This describes the fidelity when performing single shot readouts of the qubit state. Single-shot readout prepares 50% of the qubit states in the excited and 50% in the ground state.                            |     |     |
| Fidelity 2QB Cliffords averaged (%) | This is calculated from Standard Randomized Benchmarking, showing the average Clifford gate fidelity.                                                                                                            |     |     |
| Fidelity per gate (%)               | This is calculated from interleaved 2-qubit Randomized Benchmarking and describes the fidelity between the target qubit and the control qubit with an interleaved gate in the random sequence of Clifford gates. |     |     |

For further information on the figures of merit contact the [CSC Service Desk](../../../../support/contact/), reachable at servicedesk@csc.fi.