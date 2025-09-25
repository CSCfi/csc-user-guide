---
tags:
  - Free
catalog:
  name: CP2K
  description: DFT, quantum chemistry, QM/MM, AIMD etc. in particular for periodic systems
  description_fi: DFT, kvanttikemia, QM/MM, AIMD jne., erityisesti jaksollisille järjestelmille
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# CP2K { #cp2k }

Monipuolinen ab initio- ja klassinen molekyylidynamiikka. CP2K soveltuu suuriin
rinnakkaisiin kvanttikemian laskuihin, erityisesti AIMD-laskentoihin.

[TOC]

## Saatavilla { #available }

=== "Puhti"
    | Versio | Saatavilla olevat moduulit | Huomautukset |
    |:------:|:---------------------------|:------------:|
    |9.1     |`cp2k/9.1`                  |              |
    |2022.2  |`cp2k/2022.2`               |              |
    |2023.1  |`cp2k/2023.1`               |              |
    |2023.2  |`cp2k/2023.2`               |              |
    |2024.1  |`cp2k/2024.1`               |              |
    |2024.2  |`cp2k/2024.2`               |              |
    |2025.1  |`cp2k/2025.1`               |              |

=== "Mahti"
    | Versio | Saatavilla olevat moduulit | Huomautukset |
    |:------:|:---------------------------|:------------:|
    |8.2     |`cp2k/8.2`                  |              |
    |9.1     |`cp2k/9.1`                  |              |
    |2022.2  |`cp2k/2022.2`               |              |
    |2023.1  |`cp2k/2023.1`               |              |
    |2023.2  |`cp2k/2023.2`               |              |
    |2024.1  |`cp2k/2024.1`               |              |
    |2024.2  |`cp2k/2024.2`               |              |
    |2025.1  |`cp2k/2025.1`               |              |

=== "LUMI"
    | Versio | Saatavilla olevat moduulit                | Huomautukset          |
    |:------:|:------------------------------------------|:---------------------:|
    |2024.3  |`cp2k/2024.3`<br>`cp2k/2024.3-gpu`         | GPU-versio saatavilla |
    |2025.1  |`cp2k/2025.1`<br>`cp2k/2025.1-gpu`         | GPU-versio saatavilla |

## Lisenssi { #license }

CP2K on vapaasti saatavilla GPL-lisenssillä.

## Käyttö { #usage }

!!! info "LUMI"
    Päästäksesi käyttämään CSC:n moduuleja LUMIlla, lataa ensin CSC:n moduulipuu
    käyttöön komennolla

    ```bash
    module use /appl/local/csc/modulefiles
    ```

Tarkista, mitkä versiot voi ladata suoraan:

```bash
module avail cp2k
```

Kaikki asennetut versiot löytyvät komennolla:

```bash
module spider cp2k
```

Anna versionumero nähdäksesi, miten se ladataan:

```bash
module spider cp2k/<version>
```

Varmista jokaisen uuden projektin alussa, että ajosi hyödyntää tehokkaasti kaikki
eräajon skriptissä varaamasi ytimet. Nyrkkisääntö: jos kaksinkertaistat ytimien
määrän, laskennan tulisi nopeutua vähintään 1,5-kertaiseksi.

### Esimerkkieräskriptit { #example-batch-scripts }

=== "Puhti (vain MPI)"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --ntasks-per-node=40
    #SBATCH --nodes=2
    #SBATCH --mem-per-cpu=2GB
    #SBATCH --partition=large
    #SBATCH --account=<project>

    module purge
    module load gcc/14.2.0 openmpi/5.0.6
    module load cp2k/2025.1

    srun cp2k.psmp H2O-64.inp > H2O-64.out
    ```

=== "Mahti (yhdistetty MPI/OpenMP)"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:05:00
    #SBATCH --ntasks-per-node=32  # 2 - 128
    #SBATCH --cpus-per-task=4     # 128 / ntasks-per-node
    #SBATCH --nodes=2
    #SBATCH --partition=test
    #SBATCH --account=<project>

    module purge
    module load gcc/14.2.0 openmpi/5.0.6
    module load cp2k/2025.1

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    export OMP_PLACES=cores

    srun cp2k.psmp H2O-64.inp > H2O-64.out
    ```

=== "LUMI-G (täysi GPU-solmu)"

    ```bash
    #!/bin/bash
    #SBATCH --partition=standard-g
    #SBATCH --account=<project>
    #SBATCH --time=00:30:00
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=16  # Run two tasks per GCD, in this case more efficient

    export OMP_NUM_THREADS=3

    module use /appl/local/csc/modulefiles
    module load cp2k/2025.1-gpu

    export MPICH_GPU_SUPPORT_ENABLED=1

    cat << EOF > select_gpu
    #!/bin/bash

    export ROCR_VISIBLE_DEVICES=\$((SLURM_LOCALID%SLURM_GPUS_PER_NODE))
    exec \$*
    EOF

    chmod +x ./select_gpu

    CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
    CPU_BIND="${CPU_BIND},fe0000,fe000000"
    CPU_BIND="${CPU_BIND},fe,fe00"
    CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

    srun --cpu-bind=$CPU_BIND ./select_gpu cp2k.psmp H2O-dft-ls.inp >> H2O-dft-ls.out
    ```

    !!! info "Huom."
        Jokainen LUMIn GPU koostuu kahdesta AMD Graphics Compute Die -yksiköstä (GCD).
        Koska solmussa on neljä GPU:ta ja Slurm tulkitsee jokaisen GCD:n erilliseksi
        GPU:ksi, voit varata jopa 8 ”GPU:ta” per solmu. Lisätietoja:
        [LUMI-dokumentaatio](https://docs.lumi-supercomputer.eu/hardware/lumig/).

### Suorituskykyhuomiot { #performance-notes }

#### Mahti { #mahti }

Seuraava taulukko näyttää kokonaisajoajan (sekunteina)
[H2O-256-vertailulle](https://github.com/cp2k/cp2k/blob/master/benchmarks/QS/H2O-256.inp)
Mahtilla käyttäen `cp2k/2024.2`-versiota. Sarakeotsikot kertovat, montako OpenMP-säiettä
käytettiin per MPI-tehtävä.

|CPU-solmut|1     |2     |4         |8     |
|:--------:|:----:|:----:|:--------:|:----:|
|1         |197.35|164.80|169.66    |192.07|
|2         |111.95|107.78|**101.52**|117.60|
|4         |82.74 |72.12 |72.00     |97.97 |

* 256 vesimolekyylin tapauksessa paras tehokkuus saadaan 2 täydellä solmulla,
  32 MPI-tehtävällä per solmu ja 4 OpenMP-säikeellä per tehtävä. Tälle järjestelmälle
  ei ole tehokasta skaalata yli 2 solmun (256 CPU-ytimen).
* Hybridirinnakkaisuus on usein tehokas – valitse tehtävien ja säikeiden määrät
  siten, että ne summautuvat solmukohtaisiin 128 fyysiseen ytimeen (tai Puhtilla 40).
* Testaa mallijärjestelmällesi ja -menetelmällesi optimaaliset ajoasetukset.
* ELPA-diagonalisaatiokirjaston käyttäminen ScaLAPACKin sijaan voi merkittävästi
  nopeuttaa laskuja, jotka vaativat suurten matriisien diagonalisaatiota (jopa
  50 % järjestelmästä riippuen). Hyvä esimerkki ovat metalliset järjestelmät,
  jotka voivat konvergoitua heikosti OT-menetelmällä (orbital transformation) ja
  vaativat siksi Kohn–Shamin matriisin tavanomaisen diagonalisaation.

#### LUMI { #lumi }

Vain tietyt CPU-ytimet ovat suoraan kytköksissä tiettyyn GPU:hun LUMIlla, joten
moni-GPU-suorituksen maksimoimiseksi on tärkeää sitoa CPU-ytimet GPU:ihin
vastaavasti. Yllä oleva täyden GPU-solmun esimerkki huolehtii tästä ja sulkee
myös pois jokaisen 8 ytimen ryhmän ensimmäisen ytimen, joka on varattu
käyttöjärjestelmälle hälyn vähentämiseksi. Tämän vuoksi solmussa on käytettävissä
vain 56 ydintä.

!!! error "Huom."
    Huomaa, että CPU–GPU-sidonta toimii vain, kun varataan kokonaisia solmuja
    ajamalla `standard-g`-jonossa tai käyttämällä `--exclusive`-valitsinta.
    Lisätietoja LUMI-dokumentaatiosta:
    [LUMI-G-laitteisto](https://docs.lumi-supercomputer.eu/hardware/lumig/),
    [LUMI-G-esimerkit](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/),
    [GPU-sidonta](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)

Seuraava kuva esittää kokonaisajoajan
[lineaarisesti skaalautuvalle SCF-vertailulle](https://github.com/cp2k/cp2k/tree/master/benchmarks/QS_DM_LS)
(2048 vesimolekyyliä) Mahtilla (CPU), LUMI-C:llä ja LUMI-G:llä. Kun CPU–GPU-sidonta
on tehty oikein (katso esimerkki yllä), LUMI-G on noin kaksinkertaisesti
suorituskykyisempi kuin Mahti/LUMI-C, kun verrataan GPU-solmuja CPU-solmuihin.
Koska kaikkia CP2K:n rutiineja ei ole siirretty GPU:ille, varmista aina
järjestelmäsi ja menetelmäsi suorituskyky ja skaalaus – jotkin simulaatiot
(esim. tavallinen SCF) kannattaa ajaa CPU:illa, kun taas toiset ovat selvästi
nopeampia GPU:illa (esim. lineaarisesti skaalautuva SCF, post-HF-menetelmät).
Lisätietoja: [CP2K:n verkkosivut](https://www.cp2k.org/gpu).

![CP2K:n skaalautuminen Mahtissa ja LUMIssa](../img/cp2k-lumi.png 'CP2K:n skaalautuminen Mahtissa ja LUMIssa')

### Korkean läpimenon laskenta CP2K:lla { #high-throughput-computing-with-cp2k }

Korkean läpimenon laskentoja voi ajaa kätevästi CP2K:lla sisäänrakennetulla
`FARMING`-ohjelmalla. Tämä on erinomainen vaihtoehto käyttötapauksiin, joissa
tarkoituksena on ajaa suuri määrä toisistaan riippumattomia laskuja, kuten
tuotettaessa dataa AI/ML-putkille. Kaikki alitehtävät ajetaan rinnakkain
yhdessä Slurm-varauksessa, jolloin vältetään ylimääräiset `srun`- ja
`sbatch`-kutsut ja vähennetään kuormaa jonojärjestelmässä.

`FARMING`-ajot vaativat lisäsyötetiedoston, jossa määritellään työnkulun
yksityiskohdat, kuten syötekansiot ja rinnakkaisten tehtäväryhmien määrä.
Esimerkkisyöte- ja eräskriptit ovat alla. Huomaa, että `RUN_TYPE` on asetettu
arvoon `NONE` `&GLOBAL`-osiossa.

=== "Input file"

    ```text title="farming.inp"
    &GLOBAL
      PROJECT my-farming-job
      PROGRAM FARMING
      RUN_TYPE NONE
    &END GLOBAL
    &FARMING
      NGROUPS 8
      &JOB
        DIRECTORY run1
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run2
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run3
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run4
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run5
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run6
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run7
        INPUT_FILE_NAME nacl.inp
      &END JOB
      &JOB
        DIRECTORY run8
        INPUT_FILE_NAME nacl.inp
      &END JOB
    &END FARMING
    ```

=== "Batch script file"

    ```bash title="farming.sh"
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=medium
    #SBATCH --ntasks-per-node=128
    #SBATCH --nodes=1
    #SBATCH --account=<project>

    module purge
    module load gcc/14.2.0 openmpi/5.0.6
    module load cp2k/2025.1

    srun cp2k.psmp farming.inp >> farming.out
    ```

Tässä esimerkissä varataan yksi täysi Mahti-solmu 8 NaCl-kiteen
single point -laskulle eri hilarakenteilla. `farming.inp`-tiedoston lisäksi
jokainen alitehtävä tarvitsee tavallisen oman syötetiedostonsa, jotka on tässä
järjestetty omiin alihakemistoihin nimillä `run*`. Komennon `sbatch farming.sh`
antaminen yläkansiossa käynnistää kaikki laskut rinnakkain, varaten kullekin
alitehtävälle 16 ydintä.

Huomaa, että alitehtävien välille voidaan määritellä myös riippuvuuksia
`DEPENDENCIES`- ja `JOB_ID`-avaimilla `&JOB`-osiossa. Tämän avulla voidaan
määritellä monimutkaisia työnkulkuja. Lisätietoja:
[CP2K-manuaali](https://manual.cp2k.org/trunk/CP2K_INPUT/FARMING.html) ja
[regressiotestien esimerkkisyötteet](https://github.com/cp2k/cp2k/tree/master/tests/FARMING).

## Viitteet { #references }

CP2K tulostaa lokitiedoston loppupuolelle luettelon asiaankuuluvista
julkaisuista. Valitse ja siteeraa niistä ne, jotka liittyvät käyttämiisi
menetelmiin.

## Lisätietoa { #more-information }

* [CP2K-verkkokäsikirja](https://manual.cp2k.org/)
* [CP2K-kotisivu](http://www.cp2k.org/)
    * Sisältää [ohjeita](https://www.cp2k.org/howto) ja linkkejä hyödyllisiin
      [työkaluihin](https://www.cp2k.org/tools).
* [Regressiotestien syötteitä](https://github.com/cp2k/cp2k/tree/master/tests) voidaan
  käyttää esimerkkeinä CP2K:n eri ominaisuuksien käytöstä. Huomaa, että
  konvergenssikriteerit voivat olla melko väljät ja ne kannattaa testata erikseen
  tuotantoajoja varten.