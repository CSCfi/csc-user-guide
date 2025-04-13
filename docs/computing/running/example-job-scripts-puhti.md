
# Esimerkki eräajojärjestelmistä Puhti {#example-batch-job-scripts-for-puhti}

Esimerkki eräajojärjestelmistä erilaisten sovellusten/ohjelmien ajamiseen
Puhtilla.

[TOC]

!!! info "Muokkaa paikkamerkkejä tarvittaessa"
    Kun käytät näitä skriptejä, muista muuttaa resurssit (ajoaika, tehtävät jne.) niin, että ne sopivat tarpeisiisi, ja korvaa `myprog <options>` suoritettavalla ohjelmalla (ja optioilla), jota aiot käyttää. Älä myöskään unohda korvata `<project>`-kohtaa laskutusprojektisi nimellä (katso [MyCSC](https://my.csc.fi) tai `csc-projects`-komennolla).

## Sarja {#serial}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## OpenMP {#openmp}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4000

# aseta säikeiden määrä --cpus-per-task perusteella
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI {#mpi}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=40
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## Suuri MPI {#large-mpi}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=40
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## MPI + OpenMP {#mpi-openmp}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=4000

# aseta säikeiden määrä --cpus-per-task perusteella
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## Yksittäinen GPU {#single-gpu}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=8000
#SBATCH --gres=gpu:v100:1

srun myprog <options>
```

## Useita GPU:ita {#multiple-gpus}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --time=02:00:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=8000
#SBATCH --gres=gpu:v100:4

srun myprog <options>
```

## Interaktiivinen X11-grafiikalla {#interactive-with-x11-graphics}

Anna tämä suoraan komennolla eikä käyttämällä eräajojärjestelmää tai
`sbatch`ia. Huomaa, että sinun saattaa joutua jonottamaan, joten on kätevää
pyytää sähköpostivahvistus resurssien myöntämisestä (`--mail-type=BEGIN`).

```bash
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
     --account=<project> --partition=small --mail-type=BEGIN \
     myprog
```

Katso myös [Interaktiivinen käyttö](interactive-usage.md).

## Paikallinen tallennustila {#local-storage}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000
#SBATCH --gres=nvme:10

# käytä paikallista tallennustilaa muuttujan $LOCAL_SCRATCH avulla, esim.
cd $LOCAL_SCRATCH

srun myprog <options>

# siirrä tärkeät tiedot hakemistoon, josta työ lähetettiin, esim.
mv mydata $SLURM_SUBMIT_DIR
```

!!! warning "Muista palauttaa tietosi"
    Paikallinen tallennustila tyhjennetään jokaisen eräajon jälkeen. Älä unohda siirtää tietoja, jotka haluat säilyttää, paikalliselta levyltä takaisin jaettuun levyalustaan (esim. `/scratch`).

