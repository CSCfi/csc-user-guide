---
tags:
  - Free
catalog:
  name: Cirq-on-iqm
  description: open-source cirq adapter for quantum computing
  description_fi: avoimen lähdekoodin cirq-sovitin kvanttilaskentaan
  license_type: Free
  disciplines:
    - Quantum
  available_on:
    - LUMI
---

# Cirq-on-iqm { #cirq-on-iqm }

Cirq on IQM on avoimen lähdekoodin cirq-sovitin IQM:n kvanttitietokoneille. Se on LUMI-järjestelmässä nimellä `fiqci-vtt-cirq`. Sitä käytetään kvanttipiirien suorittamiseen [kvanttitietokoneilla](../computing/quantum-computing/running-quantum-jobs.md).

## Saatavilla { #available }

Tällä hetkellä tuetut [cirq-on-iqm](https://iqm-finland.github.io/cirq-on-iqm/) -versiot:

| Versio | Moduuli                               | LUMI  | Huomautukset    |
|:-------|:--------------------------------------|:-----:|-----------------|
| 16.2   | `fiqci-vtt-cirq/16.2`                 | X     |                 |

Kaikki moduulit perustuvat Tykkyyn ja käyttävät LUMI-container-wrapperia.
Wrapper-skriptit on tarjottu, jotta yleiset komennot, kuten `python`,
`python3`, `pip` ja `pip3`, toimivat normaalisti. Lisätietoja:
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

Moduuli sisältää Python-paketteja, joita käytetään usein cirqin kanssa, kuten matplotlib,
numpy ja jupyterlab.

## Lisenssi { #license }

cirq-on-iqm on lisensoitu
[Apache License 2.0](https://github.com/iqm-finland/cirq-on-iqm/blob/main/LICENSE) -lisenssillä.

## Käyttö { #usage }

Käyttääksesi `fiqci-vtt-cirq`-moduulia LUMIssa, alusta se näin:

```bash
module use /appl/local/quantum/modulefiles
```

ja 

```bash
module load fiqci-vtt-cirq
```

Tämä komento näyttää myös, miten `fiqci-vtt-cirq` ladataan:

```bash
module avail fiqci-vtt-cirq
```

### Esimerkkieräskripti { #example-batch-script }

Esimerkkieräskripti kvanttityön ajamiseen:

```bash title="LUMI"
#!/bin/bash -l

#SBATCH --job-name=quantumjob     # Job name
#SBATCH --output=quantumjob.o%j   # Name of stdout output file
#SBATCH --error=quantumjob.e%j    # Name of stderr error file
#SBATCH --partition=q_fiqci     # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --cpus-per-task=1       # Number of cores (threads)
#SBATCH --mem-per-cpu=1G        # Memory allocation
#SBATCH --time=00:15:00         # Run time (hh:mm:ss)
#SBATCH --account=project_xxx   # Project for billing

module use /appl/local/quantum/modulefiles
module load fiqci-vtt-cirq

export DEVICES=("Q5") #export DEVICES=("Q5" "Q50") to use Helmi and Q50
source $RUN_SETUP

python -u quantum_job.py
```

Lähetä skripti komennolla `sbatch <script_name>.sh`.

## Lisätietoja { #more-information }

- [Cirq-IQM-dokumentaatio](https://iqm-finland.github.io/cirq-on-iqm/user_guide.html)
- [Kvanttilaskenta](../computing/quantum-computing/running-quantum-jobs.md)