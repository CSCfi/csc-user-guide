# Running on Helmi

## Running Jobs

Jobs can be submitted to the `q_fiqci` queue by specifying `--partition=q_fiqci` in batch scripts. 

Helmi currently supports submitting jobs using Qiskit or Cirq. Qiskit and Cirq scripts can only be submitted as ordinary python files.

Before running jobs users will need to use `module use /appl/local/quantum/modulefiles` to get access to the `helmi` module. The `helmi` module can then be loaded via `module load helmi`. Doing this ensures that the correct environments are setup to submit jobs to Helmi. 

```bash
#!/bin/bash -l
 
#SBATCH --job-name=helmijob   # Job name
#SBATCH --output=helmijob.o%j # Name of stdout output file
#SBATCH --error=helmijob.e%j  # Name of stderr error file
#SBATCH --partition=q_fiqci   # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --cpus-per-task=1     # Number of cores (threads)
#SBATCH --time=00:30:00         # Run time (hh:mm:ss)
#SBATCH --account=project_<id>  # Project for billing

module use /scratch/project_462000055/modules

# uncomment correct line:
# module load helmi_qiskit
# or
# module load helmi_cirq
 
python your_python_script.py
```

The batch script can then be submitted with `sbatch`. You can also submit interactive jobs through `srun`. 

```bash
srun --account=project_<id> -t 00:30:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py
```

The `helmi_*` module sets up the correct python environment to use Qiskit or Cirq in conjunction with Helmi. A set of Quantum Tools are also set up via `import csc_qu_tools`. The tools provide additional help in submitting jobs to Helmi. 

### Qiskit

To load the Qiskit module use `module load helmi_qiskit`.

In Qiskit python scripts you will need to include the following:

```python
from csc_qu_tools.qiskit import Helmi as helmi
provider = helmi()
backend = provider.set_backend()
basis_gates = provider.basis_gates
 
circuit_decomposed = transpile(qc, backend=backend, basis_gates=basis_gates) # Decompose circuit into native basis gates
 
virtual_qubits = circuit_decomposed.qubits # Get the virtual qubits
qubit_mapping = {virtual_qubits[0]: 'QB1',
                 virtual_qubits[1]: 'QB2',
                 virtual_qubits[2]: 'QB3'
                 virtual_qubits[3]: 'QB4',
                 virtual_qubits[4]: 'QB5'  } # Set Helmi qubit mapping
job = backend.run(circuit_decomposed, shots=, qubit_mapping=qubit_mapping) # Run with decomposed circuit and qubit mapping
```


Helmi currently uses the `qiskit-iqm==2.0` environment. From this, you can make your own container wrapper if you require additional python packages in your workflow. Instructions can be found in the [LUMI container wrapper](../../../containers/tykky/) documentation.

### Cirq

To load the Cirq module use `module load helmi_cirq`.

Also Cirq requires `csc_qu_tools` to load the Helmi device. In Cirq decomposition 

```python
from csc_qu_tools.cirq import Helmi
import cirq

backend = Helmi().set_helmi()
```


Helmi currently uses `cirq-iqm==4.1` environment. From this, you can make your own container wrapper if you require additional python packages in your workflow. Instructions can be found in the [LUMI container wrapper](../../../containers/tykky/) documentation.

### OpenQASM

Submission of OpenQASM formatted files is not currently supported on Helmi. You can convert your OpenQASM circuits to Cirq or Qiskit and submit them.

* On Qiskit this can be done with `QuantumCircuit.from_qasm_file('my_circuit.qasm')`.
* On Cirq, create the circuit from a string using  `circuit_from_qasm(""" Qasm_string """)`. 


## Creating Circuits for Helmi

To make the most efficient use of Helmi, some knowledge of the underlying system architecture and topology is needed. [Helmi's topology is described here](../helmi/) and the examples below show how this topology is utilised to improve results. 

An additional set of examples can be found here [**Insert link**]. The examples emphasize the difference between running on a simulator and a real physical quantum computer, and how to construct your circuits for optimum results on Helmi. The repository also contains some useful scripts for submitting jobs. Currently, **Qiskit** examples are available.

The `csc_qu_tools` python file contains all the necessary functions and classes needed for using Helmi via LUMI. This tool is not required for Qiskit usage as it provide much of the same functionality as `qiskit-iqm`. The Cirq class is required for Helmi specific functionality, therefore we recommend users to use this for submitting jobs to Helmi. 

### Quantum Tools

A python package to help interfacing with Helmi via LUMI is provided. The `csc_qu_tools` python package provides everything necessary to connect and submit jobs to Helmi via LUMI. Users can use the tool set for both Qiskit and Cirq. 

The package can be accessed after loading one of the `helmi` modules, by `import csc_qu_tools`.


