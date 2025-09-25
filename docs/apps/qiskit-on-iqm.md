---
tags:
  - Free
catalog:
  name: Qiskit-on-iqm
  description: open-source qiskit adapter for quantum computing
  description_fi: avoimen lähdekoodin qiskit-sovitin kvanttilaskentaan
  license_type: Free
  disciplines:
    - Quantum
  available_on:
    - LUMI
---

# Qiskit-on-iqm { #qiskit-on-iqm }

Qiskit on IQM on avoimen lähdekoodin qiskit-sovitin IQM:n kvanttitietokoneille. Se on
asennettu LUMI-järjestelmään nimellä `fiqci-vtt-qiskit`. Sitä käytetään kvanttipiirien
suorittamiseen [kvanttitietokoneilla](../computing/quantum-computing/running-quantum-jobs.md).


## Saatavilla { #available }

Tällä hetkellä tuetut [qiskit-on-iqm](https://iqm-finland.github.io/qiskit-on-iqm/)
versiot:

| Versio | Moduuli                               | LUMI  | Huomautukset    |
|:-------|:--------------------------------------|:-----:|-----------------|
| 17.8   | `fiqci-vtt-qiskit/17.8`               | X     |                 |

Kaikki moduulit perustuvat Tykkyyn ja käyttävät LUMI-container-wrapperia.
Mukana on wrapper-skriptejä, jotta yleiset komennot kuten `python`,
`python3`, `pip` ja `pip3` toimivat normaalisti. Lisätietoja, katso
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

Moduuli sisältää qiskitin kanssa usein käytettyjä Python-paketteja, kuten
qiskit-experiments, matplotlib, numpy ja jupyterlab.

## Lisenssi { #license }

qiskit-on-iqm on lisensoitu
[Apache License 2.0](https://github.com/iqm-finland/qiskit-on-iqm/blob/main/LICENSE) -lisenssillä.

## Käyttö { #usage }

Käyttääksesi `fiqci-vtt-qiskit`-moduulia LUMI:ssa, alusta se komennolla:

```bash
module use /appl/local/quantum/modulefiles
```

ja 

```bash
module load fiqci-vtt-qiskit
```

Tämä komento näyttää myös, miten `fiqci-vtt-qiskit` ladataan:

```bash
module avail fiqci-vtt-qiskit
```

### Esimerkkieräskripti { #example-batch-script }

Esimerkkieräskripti kvanttityön suorittamiseen:

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
module load fiqci-vtt-qiskit
export DEVICES=("Q5") #export DEVICES=("Q5" "Q50") to use Helmi and Q50
source $RUN_SETUP
python -u quantum_job.py
```

Lähetä skripti komennolla `sbatch <script_name>.sh`.

## Lisätietoja { #more-information }

- [Qiskit-IQM-dokumentaatio](https://iqm-finland.github.io/qiskit-on-iqm/)
- [Kvanttilaskenta](../computing/quantum-computing/running-quantum-jobs.md)