---
tags:
  - Free
catalog:
  name: Pennylane
  description: Free open-source software framework for quantum machine learning and quantum computing
  description_fi: Ilmainen avoimen lähdekoodin ohjelmistokehys kvanttikoneoppimiseen ja kvanttilaskentaan
  license_type: Free
  disciplines:
    - Quantum
  available_on:
    - LUMI
---

# Pennylane

Pennylane on avoimen lähdekoodin, alustariippumaton Python-kirjasto kvanttikoneoppimiseen, kvanttikemiaan ja kvanttilaskentaan. Pennylane-lightning on Pennylanen korkean suorituskyvyn tilavektorisimulaattori. Se on tällä hetkellä GPU-tuettu LUMIssa [Kokkos](https://kokkos.github.io/kokkos-core-wiki/)-kehyksen kautta.

## Saatavilla { #available }

Tällä hetkellä tuetut Pennylane-versiot:

| Versio | Moduuli                              | LUMI  | Huomautukset    |
|:-------|:-------------------------------------|:-----:|-----------------|
| 0.42.0 | `pennylane-lightning/0.42.0-gpu`     | X     | oletusversio    |
| 0.41.1 | `pennylane-lightning/0.41.1-gpu`     | X     |                 |
| 0.40.0 | `pennylane-lightning/0.40.0-gpu`     | X     |                 |

Kaikki moduulit perustuvat Tykkyyn ja käyttävät LUMI-container-wrapperia.
Saatavilla on wrapper-skriptejä, jotta yleiset komennot kuten `python`,
`python3`, `pip` ja `pip3` toimivat normaalisti. Lisätietoja: 
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

## Lisenssi { #license }

Pennylane on lisensoitu
[Apache License 2.0](https://github.com/PennyLaneAI/pennylane/blob/master/LICENSE) -lisenssillä.

## Käyttö { #usage }

Käyttääksesi Pennylanen oletusversiota LUMIssa, alusta se komennolla:

```bash
module use /appl/local/quantum/modulefiles
```

ja 

```bash
module load pennylane-lightning
```

Jos haluat tietyn version ([katso käytettävissä olevat versiot yllä](#available)), käytä:

```bash
module load pennylane-lightning/0.42.0-gpu
```

missä `0.42.0-gpu` on määritetty versio

Tämä komento näyttää myös kaikki saatavilla olevat versiot:

```bash
module avail pennylane-lightning
```

### Esimerkkieräajon skripti { #example-batch-script }

Esimerkkieräajon skripti, joka varaa yhden GPU:n ja yhden CPU-ytimen yhdellä solmulla:

```bash title="LUMI"
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=dev-g
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=128G
#SBATCH --time=0:10:00
#SBATCH --gpus=1
#SBATCH --job-name=pennylane-example

# setting environment variables to specify how the OpenMP threads in a program are bound to processors
export OMP_PROC_BIND=spread  
export OMP_PLACES=threads

module use /appl/local/quantum/modulefiles # or module load Local-quantum
module load pennylane-lightning
python <file_name>.py
```

Lähetä skripti komennolla `sbatch <script_name>.sh`

## Lisätietoja { #more-information }

- [Pennylanen dokumentaatio](https://docs.pennylane.ai/en/stable/code/qml.html)
- [Pennylane-lightningin dokumentaatio](https://docs.pennylane.ai/projects/lightning/en/stable/)