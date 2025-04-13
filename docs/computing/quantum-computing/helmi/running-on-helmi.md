
# Ajo Helmissä {#running-on-helmi}

!!! info "Anna palautetta!"
    **Kaikki palaute on erittäin arvostettua**, kommentteja kokemuksista voi lähettää [fiqci-feedback@postit.csc.fi](mailto:fiqci-feedback@postit.csc.fi).

## Tehtävien ajo {#running-jobs}

Tehtävät voidaan lähettää `q_fiqci` jonoon määrittämällä `--partition=q_fiqci` eräajoskryptissä.

Helmi tukee tällä hetkellä tehtävien lähettämistä käyttäen Qiskitia tai Cirqiä. Qiskit- ja Cirq-skriptejä voidaan lähettää vain tavallisina python-tiedostoina. Tehtävien lähettämiseksi ja ajamiseksi Helmille tulee käyttää oikeaa ympäristöä LUMI:lla.

* Ensiksi, aja `module use /appl/local/quantum/modulefiles`. Saatavilla olevat moduulit näkyvät nyt `module avail`-komennolla.
* Toiseksi, riippuen siitä haluatko käyttää Qiskit- tai Cirq-ympäristöä, suorita:
    * `module load helmi_qiskit` tai
    * `module load helmi_cirq`

`helmi_qiskit` ja `helmi_cirq` tarjoavat esivalmistettuja python-ympäristöjä, joita voi suorittaa suoraan Helmillä. Jos haluat lisätä omia python-paketteja esivalmistettuihin python-ympäristöihin, voit tehdä niin komennolla `python -m pip install --user package`.

!!! info "Luo oma python-ympäristösi"
    Käyttäjät voivat luoda oman python-ympäristönsä, jos haluavat. Ainoa esivaatimus on ladata `helmi_standard`-moduuli. Oman ympäristön luomiseen suositellaan [container wrapper tool](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

Helmillä tuetut nykyiset ohjelmistoversiot ovat:

| Ohjelmisto | Moduuli_nimi | Versiot |
|------------|--------------|---------|
| Cirq IQM:llä | cirq_iqm |  15.2  |
| Qiskit IQM:llä | qiskit_iqm |  15.5 |
| IQM asiakas | iqm_client | >= 20.11, <= 20.13 |

Tässä on esimerkki eräajoskryptistä tehtävien lähettämiseksi Helmillä

```bash
#!/bin/bash

#SBATCH --job-name=helmijob   # Työn nimi
#SBATCH --account=project_<id>  # Projekti laskutusta varten (slurm_job_account)
#SBATCH --partition=q_fiqci   # Osasto (jono) nimi
#SBATCH --ntasks=1              # Yksi tehtävä (prosessi)
#SBATCH --mem-per-cpu=2G       # muistin allokointi
#SBATCH --cpus-per-task=1     # Ytimien (säikeiden) määrä
#SBATCH --time=00:15:00         # Ajoaika (hh:mm:ss)

module use /appl/local/quantum/modulefiles

# kommentoi oikein rivi:
# module load helmi_qiskit
# tai
# module load helmi_cirq

python your_python_script.py
```

Eräajoskrypti voidaan sitten lähettää `sbatch`-komennolla. Voit myös lähettää interaktiivisia tehtäviä `srun`-komennon kautta.

```bash
srun --account=project_<id> -t 00:15:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py
```

`helmi_*`-moduuli asettaa oikean python-ympäristön Qiskitin tai Cirqin käyttöön yhdessä Helmin kanssa.

!!! info "Ajo Helmissä"
    Kun tehtävä lähetetään Helmille, käyttäjän slurm_job_account (projekti, jossa tehtävä suoritetaan) yhdistetään project_id:hen, ja tämä tieto siirretään VTT:lle laskutustarkoituksiin.

### Qiskit {#qiskit}

Lataa Qiskit-moduuli käyttämällä `module load helmi_qiskit`.

Qiskit-python-skripteissä sinun tulee sisällyttää seuraava:

```python
import os

from qiskit import QuantumCircuit, transpile
from iqm.qiskit_iqm import IQMProvider

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')  # Tämä asetetaan moduulin lataamisen yhteydessä

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

shots = 1000  # Aseta haluamiesi ajojen määrä

# Luo kvanttivirtapiirisi.
# Tässä on esimerkki
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

### Cirq {#cirq}

Lataa Cirq-moduuli käyttämällä `module load helmi_cirq`.

```python
import os

import cirq
from iqm.cirq_iqm import Adonis
from iqm.cirq_iqm.iqm_sampler import IQMSampler

adonis = Adonis()

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')  # Tämä asetetaan moduulin lataamisen yhteydessä

sampler = IQMSampler(HELMI_CORTEX_URL)

shots = 1000

# Luo kvanttivirtapiirisi
# Tässä on esimerkki
q1, q2 = cirq.NamedQubit('QB1'), cirq.NamedQubit('QB2')
circuit = cirq.Circuit()
circuit.append(cirq.H(q1))
circuit.append(cirq.CNOT(q1, q2))
circuit.append(cirq.measure(q1, q2, key='m'))
print(circuit)

decomposed_circuit = adonis.decompose_circuit(circuit)
routed_circuit, initial_mapping, final_mapping = adonis.route_circuit(decomposed_circuit)

# Valinnaisesti tulosta yhdistely
# print(routed_circuit)
# print(initial_mapping)
# print(final_mapping)

result = sampler.run(routed_circuit, repetitions=shots)
print(result.measurements['m'])
```

## Lisäesimerkkejä {#additional-examples}

Lisää [esimerkkejä löytyy täältä](https://github.com/FiQCI/helmi-examples).
Esimerkit korostavat simuloinnin ja todellisen fyysisen kvanttitietokoneen välisiä eroja
sekä kuinka rakentaa virtapiirisi optimaalisten tulosten saamiseksi Helmissä. Arkistossa on myös hyödyllisiä
pätkiä tehtävien lähettämiseen.

## Simuloidut testiajot {#simulated-test-runs}

Koska kvanttiresurssit voivat olla rajallisia, on suositeltavaa valmistella etukäteen koodit ja algoritmit, joita aiot ajaa Helmillä. Tätä prosessia varten [`qiskit-on-iqm` tarjoaa väärennetyn melumallin mukaan](https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html#noisy-simulation-of-quantum-circuit-execution). Voit ajaa väärennettyä melumallia paikallisesti läppärilläsi simulointia ja testausta varten.

Qiskitia ja Cirqiä koskevat esimerkit ja ohjeet LUMI-Helmi-osaston käyttöön ovat saatavilla. [Löydät ne täältä](https://github.com/FiQCI/fiqci-examples).

## Työn metadata {#job-metadata}

Lisämetadata tiedoista voidaan kysyä suoraan Qiskitilla. Esimerkiksi:

```python
provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

#Palvelimen tietojen hakeminen
print(f'Natiivitoiminnot: {backend.operation_names}')
print(f'Qubittien lukumäärä: {backend.num_qubits}')
print(f'Yhdistelykartta: {backend.coupling_map}')

transpiled_circuit = transpile(circuit, backend)
job = backend.run(transpiled_circuit, shots=shots)
result = job.result()
exp_result = result._get_experiment(circuit)

print("Työn ID: ", job.job_id())  # Lähetetyn työn id:n haku
print(result.request.circuits)  # Lähetetyn virtapiiripyyntöä hakeminen
print("Kalibrointijoukon ID: ", exp_result.calibration_set_id)  # Nykyisen kalibrointijoukon id:n hakeminen.
print(result.request.qubit_mapping)  # Qubit-yhdistelyn hakeminen
print(result.request.shots)  # Haluamiesi ajojen lukumäärän hakeminen.

#hae työ käyttäen job_id:tä aiemmasta istunnosta
#old_job = backend.retrieve_job(job_id)
```

!!! info "Tallenna työsi ID!"
    Huomioi, että tällä hetkellä ei ole menetelmää aiempien Työn ID:iden listaamiseksi, joten on suositeltavaa aina tulostaa Työn ID työn lähettämisen jälkeen ja tallentaa se jonnekin! Sama koskee kalibrointijoukon ID:tä.

## Arvostelun mittasuhteet {#figures-of-merit}

Arvostelun mittasuhteet (tai laadun mittarit) voivat olla tarpeen julkaistaessa Helmilla tuotettua työtä. Ne antavat myös käsityksen Helmin nykyisestä tilasta. `helmi-examples` sisältää apuskriptin kalibrointidatan saamiseksi, mukaan lukien arvostelun mittasuhteet. Skripti löytyy [täältä](https://github.com/FiQCI/helmi-examples/blob/main/scripts/get_calibration_data.py). Tämä tiedosto voidaan lisätä omiin python-skripteihisi ja se palauttaa datan json-muodossa. Huomaa, että viimeisimmän kalibrointidatan kysely voi antaa puutteellisen tai vanhentuneen mittarijoukon. Siksi kalibrointijoukon ID:t tulee tallentaa Työn ID:iden oheen.

Tässä on lyhyt kuvaus annetuista mittareista kyselyn yhteydessä:

| Mittari                          | Kuvaus                                                                                                                       |     |     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| T1 Aika (s)                      | T1 aika kutsutaan pituussuuntainen rentoutumisnopeus ja se kuvaa kuinka nopeasti qubitin jännitetila palautuu perustilaansa. |     |     |
| T2 Aika (s)                      | T2 aika kutsutaan poikittainen rentoutumisnopeus ja se kuvaa superpositiotilan koherenssin menettämistä.                      |     |     |
| T2 Kaiku-Aika (s)                | T2 kaiku-aika kuvaa qubitin superpositiotilan koherenssin menettämistä. Se on tarkempi kuin T2 Aika, koska se on vähemmän altis matalataajuuksiselle hälylle. |     |     |
| Yksittäisen laukauksen luennan uskollisuus | Tämä kuvaa uskollisuutta yksittäisen laukauksen luentojen suorittamisen aikana qubit-tilasta. Yksittäisen laukauksen luenta valmistaa 50% qubit-tiloista jännitetilaansa ja 50% perustilaan. |     |     |
| Yksittäisen laukauksen luenta 01 virhe | Virhe jännitetilan ('1') määrittämisessä, kun tila on perustilassa ('0').                                                 |     |     |
| Yksittäisen laukauksen luenta 10 virhe | Virhe perustilan ('0') määrittämisessä, kun tila on jännitetilassa ('1').                                                |     |     |
| Fidelity 1QB portit keskiarvona    | Tämä lasketaan Randomized Benchmarkingin avulla ja kuvaa keskimääräistä porttiuskollisuutta, kun satunnainen sarja yksittäisiä qubit Clifford-portteja sovelletaan. |     |     |
| Fidelity 2QB Cliffords keskiarvona | Tämä lasketaan Randomized Benchmarkingin avulla, joka näyttää keskimääräisen Clifford-porttiuskollisuuden.                     |     |     |
| CZ portin uskollisuus             | Ohjatun z-portin uskollisuus, joka lasketaan lomitetun randomisoidun benchmarking-menetelmän avulla, jossa ohjattu z-portti lomitetaan.  |     |     |

Lisätietoa mittarista saa ottamalla yhteyttä [CSC:n Service Deskiin](../../../support/contact.md), saavutettavissa osoitteessa [servicedesk@csc.fi](mailto:servicedesk@csc.fi).

## Helmin käyttö Lumi-verkkorajapinnassa {#using-helmi-on-lumi-web-interface}

[LUMI-verkkorajapinta](https://docs.lumi-supercomputer.eu/runjobs/webui/) mahdollistaa käyttäjille kvanttitehtävien suorittamisen Helmillä verkkorajapinnan kautta. Kirjautumista LUMI:n verkkorajapinnalle koskevat tiedot voi lukea [LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/firststeps/loggingin-webui/).

### Helmin käyttäminen {#accessing-helmi}

Kun olet onnistuneesti autentikoinut, sinulla pitäisi nyt olla pääsy koontinäyttöösi. Napsauta Jupyter-sovellusta, valitse projektisi ja osasto q_fiqci. Jos sinulla on aktiivinen varaus, voit käyttää sitä valitsemalla se kohdan Varaukset alta.

Suosittelemme käyttämään 'Lisäasetuksia'. Kohdassa 'Custom init' valitse 'Teksti', ja kohdassa 'Skriptin käynnistäminen' -tekstikentässä anna seuraava skripti ympäristön konfiguroimiseksi kvanttiohjelmistoa varten.

```bash
module use /appl/local/quantum/modulefiles
module load helmi_qiskit # tai module load helmi_cirq
```

<p align="center">
    <img src="../../../../img/helmi_with_lumi_web.png" alt="Helmi Lumilla web-käyttöliittymän kanssa">
</p>

Napsauta käynnistä käynnistääksesi Jupyter-istuntosi. Tämä käynnistää Jupyterin komennolla python -m Jupyter lab. Jos käytät Helmiä kvanttilaskentakurssin aikana, saatetaan erityisesti kurssia varten luoda mukautettu ympäristö. Tässä tapauksessa voit käyttää Helmiä Jupyter-for-courses-sovelluksen kautta.

<p align="center">
    <img src="../../../../img/helmi_with_jupyter_for_courses_gui.png" alt="Helmi Lumilla web-käyttöliittymän kanssa">
</p>

## Lisälukemista {#further-reading}
* [Lumi verkkokäyttöliittymä](https://docs.lumi-supercomputer.eu/runjobs/webui/)
* [Jupyter Lumi verkkokäyttöliittymällä](https://docs.lumi-supercomputer.eu/runjobs/webui/jupyter/)
* [Helmin käyttö Lumi verkkokäyttöliittymällä](https://fiqci.fi/_posts/2024-08-23-Lumi_web_introduction/)

