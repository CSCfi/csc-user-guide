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
	 
	helmi-XXX # helmi-qiskit, helmi-cirq
	 
	python your_python_script.py

The batch script can then be submitted with `sbatch`. You can also submit interactive jobs through `srun`. Before running jobs users will need to add to their `~/.bashrc` file `export MODULEPATH=$MODULEPATH:/project_462000055/` to ensure that the correct environments are setup. 

	srun --account=project_<id> -t 00:15:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py

<!-- Each user will need to know:
	- Queue/Partition to submit jobs to on LUMI
	- Batch job preamble activate-XXX to activate env on Helmi
	- Python backend preamble to set the backend as Helmi
	- Basis gates and Qubit Mapping for Helmi
	- Printing results such that results are returned to LUMI (TBD) -->



### Qiskit

When submitting jobs to Helmi using Qiskit add the `helmi-qiskit` command in your batch script before submitting your python script. In Qiskit python scripts you will need to include the following:

	from qiskit_iqm import IQMprovider # Import IQM library
	provider = IQMProvider(iqm_server_url, iqm_settings_path)
	backend = provider.get_backend() # Set backend
	basis_gates=['r', 'cz'] # Set Helmi basis gates

	# Create your circuit
	 
	qc_decomposed = transpile(qc, backend=backend, basis_gates=basis_gates) # Decomposed circuit into basis gates
	 
	virtual_qubits = qc_decomposed.qubits # Get the virtual qubits
	qubit_mapping = {virtual_qubits[0]: 'QB'+str(qb+1)} # Set Helmi Qubit Mapping
	job = backend.run(qc_decomposed, shots=1000, qubit_mapping=qubit_mapping) # Run with decomposed circuit and qubit mapping

Details on using the [Qiskit IQM package can be found here](https://iqm-finland.github.io/qiskit-on-iqm/index.html).

As an alternative to using `helmi-qiskit` inside your batch scripts,  you can create a container for the `qiskit-iqm` Python package yourself via the [LUMI container wrapper](../../containers/tykky/). We recommend using the supplied [requirements_qiskit.txt](../../support/tutorials/helmi/requirements_qiskit.txt) file.

	module load LUMI lumi-container-wrapper
	mkdir qiskit-iqm
	pip-containerize new --prefix qiskit-iqm/ requirements_qiskit.txt
	export PATH="/users/username/qiskit-iqm/bin:$PATH"

A collection of Qiskit examples and scripts for running on LUMI-Helmi is discussed below.


### Cirq

When submitting jobs to Helmi using Cirq add the `helmi-cirq` command in your batch script before submitting your python script. In Cirq python scripts you will need to include the following:

	from csc_qu_tools import Helmi
	import cirq

	helmi = Helmi()

	# Create your circuit

	decomposed_circuit = helmi.decompose_circuit(circuit)

	routed_circuit = helmi.route_circuit(decomposed_circuit)
	sampler = Helmi('settings.json').set_helmi()
	result = sampler.run(routed_circuit, repetitions=10)
	print(result)

Details on using the [Cirq IQM package can be found here](https://iqm-finland.github.io/cirq-on-iqm/index.html).

The Cirq environment can also be created manually by downloading the supplied [requirements_cirq.txt](../../support/tutorials/helmi/requirements_cirq.txt) file. 


	module load LUMI lumi-container-wrapper
	mkdir cirq-iqm
	pip-containerize new --prefix cirq-iqm/ requirements_cirq.txt
	export PATH="/users/username/cirq-iqm/bin:$PATH"

<!-- ### OpenQASM

Circuits can also be submitted via the OpenQASM format. Note that Qiskit and Cirq already have functions in place to automatically export your circuits in OpenQASM format.

* Qiskit circuits can be exported via `qc.qasm(formatted=False, filename=None, encoding=None)`.  -->


## Creating Circuits for Helmi

In order to efficiently use Helmi, some knowledge of the underlying system architecture and topology is needed. [Helmi's topology is described here](../../../computing/helmi/) and the examples below show how this topology is utilised to improve results. 


The full set of examples can be found here [**Insert link**] showing the differences between simulators and Helmi and how to construct your circuits for optimum results. This repository also contains some useful scripts for submitting jobs. As of the Pilot-Phase project only **Qiskit** examples and scripts will be available. Users can still submit jobs to Helmi in Cirq and support for Cirq will come soon. 

The `csc_qu_tools` python file contains all the necessary functions and classes needed for using Helmi via LUMI. This tool is not required for Qiskit usage as it provide much of the same functionality as `qiskit-iqm`, the Cirq class is required for Helmi specific functionality, therefore we recommend users to use this for submitting jobs to Helmi. 


