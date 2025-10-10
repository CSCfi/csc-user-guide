!!! warning "HUOM: QPU-ajan seuranta"
    Käytetty QPU-aika ei vielä näy oikein MyCSC:ssä. Käyttö kirjautuu sisäisesti oikein,
    ja teemme korjauksia MyCSC:ssä näkyvään aikaan. Kysymyksissä voitte ottaa yhteyttä:
    [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi). 


# Ajaminen Helmillä ja Q50:llä { #running-on-helmi-and-q50 }

!!! info "Anna palautetta!"
    **Kaikki palaute on erittäin arvokasta.** Kerro kokemuksistasi
    lähettämällä sähköpostia osoitteeseen [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi).

## Töiden ajaminen { #running-jobs }

Lähettääksesi töitä kvanttitietokoneille (Helmi ja Q50) käytä q_fiqci-jonoa lisäämällä --partition=q_fiqci eräajotiedostoosi.

Tällä hetkellä Helmi ja Q50 tukevat töiden lähettämistä Qiskit- tai Cirq-kehyksillä. Nämä skriptit tulee toimittaa tavallisina Python-tiedostoina.

Ajaaksesi töitä kvanttitietokoneilla, noudata seuraavia ohjeita oikean ympäristön asettamiseksi LUMIssa:

Huom: Aja nämä komennot joko eräajotiedostossa tai srun-komennolla käynnistetyssä interaktiivisessa sessiossa.

* Lisää moduulipolku, jotta järjestelmä löytää saatavilla olevat moduulit: `module use /appl/local/quantum/modulefiles`

* Lataa sopiva ympäristömoduuli käyttämäsi kehyksen mukaan:
    * Qiskit: `module load fiqci-vtt-qiskit` 
    * Cirq: `module load fiqci-vtt-cirq`


Moduulit `fiqci-vtt-qiskit` ja `fiqci-vtt-cirq` tarjoavat esikonfiguroidut Python-ympäristöt töiden ajamiseen kvanttitietokoneilla.
Jos sinun täytyy asentaa lisä-Python-paketteja, voit tehdä sen komennolla: 

`python -m pip install --user package`.


!!! info "Luo oma Python-ympäristösi"
    Jos haluat käyttää omaa Python-ympäristöäsi,
    suosittelemme [container wrapper -työkalua](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/) ympäristösi luomiseen ja hallintaan.

Tuetut ohjelmistoversiot ovat:

| Ohjelmisto | Module_name | Versiot |
|------------|-------------|---------|
| Cirq IQM:llä | cirq_iqm |  >= 16.0, <= 17.0  |
| Qiskit IQM:llä | qiskit_iqm |  >= 17.3, <= 18.0 |
| IQM client | iqm_client | >= 22.3, <= 23.0 |

Tässä esimerkki eräajotiedostosta kvanttityön lähettämiseen

=== "Helmi"
    ```bash
    #!/bin/bash

    #SBATCH --job-name=quantumjob   # Job name
    #SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
    #SBATCH --partition=q_fiqci   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)

    module use /appl/local/quantum/modulefiles

    # uncomment the correct line:
    # module load fiqci-vtt-qiskit
    # or
    # module load fiqci-vtt-cirq
    export DEVICES=("Q5")
    source $RUN_SETUP
    python your_python_script.py
    ```

=== "Q50"
    ```bash
    #!/bin/bash

    #SBATCH --job-name=quantumjob   # Job name
    #SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
    #SBATCH --partition=q_fiqci   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)

    module use /appl/local/quantum/modulefiles

    # uncomment the correct line:
    # module load fiqci-vtt-qiskit
    # or
    # module load fiqci-vtt-cirq
    export DEVICES=("Q50")
    source $RUN_SETUP
    python your_python_script.py
    ```

=== "Useita taustajärjestelmiä"
    ```bash
    #!/bin/bash

    #SBATCH --job-name=quantumjob   # Job name
    #SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
    #SBATCH --partition=q_fiqci   # Partition (queue) name
    #SBATCH --ntasks=1              # One task (process)
    #SBATCH --mem-per-cpu=2G       # memory allocation
    #SBATCH --cpus-per-task=1     # Number of cores (threads)
    #SBATCH --time=00:05:00         # Run time (hh:mm:ss)

    module use /appl/local/quantum/modulefiles

    ## uncomment the correct line:
    # module load fiqci-vtt-qiskit
    # or
    # module load fiqci-vtt-cirq
    export DEVICES=("Q5" "Q50")
    source $RUN_SETUP
    python your_python_script.py
    ```

Eräajotiedosto voidaan lähettää komennolla `sbatch`. Voit myös lähettää interaktiivisia töitä `srun`-komennolla.

=== "Helmi"
    ```bash
    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit"
    export DEVICES=("Q5")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python your_python_script.py"
    ```

=== "Q50"
    ```bash
    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit"
    export DEVICES=("Q50")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python your_python_script.py"
    ```

=== "Useita taustajärjestelmiä"
    ```bash
    module use /appl/local/quantum/modulefiles
    module --ignore_cache load "fiqci-vtt-qiskit"
    export DEVICES=("Q5" "Q50")
    srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci bash -c "source $RUN_SETUP && python your_python_script.py"
    ```

Moduuli `fiqci-vtt-*` asettaa oikean Python-ympäristön Qiskitin tai Cirqin käyttämiseen yhdessä kvanttitietokoneiden kanssa.

!!! info "Ajaminen fyysisillä kvanttitietokoneilla"
    Kun lähetät työn Helmille tai Q50:lle, käyttäjän slurm_job_account (projekti, jolla työ ajetaan) liitetään project_id:hen, ja tämä tieto siirretään VTT:lle laskutusta varten.
    Ajaaksesi Q50:llä, määritä laite komennolla `export DEVICES=("Q50")`

### Qiskit { #qiskit }

Lataa Qiskit-moduuli komennolla `module load fiqci-vtt-qiskit`.

Qiskit Python -skripteissä tulee sisällyttää seuraava:

=== "Helmi"
    ```python
    import os

    from qiskit import QuantumCircuit, transpile
    from iqm.qiskit_iqm import IQMProvider

    DEVICE_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')

    provider = IQMProvider(DEVICE_CORTEX_URL)
    backend = provider.get_backend()

    shots = 1000  # Set the number of shots you wish to run with

    # Create your quantum circuit.
    # Here is an example
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()

    print(circuit.draw(output='text'))

    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=shots)
    counts = job.result().get_counts()
    print(counts)
    ```

=== "Q50"
    ```python
    import os

    from qiskit import QuantumCircuit, transpile
    from iqm.qiskit_iqm import IQMProvider

    DEVICE_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    provider = IQMProvider(DEVICE_CORTEX_URL)
    backend = provider.get_backend()

    shots = 1000  # Set the number of shots you wish to run with

    # Create your quantum circuit.
    # Here is an example
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()

    print(circuit.draw(output='text'))

    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=shots)
    counts = job.result().get_counts()
    print(counts)
    ```

=== "Useita taustajärjestelmiä"
    ```python
    import os

    from qiskit import QuantumCircuit, transpile
    from iqm.qiskit_iqm import IQMProvider

    HELMI_DEVICE_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
    Q50_DEVICE_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    provider_helmi = IQMProvider(HELMI_DEVICE_CORTEX_URL)
    provider_q50 = IQMProvider(Q50_DEVICE_CORTEX_URL)
    
    backend_helmi = provider_helmi.get_backend()
    backend_q50 = provider_q50.get_backend()

    shots = 1000  # Set the number of shots you wish to run with

    # Create your quantum circuit.
    # Here is an example
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()

    print(circuit.draw(output='text'))

    transpiled_circuit_helmi = transpile(circuit, backend_helmi)
    transpiled_circuit_q50= transpile(circuit, backend_q50)
    
    job_helmi = backend_helmi.run(transpiled_circuit_helmi, shots=shots)
    job_q50 = backend.run(transpiled_circuit_q50, shots=shots)

    counts_helmi = job_helmi.result().get_counts()
    counts_q50 = job_q50.result().get_counts()
    
    print(f"Counts Helmi {counts_helmi}")
    print(f"Counts Q50 {counts_q50}")
    ```

### Cirq { #cirq }

Lataa Cirq-moduuli komennolla `module load fiqci-vtt-cirq`.

=== "Helmi"
    ```python
    import os

    import cirq
    from iqm.cirq_iqm.iqm_sampler import IQMSampler

    DEVICE_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')

    sampler = IQMSampler(DEVICE_CORTEX_URL)

    shots = 1000

    # Create your quantum circuit
    # Here is an example
    q1, q2 = cirq.NamedQubit('QB1'), cirq.NamedQubit('QB2')
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q1))
    circuit.append(cirq.CNOT(q1, q2))
    circuit.append(cirq.measure(q1, q2, key='m'))
    print(circuit)

    routed_circuit, initial_mapping, final_mapping = sampler.device.route_circuit(circuit)
    decomposed_circuit = sampler.device.decompose_circuit(routed_circuit)

    # Optionally print mapping
    # print(routed_circuit)
    # print(initial_mapping)
    # print(final_mapping)
    # print(decomposed_circuit)

    result = sampler.run(decomposed_circuit, repetitions=shots)
    print(result.measurements['m'])
    ```

=== "Q50"
    ```python
    import os

    import cirq
    from iqm.cirq_iqm.iqm_sampler import IQMSampler

    DEVICE_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    sampler = IQMSampler(DEVICE_CORTEX_URL)

    shots = 1000

    # Create your quantum circuit
    # Here is an example
    q1, q2 = cirq.NamedQubit('QB1'), cirq.NamedQubit('QB2')
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q1))
    circuit.append(cirq.CNOT(q1, q2))
    circuit.append(cirq.measure(q1, q2, key='m'))
    print(circuit)

    routed_circuit, initial_mapping, final_mapping = sampler.device.route_circuit(circuit)
    decomposed_circuit = sampler.device.decompose_circuit(routed_circuit)

    # Optionally print mapping
    # print(routed_circuit)
    # print(initial_mapping)
    # print(final_mapping)
    # print(decomposed_circuit)

    result = sampler.run(decomposed_circuit, repetitions=shots)
    print(result.measurements['m'])
    ```

=== "Useita taustajärjestelmiä"
    ```python
    import os

    import cirq
    from iqm.cirq_iqm.iqm_sampler import IQMSampler

    HELMI_DEVICE_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
    Q50_DEVICE_CORTEX_URL = os.getenv('Q50_CORTEX_URL')

    sampler_helmi = IQMSampler(HELMI_DEVICE_CORTEX_URL)
    sampler_q50 = IQMSampler(Q50_DEVICE_CORTEX_URL)

    shots = 1000

    # Create your quantum circuit
    # Here is an example
    q1, q2 = cirq.NamedQubit('QB1'), cirq.NamedQubit('QB2')
    circuit = cirq.Circuit()
    circuit.append(cirq.H(q1))
    circuit.append(cirq.CNOT(q1, q2))
    circuit.append(cirq.measure(q1, q2, key='m'))
    print(circuit)

    routed_circuit_helmi, initial_mapping_helmi, final_mapping_helmi = sampler_helmi.device.route_circuit(circuit)
    decomposed_circuit_helmi = sampler_helmi.device.decompose_circuit(routed_circuit_helmi)

    routed_circuit_q50, initial_mapping_q50, final_mapping_q50 = sampler_q50.device.route_circuit(circuit)
    decomposed_circuit_q50 = sampler_q50.device.decompose_circuit(routed_circuit_q50)

    # Optionally print mapping
    # print("Mapping Helmi")
    # print(routed_circuit_helmi)
    # print(initial_mapping_helmi)
    # print(final_mapping_helmi)
    # print(decomposed_circuit_helmi)

    # print("Mapping Q50")
    # print(routed_circuit_q50)
    # print(initial_mapping_q50)
    # print(final_mapping_q50)
    # print(decomposed_circuit_q50)

    result_helmi = sampler_helmi.run(decomposed_circuit_helmi, repetitions=shots)
    result_q50 = sampler_q50.run(decomposed_circuit_q50, repetitions=shots)

    print(f"Results Helmi: {result_helmi.measurements['m']}")
    print(f"Results Q50: {result_q50.measurements['m']}")
    ```

## Lisää esimerkkejä { #additional-examples }

Lisää [esimerkkejä löytyy täältä](https://github.com/FiQCI/helmi-examples).
Esimerkit korostavat eroa simulaattorilla ajamisen ja oikealla fyysisellä kvanttitietokoneella ajamisen välillä
sekä sitä, miten rakentaa piirisi parhaan tuloksen saamiseksi kvanttitietokoneilla. Repositoriossa on myös hyödyllisiä
skriptejä töiden lähettämiseen.


## Simuloidut testiajot { #simulated-test-runs }

Koska kvanttresurssit voivat olla niukkoja, on suositeltavaa valmistella etukäteen koodit ja algoritmit, joita aiot ajaa kvanttitietokoneilla. Tämän avuksi [`qiskit-on-iqm` tarjoaa vale-kohinamallin taustan](https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html#noisy-simulation-of-quantum-circuit-execution). Voit ajaa vale-kohinamallin taustaa paikallisesti omalla kannettavallasi simulointia ja testausta varten.

Saatavilla on myös joukko Qiskit- ja Cirq-esimerkkejä ja -skriptejä, jotka auttavat `q_fiqci`-osion käytössä. [Löydät ne täältä](https://github.com/FiQCI/fiqci-examples).

## Työn metatiedot { #job-metadata }

Lisämetatietoja työstäsi voidaan kysellä suoraan Qiskitillä. Esimerkiksi:

=== "Helmi"
    ```python

    DEVICE_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')
    provider = IQMProvider(DEVICE_CORTEX_URL)
    backend = provider.get_backend()

    #Retrieving backend information
    print(f'Native operations: {backend.operation_names}')
    print(f'Number of qubits: {backend.num_qubits}')
    print(f'Coupling map: {backend.coupling_map}')

    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=shots)
    result = job.result()
    exp_result = result._get_experiment(circuit)

    print("Job ID: ", job.job_id())  # Retrieving the submitted job id
    print(result.request.circuits)  # Retrieving the circuit request sent
    print("Calibration Set ID: ", exp_result.calibration_set_id)  # Retrieving the current calibration set id.
    print(result.request.qubit_mapping)  # Retrieving the qubit mapping
    print(result.request.shots)  # Retrieving the number of requested shots.

    #retrieve a job using the job_id from a previous session
    #old_job = backend.retrieve_job(job_id)
    ```

=== "Q50"
    ```python

    DEVICE_CORTEX_URL = os.getenv('Q50_CORTEX_URL')
    provider = IQMProvider(DEVICE_CORTEX_URL)
    backend = provider.get_backend()

    #Retrieving backend information
    print(f'Native operations: {backend.operation_names}')
    print(f'Number of qubits: {backend.num_qubits}')
    print(f'Coupling map: {backend.coupling_map}')

    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=shots)
    result = job.result()
    exp_result = result._get_experiment(circuit)

    print("Job ID: ", job.job_id())  # Retrieving the submitted job id
    print(result.request.circuits)  # Retrieving the circuit request sent
    print("Calibration Set ID: ", exp_result.calibration_set_id)  # Retrieving the current calibration set id.
    print(result.request.qubit_mapping)  # Retrieving the qubit mapping
    print(result.request.shots)  # Retrieving the number of requested shots.

    #retrieve a job using the job_id from a previous session
    #old_job = backend.retrieve_job(job_id)
    ```

!!! info "Tallenna Job ID!"
    Huomaa, että aiempien Job ID:iden listaamiseen ei tällä hetkellä ole menetelmää, joten suosittelemme aina tulostamaan Job ID:n työn lähetyksen jälkeen ja tallentamaan sen talteen!
    Sama koskee myös kalibrointijoukon tunnistetta (calibration set id).


## Kalibrointidata { #calibration-data }

Kalibrointidata (tai laatuparametrit) voi olla tarpeen Helmillä/Q50:llä tuotetun työn julkaisemiseksi. Se antaa myös käsityksen kvanttitietokoneiden tämänhetkisestä tilasta. Kalibrointidata on saatavilla [FiQCI-sivulla](https://fiqci.fi/status). Lisäksi `fiqci-examples`-repositoriossa on apuskripti kalibrointidatan noutamiseen manuaalisesti. Skripti löytyy [täältä](https://github.com/FiQCI/fiqci-examples/blob/main/scripts/get_calibration_data.py). Tiedoston voi lisätä omiin Python-skripteihisi, ja se palauttaa datan JSON-muodossa. Huomaa, että uusimman kalibrointidatan kysely voi antaa puutteellisia tai vanhentuneita arvoja. Siksi kalibrointijoukkojen tunnisteet (calibration set IDs) tulisi tallentaa yhdessä Job ID:iden kanssa.

Alla on lyhyt kuvaus luvuista, jotka saat kyselyssä:

| Luku                           | Kuvaus                                                                                                                                                                                |     |     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| T1-aika (s)                    | T1-aika on pitkittäisrelaksaatiota kuvaava suure ja kertoo, kuinka nopeasti kubitin virittynyt tila palautuu perustilaansa.                                                          |     |     |
| T2-aika (s)                    | T2-aika on poikittaisrelaksaatiota kuvaava suure ja kuvaa superpositiotilan koherenssin häviötä.                                                                                     |     |     |
| T2 Echo -aika (s)              | T2 Echo -aika kuvaa kubitin superpositiotilan koherenssin häviötä. Se on tarkempi kuin T2-aika, koska se on vähemmän altis matalataajuiselle kohinalle.                              |     |     |
| Yksittäismittauksen lukuuskollisuus | Kuvaa uskollisuutta, kun suoritetaan kubitin tilan yksittäismittauksia. Yksittäismittauksessa 50 % kubittitiloista valmistellaan virittyneeseen ja 50 % perustilaan.               |     |     |
| Yksittäismittauksen 01-virhe   | Virhe, jossa virittynyt tila ('1') luokitellaan, vaikka tila on perustila ('0').                                                                                                     |     |     |
| Yksittäismittauksen 10-virhe   | Virhe, jossa perustila ('0') luokitellaan, vaikka tila on virittynyt ('1').                                                                                                          |     |     |
| 1QB-porttien keskim. uskollisuus | Lasketaan Randomized Benchmarking -menetelmästä ja kuvaa keskimääräistä portin uskollisuutta, kun satunnainen yksikubittisten Clifford-porttien sarja ajetaan.                      |     |     |
| 2QB Cliffordien keskim. uskollisuus | Lasketaan Randomized Benchmarking -menetelmästä ja kuvaa keskimääräistä Clifford-portin uskollisuutta.                                                                             |     |     |
| CZ-portin uskollisuus          | Controlled-Z-portin uskollisuus, laskettu lomitetulla Randomized Benchmarking -menetelmällä, jossa controlled-z -portti lomitetaan mittaussarjaan.                                    |     |     |


Lisätietoja kalibrointidatasta: [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi) tai [CSC Service Desk](../../support/contact.md), tavoitettavissa osoitteessa [servicedesk@csc.fi](mailto:servicedesk@csc.fi).


## Helmin/Q50:n käyttäminen LUMIn web-käyttöliittymässä { #using-helmi-q50-on-lumi-web-interface }

[LUMIn web-käyttöliittymä](https://docs.lumi-supercomputer.eu/runjobs/webui/) mahdollistaa kvanttityöiden ajamisen Helmillä ja Q50:llä selainkäyttöliittymän kautta. Kirjautumisohjeet LUMIn web-käyttöliittymään löytyvät [LUMIn dokumentaatiosta](https://docs.lumi-supercomputer.eu/firststeps/loggingin-webui/).

### Pääsy Helmiin/Q50:een { #accessing-helmi-q50 }

Onnistuneen tunnistautumisen jälkeen näet hallintapaneelisi. Napsauta Jupyter-sovellusta, valitse projektisi ja osio (partition) q_fiqci. Jos sinulla on aktiivinen varaus, voit käyttää sitä valitsemalla sen kohdasta reservation.

Suosittelemme käyttämään `Advanced settings` -asetuksia. `Custom init` -kohdassa valitse Text, ja `Script to start` -tekstikenttään syötä seuraava skripti kvanttiohjelmistopinon käyttöönottoon.

#### Qiskit { #qiskit }
=== "Helmi"
    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit
    export DEVICES=("Q5")
    source $RUN_SETUP
    ```

=== "Q50"
    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit
    export DEVICES=("Q50")
    source $RUN_SETUP
    ```

=== "Useita taustajärjestelmiä"
    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit
    export DEVICES=("Q5" "Q50")
    source $RUN_SETUP
    ```

#### Cirq { #cirq }
=== "Helmi"
    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-cirq
    export DEVICES=("Q5")
    source $RUN_SETUP
    ```

=== "Q50"
    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-cirq
    export DEVICES=("Q50")
    source $RUN_SETUP
    ```

=== "Useita taustajärjestelmiä"
    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-cirq
    export DEVICES=("Q5" "Q50")
    source $RUN_SETUP
    ```

!["QCS LUMIn webissä"](../../img/Quantum_jobs_lumi_web.png)

Napsauta Launch käynnistääksesi Jupyter-istunnon. Tämä käynnistää Jupytern komennolla python -m Jupyter lab. Jos käytät Helmiä/Q50:tä kvanttilaskennan kurssin aikana, kurssille voi olla luotu oma räätälöity ympäristö. Tässä tapauksessa voit käyttää kvanttitietokoneita Jupyter-for-courses-sovelluksen kautta.

!["QCS LUMIn web-kursseilla"](../../img/helmi_with_jupyter_for_courses_gui.png)


## Lisälukemista { #further-reading }
* [LUMIn web-käyttöliittymä](https://docs.lumi-supercomputer.eu/runjobs/webui/)
* [Jupyter LUMIn web-käyttöliittymässä](https://docs.lumi-supercomputer.eu/runjobs/webui/jupyter/)
* [Kvanttitietokoneiden käyttäminen LUMIn web-käyttöliittymän kautta](https://fiqci.fi/publications/2024-08-23-Lumi_web_introduction)