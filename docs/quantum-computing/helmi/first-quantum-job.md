# Running your first quantum computing job on Helmi through LUMI

If you've applied for a project, been accepted, setup your ssh keys and gained access to LUMI, then the next step is to run your first quantum computing job on a real quantum computer! This is a guide for exactly how to do that. The only thing you need to know is your project number! 

If you've not yet done any of the above then here are some helpful links:

- [Applying for a project](../helmi_accounts/#lumi-helmi-projects-vs.-regular-lumi-projects)
- [Setting up ssh keys](../helmi_quick/#connecting-to-lumi)


## Configuring the environment

The first step after you have logged into LUMI (via `ssh lumi` on your terminal) is to configure the environment. The base environment when first logging into LUMI does not provide the necessary tools to submit quantum jobs, therefore a quantum software stack has been created which sets up the correct python virtual environments and the correct environment variables. This is accessed through the LMOD system on LUMI using *modules*.

To use the quantum software stack you first need to tell LMOD where to search for modules. 

```bash
module use /appl/local/quantum/modulefiles
```

You can then see the list of available *modules* with `module avail`. The quantum modules should be at the top! In this walkthrough Qiskit will be used, therefore the next step is to load the module into our current environment with

```bash
module load helmi_qiskit
```


## Creating your first quantum program

The next step is to create your quantum circuit! Here a simple bell state will be created between two qubits, demonstrating entanglement between them! For this we will be using Qiskit but the steps are very similar for Cirq. It is good practice to work in your projects scratch directory, which you can navigate to with `cd /scratch/project_xxx`, inserting your project number.

!!! info "Tip!"
	
	You can quickly see your LUMI workspaces with
	`module load lumi-workspaces` and
	`lumi-workspaces`

Let us first create our python file with `nano my-first-quantum-job.py`. Here we use `nano` but if you are comfortable you can also use `vim` or `emacs`. This will bring up the `nano` text editor, the useful commands are at the bottom, to save and exit CTRL-X + Y.

### Importing the libraries

First let's import the right python libraries

```python
import qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.compiler import transpile
import numpy as np
from csc_qu_tools.qiskit import Helmi
```

### Creating the circuit

The quantum circuit is created by defining our `QuantumRegister` and our `ClassicalRegister` which hold our qubits and classical bits repectively. As this circuit only requires 2 qubits we only create a `QuantumRegister` of size 2. We will be measuring the outcome on each qubit and turning our quantum information into classical information, therefore we need a `ClassicalRegister` to hold this. 

```python
qreg = QuantumRegister(2, "qB")
creg = ClassicalRegister(2, "c")
circuit = QuantumCircuit(qreg, creg)
```

Now we actually add some gates to the circuit. Here a Hadamard gate is added to the first qubit or the first qubit in the quantum register. Then a Controlled-X gate is added with two arguments as it is a two qubit gate. 

```python
circuit.h(qreg[0])
circuit.cx(qreg[1], qreg[0])
```

Now the circuit is created! If you wish you can see what your circuit looks like by adding a print statement `print(circuit.draw())` and quickly running the python script. 

### Decomposing the circuit

The next step is to decompose the quantum circuit you've jsut created into it's *basis gates*. These basis gates are the actual quantum gates on the quantum computer. The process of decomposition involves turning the above Hadamard and Controlled-X gates into something that can be physically run on the quantum computer. Helmi's basis gates are the two-qubit Control-Z and a the one-qubit rotational gate around the x-y plane. In Qiskit these are defined by `basis_gates = ['r', 'cz']`. 

```python
basis_gates = ['r', 'cz']
circuit_decomposed = transpile(circuit, basis_gates=basis_gates)
```
You can also print your circuit like before with `print(circuit_decomposed.draw())` to see what it looks like! 

### Qubit Mapping

There is one more key piece of information that the Quantum Computer needs before being able to run. The Qubit Mapping. This is a python dictionary which simply states which *virtual* qubit should be mapped to which *real* qubit. The virtual qubits are the qubit's we've been using up until now, the real qubits are the ones on the quantum computer. 

```python
virtual_qubits = circuit_decomposed.qubits
qubit_mapping = {
                virtual_qubits[0]: "QB1",
                virtual_qubits[1]: "QB3",
            }
```

The virtual qubits are obtained from our decomposed circuit. The qubit mapping is defined via a python dictionary. Here we are mapping the first virtual qubit to the first of Helmi's qubits, QB1. The second qubit is then mapped to QB3. This is where we have made use of Helmi's topology. 

<p align="center">
    <img src="../../../img/helmi_mapping.png" alt="Helmi's node mapping">
</p>


The two qubit Controlled-X gate we implemented in our circuit is currently on the second of our two virtual qubits, `virtual_qubits[1]`. Due to Helmi's topology this needs to be mapped to QB3 on Helmi. The 1 qubit Hadamard gate can be mapped to any of the *outer* qubits, QB1, QB2, QB4, QB5, here we choose QB1. 

Now we're ready to submit it to the Quantum Computer!

### Submitting the job

First we need to set our provider and backend. The provider is the service which gives an interface to the quantum computer and the backend provides the tools necessary to submitting the quantum job. 

```python
provider = Helmi()
backend = provider.set_backend()
```

Before submitting the job there is one last thing we need to do: define the number of *shots*. The number of shots is the number of repetition of a quantum circuit. We do this because quantum computers are probabilistic machines and by repeating the result many times we can get close to a deterministic result to be able to draw conclusions from. A good number of shots for accurate results is `shots = 10000`, the qiskit default is 1024. 

Now we can run our quantum job!

```python
job = backend.run(qc_decomposed, shots=1024, qubit_mapping=qubit_mapping)
```

### Results

Before submitting we need to ensure we can get some results! The quantum job will return what are called **counts**. Counts are the accumulation of results from the 1024 times the circuit is submitting to the QPU. Each time the circuit is submitted a binary *state* is returned, this is then added to the tally.  In this case as we are submitting a 2 qubit circuit there are 4 possible resulting states: `00, 11, 01, 10`.  The expected results should be that approximately 50% of the counts should be in state `00` and 50% in state `11`.

To print your results add:

```python
counts = job.result().get_counts()
print(counts)
```

You can also print the entirety of `job.result()` which will contain all the information about your jobs results. 

## Save your file

Once you've made your first quantum program remember to save! CTRL+X then Y to save your file. 

## Running the job through LUMI

To run your quantum programme on LUMI you will need to submit the job through the SLURM batch scheduler on LUMI. Accessing Helmi is done through the `q_fiqci` partition. In the same directory where you have saved your quantum program, you can submit the job to SLURM using:

```bash
srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci python -u my-first-quantum-job.py
```

Remember to add your own project account!

This submits the job *interactively* meaning that the output will be printed straight to the terminal screen. If you wish you can also submit it using `sbatch` using this skeleton batch script. Using `nano` as before create the script `batch_script.sh`. 


```bash
#!/bin/bash -l

#SBATCH --job-name=helmijob   # Job name
#SBATCH --output=helmijob.o%j # Name of stdout output file
#SBATCH --error=helmijob.e%j  # Name of stderr error file
#SBATCH --partition=q_fiqci   # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --cpus-per-task=1     # Number of cores (threads)
#SBATCH --time=00:15:00         # Run time (hh:mm:ss)
#SBATCH --account=project_xxx  # Project for billing

module use /appl/local/quantum/modulefiles
module load helmi_qiskit

python -u my-first-quantum-job.py
```
This can be submitted with `sbatch batch_script.sh` in the same directory as your python file. Jobs in the SLURM queue can be monitored through `squeue -u username` and after the job has completed your results can be found in the `helmijob.oxxxxx` file. This can be printed to the terminal with `cat`. 


## Congratulations!

Congratulations! You have just run your first job on Helmi. 

<!-- 

ssh lumi
module use /appl/local/quantum/modulefiles
module load helmi_qiskit

create a simple qubit flipping circuit

	import the correct libs
	create qreg, clreg, and circuit

	set the backend
	transpile circuit
	set qubit mapping
	run the job


create a batch script








 -->