
---
tags:
  - Free
---

# Cirq-on-iqm

Cirq on IQM on avoimen lähdekoodin cirq-sovitin IQM-kvannietokoneille. Se 
asennetaan nimellä `helmi_cirq` LUMI:in. Sitä käytetään kvanttipiirien suorittamiseen 
[Helmissä](../computing/quantum-computing/helmi/running-on-helmi.md).

## Saatavilla {#available}

Tällä hetkellä tuetut [cirq-on-iqm](https://iqm-finland.github.io/cirq-on-iqm/) versiot:

| Versio  | Moduuli                               | LUMI  | Huomautuksia    |
|:--------|:--------------------------------------|:-----:|-----------------|
| 15.2    | `helmi_cirq/15.2`                     | X     |                 |

Kaikki moduulit pohjautuvat Tykkyyn LUMI-container-wrapperin avulla.
Käärintäskriptejä on tarjottu niin, että yleiset komennot kuten `python`,
`python3`, `pip` ja `pip3` toimivat normaalisti. Lisätietoja on saatavilla 
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

Moduuli sisältää Python-paketteja, joita käytetään usein cirq:n kanssa, kuten matplotlib, 
numpy ja jupyterlab.

## Lisenssi {#license}

Cirq-on-iqm on lisensoitu
[Apache License 2.0](https://github.com/iqm-finland/cirq-on-iqm/blob/main/LICENSE) -lisenssillä.

## Käyttö {#usage}

Käyttääksesi `helmi_cirq` LUMI:lla, alustaa se näin:

```bash
module use /appl/local/quantum/modulefiles
```

ja

```bash
module load helmi_cirq
```

Tämä komento näyttää myös kuinka `helmi_cirq` ladataan:

```bash
module avail helmi_cirq
```

### Esimerkkieräskripti {#example-batch-script}

Esimerkki eräskriptistä kvanttilaskentatehtävän suorittamiseen Helmillä:

```bash title="LUMI"
#!/bin/bash -l

#SBATCH --job-name=helmijob     # Työn nimi
#SBATCH --output=helmijob.o%j   # Stdout-tiedoston nimi
#SBATCH --error=helmijob.e%j    # Stderr-tiedoston nimi
#SBATCH --partition=q_fiqci     # Osio (jono) nimi
#SBATCH --ntasks=1              # Yksi tehtävä (prosessi)
#SBATCH --cpus-per-task=1       # Ytimien (säikeiden) määrä
#SBATCH --mem-per-cpu=1G        # Muistin jakaminen
#SBATCH --time=00:15:00         # Suoritusaika (hh:mm:ss)
#SBATCH --account=project_xxx   # Projekti laskutusta varten

module use /appl/local/quantum/modulefiles
module load helmi_cirq

python -u quantum_job.py
```

Lähetä skripti `sbatch <script_name>.sh` komennolla.

## Lisätietoa {#more-information}

- [Cirq-IQM dokumentaatio](https://iqm-finland.github.io/cirq-on-iqm/user_guide.html)
- [Kvanttitietokoneet](../computing/quantum-computing/helmi/running-on-helmi.md)

