
---
tags:
  - Free
---

# Qiskit

Qiskit on avoimen lähdekoodin ohjelmisto, joka on suunniteltu kvanttitietokoneiden käyttöön piirien, pulssejen ja algoritmien tasolla.
Tämä sivu sisältää tietoa kvanttisimulaatioiden suorittamisesta qiskit-ympäristössä singularity-kontissa. Lisätietoa qiskit:n avulla suoritettavista työajoista Helmillä: [Ajo Helmillä](../computing/quantum-computing/helmi/running-on-helmi.md).

!!! info "Uutiset"
     **19.02.2025** Asennettu `qiskit/1.3.2` singularity-konttiin LUMI:lle sisältäen kaikki merkittävät Qiskit-paketit, sekä lisätty tuki monisolmuisille Native Cray MPI GPU-kiihdytyksellä mahdollistaen tehokkaat monisolmusimulaatiot jopa 44* kubitille. Qiskit-aer on myös päivitetty versioon 0.16.

## Saatavilla olevat {#available}

Tällä hetkellä tuetut Qiskit-versiot:

| Versio | Moduuli          | Puhti | Mahti | LUMI | Huomiot                              |
| :----- | :--------------- | :---: | :---: | :---:| ------------------------------------- |
| 1.1.1  | `qiskit/1.1.1`   |  X    |  X    |      |                                       |
| 1.3.2  |                  |       |       |  X   | Native Cray MPI GPU-tuella           |

Sisältää kaikki merkittävät Qiskit-paketit (Terra, Nature, Aer, jne.) ja GPU-kiihdytyksen. `qiskit/1.1.1` ja `qiskit/1.3.2` paketit sisältävät seuraavat qiskit-lisäosat:

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

Jos huomaat jonkin paketin puuttuvan, voit usein asentaa sen itse komennolla `pip install --user`.
Katso [Python käyttöoppaamme](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules) saadaksesi lisää tietoa pakettien asentamisesta. Jos uskot, että jokin tärkeä Qiskit-aiheinen paketti tulisi sisällyttää CSC:n tarjoamiin moduuleihin, ole hyvä ja [ota yhteyttä palvelupisteeseemme](../support/contact.md).

Kaikki moduulit perustuvat Apptainer-containereihin (aiemmin tunnettiin nimellä Singularity).
Skriptejä on tarjottu niin, että normaalit komennot kuten `python`, `python3`, `pip` ja `pip3` toimivat kuten tavallista. Lisätietoja [CSC:n yleisestä ohjeistuksesta Apptainer-konttien käyttöön](../computing/containers/run-existing.md).

## Lisenssi {#license}

Qiskit on lisensoitu
[Apache License 2.0:lla](https://github.com/Qiskit/qiskit-metapackage/blob/master/LICENSE.txt).

## Käyttö {#usage}

Oletusversion Qiskitistä käyttääksesi, lataa se komennolla:

```text
module load qiskit
```

Jos haluat tietyn version ([katso yllä olevat saatavilla olevat
versiot](#available)), käytä:

```text
module load qiskit/1.1.1
```

### Esimerkkisbatch ja Python-skripti - Yksisolmuksen simulaatiot Puhtilla, Mahtilla ja LUMIllä {#example-sbatch-and-python-script---single-node-simulations-on-puhti-mahti-and-lumi}

Esimerkki `<sbatch_script_name>.sh` skripti yhden GPU:n ja kahden CPU-ytimen varaamiseen yksisolmulla Puhtilla ja Mahtilla, sekä kaikille CPU/GPU- resursseille yhdellä solmulla LUMI:n standard-g osiossa:

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

Esimerkki `<myprog>.py` Python-skriptistä yksisolmuksille simulaatioille. Huomaa, että tämä koodi on vain syntaksin esilletuontia ja toimii vain yhdellä solmulla. LUMI-simulaatioissa katso alla oleva taulukko resurrsivaatimuksista suhteessa simuloitavien kubittien lukumäärään.

=== "Puhti"
    ```Python
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator

    ## VALITSE PARAMETRIT
    num_qubits = 5              # Piirissä olevien kubittien määrä
    num_shots = 1000            # Kuinka monta kertaa simulaatiota toistetaan

    ## LUO N-KUBITTI GHZ-TILA PIIRI
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)
    for i in range(1,num_qubits):
        circuit.cx(0,i)
    circuit.measure_all()

    ## INIITOI SIMULAATTORIN TAUSTAMOOTTORI JOKA TOIMII GPU:lla
    simulator = AerSimulator(method="statevector", device="GPU")

    ## AJA TAJOUKSET CUSTATEVEC AKTIVOITUNA
    result_statevec = simulator.run(circuit, shots=num_shots, seed_simulator=12345, cuStateVec_enable=True).result()

    ## TULOSTA TULOKSET
    counts = result_statevec.get_counts()
    print(f"Counts:, {counts}")
    ```

=== "Mahti"
    ```Python
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator

    ## VALITSE PARAMETRIT
    num_qubits = 5              # Piirissä olevien kubittien määrä
    num_shots = 1000            # Kuinka monta kertaa simulaatiota toistetaan

    ## LUO N-KUBITTI GHZ-TILA PIIRI
    circuit = QuantumCircuit(num_qubits)
    circuit.h(0)
    for i in range(1,num_qubits):
        circuit.cx(0,i)
    circuit.measure_all()

    ## INIITOI SIMULAATTORIN TAUSTAMOOTTORI JOKA TOIMII GPU:lla
    simulator = AerSimulator(method="statevector", device="GPU")

    ## AJA TAJOUKSET CUSTATEVEC AKTIVOITUNA
    result_statevec = simulator.run(circuit, shots=num_shots, seed_simulator=12345, cuStateVec_enable=True).result()

    ## TULOSTA TULOKSET
    counts = result_statevec.get_counts()
    print(f"Counts:, {counts}")
    ```

=== "LUMI"
    ```Python
    from qiskit import QuantumCircuit, transpile
    from qiskit.transpiler import CouplingMap
    from qiskit_aer import AerSimulator
    from qiskit.circuit.library import QuantumVolume

    ## VALITSE PARAMETRIT
    num_qubits = 34                       # Piirissä olevien kubittien määrä
    circuit_depth = 30                    # Kvanttitilavuuspiirin syvyys
    num_shots = 1000                      # Kuinka monta kertaa simulaatiota toistetaan
    sim_method = 'statevector'            # Valitse simulaatiomenetelmä
    sim_device = 'GPU'                    # Valitse, ajetaanko simulointi CPU:illa tai GPU:illa
    use_cache_blocking = True             # Cache Blocking tekniikka jakaa yhtenäiset tilat hajautettuun muistialueeseen
    num_blocking_qubits = 29              # Määrittelee lohkokoon cache blockingille. On oltava pienempi kuin "kubitteja-log2(prosessien määrä)"
    use_batched_shots = True              # Jakaa näytteitä useille prosesseille
    num_parallel_experiments = 1          # Ei tunnu vaikuttavan kenttään MPI kanssa, ilmeisesti tarkoitettu käytettäväksi monisäikeistyksessä

    ## INIITOI SIMULAATTORIN TAUSTAMOOTTORI
    simulator = AerSimulator(method=sim_method, device=sim_device, batched_shots_gpu=use_batched_shots)

    ## LUO KVANTTITILAVUUSPIIRI
    circuit = QuantumVolume(num_qubits, circuit_depth, seed=0)
    circuit.measure_all()

    ## KÄÄNNÄ PIIRI SPESIFILLE YHDISTÄVÄSELLE KARTALLE
    coupling_map = CouplingMap.from_full(num_qubits)
    transpiled_circuit = transpile(circuit, simulator, coupling_map=coupling_map, optimization_level=0)

    ## AJA SIMULAATIO
    result_statevec = simulator.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enabled=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()

    ## KÄYTÄ YHTENÄISET TULOKSET JA JOTAKIN LISÄÄ METATIEDOT
    counts = result_statevec.get_counts()
    result_dict = result_statevec.to_dict()
    metadata = result_dict['metadata']
    input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : num_qubits, 'Depth' : circuit_depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots, 'Device' : sim_device, 'Simulation Method' : sim_method}
    if (use_cache_blocking):
        num_chunks = 2**(num_qubits - num_blocking_qubits)
        input_data['Blocking Qubits'] = num_blocking_qubits
        input_data['Number of Chunks'] = num_chunks
    
    
    ## TULOSTYÄ YHDEKSI MPI-TIEDOSTO
    if (metadata['mpi_rank'] == 0):
        print()
        print(f"Input data: {input_data}")
        print(f"Metadata: {metadata}")
        #print(f"Results: {counts}")
        print(f"-------------------- \n")

    ## TULOSTA KAIKKI MPI PROSESSIT
    #print(f"Input data: {input_data}")
    #print(f"Metadata: {metadata}")
    #print(f"-------------------- \n")
    ```

Lähetä skripti komennolla `sbatch <sbatch_script_name>.sh`

### Esimerkkisbatch ja Python-skripti - Monisolmuksiset simulaatiot, jotka hyödyntävät Native HPE Cray MPI:tä GPU-kiihdytyksellä LUMIlla {#example-sbatch-and-python-script---multi-node-simulations-which-leverage-native-hpe-cray-mpi-with-gpu-acceleration-on-lumi}

Esimerkki `<sbatch_MPI_script_name>.sh` skripti simulaation suorittamiseen monella LUMI-solmulla standard-g osassa käyttäen kaikkia GPU:ja ja kaikki CPU ytimiä solmussa. Tämä koskee simulaatioita, joissa on 35 kubittia tai enemmän (enintään 45* kubittiin - katso alla oleva taulukko suositelluista resurssien allokaatiosta simuloitaessa haluttua qubittien määrää):

=== "LUMI"
    ```bash
    #!/bin/bash
    ## Täällä on esimerkkisbatch skripti 38 kubitin kvanttitilavuus simulaatiolle (myprog_MPI.py) käyttäen 16 solmua 
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

Pieni koodiesimerkki `<myprog_MPI>.py` Python-skriptistä käyttäen 38 qubittia, jota suosittelemme ajamaan 16 solmussa 
*katso alla oleva taulukko suositelluista resurssien allokoinneista

=== "LUMI"
    ```Python
    from qiskit import QuantumCircuit, transpile
    from qiskit.transpiler import CouplingMap
    from qiskit_aer import AerSimulator
    from qiskit.circuit.library import QuantumVolume
    
    ## VALITSE PARAMETRIT
    num_qubits = 38                       # Piirissä olevien kubittien määrä
    circuit_depth = 30                    # Kvanttitilavuuspiirin syvyys
    num_shots = 1000                      # Kuinka monta kertaa simulaatiota toistetaan
    sim_method = 'statevector'            # Valitse simulaatiomenetelmä
    sim_device = 'GPU'                    # Valitse, ajetaanko simulointi CPU:illa tai GPU:illa
    use_cache_blocking = True             # Cache Blocking tekniikka jakaa yhtenäiset tilat hajautettuun muistialueeseen
    num_blocking_qubits = 29              # Määrittelee lohkokoon cache blockingille. On oltava pienempi kuin "kubitteja-log2(prosessien määrä)"
    use_batched_shots = True              # Jakaa näytteitä useille prosesseille
    num_parallel_experiments = 1          # Ei tunnu vaikuttavan kenttään MPI kanssa, ilmeisesti tarkoitettu käytettäväksi monisäikeistyksessä
    
    ## INIITOI SIMULAATTORIN TAUSTAMOOTTORI
    simulator = AerSimulator(method=sim_method, device=sim_device, batched_shots_gpu=use_batched_shots)
    
    ## LUO KVANTTITILAVUUSPIIRI
    circuit = QuantumVolume(num_qubits, circuit_depth, seed=0)
    circuit.measure_all()
    
    ## KÄÄNNÄ PIIRI SPESIFILLE YHDISTÄVÄSELLE KARTALLE
    coupling_map = CouplingMap.from_full(num_qubits)
    transpiled_circuit = transpile(circuit, simulator, coupling_map=coupling_map, optimization_level=0)
    
    ## AJA SIMULAATIO
    result_statevec = simulator.run(transpiled_circuit, shots=num_shots, seed_simulator=12345, blocking_enabled=use_cache_blocking, blocking_qubits=num_blocking_qubits, max_parallel_experiments=num_parallel_experiments).result()
    
    ## KÄYTÄ YHTENÄISET TULOKSET JA JOTAKIN LISÄÄ METATIEDOT
    counts = result_statevec.get_counts()
    result_dict = result_statevec.to_dict()
    metadata = result_dict['metadata']
    input_data = {'Circuit' : 'Quantum Volume', 'Qubits' : num_qubits, 'Depth' : circuit_depth, 'Shots' : num_shots, 'Batched Shots' : use_batched_shots, 'Device' : sim_device, 'Simulation Method' : sim_method}
    if (use_cache_blocking):
        num_chunks = 2**(num_qubits - num_blocking_qubits)
        input_data['Blocking Qubits'] = num_blocking_qubits
        input_data['Number of Chunks'] = num_chunks
    
    ## TULOSTYÄ YHDEKSI MPI-TIEDOSTO
    if (metadata['mpi_rank'] == 0):
        print()
        print(f"Input data: {input_data}")
        print(f"Metadata: {metadata}")
        #print(f"Results: {counts}")
        print(f"-------------------- \n")

    ## TULOSTA KAIKKI MPI PROSESSIT
    #print(f"Input data: {input_data}")
    #print(f"Metadata: {metadata}")
    #print(f"-------------------- \n")
    ```

Lähetä skripti komennolla `sbatch <sbatch_MPI_script_name>.sh`

### Ohjeet LUMI:n resurssien allokointiin {#guidelines-for-lumi-resource-allocation}

Valtiovektorisimulaatioiden muistivaatimukset kaksinkertaistuvat jokaiselle lisättävälle kubitille. Käyttäen 16-tavun tarkkuutta (qiskit-aer:in oletusasetus), LUMI tukee valtiovektorisimulaatioita jopa 34 kubittia yksisolmulla, ja jopa 44* kubittia käyttäen 1024 solmua cache blocking-tekniikalla. Cache blocking hyödyntää hajautettujen prosessien jakamisesta kertyvää muistia kiihdyttämisen parantamiseksi. Cache blockingin lohkokoko määrätään lohkottavilla kubiteilla, joiden tulee olla pienempi kuin yksittäisen cachen koko. LUMIn tapauksessa, cachen tulisi vastata yhden GPU:n muistikokoa, ja lohkottavien kubittien kannattaa olla alle 29.

Alla olevassa taulukossa esitetään esimerkkiparametrejä kvanttilohtimuuspiirin simulointiin syvyydellä 30 ja eri määrä kubitteja. Valtiovektorimuistin vaatimukset lasketaan käyttäen 16-tavun tarkkuutta. Solmujen määrä vastaa kahta kertaa valtiovektorin muistivaatimusta, mikä tarjoaa optimaalisen suorituskyvyn varaamalla ylimääräistä muistia cache blockingin käsittelyyn hajautettujen prosessien välisten tietojenvaihtojen hallitsemiseksi. Huomaa, että näitä parametrejä testattiin tietyssä piirissä. Solmujen määrän muuttaminen tai erilaisten piirien simulointi saattaa edellyttää erilaisten lohkoittuvien kubittien määrittelemistä.

### Muistivaatimukset ja esimerkkiparametrit valtiovektorisimulaatiolle kvanttiloivuudella syvyydellä 30 ja 16-tavun tarkkuudella

| # Kubitteja | # Lohkoittuvia kubitteja | Suositeltu # solmuja | # gpu per solmu | # tehtäviä per solmu | # gpu per tehtävä | # cpu per tehtävä | Kubittien muistivaatimukset | 
| :---------- | :-----------------------: | :------------------: | --------------- | -------------------- | ---------------- | ---------------- | ----------------------------- |
| 1           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 32 Tavua                    |
| 2           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 64                           |
| 3           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 128                          |
| 4           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 256                          |
| 5           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 512                          |
| 6           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 1024                         |
| 7           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 2 Kilotavua                  |
| 8           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 4                             |
| 9           | 0                         | 1                    | 8               | 1                    | 8                | 56               | 8                             |
| 10          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 16                            |
| 11          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 32                            |
| 12          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 64                            |
| 13          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 128                          |
| 14          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 256                          |
| 15          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 512                          |
| 16          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 1024                         |
| 17          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 2 Megatavua                  |
| 18          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 4                             |
| 19          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 8                             |
| 20          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 16                            |
| 21          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 32                            |
| 22          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 64                            |
| 23          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 128                          |
| 24          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 256                          |
| 25          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 512                          |
| 26          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 1024                         |
| 27          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 2 Gigatavua                  |
| 28          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 4                             |
| 29          | 0                         | 1                    | 8               | 1                    | 8                | 56               | 8                             |
| 30          | 29                        | 1                    | 8               | 1                    | 8                | 56               | 16                            |
| 31          | 29                        | 1                    | 8               | 1                    | 8                | 56               | 32                            |
| 32          | 29                        | 1                    | 8               | 1                    | 8                | 56               | 64                            |
| 33          | 29                        | 1                    | 8               | 1                    | 8                | 56               | 128                          |
| 34          | 29                        | 1                    | 8               | 1                    | 8                | 56               | 256                          |
| 35          | 29                        | 2                    | 8               | 8                    | 1                | 7               | 512                           |
| 36          | 29                        | 4                    | 8               | 8                    | 1                | 7               | 1024                          |
| 37          | 29                        | 8                    | 8               | 8                    | 1                | 7               | 2 Teratavua                  |
| 38          | 29                        | 16                   | 8               | 8                    | 1                | 7               | 4                             |
| 39          | 29                        | 32                   | 8               | 8                    | 1                | 7               | 8                             |
| 40          | 29                        | 64                   | 8               | 8                    | 1                | 7               | 16                            |
| 41          | 29                        | 128                  | 8               | 8                    | 1                | 7               | 32                            |
| 42          | 29                        | 256                  | 8               | 8                    | 1                | 7               | 64                            |
| 43          | 29                        | 512                  | 8               | 8                    | 1                | 7               | 128                          |
| 44          | 29                        | 1024                 | 8               | 8                    | 1                | 7               | 256                          |

* Yli 1024 solmun vaativassa ajossa LUMI:ssa on etsittävä erityistä sankarisuoritushakemusta, jotta tällaiset resurssit voidaan varata.

### Enemmän kuin LUMI:n vähimmäisresursseja simulaatiolle käyttäminen {#using-more-than-the-effective-minimum-lumi-resources-for-a-simulation}

Simulaation suoritusaika voidaan nopeuttaa lisäämällä resursseja tehokkaiden vähimmäissolmuvaatimusten ohi, mikä vastaa valtiovektorin muistivaatimusten kaksinkertaista määrää. Tällaisissa tapauksissa hajautettujen prosessien (MPI_Ranks) ja varattujen resurssien määrää tulisi harkita huolellisesti. Lohkoittuvat kubitit tulisi määrittää siten, ettei MPI-tekijöitä ole enemmän kuin cachea. Jotta voisimme arvioida työn maksimimäärä solmuista, alle on annettu kaavat oppaana.

=== "Monisolmuksisen simulaation solmumäärä Cache Blocking Kubitteilla"
    ```bash
    
                Valtion vector muisti vaaditaan n-qubittille = precision X 2^n
               Cache muisti vaaditaan nc-cache blocking qubittille = precision X 2^nc

                                       Max MPI-arvot = (Valtion vektrorimuisti)/(Cache muisti)
                                       Max MPI-arvot = (precision X 2^n)/(precision X 2^nc) = 2^(n-nc)
                                           
                                           Max Solmut = (Max MPI-jaot)/(Tehtävät Per Solmu)
    ```


## Lisätiedot {#more-information}

- [* LUMI Full Machine Runs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/hero-runs)
- [LUMI Slurm sitoutumisvaihtoehdot MPI-töille](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#slurm-binding-options)
- [qiskit-aer monen GPU:n ja/tai monen solmujen käyttö](https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html)
- [Cache Blocking Tekniikka Laajamittaiseen kvanttilaskennan simulaatioon supertietokoneilla](https://arxiv.org/abs/2102.02957)
- [Qiskit dokumentaatio](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer dokumentaatio](https://qiskit.org/ecosystem/aer/tutorials/index.html)


