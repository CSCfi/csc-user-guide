---
tags:
  - Free
---

# Qiskit

Qiskit is an open-source software for working with quantum computers at the level
of circuits, pulses, and algorithms. This page contains information in regard to running Quantum simulations using qiskit inside of a singularity container.
For information pertaining to running jobs on Helmi using qiskit please refer to this documentation: 
[Running on Helmi](../computing/quantum-computing/helmi/running-on-helmi.md).

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

=== "Puhti"
    ```bash
    qiskit=1.1.1
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
    
=== "Mahti"
    ```bash
    qiskit=1.1.1
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
    
=== "LUMI"
    ```bash
    qiskit=1.2.4
    qiskit-aer-gpu>=0.15.1
    qiskit-algorithms==0.3.1
    qiskit-dynamics==0.5.1
    qiskit-experiments==0.8.0
    qiskit-finance==0.4.1
    qiskit-ibm-experiment==0.4.8
    qiskit-machine-learning==0.8.0
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

### Example sbatch and python script - Single-node simulations on Puhti, Mahti, and LUMI

Example `<sbatch_script_name>.sh` script for reserving one GPU and two CPU cores in a single node for Puhti and Mahti and all CPU/GPU resources on a single node using the LUMI standard-g partition:

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --job-name=aer_job
    #SBATCH --output=aer_job.o%j
    #SBATCH --error=aer_job.e%j
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
    #SBATCH --job-name=aer_job
    #SBATCH --output=aer_job.o%j
    #SBATCH --error=aer_job.e%j
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
    #SBATCH --job-name=aer_job
    #SBATCH --output=aer_job.o%j
    #SBATCH --error=aer_job.e%j
    #SBATCH --account=<project_id>
    #SBATCH --time=2:00:00
    #SBATCH --partition=standard-g
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=56
    
    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_1.2.4_csc.sif
    export WRAPPER_PATH=/appl/local/quantum/qiskit/run-singularity
    
    echo "NODES                   : ${SLURM_NNODES}"
    echo "TASKS PER NODE          : ${SLURM_NTASKS_PER_NODE}"
    echo "CPUS PER TASK           : ${SLURM_CPUS_PER_TASK}"
    echo "GPUS PER NODE           : ${SLURM_GPUS_PER_NODE}"
    echo "GPUS PER TASK           : ${SLURM_GPUS_PER_TASK}"
    
    mask=mask_cpu:0xfe000000000000,0xfe00000000000000,0xfe0000,0xfe000000,0xfe,0xfe00,0xfe00000000,0xfe0000000000
    export MPICH_GPU_SUPPORT_ENABLED=1
    
    srun --cpu-bind=$mask $WRAPPER_PATH $LUMI_QISKIT_SINGULARITY_CONTAINER_PATH python myprog.py
    ```

Example `<myprog>.py` python script for single node simulations. Do note that this code is just to highlight the syntax and only works on a single node. For LUMI simulations, reference the table below for resource requirements relative to the amount of qubits you wish to simulate.

=== "Puhti"
    ```Python
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    
    ## CHOOSE PARAMETERS
    num_qubits = 5              # Number of qubits in the circuit
    num_shots = 1000            # How many times we sample the circuit
    
    ## CREATE CIRCUIT FOR N-QUBIT GHZ-STATE
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)
    for i in range(1,num_qubits):
        circuit.cx(0,i)
    circuit.measure_all()
    
    ## INITIALIZE SIMULATOR BACKEND THAT RUNS ON GPU
    simulator = AerSimulator(method="statevector", device="GPU")
    
    ## RUN THE CIRCUIT WITH CUSTATEVEC ENABLED
    result_statevec = simulator.run(circuit, shots=num_shots, seed_simulator=12345, cuStateVec_enable=True).result()
    
    ## PRINT RESULTS
    counts = result_statevec.get_counts()
    print(f"Counts:, {counts}")
    ```

=== "Mahti"
    ```Python
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    
    ## CHOOSE PARAMETERS
    num_qubits = 5              # Number of qubits in the circuit
    num_shots = 1000            # How many times we sample the circuit
    
    ## CREATE CIRCUIT FOR N-QUBIT GHZ-STATE
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)
    for i in range(1,num_qubits):
        circuit.cx(0,i)
    circuit.measure_all()
    
    ## INITIALIZE SIMULATOR BACKEND THAT RUNS ON GPU
    simulator = AerSimulator(method="statevector", device="GPU")
    
    ## RUN THE CIRCUIT WITH CUSTATEVEC ENABLED
    result_statevec = simulator.run(circuit, shots=num_shots, seed_simulator=12345, cuStateVec_enable=True).result()
    
    ## PRINT RESULTS
    counts = result_statevec.get_counts()
    print(f"Counts:, {counts}")
    ```

=== "LUMI"
    ```Python
    from qiskit import QuantumCircuit, transpile
    from qiskit.transpiler import CouplingMap
    from qiskit_aer import AerSimulator
    from qiskit.circuit.library import QuantumVolume
    
    ## CHOOSE PARAMETERS
    num_qubits = 34                       # Number of qubits in the circuit
    circuit_depth = 30                    # Layers in quantum volume circuit
    num_shots = 1000                      # How many times we sample the circuit
    sim_method = 'statevector'            # Choosing simulation method
    sim_device = 'GPU'                    # Choose whether simulation is run on CPUs or GPUs
    use_cache_blocking = True             # Cache blocking technique parallelizes simulation by distributing quantum states into distributed memory space
    num_blocking_qubits = 29              # Defines chunk size for cache blocking. Must be smaller than "qubits-log2(number-of-processes)"
    use_batched_shots = True              # Distributing shots to multiple processess
    num_parallel_experiments = 1          # Does not seem to do anything when running with MPI, probably intended to be used with multithreading
    
    ## INITIALIZE SIMULATOR BACKEND
    simulator = AerSimulator(method=sim_method, device=sim_device, batched_shots_gpu=use_batched_shots)
    
    ## CREATE QUANTUM VOLUME CIRCUIT
    circuit = QuantumVolume(num_qubits, circuit_depth, seed=0)
    circuit.measure_all()
    
    ## TRANSPILE THE CIRCUIT FOR SPECIFIC COUPLING MAP
    coupling_map = CouplingMap.from_full(num_qubits)
    transpiled_circuit = transpile(circuit, simulator, coupling_map=coupling_map, optimization_level=0)
    
    ## RUN THE SIMULATION
    result_statevec = simulator.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enabled=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()
    
    ## GATHER THE RESULTS AND SOME ADDITIONAL METADATA
    counts = result_statevec.get_counts()
    result_dict = result_statevec.to_dict()
    metadata = result_dict['metadata']
    input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : num_qubits, 'Depth' : circuit_depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots , 'Device' : sim_device, 'Simulation Method' : sim_method}
    if (use_cache_blocking):
        num_chunks = 2**(num_qubits - num_blocking_qubits)
        input_data['Blocking Qubits'] = num_blocking_qubits
        input_data['Number of Chunks'] = num_chunks
    
    
    ## PRINT FOR ONE MPI RANK
    if (metadata['mpi_rank'] == 0):
        print()
        print(f"Input data: {input_data}")
        print(f"Metadata: {metadata}")
        #print(f"Results: {counts}")
        print(f"-------------------- \n")
    
    ## PRINT ALL MPI PROCESSES
    #print(f"Input data: {input_data}")
    #print(f"Metadata: {metadata}")
    #print(f"-------------------- \n")
    ```

Submit the script with `sbatch <sbatch_script_name>.sh`

### Example sbatch and python script - Multi-node simulations which leverage Native HPE Cray MPI with GPU acceleration on LUMI

Example `<sbatch_MPI_script_name>.sh` script for running a simulation on multiple LUMI nodes in the standard-g partition using all GPUs and all CPU cores on a node. This is for simulations involving 35 qubits or more (up to a maximum 45* qubits - see table below for recommended resource allocations based on amount of qubits you wish to simulate ):

=== "LUMI"
    ```bash
    #!/bin/bash
    ## Here is an example sbatch script for a 38 qubit quantum volume simulation (myprog_MPI.py) using 16 nodes 
    #SBATCH --job-name=aer_job
    #SBATCH --output=aer_job.o%j
    #SBATCH --error=aer_job.e%j
    #SBATCH --account=<project_id>
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

Small code example of `<myprog_MPI>.py` python script using 38 qubits which we recommend running on 16 nodes 
*reference recommended resource allocation table below

=== "LUMI"
    ```Python
    from qiskit import QuantumCircuit, transpile
    from qiskit.transpiler import CouplingMap
    from qiskit_aer import AerSimulator
    from qiskit.circuit.library import QuantumVolume
    
    ## CHOOSE PARAMETERS
    num_qubits = 38                       # Number of qubits in the circuit
    circuit_depth = 30                    # Layers in quantum volume circuit
    num_shots = 1000                      # How many times we sample the circuit
    sim_method = 'statevector'            # Choosing simulation method
    sim_device = 'GPU'                    # Choose whether simulation is run on CPUs or GPUs
    use_cache_blocking = True             # Cache blocking technique parallelizes simulation by distributing quantum states into distributed memory space
    num_blocking_qubits = 29              # Defines chunk size for cache blocking. Must be smaller than "qubits-log2(number-of-processes)"
    use_batched_shots = True              # Distributing shots to multiple processess
    num_parallel_experiments = 1          # Does not seem to do anything when running with MPI, probably intended to be used with multithreading
    
    ## INITIALIZE SIMULATOR BACKEND
    simulator = AerSimulator(method=sim_method, device=sim_device, batched_shots_gpu=use_batched_shots)
    
    ## CREATE QUANTUM VOLUME CIRCUIT
    circuit = QuantumVolume(num_qubits, circuit_depth, seed=0)
    circuit.measure_all()
    
    ## TRANSPILE THE CIRCUIT FOR SPECIFIC COUPLING MAP
    coupling_map = CouplingMap.from_full(num_qubits)
    transpiled_circuit = transpile(circuit, simulator, coupling_map=coupling_map, optimization_level=0)
    
    ## RUN THE SIMULATION
    result_statevec = simulator.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enabled=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()
    
    ## GATHER THE RESULTS AND SOME ADDITIONAL METADATA
    counts = result_statevec.get_counts()
    result_dict = result_statevec.to_dict()
    metadata = result_dict['metadata']
    input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : num_qubits, 'Depth' : circuit_depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots , 'Device' : sim_device, 'Simulation Method' : sim_method}
    if (use_cache_blocking):
        num_chunks = 2**(num_qubits - num_blocking_qubits)
        input_data['Blocking Qubits'] = num_blocking_qubits
        input_data['Number of Chunks'] = num_chunks
    
    
    ## PRINT FOR ONE MPI RANK
    if (metadata['mpi_rank'] == 0):
        print()
        print(f"Input data: {input_data}")
        print(f"Metadata: {metadata}")
        #print(f"Results: {counts}")
        print(f"-------------------- \n")

    ## PRINT ALL MPI PROCESSES
    #print(f"Input data: {input_data}")
    #print(f"Metadata: {metadata}")
    #print(f"-------------------- \n")
    ```

Submit the script with `sbatch <sbatch_MPI_script_name>.sh`

### Recommended LUMI resource allocation table 

Please take note that the recommended nodes are twice the number of minimum resources needed to run a simulation but due to our tests we have found a significant speedup and cost savings of GPU hours if a user submits a job with double the amount of resources that are actually required to simulate a quantum circuit for any specific number of qubits. The Maximum number of qubits that can be simulated using the state_vector simulation method is a theoretical 45 qubits due to the total amount of nodes in the standard-g partition and the amount of system memory in each node. 

| # of Qubits | # of Blocking Qubits | Recommended # of nodes | # gpus-per-node  |
| :-----------| :------------------: | :--------------------: | ---------------- |
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

- [LUMI Slurm binding options for MPI jobs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#slurm-binding-options)
- [Qiskit-Aer Running with multiple-GPUs and/or multiple nodes](https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html)
- [Cache Blocking Technique to Large Scale Quantum Computing Simulation on Supercomputers](https://arxiv.org/abs/2102.02957)
- [Qiskit documentation](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer documentation](https://qiskit.org/ecosystem/aer/tutorials/index.html)
