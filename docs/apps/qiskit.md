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
For information pertaining to running jobs on the physical quantum computers using qiskit please refer to this documentation: 
[Running quantum jobs](../computing/quantum-computing/running-quantum-jobs.md).

!!! info "News"
     **19.05.2026** Installed `qiskit/2.3.0` in a singularity container on LUMI with all major Qiskit packages and
     added support for multi-node Native Cray MPI GPU-acceleration allowing for performant multi-node simulations 
     for up to 44* qubits. Qiskit-aer has also been upgraded to 0.17.2. Single precision is now supported in qiskit-aer. 

## Available

Currently supported Qiskit versions:

| Version | Module           | Puhti | Mahti | LUMI  | Notes                            |
| :------ | :--------------- | :---: | :---: | :---: | -------------------------------- |
| 1.1.1   | `qiskit/1.1.1`   |   X   |   X   |       |                                  |
| 2.3.0   | `container only` |       |       |   X   | Native Cray MPI with GPU support |

Includes all the major Qiskit packages (Terra, Nature, Aer, etc.) and GPU acceleration. The `qiskit/1.1.1` and `qiskit/2.3.0` packages include the following qiskit plugins:

=== "Puhti"
    ```bash
    qiskit==1.1.1
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
    qiskit==1.1.1
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
    
=== "LUMI qiskit-aer"
    ```bash
    qiskit==2.3.0
    qiskit-aer-gpu-rocm==0.17.2
    qiskit-dynamics==0.5.1
    qiskit-experiments==0.13.0
    qiskit-finance==0.4.1
    qiskit-ibm-runtime==0.46.1
    qiskit-machine-learning==0.9.0
    qiskit-nature==0.7.2
    qiskit-optimization==0.7.0
    qiskit_qasm3_import==0.6.0
    qiskit_sphinx_theme==2.0.0
    asv==0.6.5
    black==26.3.0
    click==8.3.2
    cmake==4.2.3
    conan==1.66.0
    cotengra==0.7.5
    cotengrust==0.2.0
    cvxpy==1.8.1
    Cython==0.29.37
    ddt==1.7.2
    h5py==3.16.0
    ipympl==0.10.0
    ipywidgets==8.1.8
    isort==8.0.1
    jsonschema==4.26.0
    jupyter==1.1.1
    jupyter-sphinx==0.5.3
    jupyterlab==4.5.5
    kahypar==1.3.7
    line_profiler==5.0.2
    matplotlib==3.10.8
    memory_profiler==0.61.0
    mitiq==1.0.0
    mpi4py==4.0.3
    mypy==1.19.1
    nbconvert==7.17.0
    nbsphinx==0.9.8
    ninja==1.13.0
    numba==0.64.0
    numpy==2.2.6
    opt-einsum==3.4.0
    optuna==3.6.2
    pandas==2.3.3
    Pillow==12.2.0
    pipdeptree==2.31.0
    plotly==6.6.0
    psutil==7.2.2
    pyarrow==23.0.1
    pybind11==3.0.2
    pydantic==2.13.1
    pylatexenc==2.10
    pylint==4.0.5
    pymatching==2.3.1
    pymetis==2025.2.2
    PySCF==2.12.1
    pytest==9.0.2
    pytest-cov==7.0.0
    QCut==1.1.1
    reno==4.1.0
    rich==15.0.0
    rustworkx==0.17.1
    scalene==2.1.4
    scikit-build==0.19.0
    scikit-learn==1.8.0
    scipy==1.17.1
    seaborn==0.13.2
    setuptools==68.1.2
    sparse==0.18.0
    Sphinx==8.2.3
    sphinx-design==0.7.0
    stestr==4.2.1
    stim==1.15.0
    sympy==1.14.0
    tox==4.49.1
    tqdm==4.67.3
    zarr==3.1.5
    ```

=== "LUMI qiskit-aer + ML packages (experimental)"
    ```bash
    qiskit==2.3.0
    qiskit-aer-gpu-rocm==0.17.2
    qiskit-dynamics==0.5.1
    qiskit-experiments==0.13.0
    qiskit-finance==0.4.1
    qiskit-ibm-runtime==0.45.1
    qiskit-machine-learning==0.9.0
    qiskit-nature==0.7.2
    qiskit-optimization==0.7.0
    qiskit_qasm3_import==0.6.0
    qiskit_sphinx_theme==2.0.0
    asv==0.6.5
    black==26.3.0
    click==8.3.2
    cmake==4.2.3
    conan==1.66.0
    cotengra==0.7.5
    cotengrust==0.2.0
    cvxpy==1.8.1
    Cython==0.29.37
    ddt==1.7.2
    duckdb==1.5.2
    gymnasium==1.2.3
    h5py==3.16.0
    hdbscan==0.8.42
    ipympl==0.10.0
    ipywidgets==8.1.8
    isort==8.0.1
    jsonschema==4.26.0
    jupyter==1.1.1
    jupyter-sphinx==0.5.3
    jupyterlab==4.5.5
    kahypar==1.3.7
    lightgbm==4.6.0
    line_profiler==5.0.2
    matplotlib==3.10.8
    memory_profiler==0.61.0
    mitiq==1.0.0
    mpi4py==4.0.3
    mypy==1.19.1
    nbconvert==7.17.0
    nbsphinx==0.9.8
    ninja==1.13.0
    numba==0.64.0
    numpy==2.2.6
    onnxruntime==1.25.0
    opt-einsum==3.4.0
    optuna==3.6.2
    pandas==2.3.3
    pennylane==0.44.1
    pennylane-qiskit==0.44.1
    Pillow==12.2.0
    pipdeptree==2.31.0
    plotly==6.6.0
    polars==1.40.1
    psutil==7.2.2
    pyarrow==23.0.1
    pybind11==3.0.2
    pydantic==2.13.1
    pylatexenc==2.10
    pylint==4.0.5
    pymatching==2.3.1
    pymetis==2025.2.2
    PySCF==2.12.1
    pytest==9.0.2
    pytest-cov==7.0.0
    QCut==1.1.1
    reno==4.1.0
    rich==15.0.0
    rustworkx==0.17.1
    scalene==2.1.4
    scikit-build==0.19.0
    scikit-learn==1.8.0
    scipy==1.17.1
    seaborn==0.13.2
    setuptools==68.1.2
    sparse==0.18.0
    Sphinx==8.2.3
    sphinx-design==0.7.0
    stable-baselines3==2.8.0
    statsmodels==0.14.6
    stestr==4.2.1
    stim==1.15.0
    sympy==1.13.1
    torch==2.5.1+rocm6.2
    torch-geometric==2.7.0
    torchaudio==2.5.1+rocm6.2
    torchinfo==1.8.0
    torchvision==0.20.1+rocm6.2
    tox==4.49.1
    tqdm==4.67.3
    umap-learn==0.5.12
    wandb==0.26.1
    xgboost==3.2.0
    zarr==3.1.5
    ```

If you find that some package is missing, you can often install it yourself with `pip install --user`.
Please see our [Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules) for
more information on how to install packages yourself. If you think that some important
Qiskit-related package should be included in the module provided by CSC, please
[contact our servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known as Singularity).
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[CSC's general instructions on how to run Apptainer containers](../computing/containers/overview.md#running-containers).

## License

Qiskit is licensed under
[Apache License 2.0](https://github.com/Qiskit/qiskit-metapackage/blob/master/LICENSE.txt).

## Usage

To use the default version of Qiskit on Puhti or Mahti, initialize
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

=== "LUMI qiskit-aer"

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
    
    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_2.3.0_csc.sif
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

=== "LUMI qiskit-aer + ML packages (experimental)"

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
    
    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_2.3.0_hpcqc-ml-training_csc.sif
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
    from qiskit import transpile
    from qiskit_aer import AerSimulator
    from qiskit.circuit.library import quantum_volume

    ## CHOOSE PARAMETERS
    num_qubits = 34                       # Number of qubits in the circuit
    circuit_depth = 30                    # Layers in quantum volume circuit
    num_shots = 1000                      # How many times we sample the circuit
    sim_method = 'statevector'            # Choosing simulation method
    sim_device = 'GPU'                    # Choose whether simulation is run on CPUs or GPUs
    sim_precision = 'double'              # 'single' (8 bytes/amplitude) or 'double' (16 bytes/amplitude, default).
                                          # Single halves memory and can improve GPU performance, at the cost of accuracy.
    use_cache_blocking = True             # Cache blocking technique parallelizes simulation by distributing quantum states into distributed memory space
    num_blocking_qubits = 29              # Defines chunk size for cache blocking. Must be smaller than "qubits-log2(number-of-processes)".
                                          # Use 28 with single precision; use 29 with double precision (see notes below).
    use_batched_shots = True              # Distributing shots to multiple processess
    num_parallel_experiments = 1          # Does not seem to do anything when running with MPI, probably intended to be used with multithreading

    ## INITIALIZE SIMULATOR BACKEND
    # fusion_enable combines consecutive gates into single multi-qubit gate operations,
    # reducing the total number of gate applications.
    simulator = AerSimulator(
        method=sim_method,
        device=sim_device,
        batched_shots_gpu=use_batched_shots,
        fusion_enable=True,
        fusion_max_qubit=5,
    )
    simulator.set_options(precision=sim_precision)

    ## CREATE QUANTUM VOLUME CIRCUIT
    # Note: the QuantumVolume class was deprecated in Qiskit 2.x and removed in 3.0.
    # Use the quantum_volume function instead.
    circuit = quantum_volume(num_qubits, circuit_depth, seed=0)
    circuit.measure_all()

    ## TRANSPILE THE CIRCUIT
    # Note: in Qiskit 2.x, do NOT pass the AerSimulator backend to transpile() — it triggers
    # coupling map validation that rejects circuits with more than 34 qubits. MPI distribution
    # and cache blocking are handled at sim.run() time, not at transpile time.
    transpiled_circuit = transpile(circuit, optimization_level=0)

    ## RUN THE SIMULATION
    result_statevec = simulator.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enable=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()

    ## GATHER THE RESULTS AND SOME ADDITIONAL METADATA
    counts = result_statevec.get_counts()
    result_dict = result_statevec.to_dict()
    metadata = result_dict['metadata']
    input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : num_qubits, 'Depth' : circuit_depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots, 'Device' : sim_device, 'Simulation Method' : sim_method, 'Precision' : sim_precision}
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

Example `<sbatch_MPI_script_name>.sh` script for running a simulation on multiple LUMI nodes in the standard-g partition using all GPUs and all CPU cores on a node. This is for simulations involving 35 qubits or more (up to a maximum 44* qubits - see table below for recommended resource allocations based on amount of qubits you wish to simulate ):

=== "LUMI qiskit-aer"

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

    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_2.3.0_csc.sif
    export GPU_WRAPPER_PATH=/appl/local/quantum/qiskit/run-singularity-with-gpu-affinity

    mask=mask_cpu:0xfe000000000000,0xfe00000000000000,0xfe0000,0xfe000000,0xfe,0xfe00,0xfe00000000,0xfe0000000000

    ## HPE Cray MPI optimizations for multi-node GPU simulations
    export MPICH_GPU_SUPPORT_ENABLED=1
    export MPICH_GPU_IPC_CACHE_MAX_SIZE=100
    export MPICH_GPU_IPC_THRESHOLD=524288
    export MPICH_OFI_NIC_POLICY=GPU

    srun --cpu-bind=$mask $GPU_WRAPPER_PATH $LUMI_QISKIT_SINGULARITY_CONTAINER_PATH python myprog_MPI.py
    ```

=== "LUMI qiskit-aer + ML packages (experimental)"

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

    export LUMI_QISKIT_SINGULARITY_CONTAINER_PATH=/appl/local/quantum/qiskit/qiskit_2.3.0_hpcqc-ml-training_csc.sif
    export GPU_WRAPPER_PATH=/appl/local/quantum/qiskit/run-singularity-with-gpu-affinity

    mask=mask_cpu:0xfe000000000000,0xfe00000000000000,0xfe0000,0xfe000000,0xfe,0xfe00,0xfe00000000,0xfe0000000000

    ## HPE Cray MPI optimizations for multi-node GPU simulations
    export MPICH_GPU_SUPPORT_ENABLED=1
    export MPICH_GPU_IPC_CACHE_MAX_SIZE=100
    export MPICH_GPU_IPC_THRESHOLD=524288
    export MPICH_OFI_NIC_POLICY=GPU

    srun --cpu-bind=$mask $GPU_WRAPPER_PATH $LUMI_QISKIT_SINGULARITY_CONTAINER_PATH python myprog_MPI.py
    ```

Small code example of `<myprog_MPI>.py` python script using 38 qubits which we recommend running on 16 nodes 
*reference recommended resource allocation table below

=== "LUMI"

    ```Python
    from qiskit import transpile
    from qiskit_aer import AerSimulator
    from qiskit.circuit.library import quantum_volume

    ## CHOOSE PARAMETERS
    num_qubits = 38                       # Number of qubits in the circuit
    circuit_depth = 30                    # Layers in quantum volume circuit
    num_shots = 1000                      # How many times we sample the circuit
    sim_method = 'statevector'            # Choosing simulation method
    sim_device = 'GPU'                    # Choose whether simulation is run on CPUs or GPUs
    sim_precision = 'double'              # 'single' (8 bytes/amplitude) or 'double' (16 bytes/amplitude, default).
                                          # Single halves memory and can improve GPU performance, at the cost of accuracy.
    use_cache_blocking = True             # Cache blocking technique parallelizes simulation by distributing quantum states into distributed memory space
    num_blocking_qubits = 29              # Defines chunk size for cache blocking. Must be smaller than "qubits-log2(number-of-processes)".
                                          # Use 28 with single precision; use 29 with double precision (see notes below).
    use_batched_shots = True              # Distributing shots to multiple processess
    num_parallel_experiments = 1          # Does not seem to do anything when running with MPI, probably intended to be used with multithreading

    ## INITIALIZE SIMULATOR BACKEND
    # fusion_enable combines consecutive gates into single multi-qubit gate operations,
    # reducing the total number of gate applications.
    simulator = AerSimulator(
        method=sim_method,
        device=sim_device,
        batched_shots_gpu=use_batched_shots,
        fusion_enable=True,
        fusion_max_qubit=5,
    )
    simulator.set_options(precision=sim_precision)

    ## CREATE QUANTUM VOLUME CIRCUIT
    # Note: the QuantumVolume class was deprecated in Qiskit 2.x and removed in 3.0.
    # Use the quantum_volume function instead.
    circuit = quantum_volume(num_qubits, circuit_depth, seed=0)
    circuit.measure_all()

    ## TRANSPILE THE CIRCUIT
    # Note: in Qiskit 2.x, do NOT pass the AerSimulator backend to transpile() — it triggers
    # coupling map validation that rejects circuits with more than 34 qubits. MPI distribution
    # and cache blocking are handled at sim.run() time, not at transpile time.
    transpiled_circuit = transpile(circuit, optimization_level=0)

    ## RUN THE SIMULATION
    result_statevec = simulator.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enable=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()

    ## GATHER THE RESULTS AND SOME ADDITIONAL METADATA
    counts = result_statevec.get_counts()
    result_dict = result_statevec.to_dict()
    metadata = result_dict['metadata']
    input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : num_qubits, 'Depth' : circuit_depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots, 'Device' : sim_device, 'Simulation Method' : sim_method, 'Precision' : sim_precision}
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

### Memory requirements and example parameters

The memory required for a statevector simulation **doubles for every qubit added**. With the default 16-byte (double) precision, LUMI supports statevector simulations up to **34 qubits on a single node**, and up to **44* qubits on 1024 nodes** using the cache blocking technique. Cache blocking distributes the quantum state across distributed GPU memory to parallelize the simulation; the chunk size on each MPI rank is set by the `blocking_qubits` parameter, which in good practice should be less than 25% of the VRAM on a single GCD. On LUMI, that means blocking_qubits should not be larger than 29: with double precision, blocking_qubits = 29 produces an 8 GB chunk (16 × 2²⁹ bytes), which is 12.5% of a 64 GB MI250X GCD — comfortably under the 25% threshold.

The table below shows example parameters for simulating a Quantum Volume circuit with double precision. Statevector memory depends only on qubit count, not on circuit depth, so the memory column is depth-independent. Recommended node counts correspond to roughly **twice the statevector memory**, leaving headroom for cache-blocking data exchange between processes. These values were benchmarked on Quantum Volume circuits at depths of 10, 30, 100, and 300 and held up across all of them — see [LUMI quantum simulations with qiskit-aer](https://fiqci.fi/publications/2025-04-01-LUMI-quantum-simulations-qiskit-aer) for the full results. Other circuit families, or running the same circuit on a different number of nodes, may still require different blocking-qubit values.

With single precision, the same resources will run faster; alternatively, you can simulate the same number of qubits with roughly **half the nodes** shown below (and `blocking_qubits = 28` instead of 29).

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
- [LUMI quantum simulations with qiskit-aer — benchmarks across multiple QV depths](https://fiqci.fi/publications/2025-04-01-LUMI-quantum-simulations-qiskit-aer)
- [Qiskit-Aer Running with multiple-GPUs and/or multiple nodes](https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html)
- [Qiskit-Aer AerSimulator API reference (blocking_qubits memory rule)](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)
- [Cache Blocking Technique to Large Scale Quantum Computing Simulation on Supercomputers](https://arxiv.org/abs/2102.02957)
- [Qiskit documentation](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer documentation](https://qiskit.org/ecosystem/aer/tutorials/index.html)
