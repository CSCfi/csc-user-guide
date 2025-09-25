---
tags:
  - Free
catalog:
  name: GPAW
  description: Versatile DFT package
  description_fi: Monipuolinen DFT-paketti
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# GPAW { #gpaw }

GPAW on tehokas ohjelmistopaketti elektronirakennelaskentaan. Se perustuu tiheysfunktionaaliteoriaan (DFT), joka on toteutettu projector augmented wave (PAW) -menetelmän puitteissa, ja se voi käyttää erilaisia kantajoukkoja (tasaiset reaalitilan hilat, tasoaallot, lokalisoidut atomiorbitaalit).

Ohjelmiston ominaisuuksiin kuuluvat mm.:

- kokonaisenergialaskut
- rakenneoptimoinnit
- erilaiset reunaehdot (finiitti, lanka, kalvo, bulk)
- tehokas rinnakkaistus
- viritystilojen ominaisuudet aikariippuvan tiheysfunktionaaliteorian puitteissa

[TOC]

## Saatavuus { #available }

- Puhti: 20.10.0, 21.1.0, 21.6.0, 22.1.0, 22.8.0
- Mahti: 20.10.0, 21.1.0, 21.6.0, 22.1.0, 22.8.0, 23.9.1, 24.1.0
- Katso kaikki saatavilla olevat versiot (ja oletusversio) komennolla
    `module avail gpaw`
- Päätteeseen `-omp` päättyvissä moduleissa valinnainen OpenMP-rinnakkaistus on käytössä;
    katso lisätietoja kohdasta [GPAW:n dokumentaatio rinnakkaisajoista](https://wiki.fysik.dtu.dk/gpaw/documentation/parallel_runs/parallel_runs.html?highlight=openmp#manual-openmp).

### PAW-asetukset { #paw-setups }

Kaikissa asennuksissa (paitsi 24.1.0) käytetään GPAW:n PAW-asetusten versiota **0.9.20000**.

## Lisenssi { #license }

GPAW on vapaa ohjelmisto, jota jaellaan GPL-lisenssillä, versio 3+.

## Käyttö { #usage }

Koska oletusversio, jonka saa komennolla `module load gpaw`, voi muuttua uusien versioiden myötä, suosittelemme aina lataamaan tietyn GPAW-version:

```bash
module load gpaw/version
```

!!! warning "Huom."
    CSC-ympäristössä GPAW-laskut ajetaan komennolla `gpaw-python`.

### ELPA:n käyttöönotto { #enabling-elpa }

Mahti-järjestelmässä GPAW voi käyttää ELPA-kirjastoa diagonalisaatiovaiheen nopeuttamiseen. Erityisesti LCAO-laskuissa ELPA voi parantaa suorituskykyä. ELPA:n käyttöä varten asetus 'use_elpa' : True tulee sisällyttää GPAW-syötteen rinnakkaistusasetuksiin (katso lisätietoja: [GPAW:n dokumentaatio](https://wiki.fysik.dtu.dk/gpaw/documentation/lcao/lcao.html#notes-on-performance)).

### Eräajoesimerkit { #batch-script-examples }

=== "Puhti"

    ```bash
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40
    #SBATCH --mem-per-cpu=2GB
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END #uncomment to get mail

    # this script runs a 80 core (2 full nodes) gpaw job, requesting
    # 30 minutes time and 2 GB of memory for each core

    module load gpaw/21.1.0

    srun gpaw-python input.py
    ```

=== "Mahti (hybridi MPI/OpenMP -rinnakkaistus)"

    ```bash
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=medium
    #SBATCH --nodes=10
    #SBATCH --ntasks-per-node=32
    #SBATCH --cpus-per-task=4
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END #uncomment to get mail

    # this script runs a 1280 core (10 full nodes) gpaw job, using hybrid
    # MPI/OpenMP parallelization with 4 OpenMP threads per node,
    # requesting 30 minutes time.
    # Please experiment with optimum MPI task / OpenMP thread ratio with
    # your particular input

    # Note: only the modules with "-omp" ending supports OpenMP
    # (default version in Mahti is OpenMP enabled)

    module load gpaw/21.1.0-omp

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

    srun gpaw-python input.py
    ```

=== "Mahti (pelkkä MPI-rinnakkaistus)"

    ```bash
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=medium
    #SBATCH --nodes=10
    #SBATCH --ntasks-per-node=128
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END #uncomment to get mail

    # this script runs a 1280 core (10 full nodes) gpaw job, using pure
    # MPI parallelization requesting 30 minutes time.

    module load gpaw/21.1.0

    export OMP_NUM_THREADS=1

    srun gpaw-python input.py
    ```

## Lisätietoja { #more-information }

- [GPAW-kotisivu](https://wiki.fysik.dtu.dk/gpaw/)