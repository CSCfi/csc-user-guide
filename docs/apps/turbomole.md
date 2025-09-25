---
tags:
  - Academic
catalog:
  name: TURBOMOLE
  description: Efficient program package for electronic structure calculations
  description_fi: Tehokas ohjelmistopaketti elektronirakennelaskentaan
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# TURBOMOLE { #turbomole }

[TURBOMOLE](https://www.turbomole.org/turbomole/turbomole-features/) on nopea
ja luotettava kvanttikemian ohjelmistopaketti, jossa on erittäin tehokkaat
toteutukset useille laskentamenetelmille (HF/DFT/MP2/CC). Ominaisuuksia voidaan
laskea sekä perus- että virittyneissä tiloissa. TURBOMOLE on suunniteltu
suurten järjestelmien tehokkaaseen tutkimiseen. 

## Saatavilla { #available }

- Puhti: 7.5.1, 7.6, 7.7, 7.8
- Mahti: 7.5.1, 7.6, 7.7, 7.8

## Lisenssi { #license }

- Ohjelmistoa saa käyttää ainoastaan voittoa tavoittelemattomaan tutkimus-
  tarkoitukseen.
- Vain akateemisten (eli tutkintoja myöntävien) oppilaitosten käyttäjät
  saavat käyttää ohjelmistoa

## Käyttö { #usage }

Alusta TURBOMOLE-ympäristö:

```bash
module load turbomole/7.8
```

### Eräajoesimerkki Puhtissa käyttäen MPI-rinnakkaistusta { #batch-script-example-for-puhti-using-mpi-parallelization }

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as `hh:mm:ss`
export PARA_ARCH=MPI         # use MPI 
module load turbomole/7.8
export SLURM_CPU_BIND=none
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

### Eräajoesimerkki Puhtissa käyttäen SMP-rinnakkaistusta { #batch-script-example-for-puhti-using-smp-parallelization }

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1            # for SMP only 1 is possible
#SBATCH --cpus-per-task=40   # SMP threads
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`
export PARA_ARCH=SMP         # use SMP threads   
module load turbomole/7.8
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_CPUS_PER_TASK  # for SMP
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

!!! info "Huom."
    Ajoittain `mpshift`-laskut päättyvät keskeytykseen, koska paikallinen `/tmp`
    täyttyy. Ongelman voi kiertää määrittelemällä `$TMPDIR`-muuttujan uudelleen:
    ```bash
    export TMPDIR=$TURBOTMPDIR
    ```

!!! info "Huom."
    Erityisesti jotkin aaltotoimintoon perustuvat elektronikorrelaatiomenetelmät
    voivat olla hyvin levy-I/O-intensiivisiä. Tällaiset ajot hyötyvät Puhtin
    nopean paikallistallennuksen käytöstä. Paikallislevyn käyttö tällaisissa
    ajoissa vähentää myös Lustre-rinnakkaistiedostojärjestelmän kuormitusta.
 
### Eräajoesimerkki Puhtissa käyttäen MPI-rinnakkaistusta ja paikallislevyä { #batch-script-example-for-puhti-using-mpi-parallelization-and-local-disk }

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`
#SBATCH --gres=nvme:100      # requested local disk in GB
export PARA_ARCH=MPI         # use MPI
module load turbomole/7.8
export SLURM_CPU_BIND=none
# define local disk as scratch
export TURBOTMPDIR=$LOCAL_SCRATCH/$SLURM_JOBID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
dscf > dscf.out
ccsdf12 > ccsdt.out
```

### Eräajoesimerkki Mahtissa käyttäen MPI-rinnakkaistusta { #batch-script-example-for-mahti-using-mpi-parallelization }

```bash
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128 # MPI tasks per node
#SBATCH --account=<project>   # insert here the project to be billed
#SBATCH --time=00:60:00       # time as `hh:mm:ss`
export PARA_ARCH=MPI          # use MPI
module load turbomole/7.8
export SLURM_CPU_BIND=none
# This setting of TURBOTMPDIR assumes that the job is 
# submitted from a directory below /scratch/<project>
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # for MPI
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

### NumForce-laskut { #numforce-calculations }

NumForce on työkalu, jolla voidaan laskea toiset derivaatat (molekyylin
Hessian) kaikille menetelmille, joille analyyttiset gradientit ovat
saatavilla `TURBOMOLE`ssa. NumForce-ajo käynnistää `3*N*2` (`N` = atomien
lukumäärä) riippumatonta gradienttilaskua. Yleensä on tehokkainta, että
yksittäiset gradienttilaskut ajetaan sarjana (`unset PARA_ARCH`). Kunkin
sarjalaskun odotetaan kestävän suunnilleen yhtä kauan, joten optimaalisesti
gradienttilaskujen kokonaismäärän tulisi olla varattujen ytimien määrän
kokonaislukukertainen monikerta.

NumForce-vaihe eräajotiedostossa:

```bash
unset PARA_ARCH
export HOSTS_FILE=$PWD/turbomole.machines
rm -f $HOSTS_FILE
srun hostname > $HOSTS_FILE
ulimit -s unlimited
kdg tmpdir
NumForce -ri -central -mfile $HOSTS_FILE > NumForce.out
```

## Viitteet { #references }

Ilmoittakaa ohjelmistopaketin käyttö versiotiedon kera:

- TURBOMOLE V7.8, Karlsruhen yliopiston ja
  Forschungszentrum Karlsruhe GmbH:n kehittämä, 1989-2007; TURBOMOLE GmbH
  vuodesta 2007; saatavilla osoitteesta https://www.turbomole.org
- Myös katsausartikkeli tulisi mainita:
  https://doi.org/10.1063/5.0004635
- Tieteellisissä julkaisuissa käytetyt menetelmät ja menettelyt
  on viitattava asianmukaisesti. TURBOMOLE-moduulien tulosteiden
  otsikot sisältävät asiaankuuluvat viitteet. 

## Lisätietoja { #more-information }

- [TURBOMOLE GmbH](https://www.turbomole.org/turbomole/turbomole-documentation/) 
- [TURBOMOLE: Today and Tomorrow](https://pubs.acs.org/doi/10.1021/acs.jctc.3c00347)
- [TURBOMOLE-katsaus](https://aip.scitation.org/doi/10.1063/5.0004635) 
- [TURBOMOLE-opas](https://www.turbomole.org/wp-content/uploads/Tutorial_7-7.pdf)
- [TURBOMOLE-käyttäjäfoorumi](https://forum.turbomole.org/index.php)