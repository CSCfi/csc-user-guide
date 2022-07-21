# Running on Helmi

## Running Jobs

Jobs can be submitted to the `q_fiqci` queue by specifying `--partition=q_fiqci` in batch scripts. 

Helmi currently supports submitting jobs using Qiskit, Cirq or OpenQASM. Qiskit and Cirq scripts can only be submitted as ordinary python files. Jupyter-notebook is **not** currently supported on LUMI.

	#!/bin/bash -l
	 
	#SBATCH --job-name=helmijob   # Job name
	#SBATCH --output=helmijob.o%j # Name of stdout output file
	#SBATCH --error=helmijob.e%j  # Name of stderr error file
	#SBATCH --partition=q_fiqci   # Partition (queue) name
	#SBATCH --ntasks=1              # One task (process)
	#SBATCH --cpus-per-task=128     # Number of cores (threads)
	#SBATCH --time=00:10:00         # Run time (hh:mm:ss)
	#SBATCH --account=project_<id>  # Project for billing
	 
	activate-XXX # activate-qiskit, activate-cirq, activate-qasm
	 
	python your_python_script.py

The batch script can then be submitted with `sbatch`. You can also submit interactive jobs through `srun` 

	srun --account=project_<id> -t 00:15:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py

<!-- Each user will need to know:
	- Queue/Partition to submit jobs to on LUMI
	- Batch job preamble activate-XXX to activate env on Helmi
	- Python backend preamble to set the backend as Helmi
	- Basis gates and Qubit Mapping for Helmi
	- Printing results such that results are returned to LUMI (TBD) -->



### Qiskit

When submitting jobs to Helmi using Qiskit add the `activate-qiskit` command in your batch script before submitting your python script. In Qiskit python scripts you will need to include the following:

	from qiskit_iqm import IQMprovider # Import IQM library
	 # Set backend
	 # Helmi basis gates
	 
	qc_decomposed = transpile(qc, backend=backend, basis_gates=basis_gates) # Decomposed circuit into basis gates
	 
	virtual_qubits = qc_decomposed.qubits # Get the virtual qubits
	qubit_mapping = {virtual_qubits[0]: 'QB'+str(qb+1)} # Set Helmi Qubit Mapping
	job = backend.run(qc_decomposed, shots=1000, qubit_mapping=qubit_mapping) # Run with decomposed circuit and qubit mapping

Alternatively you can create a container for the `qiskit-iqm` Python package via the [LUMI container wrapper](../../containers/tykky/). We recommend using the supplied [requirements_qiskit.txt](../../support/tutorials/helmi/requirements_qiskit.txt) file.

	module load LUMI lumi-container-wrapper
	mkdir qiskit-iqm
	pip-containerize new --prefix qiskit-iqm/ requirements_qiskit.txt
	export PATH="/users/username/qiskit-iqm/bin:$PATH"



### Cirq

When submitting jobs to Helmi using Cirq add the `activate-cirq` command in your batch script before submitting your python script.


The Cirq environment can also be created manually by downloading the supplied [requirements_cirq.txt](../../support/tutorials/helmi/requirements_cirq.txt) file. 


	module load LUMI lumi-container-wrapper
	mkdir cirq-iqm
	pip-containerize new --prefix cirq-iqm/ requirements_cirq.txt
	export PATH="/users/username/cirq-iqm/bin:$PATH"

### OpenQASM

Circuits can also be submitted via the OpenQASM format. Note that Qiskit and Cirq already have functions in place to automatically export your circuits in OpenQASM format.

* Qiskit circuits can be exported via `qc.qasm(formatted=False, filename=None, encoding=None)`. 


## Creating Circuits for Helmi

In order to efficiently use Helmi, some knowledge of the underlying system architecture and topology is needed. [Helmi's topology is described here](../../../computing/helmi/) and the examples below show how this topology is utilised to improve results. 


The full set of examples can be found here [**Insert link**] showing the differences between simulators and Helmi and how to construct your circuits for optimum results. This repository also contains some useful scripts for submitting jobs. 

