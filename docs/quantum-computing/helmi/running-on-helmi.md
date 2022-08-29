# Running on Helmi

## Running Jobs

Jobs can be submitted to the `q_fiqci` queue by specifying `--partition=q_fiqci` in batch scripts. 

Helmi currently supports submitting jobs using Qiskit, Cirq or OpenQASM. Qiskit and Cirq scripts can only be submitted as ordinary python files. Jupyter-notebook is **not** currently supported on LUMI. Pulse level access to Helmi is not currently available. 

Before running jobs users will need to use `module use /scratch/project_462000055/modules` to get access to the `helmi` module. The `helmi` module can then be loaded via `module load helmi`. Doing this ensures that the correct environments are setup to submit jobs to Helmi. 

	#!/bin/bash -l
	 
	#SBATCH --job-name=helmijob   # Job name
	#SBATCH --output=helmijob.o%j # Name of stdout output file
	#SBATCH --error=helmijob.e%j  # Name of stderr error file
	#SBATCH --partition=q_fiqci   # Partition (queue) name
	#SBATCH --ntasks=1              # One task (process)
	#SBATCH --cpus-per-task=1     # Number of cores (threads)
	#SBATCH --time=00:15:00         # Run time (hh:mm:ss)
	#SBATCH --account=project_<id>  # Project for billing

	module use /scratch/project_462000055/modules
	module load helmi_qiskit
	# or
	module load helmi_cirq
	 
	python your_python_script.py

The batch script can then be submitted with `sbatch`. You can also submit interactive jobs through `srun`. 

	srun --account=project_<id> -t 00:15:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py

The `helmi` module sets up the correct python environment to use Qiskit and Cirq in conjunction with Helmi as well as a set of CSC Quantum Tools via `import csc_qu_tools` which provide additional help in submitting jobs to Helmi. 

### Qiskit

To load the Qiskit module use `module load helmi_qiskit`.

In Qiskit python scripts you will need to include the following:

    from csc_qu_tools.qiskit import Helmi as helmi
    provider = helmi()
    backend = provider.set_backend()
    basis_gates = provider.basis_gates
     
    qc_decomposed = transpile(qc, backend=backend, basis_gates=basis_gates) # Decomposed circuit into basis gates
     
    virtual_qubits = qc_decomposed.qubits # Get the virtual qubits
    qubit_mapping = {virtual_qubits[0]: 'QB1',
                      virtual_qubits[1]: 'QB2',
                      virtual_qubits[2]: 'QB3'
                      virtual_qubits[3]: 'QB4',
                      virtual_qubits[4]: 'QB5'  } # Set Helmi Qubit Mapping like this.
    job = backend.run(qc_decomposed, shots=, qubit_mapping=qubit_mapping) # Run with decomposed circuit and qubit mapping

Helmi currently uses `qiskit-iqm==2.0` from which you can make your own container wrapper if you require additional python packages in your workflow. Instructions can be found via the [LUMI container wrapper](../../../computing/containers/tykky/). You will still need the `csc_qu_tools` python package to submit jobs to Helmi. 

<!--     module load LUMI lumi-container-wrapper
    mkdir qiskit-iqm
    pip-containerize new --prefix qiskit-iqm/ requirements.txt
    export PATH="/users/username/qiskit-iqm/bin:$PATH" -->

### Cirq

To load the Cirq module use `module load helmi_cirq`.

Cirq requires `csc_qu_tools` to load the Helmi device, this can be accessed through `module load helmi_cirq`. In Cirq decomposition 

    from csc_qu_tools.cirq import Helmi
    import cirq

    backend = Helmi().set_helmi()


Helmi currently uses `cirq-iqm==4.1` from which you can make your own container wrapper if you require additional python packages in your workflow. Instructions can be found via the [LUMI container wrapper](../../../computing/containers/tykky/).

### OpenQASM

Submission of OpenQASM formatted files is not currently supported on Helmi. You can convert your OpenQASM circuits to Cirq or Qiskit and submit them. On Qiskit this can be done with `QuantumCircuit.from_qasm_file('my_circuit.qasm')` or on Cirq creating the circuit from a string using  `circuit_from_qasm(""" Qasm_string """)`. 


## Creating Circuits for Helmi

In order to efficiently use Helmi, some knowledge of the underlying system architecture and topology is needed. [Helmi's topology is described here](../helmi/) and the examples below show how this topology is utilised to improve results. 


The full set of examples can be found here [**Insert link**] showing the differences between simulators and Helmi and how to construct your circuits for optimum results. This repository also contains some useful scripts for submitting jobs. As of the Pilot-Phase project only **Qiskit** examples and scripts will be available. Users can still submit jobs to Helmi in Cirq and support for Cirq will come soon. 

The `csc_qu_tools` python file contains all the necessary functions and classes needed for using Helmi via LUMI. This tool is not required for Qiskit usage as it provide much of the same functionality as `qiskit-iqm`, the Cirq class is required for Helmi specific functionality, therefore we recommend users to use this for submitting jobs to Helmi. 

### CSC Quantum Tools

CSC also provides a python package to help in interfacing with Helmi via LUMI. The `csc_qu_tools` python package provides everything necessary to connect and submit jobs to Helmi via LUMI without any of the additional steps for setting up your python files. Currently users can use this tools for both Qiskit and Cirq. 

This package can be accessed if you have the `helmi` module loaded via `import csc_qu_tools`. Further documentation to follow...


