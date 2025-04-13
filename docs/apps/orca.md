
---
tags:
  - Other
---

# ORCA

[ORCA](https://orcaforum.kofo.mpg.de/app.php/portal) on ab initio kvanttikemian ohjelmistopaketti, joka sisältää moderneja elektronirakennemenetelmiä, kuten tiheystoiminnallisen teorian, usean kappaleen häiriöteorian, kytketyn klusterin menetelmiä, moniviitemenetelmiä ja puolikokeellisia kvanttikemian menetelmiä. Sen pääasiallinen sovelluskenttä on suuremmat molekyylit, siirtymämetallikompleksit ja niiden spektroskooppiset ominaisuudet. ORCA-ohjelmiston kehitys tapahtuu [Frank Neesen](https://en.wikipedia.org/wiki/Frank_Neese) tutkimusryhmässä. Vapaa versio on saatavilla vain akateemiseen käyttöön akateemisissa laitoksissa.

[TOC]

## Saatavilla {#available}

- Puhti: 6.0.0
- Mahti: 6.0.0

Huomaa, että lisenssiongelmien vuoksi jokaisen käyttäjän on asennettava oma kopiopa ohjelmasta.

## Lisenssi {#license}

ORCA-käyttäjien tulisi rekisteröityä, hyväksyä EULA, ladata ja asentaa oma kopio ohjelmasta
([ORCA-foorumin verkkosivun kautta](https://orcaforum.kofo.mpg.de/app.php/portal)). Vapaa versio on saatavilla vain akateemiseen käyttöön akateemisissa laitoksissa.

## Käyttö {#usage}

- Lataa ORCA 6.0.0, Linux, x86-64, jaettu versio, `orca_6_0_0_linux_x86-64_avx2_shared_openmpi416.tar.xz`
- Siirrä ladattu tiedosto laskentaprojektisi sovellusalueelle (`/projappl/<proj>`) Puhtilla
- Pure paketti, `tar xf orca_6_0_0_linux_x86-64_avx2_shared_openmpi416.tar.xz`

### Esimerkki eräkäsittelyskripteistä {#example-batch-scripts}

!!! info "Huomio"
    Aaltotoimintoperäiset korrelaatiomenetelmät, sekä yksittäis- että moniviite, luovat usein merkittävän määrän levy I/O:ta. Parhaan suorituskyvyn saavuttamiseksi työtehtävälle ja Lusterin rinnakkaistiedostojärjestelmän liiallisen kuormituksen välttämiseksi on suositeltavaa käyttää paikallista levyä.

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI-tehtäviä per solmu
    #SBATCH --account=yourproject     # täytä tähän laskutettava projekti 
    #SBATCH --time=00:15:00           # aika muodossa `hh:mm:ss`
    module purge
    module load gcc/11.3.0 openmpi/4.1.4 intel-oneapi-mkl/2022.1.0
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # Määritä $ORCA_TMPDIR osoittamaan lähetyshakemistoon
    export ORCA_TMPDIR=$SLURM_SUBMIT_DIR
    # luo mpirun skripti joka suorittaa srun-komennon
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    export PATH=${SLURM_SUBMIT_DIR}:${PATH}
    touch Jobid_is_$SLURM_JOB_ID 

    ${ORCADIR}/orca orca6.inp > orca6.out
    rm -f  ${SLURM_SUBMIT_DIR}/mpirun
    ```

=== "Puhti, paikallinen levy"

    ```bash
    #!/bin/bash
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40
    #SBATCH --account=yourproject     # täytä tähän laskutettava projekti
    #SBATCH --time=00:15:00           # aika muodossa `hh:mm:ss`
    #SBATCH --gres=nvme:100  # pyydetty paikallisen levyn tila GB:ssa
    module purge
    module load gcc/11.3.0 openmpi/4.1.4 intel-oneapi-mkl/2022.1.0
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # luo mpirun skripti joka suorittaa srun-komennon
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    export PATH=${SLURM_SUBMIT_DIR}:${PATH}
    touch Jobid_is_$SLURM_JOB_ID 


    # Määritä $ORCA_TMPDIR paikalliselle levylle
    export ORCA_TMPDIR=$LOCAL_SCRATCH
    # Kopioi vain tarvittavat tiedostot $ORCA_TMPDIR:iin
    cp $SLURM_SUBMIT_DIR/*.inp $ORCA_TMPDIR/
    # Siirry $ORCA_TMPDIR:iin
    cd $ORCA_TMPDIR

    $ORCADIR/orca orca6.inp > ${SLURM_SUBMIT_DIR}/orca6.out
    rm -f  ${SLURM_SUBMIT_DIR}/mpirun
    # Kopioi kaikki tulosteet lähetyshakemistoon
    cp -r $ORCA_TMPDIR $SLURM_SUBMIT_DIR
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --account=yourproject     # täytä tähän laskutettava projekti
    #SBATCH --time=0:10:00 # aika muodossa hh:mm:ss
    module purge
    module load gcc/11.2.0 openmpi/4.1.2 openblas/0.3.18-omp
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # luo mpirun skripti joka suorittaa srun-komennon
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    export PATH=${SLURM_SUBMIT_DIR}:${PATH}
    touch Jobid_is_$SLURM_JOB_ID

    ${ORCADIR}/orca orca6.inp > orca6.out
    rm -f  ${SLURM_SUBMIT_DIR}/mpirun
    ```

!!! info "Huomio"
    Muistathan säätää `%pal nproc` syötteessäsi vastaamaan pyydettyjen MPI-tehtävien kokonaismäärää (`--nodes` * `--ntasks-per-node`).

## Viitteet {#references}

ORCA:n yleiset viitteet ovat:

- Frank Neese. ORCA ohjelmistojärjestelmä. Wiley Interdiscip. Rev. Comput. Mol. Sci., 2(1):73–78, 2012. doi:<https://doi.wiley.com/10.1002/wcms.81>.
- Frank Neese. Ohjelmistopäivitys: ORCA ohjelmistojärjestelmä, versio 4.0. Wiley Interdiscip. Rev. Comput. Mol. Sci., 8(1):e1327, 2018. doi:<https://doi.wiley.com/10.1002/wcms.1327>.
- Frank Neese, Frank Wennmohs, Ute Becker, and Christoph Riplinger. ORCA kvanttikemian ohjelmistopaketti. J. Chem. Phys., 152(22):224108, 2020. doi:<https://aip.scitation.org/doi/10.1063/5.0004608>.

Älä pelkästään viittaa ylläolevaan yleiseen viitteeseen, vaan viittaa lisäksi
[alkuperäisiin artikkeleihin](https://www.faccts.de/docs/orca/6.0/manual/contents/public.html)
joissa on raportoitu kehittämät ja ORCA:n implementaatiot menetelmistä, joita olet käyttänyt
tutkimuksissasi! Julkaisut, jotka kuvaavat ORCA:ssa toteutettua toimintaa, on annettu käsikirjassa.

## Lisätietoa {#more-information}

- [ORCA Forum (kirjautuminen samoilla tunnuksilla kuin lataamiseen)](https://orcaforum.kofo.mpg.de/app.php/portal)
- [ORCA 6 Muutokset](https://www.faccts.de/docs/orca/6.0/manual/contents/changes.html)
- [ORCA 6 Käsikirja](https://www.faccts.de/docs/orca/6.0/manual/ )
- [ORCA 6 Oppaat](https://www.faccts.de/docs/orca/6.0/tutorials/)
- [ORCA YouTube-kanava](https://www.youtube.com/@orcaquantumchemistry)
- [ORCA Syöttökirjasto, joka sisältää esimerkkisyötteitä](https://sites.google.com/site/orcainputlibrary/home)

