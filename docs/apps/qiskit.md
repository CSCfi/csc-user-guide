---
tags:
  - Free
catalog:
  name: Qiskit
  description: open-source toolkit for useful quantum computing
  license_type: Free
  disciplines:
    - Quantum
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Qiskit

Qiskit is an open-source software for working with quantum computers at the level of circuits, pulses, and algorithms. 
This page contains information in regard to running Quantum simulations using qiskit inside of a singularity container.
For information pertaining to running jobs on Helmi using qiskit please refer to this documentation: 
[Running on Helmi](../computing/quantum-computing/helmi/running-on-helmi.md).

!!! info "News"
     **19.02.2025** Installed `qiskit/1.3.2` in a singularity container on LUMI with all major Qiskit packages and
     added support for multi-node Native Cray MPI GPU-acceleration allowing for performant multi node simulations. 
     for up to 44* qubits. Qiskit-aer has also been upgraded to 0.16

## Available

Currently supported Qiskit versions:

| Version | Module          | Puhti | Mahti | LUMI  | Notes                            |
| :------ | :-------------- | :---: | :---: | :---: | -------------------------------- |
| 1.1.1   | `qiskit/1.1.1`  |   X   |   X   |       |                                  |
| 1.3.2   |                 |       |       |   X   | Native Cray MPI with GPU support |

Includes all the major Qiskit packages (Terra, Nature, Aer, etc.) and GPU acceleration. The `qiskit/1.1.1` and `qiskit/1.3.2` packages include the following qiskit plugins:

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
    qiskit==1.3.2
    qiskit-aer-gpu==0.16.0
    qiskit-algorithms==0.3.1
    qiskit-dynamics==0.5.1
    qiskit-experiments==0.8.1
    qiskit-finance==0.4.1
    qiskit-ibm-experiment==0.4.8
    qiskit-machine-learning==0.8.2
    qiskit-nature==0.7.2
    qiskit-optimization==0.6.1
    qiskit_qasm3_import==0.5.1
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
    
    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_1.3.2_csc.sif
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
    
    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_1.3.2_csc.sif
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

### Guidelines for LUMI resource allocation

The required memory for running statevector simulation is doubled for every qubit added. Using 16-byte precision (default for qiskit-aer), LUMI supports statevector simulations up to 34 qubits using a single node, and up to 44* qubits using 1024 nodes with cache blocking technique. Cache blocking utilizes distributed memory spaces of GPU memory to parallelize the simulation. The size of distributed processes is defined by blocking qubits parameters, which cannot be larger than the size of a single cache. In LUMI, the cache should correspond to the memory of a single GPU, and blocking qubits should not be larger than 29.

The table below showcases example parameters for simulating a Quantum Volume circuit of depth 30 with different numbers of qubits on a LUMI standard-g partition. The statevector required memory is calculated for 16-byte precision. The amount of nodes used corresponds to twice the amount of memory required by the statevector, which results in optimal performance by reserving additional memory for cache blocking to handle data exchange between distributed processes. Please take note that these parameters were tested for a specific circuit. Changing the number of nodes or simulating different circuits might require specifying different amounts of blocking qubits.

### Memory requirements and example parameters for statevector simulation of quantum volume with circuit depth 30 and 16 byte precision

| # of Qubits | # of Blocking Qubits | Recommended # of nodes | # gpus-per-node | # tasks-per-node | # gpus-per-task | # cpus-per-task | Qubit memory requirements | 
| :-----------| :------------------: | :--------------------: | --------------- | ---------------- | --------------- | --------------- | ------------------------- |
| 1           | 0                    | 1                      | 8               | 1                | 8               | 56              | 32 Bytes                  |
| 2           | 0                    | 1                      | 8               | 1                | 8               | 56              | 64                        |
| 3           | 0                    | 1                      | 8               | 1                | 8               | 56              | 128                       |
| 4           | 0                    | 1                      | 8               | 1                | 8               | 56              | 256                       |
| 5           | 0                    | 1                      | 8               | 1                | 8               | 56              | 512                       |
| 6           | 0                    | 1                      | 8               | 1                | 8               | 56              | 1024                      |
| 7           | 0                    | 1                      | 8               | 1                | 8               | 56              | 2 Kilobytes               |
| 8           | 0                    | 1                      | 8               | 1                | 8               | 56              | 4                         |
| 9           | 0                    | 1                      | 8               | 1                | 8               | 56              | 8                         |
| 10          | 0                    | 1                      | 8               | 1                | 8               | 56              | 16                        |
| 11          | 0                    | 1                      | 8               | 1                | 8               | 56              | 32                        |
| 12          | 0                    | 1                      | 8               | 1                | 8               | 56              | 64                        |
| 13          | 0                    | 1                      | 8               | 1                | 8               | 56              | 128                       |
| 14          | 0                    | 1                      | 8               | 1                | 8               | 56              | 256                       |
| 15          | 0                    | 1                      | 8               | 1                | 8               | 56              | 512                       |
| 16          | 0                    | 1                      | 8               | 1                | 8               | 56              | 1024                      |
| 17          | 0                    | 1                      | 8               | 1                | 8               | 56              | 2 Megabytes               |
| 18          | 0                    | 1                      | 8               | 1                | 8               | 56              | 4                         |
| 19          | 0                    | 1                      | 8               | 1                | 8               | 56              | 8                         |
| 20          | 0                    | 1                      | 8               | 1                | 8               | 56              | 16                        |
| 21          | 0                    | 1                      | 8               | 1                | 8               | 56              | 32                        |
| 22          | 0                    | 1                      | 8               | 1                | 8               | 56              | 64                        |
| 23          | 0                    | 1                      | 8               | 1                | 8               | 56              | 128                       |
| 24          | 0                    | 1                      | 8               | 1                | 8               | 56              | 256                       |
| 25          | 0                    | 1                      | 8               | 1                | 8               | 56              | 512                       |
| 26          | 0                    | 1                      | 8               | 1                | 8               | 56              | 1024                      |
| 27          | 0                    | 1                      | 8               | 1                | 8               | 56              | 2 Gigabytes               |
| 28          | 0                    | 1                      | 8               | 1                | 8               | 56              | 4                         |
| 29          | 0                    | 1                      | 8               | 1                | 8               | 56              | 8                         |
| 30          | 29                   | 1                      | 8               | 1                | 8               | 56              | 16                        |
| 31          | 29                   | 1                      | 8               | 1                | 8               | 56              | 32                        |
| 32          | 29                   | 1                      | 8               | 1                | 8               | 56              | 64                        |
| 33          | 29                   | 1                      | 8               | 1                | 8               | 56              | 128                       |
| 34          | 29                   | 1                      | 8               | 1                | 8               | 56              | 256                       |
| 35          | 29                   | 2                      | 8               | 8                | 1               | 7               | 512                       |
| 36          | 29                   | 4                      | 8               | 8                | 1               | 7               | 1024                      |
| 37          | 29                   | 8                      | 8               | 8                | 1               | 7               | 2 Terabytes               |
| 38          | 29                   | 16                     | 8               | 8                | 1               | 7               | 4                         |
| 39          | 29                   | 32                     | 8               | 8                | 1               | 7               | 8                         |
| 40          | 29                   | 64                     | 8               | 8                | 1               | 7               | 16                        |
| 41          | 29                   | 128                    | 8               | 8                | 1               | 7               | 32                        |
| 42          | 29                   | 256                    | 8               | 8                | 1               | 7               | 64                        |
| 43          | 29                   | 512                    | 8               | 8                | 1               | 7               | 128                       |
| 44          | 29                   | 1024                   | 8               | 8                | 1               | 7               | 256                       |

* For a job submitted to LUMI where more than 1024 nodes are required, a special petition for a hero run must be filed to request the allocation of such resources.

### Using more than the effective minimum LUMI resources for a simulation

It is possible to speed up the execution time for a simulation by increasing the number of resources beyond the effective minimum number of nodes, which corresponds to double the statevector memory requirements. In such cases, the number of distributed processes (MPI_Ranks) and allocated resources should be carefully considered. Blocking qubits should be specified so that there are no more MPI ranks than there are caches. In order to obtain an estimate of the max # of nodes for a job, we have the below formulas as a guideline.

=== "Number of nodes for multi-node simulation with Cache Blocking Qubits"
    ```bash
    
                Statevector memory required for n-qubits = precision*2^n
      Cache memory required for nc-cache-blocking-qubits = precision*2^nc
      
                                           Max MPI-ranks = (Statevector Memory)/(Cache Memory)
                                           Max MPI-ranks = (precision*2^n)/(precision*2^nc) = 2^(n-nc)
                                           
                                               Max Nodes = (Max MPI-Ranks)/(Tasks Per Node)
    ```


## More information

- [* LUMI Full Machine Runs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/hero-runs)
- [LUMI Slurm binding options for MPI jobs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#slurm-binding-options)
- [Qiskit-Aer Running with multiple-GPUs and/or multiple nodes](https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html)
- [Cache Blocking Technique to Large Scale Quantum Computing Simulation on Supercomputers](https://arxiv.org/abs/2102.02957)
- [Qiskit documentation](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer documentation](https://qiskit.org/ecosystem/aer/tutorials/index.html)
