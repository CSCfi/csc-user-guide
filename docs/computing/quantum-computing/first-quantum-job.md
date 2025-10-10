# Ensimmäisen kvanttilaskenta-ajon suorittaminen LUMIn kautta kvanttitietokoneilla { #running-your-first-quantum-computing-job-on-the-quantum-computers-through-lumi }

Jos olet hakenut projektia, tullut hyväksytyksi, määrittänyt SSH-avaimesi ja saanut pääsyn LUMIin, seuraava askel on suorittaa ensimmäinen kvanttilaskenta-ajosi oikealla kvanttitietokoneella! Tämä opas kertoo täsmälleen, miten se tehdään. Ainoa asia, joka sinun tarvitsee tietää, on projektinumerosi!

## Ympäristön määrittäminen { #configuring-the-environment }

Ensimmäinen askel LUMIin kirjautumisen jälkeen (komennolla `ssh lumi` terminaalissasi) on ympäristön määrittäminen. LUMIn oletusympäristö kirjautumisen jälkeen ei tarjoa tarvittavia työkaluja kvanttiajotehtävien lähettämiseen, joten on luotu kvanttiohjelmistopino, joka asettaa oikeat Python-virtuaaliympäristöt ja ympäristömuuttujat. Tähän pääsee LUMIn LMOD-järjestelmän kautta käyttämällä moduleita.

Käyttääksesi kvanttiohjelmistopinoa sinun tulee ensin ladata Quantum-modulepuu.

```bash
module use /appl/local/quantum/modulefiles
```

Vaihtoehtoisesti voit saavuttaa saman tuloksen lataamalla Local-quantum-moduulin.

```bash
module load Local-quantum
```

Voit nähdä käytettävissä olevat moduulit komennolla `module avail`. Kvanttimuodulit pitäisi näkyä listan kärjessä! Tässä läpikäynnissä käytämme Qiskitiä, joten seuraava askel on ladata moduuli nykyiseen ympäristöön komennolla

```bash
module load fiqci-vtt-qiskit
```

## Ensimmäisen kvanttiohjelmasi luominen { #creating-your-first-quantum-program }

Seuraavaksi luodaan kvanttikehä! Tässä luodaan yksinkertainen Bellin tila kahden kubitin välille, mikä demonstroi niiden lomittumista. Käytämme tähän Qiskitiä, mutta vaiheet ovat hyvin samankaltaiset Cirqin kanssa. On hyvä tapa työskennellä projektisi scratch-hakemistossa, jonne voit siirtyä komennolla `cd /scratch/project_xxx`, korvaten projektinumerolla.

!!! info "Vinkki!"
	
	Voit nähdä LUMI-työtilasi nopeasti komennolla
	`lumi-workspaces`

Luodaan ensin Python-tiedosto komennolla `nano first_quantum_job.py`. Tässä käytämme `nanoa`, mutta jos olet mukavuusalueellasi, voit käyttää myös `vim`iä tai `emacs`ia. Tämä avaa `nano`-tekstieditorin; hyödylliset komennot näkyvät alhaalla. Tallenna ja poistu näppäinyhdistelmällä CTRL-X + Y.

### Kirjastojen tuonti { #importing-the-libraries }

Tuodaan ensin oikeat Python-kirjastot

```python
import os
from qiskit import QuantumCircuit, QuantumRegister, transpile
from iqm.qiskit_iqm import IQMProvider
```

### Kehän luominen { #creating-the-circuit }

Kvanttikehä luodaan määrittämällä `QuantumRegister`, joka pitää sisällään kubitit ja klassiset bitit. Koska tämä kehä vaatii vain 2 kubittia, luomme vain 2-kokoisen `QuantumRegister`-rekisterin. Myös laukaisujen määrä määritetään tässä. Laukaisujen määrä on se, kuinka monta kertaa kvanttikehä suoritetaan. Teemme tämän, koska kvanttitietokoneet ovat probabilistisia koneita, ja toistamalla koetta monta kertaa voimme päästä lähelle determinististä tulosta johtopäätösten tekemiseksi. Hyvä laukaisumäärä ensimmäiselle kvanttiajollesi on `shots = 1000`. Laukaisujen kasvattaminen parantaa tulosten tarkkuutta.

```python
shots = 1000  # Number of repetitions of the Quantum Circuit

qreg = QuantumRegister(2, "qB")
circuit = QuantumCircuit(qreg, name='Bell pair circuit')
```

Lisätään nyt kehässä portteja. Tässä lisätään Hadamard-portti ensimmäiselle kubitille (ensimmäiselle kubitille kvanttirekisterissä). Sen jälkeen lisätään controlled-x -portti kahdella argumentilla, koska kyseessä on kahden kubitin portti.

```python
circuit.h(qreg[0])  # Hadamard gate on the first qubit in the Quantum Register
circuit.cx(qreg[1], qreg[0])  # Controlled-X gate between the second qubit and first qubit
circuit.measure_all()  # Measure all qubits in the Quantum Register.
```

Huomaa, että [`measure_all()`](https://qiskit.org/documentation/stubs/qiskit.circuit.QuantumCircuit.html#qiskit.circuit.QuantumCircuit.measure_all) luo oman [`ClassicalRegister`](https://qiskit.org/documentation/stubs/qiskit.circuit.ClassicalRegister.html)!

Nyt kehä on luotu! Halutessasi voit nähdä miltä kehäsi näyttää lisäämällä tulostuksen `print(circuit.draw())` ja ajamalla Python-skriptin pikaisesti.

## Taustaosan (backend) asettaminen { #setting-the-backend }

Ensin asetetaan provider ja backend. Provider on palvelu, joka tarjoaa käyttöliittymän kvanttitietokoneelle, ja backend tarjoaa työkalut kvanttiajotehtävän lähettämiseen. `HELMI_CORTEX_URL` on päätepiste Helmiin (5 kubitin kone), ja siihen pääsee vain `q_fiqci`-osiossa. `Q50_CORTEX_URL` on päätepiste Q50:een (50 kubitin kone). Tämä ympäristömuuttuja asetetaan automaattisesti, kun lataat minkä tahansa kvanttilaskentamoduulin, kuten `fiqci-vtt-qiskit`.

=== "Helmi"
    ```python
    # Accessing Helmi

    HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
    provider_helmi = IQMProvider(HELMI_CORTEX_URL)
    backend_helmi = provider_helmi.get_backend()
    ```

=== "Q50"
    ```python
    # Accessing Q50

    Q50_CORTEX_URL = os.getenv('Q50_CORTEX_URL')
    provider_q50 = IQMProvider(Q50_CORTEX_URL)
    backend_q50 = provider_q50.get_backend()
    ```

=== "Useita backend-palveluja"
    ```python
    # It is possible to simultaneously run jobs on multiple backends

    HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
    provider_helmi = IQMProvider(HELMI_CORTEX_URL)
    backend_helmi = provider.get_backend()

    Q50_CORTEX_URL = os.getenv('Q50_CORTEX_URL')
    provider_q50 = IQMProvider(Q50_CORTEX_URL)
    backend_q50 = provider_q50.get_backend()
    ```

### Kehän transpilaus { #transpiling-the-circuit }

Seuraavassa vaiheessa juuri luomasi kvanttikehä hajotetaan (transpiloidaan) perusporteikseen. Nämä perusportit ovat ne todelliset kvanttiportit, jotka ovat käytettävissä kvanttitietokoneessa. Hajotusprosessi muuntaa yllä käytetyt Hadamard- ja controlled-x -portit muotoon, joka voidaan fyysisesti suorittaa kvanttitietokoneella. Helmissä ja Q50:ssä perusportteja ovat lomitusportti controlled-z ja yhden kubitin phased-rx -portti. Qiskitissä nämä on määritelty backendissä, ja ne voi tulostaa komennolla `backend.operation_names`. Lisätietoja spekseistä: [Topologian yleiskuvaus](specs.md)

```python
circuit_decomposed = transpile(circuit, backend=backend)
```
Voit myös tulostaa kehän kuten aiemmin komennolla `print(circuit_decomposed.draw())` nähdäksesi miltä se näyttää!

### Valinnainen kubittien sijoittelu (mapping) { #optional-qubit-mapping }

Tämä vaihe on valinnainen, mutta voi auttaa saamaan laitteesta parhaan mahdollisen suorituskyvyn. Se on Python-sanakirja, joka kertoo, mitkä kvanttirekisterin kubitit sijoitetaan mille fyysisille kubiteille.

```python
qubit_mapping = {
                qreg[0]: 0,
                qreg[1]: 2,
            }
```

Esimerkkinä tässä sijoitamme kvanttirekisterin ensimmäisen kubitin Helmin ensimmäiselle kubitille, QB1:lle, joka sijaitsee indeksissä 0, koska Qiskit käyttää nollapohjaista indeksointia. Toinen kubitti sijoitetaan QB3:lle. Tässä hyödynnetään Helmin topologiaa. Sama prosessi voidaan soveltaa muihin kvanttitietokoneisiin, esimerkiksi Q50:een.

<center>!["Helmi's node mapping"](../../img/helmi_mapping.png)</center>

Kaksikubittinen Controlled-X -portti, jonka lisäsimme kehäämme, on tällä hetkellä kvanttirekisterimme toisessa kubitissa, `qreg[1]`. Helmin topologian vuoksi tämä täytyy sijoittaa Helmissä QB3:lle. Yhden kubitin Hadamard-portti voidaan sijoittaa mille tahansa ulommista kubiteista, QB1, QB2, QB4, QB5; tässä valitsemme QB1:n.

Huomaa, että tämä vaihe on täysin valinnainen. `transpile`-toiminnon käyttäminen tekee sijoittelun automaattisesti backendin tallentamien tietojen perusteella. Kubittien sijoittelun syöttäminen käsin antaa käyttäjälle vain enemmän kontrollia.

Jos haluat transpiloida kehän käyttäen määritettyä kubittisijoittelua, voit tehdä seuraavasti:

```python
circuit_decomposed = transpile(circuit, backend=backend, initial_layout=qubit_mapping)
```

### Työn lähettäminen { #submitting-the-job }

Nyt voimme ajaa kvanttitehtävämme!

```python
job = backend.run(circuit_decomposed, shots=shots)
```

### Työsi tilan tarkastelu { #viewing-the-status-of-your-job }

Voit tarkastella työsi tilaa komennolla

```python
job.status()
```

### Tulokset { #results }

Ennen lähettämistä varmistetaan, että saamme tuloksia! Kvanttitehtävä palauttaa niin kutsutut counts-arvot. Counts on niiden tulosten kertymä, jotka saadaan, kun kehä ajetaan 1000 kertaa QPU:lla. Joka kerta, kun kehä ajetaan, saadaan binäärinen tila, joka lisätään laskuriin. Tässä tapauksessa, koska lähetämme 2-kubittisen kehän, mahdollisia tiloja on 4: `00, 11, 01, 10`. Odotettu tulos on, että noin 50 % laskennoista on tilassa `00` ja 50 % tilassa `11`. Kubittien tilat ovat siis lomittuneita: jos toinen kubiteista mitataan tilaan |0>, toinen romahtaa välittömästi samaan tilaan, ja päinvastoin. Koska todelliset kvanttitietokoneet eivät ole täydellisiä, näet todennäköisesti myös joitakin mittauksia tiloissa |01> ja |10>.

Tulostaaksesi tulokset lisää:

```python
counts = job.result().get_counts()
print(counts)
```

Voit myös tulostaa koko `job.result()`-olion, joka sisältää kaiken tiedon työsi tuloksista.

## Tallenna tiedostosi { #save-your-file }

Kun olet tehnyt ensimmäisen kvanttiohjelmasi, muista tallentaa! CTRL+X ja sitten Y tallentaaksesi tiedoston.

## Työn ajaminen LUMIn kautta { #running-the-job-through-lumi }

Ajaaksesi kvanttiohjelmasi LUMIssa sinun tulee lähettää työ SLURM-eräajonhallinnan kautta LUMIssa. Pääsy kvanttitietokoneille (Helmi, Q50) tapahtuu `q_fiqci`-osaston kautta. Samassa hakemistossa, johon olet tallentanut kvanttiohjelmasi, voit lähettää työn SLURMille seuraavasti:

=== "Helmi"
    ```bash
    # Using Helmi

    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit"
    export DEVICES=("Q5")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python -u first_quantum_job.py"
    ```

=== "Q50"
    ```bash
    # Using Q50

    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit"
    export DEVICES=("Q50")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python -u first_quantum_job.py"
    ```

=== "Useita backend-palveluja"
    ```bash
    # Using multiple backends

    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit"
    export DEVICES=("Q5" "Q50")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python -u first_quantum_job.py"
    ```

Muista lisätä oma projektitilisi!

Tämä lähettää työn interaktiivisesti, eli tuloste kirjoitetaan suoraan terminaalin ruudulle. Halutessasi voit myös lähettää sen komennolla `sbatch` käyttäen tätä rungoksi sopivaa eräajon skriptiä. Luo skripti `batch_script.sh` komennolla `nano` kuten aiemmin.

=== "Helmi"
    ```bash
    #!/bin/bash -l

    #SBATCH --job-name=quantumjob   # Job name
    #SBATCH --output=quantumjob.o%j # Name of stdout output file
    #SBATCH --error=quantumjob.e%j  # Name of stderr error file
    #SBATCH --partition=q_fiqci   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)
    #SBATCH --account=project_xxx  # Project for billing

    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit

    export DEVICES=("Q5")

    source $RUN_SETUP

    python -u first_quantum_job.py
    ```

=== "Q50"
    ```bash
    #!/bin/bash -l

    #SBATCH --job-name=quantumjob   # Job name
    #SBATCH --output=quantumjob.o%j # Name of stdout output file
    #SBATCH --error=quantumjob.e%j  # Name of stderr error file
    #SBATCH --partition=q_fiqci   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)
    #SBATCH --account=project_xxx  # Project for billing

    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit

    export DEVICES=("Q50")

    source $RUN_SETUP

    python -u first_quantum_job.py
    ```

=== "Useita backend-palveluja"
    ```bash
    #!/bin/bash -l

    #SBATCH --job-name=quantumjob   # Job name
    #SBATCH --output=quantumjob.o%j # Name of stdout output file
    #SBATCH --error=quantumjob.e%j  # Name of stderr error file
    #SBATCH --partition=q_fiqci   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)
    #SBATCH --account=project_xxx  # Project for billing

    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit

    export DEVICES=("Q5" "Q50")

    source $RUN_SETUP

    python -u first_quantum_job.py
    ```

Tämän voi lähettää komennolla `sbatch batch_script.sh` samassa hakemistossa kuin Python-tiedostosi. SLURM-jonossa olevia töitä voi seurata komennolla `squeue -u username`, ja työn valmistuttua tulokset löytyvät tiedostosta `quantumjob.oxxxxx`. Tämän voi tulostaa terminaaliin komennolla `cat`. Jos haluat ajaa sekä Helmillä että Q50:llä tai pelkästään Q50:llä, sinun tulee määrittää tarvitsemasi laitteet. Tässä `Q5` tarkoittaa Helmiä ja `Q50` 50 kubitin konetta.

## Onneksi olkoon! { #congratulations }

Onneksi olkoon! Suoritit juuri ensimmäisen ajosi kvanttitietokoneella.

Koko Python-skripti löytyy alta.

=== "Helmi"
    ```python
    import os

    from qiskit import QuantumCircuit, QuantumRegister, transpile
    from iqm.qiskit_iqm import IQMProvider

    shots = 1000

    qreg = QuantumRegister(2, "QB")
    circuit = QuantumCircuit(qreg, name='Bell pair circuit')

    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.measure_all()

    # Uncomment if you wish to print the circuit
    # print(circuit.draw())

    HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')

    provider_helmi = IQMProvider(HELMI_CORTEX_URL)
    backend_helmi = provider_helmi.get_backend()

    # Retrieving backend information
    # print(f'Native operations: {backend_helmi.operation_names}')
    # print(f'Number of qubits: {backend_helmi.num_qubits}')
    # print(f'Coupling map: {backend_helmi.coupling_map}')

    transpiled_circuit = transpile(circuit, backend_helmi)

    job = backend.run(transpiled_circuit, shots=shots)
    result = job.result()

    # You can retrieve the job at a later date with backend.retrieve_job(job_id)
    # Uncomment the following lines to get more information about your submitted job
    # print("Job ID: ", job.job_id())
    # print(result.request.circuits)
    # exp_result = job.result()._get_experiment(circuit)
    # print("Calibration Set ID: ", exp_result.calibration_set_id)
    # print(result.request.qubit_mapping)
    # print(result.request.shots)

    counts = result.get_counts()
    print(counts)
    ```

=== "Q50"
    ```python
    import os

    from qiskit import QuantumCircuit, QuantumRegister, transpile
    from iqm.qiskit_iqm import IQMProvider

    shots = 1000

    qreg = QuantumRegister(2, "QB")
    circuit = QuantumCircuit(qreg, name='Bell pair circuit')

    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.measure_all()

    # Uncomment if you wish to print the circuit
    # print(circuit.draw())

    Q50_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    provider_q50 = IQMProvider(Q50_CORTEX_URL)
    backend_q50 = provider_q50.get_backend()

    # Retrieving backend information
    # print(f'Native operations: {backend_q50.operation_names}')
    # print(f'Number of qubits: {backend_q50.num_qubits}')
    # print(f'Coupling map: {backend_q50.coupling_map}')

    transpiled_circuit = transpile(circuit, backend_q50)
    
    job = backend_q50.run(transpiled_circuit, shots=shots)
    result = job.result()

    # You can retrieve the job at a later date with backend.retrieve_job(job_id)
    # Uncomment the following lines to get more information about your submitted job
    # print("Job ID: ", job.job_id())
    # print(result.request.circuits)
    # exp_result = job.result()._get_experiment(circuit)
    # print("Calibration Set ID: ", exp_result.calibration_set_id)
    # print(result.request.qubit_mapping)
    # print(result.request.shots)

    counts = result.get_counts()
    print(counts)
    ```

=== "Useita backend-palveluja"
    ```python
    import os

    from qiskit import QuantumCircuit, QuantumRegister, transpile
    from iqm.qiskit_iqm import IQMProvider

    shots = 1000

    qreg = QuantumRegister(2, "QB")
    circuit = QuantumCircuit(qreg, name='Bell pair circuit')

    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    circuit.measure_all()

    # Uncomment if you wish to print the circuit
    # print(circuit.draw())

    HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
    Q50_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    provider_helmi = IQMProvider(HELMI_CORTEX_URL)
    backend_helmi = provider_helmi.get_backend()

    provider_q50 = IQMProvider(Q50_CORTEX_URL)
    backend_q50= provider_q50.get_backend()


    # Retrieving backend information
    # print(f'Native operations: {backend.operation_names}')
    # print(f'Number of qubits: {backend.num_qubits}')
    # print(f'Coupling map: {backend.coupling_map}')

    transpiled_circuit_helmi = transpile(circuit, backend_helmi)
    transpiled_circuit_q50 = transpile(circuit, backend_q50)
    
    job_helmi = backend_helmi.run(transpiled_circuit_helmi, shots=shots)
    job_q50 = backend_q50.run(transpiled_circuit_q50, shots=shots)
    
    result_helmi = job_helmi.result()
    result_q50 = job_q50.result()

    # You can retrieve the job at a later date with backend.retrieve_job(job_id)
    # Uncomment the following lines to get more information about your submitted jobs
    # print("Helmi Job ID: ", job_helmi.job_id())
    # print(result_helmi.request.circuits)
    # exp_result_helmi = job_helmi.result()._get_experiment(circuit)
    # print("Helmi Calibration Set ID: ", exp_result_helmi.calibration_set_id)
    # print(result_helmi.request.qubit_mapping)
    # print(result_helmi.request.shots)

    # print("Q50 job ID: ", job_q50.job_id())
    # print(result_q50.request.circuits)
    # exp_result_q50 = job_q50.result()._get_experiment(circuit)
    # print("Q50 Calibration Set ID: ", exp_result_q50.calibration_set_id)
    # print(result_q50.request.qubit_mapping)
    # print(result_q50.request.shots)

    counts_helmi = result_helmi.get_counts()
    counts_q50 = result_q50.get_counts()

    print(f"Helmi results: {counts_helmi}")
    print(f"Q50 results: {counts_q50}")
    ```