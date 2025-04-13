# Ensimmäisen kvanttitietokoneajosi suorittaminen Helmillä LUMIn kautta

Jos olet hakenut projektia, sinut on hyväksytty, olet asentanut ssh-avaimet ja saanut pääsyn LUMIin, seuraava askel on suorittaa ensimmäinen kvanttitietokoneajosi oikealla kvanttitietokoneella! Tämä on opas siihen, kuinka se tehdään. Ainoa asia, joka sinun tarvitsee tietää, on projektinumerosi!

## Ympäristön konfigurointi {#configuring-the-environment}

Ensimmäinen askel, kun olet kirjautunut LUMIin (`ssh lumi` päätelaitteellasi), on ympäristön konfigurointi. LUMIin ensimmäistä kertaa kirjauduessa perusympäristö ei sisällä tarvittavia työkaluja kvanttiajojen lähettämiseen, joten kvanttiohjelmistopino on luotu asettamaan oikea Python-virtuaaliympäristö ja tarvittavat ympäristömuuttujat. Tämä haetaan LUMIn LMOD-järjestelmästä käyttäen *moduleita*.

Kvanttiohjelmistopinoa käyttääksesi sinun täytyy ensin ladata Kvanttimodulipuu.

```bash
module use /appl/local/quantum/modulefiles
```

Vaihtoehtoisesti voit saavuttaa saman tuloksen lataamalla Local-quantum-modulin.

```bash
module load Local-quantum
```

Tämän jälkeen voit nähdä listan saatavilla olevista *moduleista* komennolla `module avail`. Kvanttiohjelmistopinojen tulisi olla ylimpänä! Tässä läpikäynnissä käytetään Qiskit-ohjelmistoa, joten seuraava askel on ladata moduli nykyiseen ympäristöön

```bash
module load helmi_qiskit
```

## Ensimmäisen kvanttiohjelman luominen {#creating-your-first-quantum-program}

Seuraava askel on luoda kvanttireaktio! Tässä luodaan yksinkertainen bell-tila kahden kubitin välillä, osoittaen niiden keskinäisen lomittumisen! Tässä käytetään Qiskitiä, mutta askeleet ovat hyvin samanlaisia Cirqille. On suositeltavaa työskennellä projektisi väliaikaisessa hakemistossa, johon voit siirtyä komennolla `cd /scratch/project_xxx`, syöttäen oma projektinumerosi.

!!! info "Vinkki!"
	
	Voit nopeasti nähdä LUMI-työtilasi komennolla
	`module load lumi-workspaces` ja
	`lumi-workspaces`

Luodaan ensin Python-tiedosto komennolla `nano first_quantum_job.py`. Tässä käytämme `nano`, mutta jos olet tottuneempi, voit käyttää `vim` tai `emacs`. Tämä avaa `nano`-tekstieditorin, hyödylliset komennot ovat alhaalla; tallenna ja poistu painamalla CTRL+X + Y.

### Kirjastojen tuonti {#importing-the-libraries}

Aloitetaan tuomalla oikeat Python-kirjastot

```python
import os
from qiskit import QuantumCircuit, QuantumRegister, transpile
from iqm.qiskit_iqm import IQMProvider
```

### Piirin luominen {#creating-the-circuit}

Kvanttipiiri luodaan määrittelemällä `QuantumRegister`, joka pitää kubitit ja klassiset bitit vastaavasti. Koska tämä piiri vaatii vain 2 kubittia, luomme vain `QuantumRegister`-nimikkeen kooltaan 2. Myös laukaisu määrä määritellään täällä. Laukaisumäärä tarkoittaa kvanttipiirin suoritusmäärää. Teemme tämän, koska kvanttitietokoneet ovat todennäköisyysperäisiä koneita ja toistamalla kokeen monta kertaa voimme päästä lähelle determinististä tulosta, jotta voimme vetää johtopäätöksiä. Hyvä laukaisumäärä ensimmäiselle kvanttile tuotetulle kvanttityölle on `shots = 1000`. Laukaisujen lisääminen lisää tulostesi tarkkuutta. 

```python
shots = 1000  # Quantum Circuitin toistojen määrä

qreg = QuantumRegister(2, "qB")
circuit = QuantumCircuit(qreg, name='Bell pair circuit')
```

Nyt lisätään joitain portteja piiriin. Tässä lisätään Hadamard-portti ensimmäiseen kubittiin tai kvanttirekisterin ensimmäiseen kubittiin. Sitten lisätään kontrolloitu-x-portti kahdella argumentilla, koska se on kahden kubitin portti. 

```python
circuit.h(qreg[0])  # Hadamard-portti kvanttirekisterin ensimmäiseen kubittiin
circuit.cx(qreg[1], qreg[0])  # Kontrolloitu-X-portti toisen ja ensimmäisen kubittien välille
circuit.measure_all()  # Mittaa kaikki kvanttirekisterin kubitit.
```

Huomaa, että [`measure_all()`](https://qiskit.org/documentation/stubs/qiskit.circuit.QuantumCircuit.html#qiskit.circuit.QuantumCircuit.measure_all) luo oman [`ClassicalRegister`](https://qiskit.org/documentation/stubs/qiskit.circuit.ClassicalRegister.html)!

Nyt piiri on luotu! Jos haluat, voit nähdä miltä piiriki näyttää lisäämällä print-komennon `print(circuit.draw())` ja nopeasti suorittamalla python-skriptin. 

## Taustajärjestelmän asettaminen {#setting-the-backend}

Ensin meidän on asetettava palveluntarjoajamme ja taustajärjestelmämme. Palveluntarjoaja tarjoaa käyttöliittymän kvanttitietokoneelle ja taustajärjestelmä tarjoaa työkalut kvanttityön lähettämiseksi. `HELMI_CORTEX_URL` on päätepiste, jolla saavutetaan Helmi ja se on tavoitettavissa vain `q_fiqci` -osiosta. Tämä ympäristömuuttuja asetetaan automaattisesti lataamalla mikä tahansa `helmi_*` -moduli, kuten `helmi_qiskit` -moduli.

```python
HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()
```
### Piirin purkaminen (*Valinnainen*) {#decomposing-the-circuit}

Seuraava askel on valinnainen, jossa juuri luotu kvanttipiiri muutetaan sen *perusporteiksi*. Nämä perusportit ovat todellisia kvanttiportteja kvanttitietokoneessa. Purkuprosessi tarkoittaa yllä olevien Hadamard- ja kontrolloitu-x-porttien muuntamista sellaiseen muotoon, joka voidaan fyysisesti suorittaa kvanttitietokoneella. Helmin perusportit ovat lomittumisporttiin kontrolloitu-z ja yhden kubitin phased-rx portti. Qiskitissä nämä määritellään taustajärjestelmässä ja ne voidaan tulostaa komennolla `backend.operation_names`. 

```python
circuit_decomposed = transpile(circuit, backend=backend)
```
Voit myös tulostaa piirin kuten aiemmin `print(circuit_decomposed.draw())` nähdäksesi miltä se näyttää! 

### *Valinnainen* Kubittien kartoittaminen {#optional-qubit-mapping}

Tämä on valinnainen askel mutta voi olla hyödyllinen saavuttaaksesi parhaan mahdollisen tuloksen kvanttitietokoneelta. Tämä on Python-sanakirja, joka yksinkertaisesti määrittelee, mitkä kvanttirekisterin kubitit tulee kartoittaa mihin *fyysisiin* kubitteihin.

```python
qubit_mapping = {
                qreg[0]: 0,
                qreg[1]: 2,
            }
```

Tässä kartoitamme ensimmäisen kvanttirekisterin kubitin ensimmäiseen Helmin kubittiin, QB1, joka sijaitsee nollasijainnissa Qiskitin nollaperusteisen numeroinnin vuoksi. Toinen kubitti sitten kartoitetaan QB3:een. Tässä käytimme Helmin topologiaa.
стоящего работать в поле quantum.
transfernentа la click, etablishent и также чтобы wasser, jdроекции, sieveый для предоставления, входский корансылки. node'selectron the || обза ménage- 기`.
ukro-модек-фракции/

----------------------
The two qubit Controlled-X gate we implemented in our circuit is currently on the second of our two qubits in the Quantum register, `qreg[1]`. Due to Helmi's topology this needs to be mapped to QB3 on Helmi. The 1 qubit Hadamard gate can be mapped to any of the *outer* qubits, QB1, QB2, QB4, QB5, here we choose QB1. 

Note that this step is entirely optional. Using the `execute` function automatically does the mapping based on the information stored in the backend. Inputting the qubit mapping simply gives more control to the user. 

To transpile a circuit using the specified qubit mapping you can do the following:

```python
circuit_decomposed = transpile(circuit, backend=backend, initial_layout=qubit_mapping)
```

### Työn lähettäminen {#submitting-the-job}

Nyt voimme suorittaa kvanttityömme!

```python
job = backend.run(circuit_decomposed, shots=shots)
```

### Työn tilan tarkastelu {#viewing-the-status-of-your-job}

Voit nähdä työsi tilan komennolla 

```python
job.status()
```

### Tulokset {#results}

Ennen lähettämistä meidän on varmistettava, että saamme tuloksia! Kvanttityö palauttaa niin kutsutut **laskurit**. Laskurit ovat tulosten kertyminen niistä 1000 kerrasta, kun piiri lähetetään QPU:lle. Joka kerta kun piiri lähetetään, palautetaan binaarinen *tila*, joka sitten lisätään laskuriin. Tässä tapauksessa, kun lähetämme 2 kubitin piirin, on neljä mahdollista tulostustilaa: `00, 11, 01, 10`. Odotettujen tulosten pitäisi olla, että noin 50 % laskureista on tilassa `00` ja 50 % tilassa `11`. Kubittien tilat ovat siten lomittuneet: jos yksi kubitti mitataan olevan tilassa |0>, toinen kubitti romahtaa välittömästi samaan tilaan, ja päinvastoin. Koska todelliset kvanttitietokoneet eivät ole täydellisiä, näet todennäköisesti myös, että jotkut mittaukset löytävät tilat |01> ja |10>.

Tulosten tulostamiseksi lisää:

```python
counts = job.result().get_counts()
print(counts)
```

Voit myös tulostaa `job.result()` kokonaisuudessaan, joka sisältää kaikki tiedot työsi tuloksista.

## Tallenna tiedostosi {#save-your-file}

Kun olet tehnyt ensimmäisen kvanttiohjelmasi, muista tallentaa se! CTRL+X, sitten Y tallentaaksesi tiedoston.

## Ajon suorittaminen LUMIn kautta {#running-the-job-through-lumi}

Suorittaaksesi kvanttiohjelmasi LUMIn kautta sinun tulee lähettää työ SLURM-eräajosuunnittelijan kautta LUMIin. Helmin käyttö tapahtuu `q_fiqci` -osasta. Samassa hakemistossa, johon olet tallentanut kvanttiohjelmasi, voit lähettää työn SLURMille käyttäen:

```bash
srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition q_fiqci python -u first_quantum_job.py
```

Muista lisätä oma projektitilisi!

Tämä lähettää työn *interaktiivisesti* tarkoittaen, että tulos tulostuu suoraan päätelaitteen näytölle. Jos haluat, voit myös lähettää sen käyttäen `sbatch` seuraavan rungon eräskriptillä. Käyttäen `nano`, kuten aiemmin, luo skripti `batch_script.sh`.

```bash
#!/bin/bash -l

#SBATCH --job-name=helmijob   # Työn nimi
#SBATCH --output=helmijob.o%j # stdout tulostiedoston nimi
#SBATCH --error=helmijob.e%j  # stderr virhetiedoston nimi
#SBATCH --partition=q_fiqci   # Osion nimi
#SBATCH --ntasks=1              # Yksi tehtävä (prosessi)
#SBATCH --mem-per-cpu=2G       # Muistivaraus
#SBATCH --cpus-per-task=1     # Ytimien (säikeiden) määrä
#SBATCH --time=00:15:00         # Suoritusaika (hh:mm:ss)
#SBATCH --account=project_xxx  # Laskutusprojekti

module use /appl/local/quantum/modulefiles
module load helmi_qiskit

python -u first_quantum_job.py
```
Tämä voidaan lähettää `sbatch batch_script.sh` komennolla samassa hakemistossa kuin Python-tiedostosi. Työjonossaan olevien SLURM-töiden tilaa voidaan seurata komennolla `squeue -u käyttäjänimi` ja työn valmistuttua tulokset löytyvät `helmijob.oxxxxx` tiedostosta. Tämän voi tulostaa päätelaitteelle komennolla `cat`. 

## Onnittelut! {#congratulations}

Onnittelut! Olet juuri suorittanut ensimmäisen ajosi Helmillä.

Koko Python-skripti löytyy alta.

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

# Poista kommentti, jos haluat tulostaa piirin
# print(circuit.draw())

HELMI_CORTEX_URL = os.getenv('HELMI_CORTEX_URL')

provider = IQMProvider(HELMI_CORTEX_URL)
backend = provider.get_backend()

# Taustajärjestelmän tietojen hakeminen
# print(f'Natiivitoiminnot: {backend.operation_names}')
# print(f'Kubitit: {backend.num_qubits}')
# print(f'Kytkentäkartta: {backend.coupling_map}')

transpiled_circuit = transpile(circuit, backend)
job = backend.run(transpiled_circuit, shots=shots)
result = job.result()
exp_result = job.result()._get_experiment(circuit)
# Voit hakea työn myöhemmin backend.retrieve_job(job_id)
# Poista seuraavat rivit kommentista saadaksesi lisätietoja lähetetystä työstäsi
# print("Työn ID: ", job.job_id())
# print(result.request.circuits)
# print("Kalibrointijoukko ID: ", exp_result.calibration_set_id)
# print(result.request.qubit_mapping)
# print(result.request.shots)

counts = result.get_counts()
print(counts)
