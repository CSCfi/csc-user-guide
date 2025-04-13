# Esimerkkejä eräkäsittelyskripteistä Mahti-järjestelmälle {#example-batch-job-scripts-for-mahti}

Esimerkkejä eräajoista eri ohjelmatyypeille:

[TOC]

!!! huom
    Jos käytät skriptejä (suositellaan!), älä unohda muuttaa resursseja (aika, tehtävät jne.) tarpeidesi mukaan ja korvata `myprog <options>` ajettavan ohjelman suoritettavalla tiedostolla (ja valinnoilla) sekä `<project>` projektisi nimellä.

## MPI {#mpi}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=02:00:00
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=128

srun myprog <options>
```

## Suuri MPI {#large-mpi}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --ntasks-per-node=128

srun myprog <options>
```

## MPI + OpenMP {#mpi-openmp}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8

# Aseta ketjujen määrä perustuen --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI + OpenMP langan sidonnalla {#mpi-openmp-with-thread-binding}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8

# Aseta ketjujen määrä perustuen --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores

srun myprog <options>
```

## MPI + OpenMP samanaikaisella monisäikeistyksellä {#mpi-openmp-with-simultaneous-multithreading}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --hint=multithread
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=16

# Huomaa että ntasks-per-node * cpus-per-task = 256

# Aseta ketjujen määrä perustuen --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI yhdellä tehtävällä per NUMA-alue {#mpi-with-one-task-per-numa-domain}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=02:00:00
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

# Laskentasolmuilla on 8 NUMA-aluetta, joissa jokaisessa on 16 ydintä
# Slurm sijoittaa MPI-tehtävät --cpus-per-task etäisyydelle toisistaan

srun myprog <options>
```

## OpenMP {#openmp}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=128

# aseta ketjujen määrä perustuen --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## Paikallinen levy ja `small` osio {#local-disk-and-small-partition}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=nvme:100

# Small osio:
# - Jokainen työ saa automaattisesti 1,875 GB muistia per varattu ydin.
#   Jos tehtävä tarvitsee lisää muistia, käytä `--cpus-per-task` asetusta.
# - Muistivaraukset slurm-asetukset ohitetaan
# - Paikallinen NVMe-levy jopa 3500 GiB on saatavilla, varaa asetuksella
#   `--gres=nvme:<koko GiB>` ja käytä $LOCAL_SCRATCH ympäristömuuttujan kautta

export MY_JOB_TMPDIR=$LOCAL_SCRATCH
srun myprog <options>
```

## 1-2 GPU-tehtävä eli `gpusmall` osio {#1-2-gpu-job-i.e.-gpusmall-partition}

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpusmall
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:1
## jos tarvitset myös paikallisen nopean levyn solmussa, korvaa edellinen rivi:
#SBATCH --gres=gpu:a100:1,nvme:900
#
## Muista ladata ympäristö, jota sovelluksesi saattaa tarvita.
## Ja käytä muuttujaa $LOCAL_SCRATCH eräkäsittelyskriptissäsi 
## paikallisen nopean tallennustilan käyttämiseen jokaisessa solmussa.

srun myprog <options>
```

## 4 GPU:ta per solmu ja monisoluinen GPU-tehtävä eli `gpumedium` osio {#4-gpus-per-node-and-multinode-gpu-job-i.e.-gpumedium-partition}

```bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpumedium
#SBATCH --time=02:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:4
## jos tarvitset myös paikallisen nopean levyn solmuissa, korvaa edellinen rivi: 
#SBATCH --gres=gpu:a100:4,nvme:3600
#
## Muista ladata ympäristö, jota sovelluksesi saattaa tarvita.
## Ja käytä muuttujaa $LOCAL_SCRATCH eräkäsittelyskriptissäsi 
## paikallisen nopean tallennustilan käyttämiseen jokaisessa solmussa.

srun myprog <options>
