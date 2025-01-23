---
tags:
  - Free
---

# Qiskit

Qiskit is an open-source software for working with quantum computers at the level
of circuits, pulses, and algorithms. 

!!! info "News"
     **23.01.2025** Installed `qiskit/1.2.4` in a singularity container on LUMI with all major Qiskit packages and
     added support for multi-node Native Cray MPI GPU-acceleration allowing for performant multi node simulations 
     for up to 45* qubits.

## Available

Currently supported Qiskit versions:

| Version | Module          | Puhti | Mahti | LUMI  | Notes                            |
| :------ | :-------------- | :---: | :---: | :---: | -------------------------------- |
| 1.1.1   | `qiskit/1.1.1`  |   X   |   X   |       |                                  |
| 1.2.4   | `qiskit/1.2.4`  |       |       |   X   | Native Cray MPI with GPU support |

Includes all the major Qiskit packages (Terra, Nature, Aer, etc.) and GPU acceleration. The `qiskit/1.1.1` and `qiskit/1.2.4` packages include the following qiskit plugins:

```bash
qiskit-aer-gpu>=0.14.2
qiskit-algorithms==0.3.0
qiskit-dynamics==0.5.1
qiskit-experiments==0.7.0
qiskit-finance==0.4.1
qiskit-ibm-experiment==0.4.7
qiskit-machine-learning==0.7.2
qiskit-nature==0.7.2
qiskit-optimization==0.6.1
```


If you find that some package is missing, you can often install it yourself with `pip install --user`.
Please see our [Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules) for
more information on how to install packages yourself. If you think that some important
Qiskit-related package should be included in the module provided by CSC, please
[contact our servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known as Singularity).
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[CSC's general instructions on how to run Apptainer containers](../computing/containers/run-existing.md).

## License

Qiskit is licensed under
[Apache License 2.0](https://github.com/Qiskit/qiskit-metapackage/blob/master/LICENSE.txt).

## Usage

To use the default version of Qiskit, initialize
it with:

```text
module load qiskit
```

If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load qiskit/1.1.1
```

### Example batch script - Single-node simulations on Puhti, Mahti, and LUMI

Example batch script for reserving one GPU and two CPU cores in a single node for Puhti and Mahti and all CPU/GPU resources on a single node using the LUMI standard-g partition :

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=2
    #SBATCH --mem=8G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
        
    module load qiskit
    srun python myprog.py <options>
    ```

=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=2
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:1
    
    module load qiskit
    srun python myprog.py <options>
    ```

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard-g
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=1
    #SBATCH --gpus-per-task=8
    #SBATCH --cpus-per-task=56
    #SBATCH --time=1:00:00

    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_1.2.4_csc.sif
    export WRAPPER_PATH=/appl/local/quantum/qiskit/run-singularity

    mask=mask_cpu:0xfe000000000000,0xfe00000000000000,0xfe0000,0xfe000000,0xfe,0xfe00,0xfe00000000,0xfe0000000000
    export MPICH_GPU_SUPPORT_ENABLED=1 

    srun --cpu-bind=$mask $WRAPPER_PATH $LUMI_QISKIT_SINGULARITY_CONTAINER_PATH python myprog.py
    ```

### Small code example of "myprog.py" without MPI

Do note that this code is just to highlight the syntax and only works on a single node.

```Python
import qiskit
from qiskit_aer import AerSimulator

# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure_all()

shots = 1000

# Construct an ideal simulator that uses GPU
simulator = AerSimulator(method="statevector", device="GPU")

# Execute the circuit with cuStateVec enabled. 
result_ideal = simulator.run(circ,shots=shots,seed_simulator=12345, cuStateVec_enable=True).result()

counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)
```

Submit the script with `sbatch <script_name>.sh`


### Small code example of "myprog.py" on LUMI using a single node for 34 qubits 
* please reference the recommended resource allocation table below to see how many resources are required per amount of qubits you wish to simulate on LUMI. The example script below works on a single node as well as on multiple nodes.

```Python
from qiskit import QuantumCircuit, transpile
from qiskit.transpiler import CouplingMap
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QuantumVolume
import time

## CHOOSE PARAMETERS - Values obtained from sbatch script that are imported into SINGULARITY CONTAINER using SINGULARITYENV_*env variable -----------------------------------------

qubits = 34
depth = 30                            # How many layers of quantum gates dioes the circuit have (Applies for Quantum Volume circuit)
num_shots = 1000                      # How many times we sample the circuit
sim_method = 'statevector'            # Circuits with over 30 qubits start to require a lot of memory if using statevector simulator
sim_device = 'GPU'                    # Requires system that provides GPU
use_cache_blocking = True             # Enables cache blocking technique. Qiskit Aer parallelizes simulations by distributing quantum states into distributed memory space.
num_blocking_qubits = 29              # Must be smaller than qubits-log2(num_processes). Smaller number of blocking qubits -> more processess (beneficial to utilize MPI by allocating more resources)
use_batched_shots = True              # Enables distributing shots to multiple processess
num_parallel_experiments = 1          # Does not seem to do anything when running with MPI, probably intended to be used with multithreading

start_time = time.time()

## INITIALIZE SIMULATOR BACKEND ---------------------------------------------------------------------------------------------------
sim = AerSimulator(method=sim_method, device=sim_device, batched_shots_gpu=use_batched_shots)

## CREATE CIRCUIT -----------------------------------------------------------------------------------------------------------------
circuit = QuantumVolume(qubits, depth, seed=0)
circuit.measure_all()

## TRANSPILE THE FOR CIRCUIT FOR FULL COUPLING MAP --------------------------------------------------------------------------------
coupling_map = CouplingMap.from_full(qubits)
transpiled_circuit = transpile(circuit, sim, coupling_map=coupling_map, optimization_level=0)

## RUN THE SIMULATION -------------------------------------------------------------------------------------------------------------
result_statevec = sim.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enabled=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()

## GATHER THE RESULTS AND PRINT WITH SOME ADDITIONAL METADATA ---------------------------------------------------------------------
input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : qubits, 'Depth' : depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots , 'Device' : sim_device, 'Simulation Method' : sim_method}
if (use_cache_blocking):
    num_processes = 2**(qubits - num_blocking_qubits)
    input_data['Blocking Qubits'] = num_blocking_qubits
    input_data['Num Processes'] = num_processes

dict = result_statevec.to_dict()
meta = dict['metadata']

print(f"{input_data}")
print(f"{meta}")
print(f"-------------------------------------------------------------- \n")
```

Submit the script with `sbatch <script_name>.sh`

### Example batch script - Multi-node simulations which leverage Native HPE Cray MPI with GPU acceleration

Example batch script for running a simulation on multiple LUMI nodes in the standard-g partition using all GPUs and all CPU cores on a node. This is for simulations involving 35 qubits or more (up to a maximum 45* qubits - see table below for recommended resource allocations based on amount of qubits you wish to simulate ):

=== "LUMI"
    ```bash
    ## Here is an example sbatch script for a 38 qubit simulation using 16 nodes
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --time=2:00:00
    #SBATCH --partition=standard-g
    #SBATCH --nodes=16
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    
    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_1.2.4_csc.sif
    export GPU_WRAPPER_PATH=/appl/local/quantum/qiskit/run-singularity-with-gpu-affinity

    mask=mask_cpu:0xfe000000000000,0xfe00000000000000,0xfe0000,0xfe000000,0xfe,0xfe00,0xfe00000000,0xfe0000000000
    export MPICH_GPU_SUPPORT_ENABLED=1 

    srun --cpu-bind=$mask $GPU_WRAPPER_PATH $LUMI_QISKIT_SINGULARITY_CONTAINER_PATH python myprog_MPI.py
    ```

### Small code example of "myprog_MPI.py" using 38 qubits which we recommend running on 16 nodes 
*reference recommended resource allocation table below

```Python
from qiskit import QuantumCircuit, transpile
from qiskit.transpiler import CouplingMap
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QuantumVolume
import time

## CHOOSE PARAMETERS - Values obtained from sbatch script that are imported into SINGULARITY CONTAINER using SINGULARITYENV_*env variable -----------------------------------------

qubits = 38
depth = 30                            # How many layers of quantum gates dioes the circuit have (Applies for Quantum Volume circuit)
num_shots = 1000                      # How many times we sample the circuit
sim_method = 'statevector'            # Circuits with over 30 qubits start to require a lot of memory if using statevector simulator
sim_device = 'GPU'                    # Requires system that provides GPU
use_cache_blocking = True             # Enables cache blocking technique. Qiskit Aer parallelizes simulations by distributing quantum states into distributed memory space.
num_blocking_qubits = 29              # Must be smaller than qubits-log2(num_processes). Smaller number of blocking qubits -> more processess (beneficial to utilize MPI by allocating more resources)
use_batched_shots = True              # Enables distributing shots to multiple processess
num_parallel_experiments = 1          # Does not seem to do anything when running with MPI, probably intended to be used with multithreading

start_time = time.time()

## INITIALIZE SIMULATOR BACKEND ---------------------------------------------------------------------------------------------------
sim = AerSimulator(method=sim_method, device=sim_device, batched_shots_gpu=use_batched_shots)

## CREATE CIRCUIT -----------------------------------------------------------------------------------------------------------------
circuit = QuantumVolume(qubits, depth, seed=0)
circuit.measure_all()

## TRANSPILE THE FOR CIRCUIT FOR FULL COUPLING MAP --------------------------------------------------------------------------------
coupling_map = CouplingMap.from_full(qubits)
transpiled_circuit = transpile(circuit, sim, coupling_map=coupling_map, optimization_level=0)

## RUN THE SIMULATION -------------------------------------------------------------------------------------------------------------
result_statevec = sim.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enabled=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()

## GATHER THE RESULTS AND PRINT WITH SOME ADDITIONAL METADATA ---------------------------------------------------------------------
input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : qubits, 'Depth' : depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots , 'Device' : sim_device, 'Simulation Method' : sim_method}
if (use_cache_blocking):
    num_processes = 2**(qubits - num_blocking_qubits)
    input_data['Blocking Qubits'] = num_blocking_qubits
    input_data['Num Processes'] = num_processes

dict = result_statevec.to_dict()
meta = dict['metadata']

print(f"{input_data}")
print(f"{meta}")
print(f"-------------------------------------------------------------- \n")
```

Submit the script with `sbatch <script_name>.sh`

### Recommended resource allocation based on number of qubits in your circuit for a "normal" Slurm job. 

Please take note that the recommended nodes are twice the number of minimum resources needed to run a simulation but due to our tests we have found a significant speedup and cost savings of GPU hours if a user submits a job with double the amount of resources that are actually required to simulate a quantum circuit for any specific number of qubits. The Maximum number of qubits that can be simulated using the state_vector simulation method is a theoretical 45 qubits due to the total amount of nodes in the standard-g partition and the amount of system memory in each node. 

| # of Qubits | # of Blocking Qubits | Recommended # of nodes | # gpus-per-node  |
| :-----------| :------------------- | :--------------------: | :--------------: |
| 1           | 0                    | 1                      | 8                |
| 2           | 0                    | 1                      | 8                |
| 3           | 0                    | 1                      | 8                |
| 4           | 0                    | 1                      | 8                |
| .           | 0                    | 1                      | 8                |
| .           | 0                    | 1                      | 8                |
| 28          | 0                    | 1                      | 8                |
| 29          | 0                    | 1                      | 8                |
| 30          | 28                   | 1                      | 8                |
| 31          | 29                   | 1                      | 8                |
| 32          | 29                   | 1                      | 8                |
| 33          | 29                   | 1                      | 8                |
| 34          | 29                   | 1                      | 8                |
| 35          | 29                   | 2                      | 8                |
| 36          | 29                   | 4                      | 8                |
| 37          | 29                   | 8                      | 8                |
| 38          | 29                   | 16                     | 8                |
| 39          | 29                   | 32                     | 8                |
| 40          | 29                   | 64                     | 8                |
| 41          | 29                   | 128                    | 8                |
| 42          | 29                   | 256                    | 8                |
| 43          | 29                   | 512                    | 8                |
| 44          | 29                   | 1024                   | 8                |
| 45*         | 29                   | 2048                   | 8                |
* For a job submitted to LUMI where more than 1024 nodes are required, a special petition must be filed to request the allocation of such resources


## More information

- [Qiskit documentation](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer documentation](https://qiskit.org/ecosystem/aer/tutorials/index.html)
