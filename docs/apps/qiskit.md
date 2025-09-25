---
tags:
  - Free
catalog:
  name: Qiskit
  description: open-source toolkit for useful quantum computing
  description_fi: avoimen lähdekoodin työkalupakki käytännön kvanttilaskentaan
  license_type: Free
  disciplines:
    - Quantum
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Qiskit { #qiskit }

Qiskit on avoimen lähdekoodin ohjelmisto kvanttitietokoneiden kanssa työskentelyyn piirien, pulssien ja algoritmien tasolla.
Tämä sivu sisältää tietoa kvanttisimulaatioiden ajamisesta Qiskitillä Singularity-kontissa.
Fyysisillä kvanttitietokoneilla ajettavista töistä Qiskitillä katso tämä dokumentaatio:
[Running quantum jobs](../computing/quantum-computing/running-quantum-jobs.md).

!!! info "Uutiset"
     **19.02.2025** Asennettu `qiskit/1.3.2` Singularity-konttiin LUMIssa kaikkien keskeisten Qiskit-pakettien kanssa ja
     lisätty tuki monisolmuiseen Native Cray MPI -GPU-kiihdytykseen, mikä mahdollistaa suorituskykyiset monisolmusimulaatiot 
     jopa 44* kubittiin asti. Qiskit-aer on myös päivitetty versioon 0.16

## Saatavilla { #available }

Tällä hetkellä tuetut Qiskit-versiot:

| Versio | Moduuli         | Puhti | Mahti | LUMI  | Huomautukset                     |
| :----- | :-------------- | :---: | :---: | :---: | -------------------------------- |
| 1.1.1  | `qiskit/1.1.1`  |   X   |   X   |       |                                  |
| 1.3.2  |                 |       |       |   X   | Native Cray MPI GPU-tuella       |

Sisältää kaikki keskeiset Qiskit-paketit (Terra, Nature, Aer jne.) sekä GPU-kiihdytyksen. `qiskit/1.1.1`- ja `qiskit/1.3.2`-paketit sisältävät seuraavat Qiskit-liitännäiset:

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

Jos huomaat, että jokin paketti puuttuu, voit usein asentaa sen itse komennolla `pip install --user`.
Katso [Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules) -ohjeestamme
lisätietoja pakettien omatoimisesta asennuksesta. Jos mielestäsi jokin tärkeä
Qiskit-työkalu pitäisi sisällyttää CSC:n tarjoamaan moduuliin, ole hyvä ja
[ota yhteyttä palvelupisteeseemme](../support/contact.md).

Kaikki moduulit perustuvat Apptainer-kontteihin (aiemmin Singularity).
Käytössä on kääreskriptit, joten tavalliset komennot kuten `python`,
`python3`, `pip` ja `pip3` toimivat normaalisti. Lisätietoja:
[CSC:n yleiset ohjeet Apptainer-konttien ajamiseen](../computing/containers/overview.md#running-containers).

## Lisenssi { #license }

Qiskit on lisensoitu
[Apache License 2.0](https://github.com/Qiskit/qiskit-metapackage/blob/master/LICENSE.txt) -lisenssillä.

## Käyttö { #usage }

Käyttääksesi Qiskitin oletusversiota, ota se käyttöön komennolla:

```text
module load qiskit
```

Jos haluat tietyn version ([katso saatavilla olevat versiot yllä](#available)), käytä:

```text
module load qiskit/1.1.1
```

### Esimerkkisbatch- ja Python-skripti – Yhden solmun simulaatiot Puhtilla, Mahtilla ja LUMIlla { #example-sbatch-and-python-script-single-node-simulations-on-puhti-mahti-and-lumi }

Esimerkkiskripti `<sbatch_script_name>.sh` varaa yhden GPU:n ja kaksi CPU-ydintä yhdellä solmulla Puhtilla ja Mahtilla sekä kaikki CPU/GPU-resurssit yhdellä solmulla LUMIn standard-g-osiossa:

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

Esimerkkipython-skripti `<myprog>.py` yhden solmun simulaatioihin. Huomaa, että tämä koodi on vain syntaksin havainnollistamiseksi ja toimii vain yhdellä solmulla. LUMIn simulaatioita varten katso alla olevaa taulukkoa resurssivaatimuksista suhteessa simuloitavien kubittien määrään.

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

Lähetä ajo jonoon komennolla `sbatch <sbatch_script_name>.sh`

### Esimerkkisbatch- ja Python-skripti – Monisolmuiset simulaatiot, jotka hyödyntävät Native HPE Cray MPI:tä GPU-kiihdytyksellä LUMIssa { #example-sbatch-and-python-script-multi-node-simulations-which-leverage-native-hpe-cray-mpi-with-gpu-acceleration-on-lumi }

Esimerkkiskripti `<sbatch_MPI_script_name>.sh` simulaation ajamiseen usealla LUMIn solmulla standard-g-osiossa käyttäen kaikkia GPU:ita ja kaikkia CPU-ytimiä per solmu. Tämä on tarkoitettu simulaatioille, joissa on 35 kubittia tai enemmän (enintään 45* kubittia – katso alla oleva taulukko suositelluista resurssivarauksista haluamasi kubittimäärän mukaan):

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

Pieni koodiesimerkki `<myprog_MPI>.py`-python-skriptistä, joka käyttää 38 kubittia ja jota suosittelemme ajamaan 16 solmulla
*katso suositeltu resurssivaraustaulukko alla

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

Lähetä ajo jonoon komennolla `sbatch <sbatch_MPI_script_name>.sh`

### Ohjeita LUMIn resurssien varaamiseen { #guidelines-for-lumi-resource-allocation }

Statevector-simulaation muistivaatimus kaksinkertaistuu jokaisen lisätyn kubitin myötä. 16 tavun tarkkuudella (qiskit-aerin oletus) LUMI tukee statevector-simulaatioita jopa 34 kubittiin yhdellä solmulla ja jopa 44* kubittiin 1024 solmulla käyttäen cache blocking -tekniikkaa. Cache blocking hyödyntää GPU-muistin hajautettuja muistialueita simulaation rinnakkaistamiseen. Hajautettujen prosessien kokoa määrittää blocking qubits -parametri, joka ei voi olla suurempi kuin yksittäisen välimuistin (cache) koko. LUMIssa välimuistin oletetaan vastaavan yhden GPU:n muistia, eikä blocking qubits -arvon tulisi olla suurempi kuin 29.

Alla oleva taulukko esittää esimerkkiparametreja Quantum Volume -piirin (syvyys 30) simuloimiseksi eri kubittimäärillä LUMIn standard-g-osiossa. Statevectorin muistivaatimus on laskettu 16 tavun tarkkuudella. Solmujen määrä vastaa kahta kertaa statevectorin muistivaatimusta, mikä tuottaa optimaalisen suorituskyvyn varaamalla lisämuistia cache blockingiin hajautettujen prosessien välisen tiedonvaihdon käsittelemiseksi. Huomaa, että nämä parametrit on testattu tietylle piirille. Solmujen määrän muuttaminen tai erilaisten piirien simuloiminen saattaa edellyttää eri blocking qubits -arvoa.

### Muistivaatimukset ja esimerkkiparametrit Quantum Volume -statevector-simulaatiolle, piirin syvyys 30 ja 16 tavun tarkkuus { #memory-requirements-and-example-parameters-for-statevector-simulation-of-quantum-volume-with-circuit-depth-30-and-16-byte-precision }

| # of Qubits | # of Blocking Qubits | Recommended # of nodes | # gpus-per-node | # tasks-per-node | # gpus-per-task | # cpus-per-task | Kubittien muistivaatimukset |
| :-----------| :------------------: | :--------------------: | --------------- | ---------------- | --------------- | --------------- | --------------------------- |
| 1           | 0                    | 1                      | 8               | 1                | 8               | 56              | 32 tavua                    |
| 2           | 0                    | 1                      | 8               | 1                | 8               | 56              | 64                          |
| 3           | 0                    | 1                      | 8               | 1                | 8               | 56              | 128                         |
| 4           | 0                    | 1                      | 8               | 1                | 8               | 56              | 256                         |
| 5           | 0                    | 1                      | 8               | 1                | 8               | 56              | 512                         |
| 6           | 0                    | 1                      | 8               | 1                | 8               | 56              | 1024                        |
| 7           | 0                    | 1                      | 8               | 1                | 8               | 56              | 2 kilotavua                 |
| 8           | 0                    | 1                      | 8               | 1                | 8               | 56              | 4                           |
| 9           | 0                    | 1                      | 8               | 1                | 8               | 56              | 8                           |
| 10          | 0                    | 1                      | 8               | 1                | 8               | 56              | 16                          |
| 11          | 0                    | 1                      | 8               | 1                | 8               | 56              | 32                          |
| 12          | 0                    | 1                      | 8               | 1                | 8               | 56              | 64                          |
| 13          | 0                    | 1                      | 8               | 1                | 8               | 56              | 128                         |
| 14          | 0                    | 1                      | 8               | 1                | 8               | 56              | 256                         |
| 15          | 0                    | 1                      | 8               | 1                | 8               | 56              | 512                         |
| 16          | 0                    | 1                      | 8               | 1                | 8               | 56              | 1024                        |
| 17          | 0                    | 1                      | 8               | 1                | 8               | 56              | 2 megatavua                 |
| 18          | 0                    | 1                      | 8               | 1                | 8               | 56              | 4                           |
| 19          | 0                    | 1                      | 8               | 1                | 8               | 56              | 8                           |
| 20          | 0                    | 1                      | 8               | 1                | 8               | 56              | 16                          |
| 21          | 0                    | 1                      | 8               | 1                | 8               | 56              | 32                          |
| 22          | 0                    | 1                      | 8               | 1                | 8               | 56              | 64                          |
| 23          | 0                    | 1                      | 8               | 1                | 8               | 56              | 128                         |
| 24          | 0                    | 1                      | 8               | 1                | 8               | 56              | 256                         |
| 25          | 0                    | 1                      | 8               | 1                | 8               | 56              | 512                         |
| 26          | 0                    | 1                      | 8               | 1                | 8               | 56              | 1024                        |
| 27          | 0                    | 1                      | 8               | 1                | 8               | 56              | 2 gigatavua                 |
| 28          | 0                    | 1                      | 8               | 1                | 8               | 56              | 4                           |
| 29          | 0                    | 1                      | 8               | 1                | 8               | 56              | 8                           |
| 30          | 29                   | 1                      | 8               | 1                | 8               | 56              | 16                          |
| 31          | 29                   | 1                      | 8               | 1                | 8               | 56              | 32                          |
| 32          | 29                   | 1                      | 8               | 1                | 8               | 56              | 64                          |
| 33          | 29                   | 1                      | 8               | 1                | 8               | 56              | 128                         |
| 34          | 29                   | 1                      | 8               | 1                | 8               | 56              | 256                         |
| 35          | 29                   | 2                      | 8               | 8                | 1               | 7               | 512                         |
| 36          | 29                   | 4                      | 8               | 8                | 1               | 7               | 1024                        |
| 37          | 29                   | 8                      | 8               | 8                | 1               | 7               | 2 teratavua                 |
| 38          | 29                   | 16                     | 8               | 8                | 1               | 7               | 4                           |
| 39          | 29                   | 32                     | 8               | 8                | 1               | 7               | 8                           |
| 40          | 29                   | 64                     | 8               | 8                | 1               | 7               | 16                          |
| 41          | 29                   | 128                    | 8               | 8                | 1               | 7               | 32                          |
| 42          | 29                   | 256                    | 8               | 8                | 1               | 7               | 64                          |
| 43          | 29                   | 512                    | 8               | 8                | 1               | 7               | 128                         |
| 44          | 29                   | 1024                   | 8               | 8                | 1               | 7               | 256                         |

* Jos LUMIin jätetty työ vaatii yli 1024 solmua, tällaisesta resurssivarauksesta on jätettävä erityinen pyyntö (hero-ajo).

### Simulaation ajaminen suuremmilla kuin tehokkailla minimi-LUMI-resursseilla { #using-more-than-the-effective-minimum-lumi-resources-for-a-simulation }

Simulaation suoritusaikaa voidaan nopeuttaa kasvattamalla resurssien määrää yli tehokkaan minimimäärän (joka vastaa statevectorin muistivaatimusta kerrottuna kahdella). Tällöin hajautettujen prosessien (MPI_Ranks) ja varattujen resurssien määrä kannattaa harkita huolellisesti. Blocking qubits tulisi määrittää niin, ettei MPI rankeja ole enempää kuin välimuisteja. Arvioidaksesi työn maksimisolmujen määrää, alla on suuntaa-antavat kaavat.

=== "Number of nodes for multi-node simulation with Cache Blocking Qubits"
    ```bash
    
                Statevector memory required for n-qubits = precision*2^n
      Cache memory required for nc-cache-blocking-qubits = precision*2^nc
      
                                           Max MPI-ranks = (Statevector Memory)/(Cache Memory)
                                           Max MPI-ranks = (precision*2^n)/(precision*2^nc) = 2^(n-nc)
                                           
                                               Max Nodes = (Max MPI-Ranks)/(Tasks Per Node)
    ```

## Lisätietoja { #more-information }

- [* LUMI-hero-ajot](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/hero-runs)
- [LUMIn Slurm-sidontaoptiot MPI-töille](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#slurm-binding-options)
- [Qiskit-Aer: Ajo useilla GPU:illa ja/tai useilla solmuilla](https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html)
- [Cache blocking -tekniikka kvanttilaskennan laajamittaisiin simulaatioihin supertietokoneilla](https://arxiv.org/abs/2102.02957)
- [Qiskit-dokumentaatio](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer-dokumentaatio](https://qiskit.org/ecosystem/aer/tutorials/index.html)