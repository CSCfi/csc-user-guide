
---
tags:
  - Academic
---

# TURBOMOLE

[TURBOMOLE](https://www.turbomole.org/turbomole/turbomole-features/) on nopea
ja luotettava kvanttikemian ohjelmistopaketti, jossa on erittäin tehokkaat
erilaisten laskentamenetelmien (HF/DFT/MP2/CC) toteutukset. Ominaisuuksia voi
laskea sekä perus- että viritetyille tiloille. TURBOMOLE on suunniteltu
suurien järjestelmien tehokkaaseen tutkimiseen. 

## Saatavilla {#available}

- Puhti: 7.5.1, 7.6, 7.7, 7.8
- Mahti: 7.5.1, 7.6, 7.7, 7.8

## Lisenssi {#license}

- Ohjelmistoa saa käyttää vain voittoa tavoittelemattomaan tutkimukseen.
- Ohjelmistoa saavat käyttää vain akateemisten (esim. tutkinto-oikeuksia myöntävien) laitosten käyttäjät.

## Käyttö {#usage}

Alusta TURBOMOLE-ympäristö:

```bash
module load turbomole/7.8
```

### Eräajojen esimerkkiskripti Puhtille käyttäen MPI-parallelisointia {#batch-script-example-for-puhti-using-mpi-parallelization}

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI-tehtäviä per solmu
#SBATCH --account=<project>  # lisää tähän laskutettava projekti
#SBATCH --time=00:10:00      # aika muodossa `hh:mm:ss`
export PARA_ARCH=MPI         # käytä MPI:tä
module load turbomole/7.8
export SLURM_CPU_BIND=none
# Tämä TURBOTMPDIR-asetuksen oletus on, että työ
# on lähetetty /scratch/<project>-alla olevasta hakemistosta
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # MPI:lle
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

### Eräajojen esimerkkiskripti Puhtille käyttäen SMP-parallelisointia {#batch-script-example-for-puhti-using-smp-parallelization}

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=1            # SMP:lle vain 1 on mahdollinen
#SBATCH --cpus-per-task=40   # SMP-säikeitä
#SBATCH --account=<project>  # lisää tähän laskutettava projekti
#SBATCH --time=00:10:00      # aika muodossa `hh:mm:ss`
export PARA_ARCH=SMP         # käytä SMP-säikeitä   
module load turbomole/7.8
# Tämä TURBOTMPDIR-asetuksen oletus on, että työ
# on lähetetty /scratch/<project>-alla olevasta hakemistosta
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_CPUS_PER_TASK  # SMP:lle
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

!!! info "Huomio"
    Joskus `mpshift`-laskelmat keskeytyvät, kun paikallinen `/tmp`
    täyttyy. Ongelman voi kiertää määrittelemällä `$TMPDIR`:n uudelleen:
    ```bash
    export TMPDIR=$TURBOTMPDIR
    ```

!!! info "Huomio"
    Erityisesti jotkin aaltofunktioon perustuvat elektronikorrelaatiomenetelmät
    voivat olla erittäin levy-I/O-intensiivisiä. Tällaisista töistä on hyötyä
    Puhtin nopeasta paikallisesta tallennustilasta. Paikallisen levyn
    käyttäminen tällaisissa töissä vähentää myös kuormitusta Lustren rinnakkaisessa tiedostojärjestelmässä.
 
### Eräajojen esimerkkiskripti Puhti käyttäen MPI-parallelisointia ja paikallista levyä {#batch-script-example-for-puhti-using-mpi-parallelization-and-local-disk}

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40 # MPI-tehtäviä per solmu
#SBATCH --account=<project>  # lisää tähän laskutettava projekti
#SBATCH --time=00:10:00      # aika muodossa `hh:mm:ss`
#SBATCH --gres=nvme:100      # pyydetty paikallisen levyn koko GB
export PARA_ARCH=MPI         # käytä MPI:tä
module load turbomole/7.8
export SLURM_CPU_BIND=none
# määritä paikallinen levy tilapäisvälimuistiksi
export TURBOTMPDIR=$LOCAL_SCRATCH/$SLURM_JOBID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # MPI:lle
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
dscf > dscf.out
ccsdf12 > ccsdt.out
```

### Eräajojen esimerkkiskripti Mahti käyttäen MPI-parallelisointia {#batch-script-example-for-mahti-using-mpi-parallelization}

```bash
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128 # MPI-tehtäviä per solmu
#SBATCH --account=<project>   # lisää tähän laskutettava projekti
#SBATCH --time=00:60:00       # aika muodossa `hh:mm:ss`
export PARA_ARCH=MPI          # käytä MPI:tä
module load turbomole/7.8
export SLURM_CPU_BIND=none
# Tämä TURBOTMPDIR-asetuksen oletus on, että työ
# on lähetetty /scratch/<project>-alla olevasta hakemistosta
export TURBOTMPDIR=`echo $PWD |cut -d'/' -f1-3`"/TM_TMPDIR/"$SLURM_JOB_ID
mkdir -p $TURBOTMPDIR
export PARNODES=$SLURM_NTASKS  # MPI:lle
export PATH=$TURBODIR/bin/`$TURBODIR/scripts/sysname`:$PATH
jobex -ri -c 300 > jobex.out
```

### NumForce-laskelmat {#numforce-calculations}

NumForce on työkalu, jota voidaan käyttää toisen kertaluvun derivaattojen (molekyylin
Hessian) laskemiseen kaikilla menetelmillä, joille analyyttisiä gradientteja on saatavilla
`TURBOMOLE:ssa`. NumForce-työ synnyttää `3*N*2` (`N` = atomien
lukumäärä) itsenäistä gradientin laskentaa. Yleensä on tehokkainta, että yksittäiset gradientin
laskennat suoritetaan sarjana (`unset PARA_ARCH`). Jokaisen sarjallisen laskennan
odotetaan kestävän yhtä kauan, joten optimaalisesti gradienttien laskentojen määrä
pitäisi olla jaollinen varattujen ytimien määrällä.

NumForce-vaihe työskentelytiedostossa:

```bash
unset PARA_ARCH
export HOSTS_FILE=$PWD/turbomole.machines
rm -f $HOSTS_FILE
srun hostname > $HOSTS_FILE
ulimit -s unlimited
kdg tmpdir
NumForce -ri -central -mfile $HOSTS_FILE > NumForce.out
```

## Viitteet {#references}

Ole hyvä ja siteeraa ohjelmistopaketin käyttöä huomioiden
versiokoodi:

- TURBOMOLE V7.8, kehittänyt Karlsruhen yliopisto ja
  Forschungszentrum Karlsruhe GmbH, 1989-2007, TURBOMOLE GmbH, vuodesta 2007 lähtien;
  saatavilla osoitteesta https://www.turbomole.org
- Myös katsausartikkeli tulisi mainita:
  https://doi.org/10.1063/5.0004635
- Tieteelliset julkaisut vaativat menetelmien ja
  käytettyjen menettelyjen oikean siteraamisen. TURBOMOLE-moduulien tulostuspääte
  sisältää asiaankuuluvat julkaisut. 

## Lisätietoja {#more-information}

- [TURBOMOLE GmbH](https://www.turbomole.org/turbomole/turbomole-documentation/)
- [TURBOMOLE: Tänään ja huomenna](https://pubs.acs.org/doi/10.1021/acs.jctc.3c00347)
- [TURBOMOLE arviointi](https://aip.scitation.org/doi/10.1063/5.0004635)
- [TURBOMOLE tutoriaali](https://www.turbomole.org/wp-content/uploads/Tutorial_7-7.pdf)
- [TURBOMOLE käyttäjäfoorumi](https://forum.turbomole.org/index.php)
